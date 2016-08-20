'''
    usage:
    ---------
    > python gbdt_training_predicting/gbdt_plots.py --option=importances
'''

import sys
import pandas as pd
import xgboost as xgb
import numpy as np
import operator
from matplotlib import pylab as plt
import matplotlib.ticker as ticker
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()



feature_names = [
                 r'$N_{hits}$',r'$length$',r'$y_{start}$',r'$z_{start}$',r'$y_{end}$',r'$z_{end}$',r'$\theta$',r'$\phi$', r'${|\vec{d}|/l}$',
                 r'$dq/dx_{start}$',r'$dq/dx_{end}$',r'$\Delta dq/dx$',r'$dq/dx_{ratio}$',r'$dq/dx_{total}$',r'$dq/dx_{average}$',
                 r'$score_{cosmic}$',r'$score_{contained-cosmic}$',r'${PID_{a}}$',r'${PID_\chi}$'
                 ]

ModelName   = "cosmic_trained_only_on_mc"
model_path  = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna/GBDTmodels"

Booster = xgb.Booster(model_file = model_path + "/" + ModelName + ".bst")





if flags.option == "importances":

    outfile = open('xgb.fmap', 'w')
    i = 0
    for feat in feature_names:
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close()


    importance = Booster.get_fscore(fmap='xgb.fmap')
    importance = sorted(importance.items(), key=operator.itemgetter(1))

    df = pd.DataFrame(importance, columns=['feature', 'fscore'])
    df['fscore'] = df['fscore'] / df['fscore'].sum()

    plt.figure()
    df.plot()
    df.plot(kind='barh', x='feature', y='fscore', legend=False, figsize=(6, 10))
    plt.title('XGBoost Feature Importance',fontsize=22)
    plt.xlabel('relative importance',fontsize=22)
    plt.show()
    plt.gcf().savefig('/Users/erezcohen/Desktop/importances'+ModelName+'.pdf')














elif flags.option == "test - efficiency":

    import os , math , time
    sys.path.insert(0, '../../protonid')
    import predict_cosmic



    TestSample      = "55650_tracks_openCOSMIC_MC_AnalysisTrees"
    Path            = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"
    TestSampleName  = Path + "/TestSamples/testsample_" + TestSample + ".csv"
    TestSampleScoresName = TestSampleName + "_with_predicted_scores.csv"

    AskPredict = int(input("predict on MC? \n( yes-1 / no-0 ):\n > "))
    DoPredict = True if AskPredict==1 else False

    if DoPredict:
        
        data = pd.read_csv( TestSampleName )
        data_scores = predict_cosmic.predict_data( data , model_path + "/" + ModelName + ".bst" )
        data_scores[['run','subrun','event','trackid'
                     ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
                     ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
                     ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
                     ,'MCpdgCode'
                     ,'pscore' ]].to_csv( TestSampleScoresName)
        print "predicted scores and saved into \n"+ TestSampleScoresName

    else:
    
        data_scores = pd.read_csv( TestSampleScoresName )
        print "data with scores\n",data_scores


    protons     = data_scores[data_scores.MCpdgCode == 2212]
    nonprotons  = data_scores[data_scores.MCpdgCode != 2212]

    N           = 100
    score       = []
    p_protons   = []
    p_nonprotons= []

    for i in range(N):
    
        score.append(float(i)/N)
        protons_pass = protons[protons.pscore > score[i]]
        nonprotons_pass = nonprotons[nonprotons.pscore > score[i]]

        p_protons.append(100*float(len(protons_pass))/len(protons))
        p_nonprotons.append(100*float(len(nonprotons_pass))/len(nonprotons))

        if flags.verbose>0 and N>10:
            if (i%(N/10)==0): print "\n[%.0f%%]"%(100.*float(i)/N)

        print "[%.0f%%]"%(100.*float(i)/N)


    # percentage of classified protons vs. score
    plt.plot( score , p_protons , 'b-')
    plt.hold('on')
    plt.plot( score , p_nonprotons , 'r-')
    plt.xlabel('score' , fontsize=22)
    plt.ylabel('classified as protons [%]' , fontsize=22)
    plt.legend(['(MC) protons', '(MC) non-protons'])
    plt.title('cosmic mc classification' , fontsize=22)
    plt.grid()
    plt.show()
    plt.savefig( "/Users/erezcohen/Desktop/test_purity_vs_score_" + ModelName + ".pdf" )


    protons_scores = protons['pscore']
    nonprotons_scores = nonprotons['pscore']
    plt.hist([nonprotons_scores,protons_scores],bins=50,color=['r','b'],stacked=True,normed=True)
    plt.legend(['(MC) non-protons','(MC) protons'])
    plt.xlabel('score' , fontsize=22)
    plt.ylabel('frequnecy' , fontsize=22)
    plt.title('cosmic MC classification score' , fontsize=22)
    plt.show()
    plt.savefig( "/Users/erezcohen/Desktop/test_falsepos_falseneg_" + ModelName + ".pdf" )

    score90protons      = 0.76
    N_true_positive     = len(protons[protons.pscore > score90protons])
    N_false_positive    = len(nonprotons[nonprotons.pscore > score90protons])
    true_positive       = 100*float(N_true_positive) / (N_true_positive + N_false_positive)
    false_positive      = 100*float(N_false_positive) / (N_true_positive + N_false_positive)

    N_false_negative    = len(protons[protons.pscore < score90protons])
    N_true_negative     = len(nonprotons[nonprotons.pscore < score90protons])
    false_negative      = 100*float(N_false_negative) / (N_true_negative + N_false_positive)
    true_negative       = 100*float(N_true_negative) / (N_true_negative + N_false_positive)

    print "percentages:"
    print "for score: ",score90protons
    print "true_positive: ",true_positive
    print "false_positive: ",false_positive
    print "false_negative: ",false_negative
    print "true_negative: ",true_negative


