# take csv data and predict proton scores

import ROOT ,os, sys , math
sys.path.insert(0, "python_gbdt")
import gbdt_classification as gbdt
import input_flags
import matplotlib.pyplot as plt
from rootpy.interactive import wait
import pandas as pd
import predict_multi
flags = input_flags.get_args()
[debug,print_every_entry,files_fraction,evts_fraction,worker] = [flags.verbose,flags.print_mod,flags.files_frac,flags.ev_frac,flags.worker]

score = 0.95

ListName = "small_20_files_extBNB_AnalysisTrees" if debug>4 else "extBNB_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
ScoresName = "CORSIKAtraining"
PassedGBDTFileName = Path+"/PassedGBDTFiles" + "/" +ListName + "/" + "passedGBDT_"+ListName+"_"+ScoresName+"_score_%.2f.csv"%score

data = pd.read_csv(GBDTScoresFileName,sep=' ',names=['run','subrun','event','trackid'
                                                     ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
                                                     ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
                                                     ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
                                                     ,'mscore' ])
if debug>0:
    print GBDTScoresFileName
    print "loaded %d tracks "%len(data)
    if debug>1:
        print data
        print data['mscore']

data_pass = data[data.mscore > score]
    
purity = float(len(data_pass))/len(data)
    
if debug>0: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score,purity,len(data_pass),len(data))
    

# now dump the run and event number to csv to use as input to larsoft filter
data_pass[['run','subrun','event','trackid'
            ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
            ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
            ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
            ,'mscore' ]].to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')



print "written csv file:\n" + PassedGBDTFileName
