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

# number of efficiency vs. score points
N = 10

# paths and names
ListName = "small_20_files_extBNB_AnalysisTrees" if debug>2 else "extBNB_AnalysisTrees"


Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
try:
    os.makedirs(Path+"/PassedGBDTFiles/"+ListName)
except OSError, e:
    if e.errno != 17:
        raise # This was not a "directory exist" error..
inputCSVFileName = Path+"/CSVOutFiles"+"/"+"features_"+ListName+".csv"
PlotPath = "/Users/erezcohen/Desktop/" if worker=="erez" else "/uboone/app/users/ecohen/"
GBDTScoresFileName = Path+"/PassedGBDTFiles" + "/" +ListName + "/" + "passedGBDT_"+ListName+"_scores.csv"

if debug>0: print "loading data from %s"%inputCSVFileName
data = pd.read_csv(inputCSVFileName)
if debug>0: print "loaded %d tracks"%len(data)

data_scores = predict_multi.predict_data(data)
data_scores[['run','subrun','event','mscore_mu','mscore_pi','mscore_em','mscore_cos','mscore_p']].to_csv(GBDTScoresFileName)
if debug>0: print "pluged scores into %s"%GBDTScoresFileName

score = []
efficiency = []

# loop to get eff. vs. score
for i in range(N):
    
    score.append(100*(float(i)/N))

    efficiency.append(100*gbdt.classify( data_scores , debug , Path , ListName , score[i] ))
    
    if debug>1: print "efficiency for score %.2f is %.2f"%(score[i],efficiency[i])
    
    if debug>0 and N>10:
        if (i%(N/10)==0): print "[%.0f%%]"%(100.*float(i)/N)



# plot....
fig = plt.figure(3)
plt.title("proton GBDT classification: "+r'$\epsilon \; vs. \; score$', fontsize=18)
plt.plot( score , efficiency , "ok")
plt.xlabel(r'score [%]', fontsize=22)
plt.ylabel(r'$\epsilon$ [%]', fontsize=22)

             
plt.show()
fig.savefig(PlotPath+'efficiency_vs_score.pdf')
