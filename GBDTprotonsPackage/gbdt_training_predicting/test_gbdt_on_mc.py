

'''
    usage:
    ---------
    python gbdt_training_predicting/test_gbdt_on_mc.py -werez -v1
'''


import ROOT ,os, sys , math , time
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
sys.path.insert(0, '../../protonid')
import boost_cosmic
import predict_cosmic
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()
from prompter import yesno



'''

    application on beam-off data, training on cosmic MC
    ----------------------------------------------------
    ModelName = "cosmic_trained_only_on_mc"
    TestSample = "55650_tracks_openCOSMIC_MC_AnalysisTrees"

    application on beam-on data, training only on MC-BNB
    ----------------------------------------------------
    ModelName = "BNB_TrainedOn_only_MC_BNB"
    TestSample = "87789_tracks_MC_BNB"

'''

ModelName = "BNB_TrainedOn_only_MC_BNB" # ToDo: Change this to add training on cosmic-data as 'bad' signal as well
TestSample = "87789_tracks_MC_BNB"


Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
TestSampleName = Path+"/TestSamples/testsample_" + TestSample + ".csv"
TestSampleScoresName = Path+"/TestSamples/testsample_" + TestSample + "_with_predicted_scores.csv"
model_path = ("/Users/erezcohen/Desktop/uBoone/" if flags.worker=="erez" else "/uboone/app/users/ecohen/") +"AnalysisTreesAna/GBDTmodels"




# (A) load the test sample data and the model
# ---------------------------------------
DoPredict = yesno('predict on MC?')


if (DoPredict):

    data = pd.read_csv( TestSampleName )

    if flags.verbose>0:
        print "loaded data and model"
        print "data: \n",data

    # (B) predict on the MC data
    # ---------------------------------------
    from definitions import feature_names
    print "feature_names: ",feature_names
    data_scores = predict_cosmic.predict_data( data , model_path + "/" + ModelName + ".bst" , feature_names )
    # now dump the run and event number to csv to use as input to larsoft filter
    data_scores[['run','subrun','event','trackid'
                 ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
                 ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
                 ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
                 ,'MCpdgCode'
                 ,'p_score' ]].to_csv( TestSampleScoresName)
    print "predicted scores and saved into \n"+ TestSampleScoresName

else:
    
    data_scores = pd.read_csv( TestSampleScoresName )
    print "data with scores\n",data_scores


protons = data_scores[data_scores.MCpdgCode == 2212]
unknown = data_scores[data_scores.MCpdgCode == -9999]
muons = data_scores[abs(data_scores.MCpdgCode) == 13]
pions = data_scores[ (data_scores.MCpdgCode == 211) | (data_scores.MCpdgCode == -211) | (data_scores.MCpdgCode == 111)]
em = data_scores[(data_scores.MCpdgCode == 11) | (data_scores.MCpdgCode == -11) | (data_scores.MCpdgCode == 22)]

data_others = [ unknown , muons         , pions             , em    ]
cols_others = [ 'green' , 'black'       , 'purple'          , 'red' ]
titl_others = [ r'-9999', r'$\mu^{\pm}$', r'$\pi^{\pm,0}$'  , r'e$^{\pm}$/$\gamma$' ]



# (C) plot scores vs. actual mc code
# ---------------------------------------
bins = np.linspace(0, 1, 100)
plt.figure()
for i in range(len(data_others)):
    
    plt.subplot(2,2,i+1)
    plt.hist( protons['p_score'] , bins , color='blue' , alpha=0.5, normed = 100, label='protons')
    plt.hist( data_others[i]['p_score'] , bins , color=cols_others[i] , alpha=0.5, normed = 100, label=titl_others[i])
    plt.title("protons vs. "+titl_others[i])
    plt.xlabel("score")
    plt.ylabel("frequency [%]")
    plt.legend(loc='upper right')
    print "%d in sample of %s"%(len(data_others[i]),titl_others[i])

plt.savefig( "/Users/erezcohen/Desktop/test_score_vs_pdg_" + ModelName + ".pdf" )
plt.show()

     