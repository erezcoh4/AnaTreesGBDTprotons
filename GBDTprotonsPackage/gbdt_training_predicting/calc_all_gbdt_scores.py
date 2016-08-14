# take csv data and predict proton scores

import ROOT ,os, sys , math
sys.path.insert(0, "/Users/erezcohen/larlite/UserDev/protonid")
import gbdt_classification as gbdt
import input_flags
import matplotlib.pyplot as plt
from rootpy.interactive import wait
import pandas as pd
import predict_cosmic
flags = input_flags.get_args()
[debug,print_every_entry,files_fraction,evts_fraction,worker] = [flags.verbose,flags.print_mod,flags.files_frac,flags.ev_frac,flags.worker]


ListName = "small_20_files_extBNB_AnalysisTrees" if debug>4 else "extBNB_AnalysisTrees" # small_20_files_extBNB_AnalysisTrees is for monitoring....
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
ScoresName = "CORSIKAtraining"
try:
    os.makedirs(Path+"/PassedGBDTFiles/"+ListName+"_"+ScoresName)
except OSError, e:
    if e.errno != 17:
        raise

inputCSVFileName = Path+"/CSVOutFiles"+"/"+"features_"+ListName+".csv"
PlotPath = "/Users/erezcohen/Desktop/" if worker=="erez" else "/uboone/app/users/ecohen/"
PassedGBDTFileName = Path+"/PassedGBDTFiles" + "/" +ListName + "/" + "passedGBDT_"+ListName+"_"+ScoresName+"_allscores.csv"

if debug>0: print "loading data from %s"%inputCSVFileName
data = pd.read_csv(inputCSVFileName)
if debug>0: print "loaded %d tracks"%len(data)
data_scores = predict_cosmic.predict_data( data )
if debug>0: print "predicted to %d tracks"%len(data)


# now dump the run and event number to csv to use as input to larsoft filter
data_scores[['run','subrun','event','trackid'
             ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
             ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
             ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
             ,'mscore' ]].to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')

print "written csv file of all scores:\n" + PassedGBDTFileName
