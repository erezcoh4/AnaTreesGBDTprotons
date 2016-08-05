# take csv data and predict proton scores
import ROOT ,os, sys , math
sys.path.insert(0, "python_gbdt")
import matplotlib.pyplot as plt
from rootpy.interactive import wait
import pandas as pd
import gbdt_classification as gbdt

import input_flags
flags = input_flags.get_args()
[debug,print_every_entry,files_fraction,evts_fraction,worker] = [flags.verbose,flags.print_mod,flags.files_frac,flags.ev_frac,flags.worker]


N = 1000 # number of efficiency vs. score points


ListName = "small_20_files_extBNB_AnalysisTrees" if debug>4 else "extBNB_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
ScoresName = "CORSIKAtraining"
GBDTScoresFileName = Path+"/PassedGBDTFiles" + "/" +ListName + "/" + "passedGBDT_"+ListName+"_"+ScoresName+"_allscores.csv"

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

score = []
purity = []

# loop to get purity. vs. score
for i in range(N):
    
    score.append(float(i)/N)
    
    data_pass = data[data.mscore > score[i]]

    purity.append(float(len(data_pass))/len(data))
    
    if debug>1: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score[i],purity[i],len(data_pass),len(data))
    
    if debug>0 and N>10:
        if (i%(N/10)==0): print "[%.0f%%]"%(100.*float(i)/N)




# plot....
fig = plt.figure(3)
plt.title("proton GBDT classification: "+r'$purity \; vs. \; score$', fontsize=18)
plt.plot( score , purity , "ok")
plt.xlabel(r'score', fontsize=22)
plt.ylabel(r'$purity$', fontsize=22)
plt.show()
fig.savefig("~/Desktop/"+ListName+"_"+ScoresName+"purity_vs_score.pdf")
