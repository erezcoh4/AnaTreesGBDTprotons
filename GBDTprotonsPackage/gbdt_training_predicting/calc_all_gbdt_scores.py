'''
    usage:
    ---------
    > python gbdt_training_predicting/calc_all_gbdt_scores.py -werez -v1
'''



import ROOT ,os, sys , math
sys.path.insert(0, '../../protonid')
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
import matplotlib.pyplot as plt
from rootpy.interactive import wait
import pandas as pd
import predict_cosmic
flags = input_flags.get_args()






ListName    = "extBNB_AnalysisTrees"
ModelName   = "cosmic_trained_only_on_mc"


if flags.verbose>4: # for debuging
        ListName    = "smallfileslist_" + ListName

if flags.worker=="erez":

    Path            = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"
    model_path      = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna/GBDTmodels"
    PlotPath        = "/Users/erezcohen/Desktop/"
                       
elif flags.worker=="uboone":

    Path            = "/uboone/app/users/ecohen/AnalysisTreesAna"
    model_path      = "/uboone/app/users/ecohen/AnalysisTreesAna/GBDTmodels"
    PlotPath        = "/uboone/app/users/ecohen/"


SampleName          = Path+"/FeaturesFiles/features_" + ListName + ".csv"
PassedGBDTFileName  = Path+"/PassedGBDTFiles" + "/" +ListName+"_"+ModelName + "/" + "passedGBDT_"+ListName+"_"+ModelName+"_allscores.csv"

try:
    os.makedirs(Path+"/PassedGBDTFiles/"+ListName+"_"+ModelName)
except OSError, e:
    if e.errno != 17:
        raise


if flags.verbose>0: print "loading data from %s"%SampleName
data = pd.read_csv( SampleName )
if flags.verbose>0: print "loaded %d tracks"%len(data)
data_scores = predict_cosmic.predict_data( data , model_path + "/" + ModelName + ".bst"  )
if flags.verbose>0: print "predicted to %d tracks"%len(data)


# now dump the run and event number to csv to use as input to larsoft filter
#data_scores[['run','subrun','event','trackid'
#             ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
#             ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
#             ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
#             ,'score' ]].to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')
data_scores.to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')

print "written csv file of all scores:\n" + PassedGBDTFileName
