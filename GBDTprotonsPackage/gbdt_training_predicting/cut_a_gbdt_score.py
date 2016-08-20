'''
    usage:
    ---------
    > python gbdt_training_predicting/cut_a_gbdt_score.py -werez
'''

import ROOT ,os, sys , math
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
import matplotlib.pyplot as plt
import pandas as pd
flags = input_flags.get_args()

score       = 0.99
ModelName   = "cosmic_trained_only_on_mc"

ListName = "small_20_files_extBNB_AnalysisTrees" if flags.verbose>5 else "extBNB_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
GBDTScoresFileName = Path+"/PassedGBDTFiles" + "/" +ListName +"_"+ModelName+ "/" + "passedGBDT_"+ListName+"_"+ModelName+"_allscores.csv"
PassedGBDTFileName = Path+"/PassedGBDTFiles" + "/" +ListName +"_"+ModelName+ "/" + "passedGBDT_"+ListName+"_"+ModelName+"_score_%.2f.csv"%score


#data = pd.read_csv(GBDTScoresFileName,sep=',') # file got from Katherine has ROIs start/end reversed

data = pd.read_csv(GBDTScoresFileName,sep=' ',names=['run','subrun','event','trackid'
                                                     ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
                                                     ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
                                                     ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
                                                     ,'score' ]) # i make these files...
if flags.verbose>0:
    print GBDTScoresFileName
    print "loaded %d tracks "%len(data)
    if flags.verbose>1:
        print data
        print data['score']

data_pass = data[data.score > score]
    
purity = float(len(data_pass))/len(data)
    
if flags.verbose>0: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score,purity,len(data_pass),len(data))
    

# now dump the run and event number to csv to use as input to larsoft filter
data_pass[['run','subrun','event','trackid'
            ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
            ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
            ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
            ,'score' ]].to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')



print "written csv file:\n" + PassedGBDTFileName
