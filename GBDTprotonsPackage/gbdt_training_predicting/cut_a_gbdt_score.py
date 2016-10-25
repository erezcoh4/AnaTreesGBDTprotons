'''
    usage:
    ---------
    python gbdt_training_predicting/cut_a_gbdt_score.py -werez
'''
#import ROOT ,os, sys , math
#sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
#import input_flags
#import pandas as pd
#flags = input_flags.get_args()
from definitions import *

score = 0.99

#Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
#GBDTScoresFileName = Path+"/PassedGBDTFiles" + "/" +ListName +"_"+ModelName+ "/" + "passedGBDT_"+ListName+"_"+ModelName+"_allscores.csv"
PassedGBDTFileName = Path+"/PassedGBDTFiles" + "/" +ListName +"_"+ModelName+ "/" + "passedGBDT_"+ListName+"_"+ModelName+"_score_%.2f.csv"%score


#data = pd.read_csv(GBDTScoresFileName,sep=',') # file got from Katherine has ROIs start/end reversed

data = pd.read_csv( PassedGBDTAllScores )
if flags.verbose>0:
    print PassedGBDTAllScores
    print "loaded %d tracks "%len(data)
    if flags.verbose>1:
        print data
        print data['score']

data_pass = data[data.p_score > score]
    
purity = float(len(data_pass))/len(data)
    
if flags.verbose>0: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score,purity,len(data_pass),len(data))
    

# now dump the run and event number to csv to use as input to larsoft filter
# use only the relevant variables (the ones that we actually need for later)
data_pass.to_csv(PassedGBDTFileName,header=False,index=False,sep=' ')



print "written csv file:\n" + PassedGBDTFileName
