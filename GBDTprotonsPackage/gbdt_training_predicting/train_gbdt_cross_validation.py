'''
    usage:
    ---------
    python gbdt_training_predicting/train_gbdt_cross_validation.py -werez -v1
'''

import ROOT ,os, sys , math , time
import matplotlib.pyplot as plt
import pandas as pd
sys.path.insert(0, '../../protonid')
import boost_cosmic
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()




'''
    application on beam-off data, training on cosmic MC
    ----------------------------------------------------
    ModelName = "cosmic_trained_only_on_mc"
    TrainingSample = "200000_tracks_openCOSMIC_MC"

    application on beam-on data, training only on MC-BNB
    ----------------------------------------------------
    ModelName = "BNB_TrainedOn_only_MC_BNB"
    TrainingSample = "300000_tracks_MC_BNB"

'''

ModelName = "BNB_TrainedOn_only_MC_BNB" # ToDo: Change this to add training on cosmic-data as 'bad' signal as well
TrainingSample = "300000_tracks_MC_BNB"



Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
TrainingSampleName = Path+"/TrainingSamples/trainsample_" + TrainingSample + ".csv"
model_path = ("/Users/erezcohen/Desktop/uBoone/" if flags.worker=="erez" else "/uboone/app/users/ecohen/") +"AnalysisTreesAna/GBDTmodels"

from definitions import feature_names

param = {}
param['debug']              = flags.verbose     # just for monitoring....
'''
    use logistic regression loss, use raw prediction before logistic transformation
    since we only need the rank cosmic data parameters
'''
param['objective']          = 'binary:logistic'
param['eta']                = 0.025
param['eval_metric']        = 'error'
param['silent']             = 1
param['nthread']            = 6
param['min_child_weight']   = 4
param['max_depth']          = 13
param['gamma']              = 0.7
param['colsample_bytree']   = 0.5    # Kat: 0.5
param['subsample']          = 0.8
param['Ntrees']             = 500    # Kat: 500
param['Nfolds']             = 10     # Kat: 10
#param['reg_alpha']         = 1e-5



AskCrossValidation = int(input("cross validate model? \n( yes-1 / no-0 ):\n > "))
DoCrossValidation = True if AskCrossValidation==1 else False


# (A) load the data
# ---------------------------------------
data,label,weight = boost_cosmic.load_data( TrainingSampleName , feature_names )


if flags.verbose>0:
    print "loaded data"
    print "data: \n",data
    print "label: \n",label
    print "weight: \n",weight



# (B) cross-validation step
# ---------------------------------------
if DoCrossValidation:
    test_error,test_falsepos,test_falseneg,scores = boost_cosmic.run_cv( data , label , weight , param )


    if flags.verbose>0:
        print "ran cross-validation"
        print "test_error: \n",test_error
        print "test_falsepos: \n",test_falsepos
        print "test_falseneg: \n",test_falseneg
        print "scores: \n",scores




# (C) check if errors are stable
# ---------------------------------------
    plt.figure()
    plt.hist( test_error )
    plt.title("test errors")
    plt.xlabel("error")
    plt.ylabel("Frequency")
    plt.savefig( model_path + "/test_errors_" + ModelName + ".pdf" )
    plt.show()


    AskContinue = int(input("build model? \n( yes-1 / no-0 ):\n > "))
    DoContinue = True if AskContinue==1 else False


if DoCrossValidation == False: DoContinue = True


# (D) build the GBDTs which is training on the entire
# training sample, with no boot-strapping
# ---------------------------------------
if DoContinue:

    BoostedTree = boost_cosmic.make_bdt( data , label , weight , param )
    BoostedTree.save_model( model_path + "/" + ModelName + ".bst")

    if flags.verbose>0:
        print "done"
        print "BoostedTree: \n",BoostedTree
        print "now use the test sample and test this"




# plot the importances...
importances_fig = boost_cosmic.plot_importances(BoostedTree).figure
importances_fig.savefig( model_path + "/importances_" + ModelName + ".pdf" )
importances_fig.show()



file = open ( model_path + "/README_" + ModelName   , "wb" )

string =        "\nGBDT modeling \n--------------------- \n"
string+=        ("built the model to \n " + model_path + "/" + ModelName + ".bst") if DoContinue else "did not built the model..."
string+=        "\n%4d-%02d-%02d"       %time.localtime()[0:3]
string+=        "\n--------------------- \n"
string+=        "\nmodel: "             +ModelName
string+=        "\nobjective: "         +param['objective']
string+=        "\neta: "               +str(param['eta'])
string+=        "\neval_metric: "       +str(param['eval_metric'])
string+=        "\nsilent: "            +str(param['silent'])
string+=        "\nnthread: "           +str(param['nthread'])
string+=        "\nmin_child_weight: "  +str(param['min_child_weight'])
string+=        "\nmax_depth: "         +str(param['max_depth'])
string+=        "\ngamma: "             +str(param['gamma'])
string+=        "\ncolsample_bytree: "  +str(param['colsample_bytree'])
string+=        "\nsubsample: "         +str(param['subsample'])
string+=        "\nNtrees: "            +str(param['Ntrees'])
string+=        "\nNfolds: "            +str(param['Nfolds'])
string+=        "\n--------------------- \n"
if DoCrossValidation == True:
    string+=        "\terrors:\n"
    string+=        str(test_error[:])
    string+=        "\n--------------------- \n"
    string+=        "false-positive: \n"
    string+=        str(test_falsepos[:])
    string+=        "\n--------------------- \n"
    string+=        "false-negative: \n"
    string+=        str(test_falseneg[:])
string+=        "\n--------------------- \n"
string+=        "\n\n\n\n"

file.write(string)

print "done,"

if DoContinue:
    print "built the model to \n" + model_path + "/" + ModelName + ".bst"
else:
    print "did not built the model"

print "see \n" + model_path + "/README_" + ModelName
print "and \n" + model_path + "/importances_" + ModelName + ".pdf"
print model_path + "/importances_" + ModelName + ".pdf"






