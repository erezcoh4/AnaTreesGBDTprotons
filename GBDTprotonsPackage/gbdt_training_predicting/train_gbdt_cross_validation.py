
import ROOT ,os, sys , math
import matplotlib.pyplot as plt
import pandas as pd
sys.path.insert(0, '../../protonid')
import boost_cosmic
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()


TrainingSample = "200000_tracks_openCOSMIC_MC_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
TrainingSampleName = Path+"/TrainingSamples/trainsample_" + TrainingSample + ".csv"


# The features that we want to use for the GBDT
feature_names = [
                 'nhits','length','starty','startz','endy','endz','theta','phi', 'distlenratio',    # geometry
                 'startdqdx','enddqdx','dqdxdiff','dqdxratio','totaldqdx','averagedqdx',            # calorimetry
                 'cosmicscore','coscontscore','pidpida','pidchi'                                    # uboonecode tagging and PID
                 ]
#                 'cfdistance'                                                     # optical information - unused for open cosmic MC


param = {}
param['debug']              = flags.verbose     # just for monitoring....
'''
    use logistic regression loss, use raw prediction before logistic transformation
    since we only need the rank cosmic data parameters
'''
param['objective'] = 'binary:logistic'
param['eta']                = 0.025
param['eval_metric']        = 'error'
param['silent']             = 1
param['nthread']            = 6
param['min_child_weight']   = 4
param['max_depth']          = 13
param['gamma']              = 0.7
param['colsample_bytree']   = 0.3   # Kat: 0.5
param['subsample']          = 0.8
param['Ntrees']             = 50    # Kat: 500
param['Nfolds']             = 2     # Kat: 10
#param['reg_alpha']         = 1e-5


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
test_error,test_falsepos,test_falseneg,scores = boost_cosmic.run_cv( data , label , weight , param )


if flags.verbose>0:
    print "ran cross-validation"
    print "test_error: \n",test_error
    print "test_falsepos: \n",test_falsepos
    print "test_falseneg: \n",test_falseneg
    print "scores: \n",scores




# (C) if we are pleased, build the GBDTs
# which is training on ALL the training
# sample, with no boot-strapping
# ---------------------------------------
BoostedTree = boost_cosmic.make_bdt( data , label , weight , param )

if flags.verbose>0:
    print "done"
    print "BoostedTree: \n",BoostedTree
    print "now use the test sample and test this"



