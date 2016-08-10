# take csv data and predict proton scores
import ROOT ,os, sys , math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab
import matplotlib.ticker as ticker

import input_flags
flags = input_flags.get_args()
[debug,print_every_entry,files_fraction,evts_fraction,worker] = [flags.verbose,flags.print_mod,flags.files_frac,flags.ev_frac,flags.worker]


N = 1000 # number of efficiency vs. score points


ListName = "extBNB_AnalysisTrees" if debug<4 else "small_20_files_extBNB_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
ScoresName = "JustMCtraining" if debug<4 else ""
GBDTScoresFileName = Path+"/PassedGBDTFiles" + "/" +ListName+"_"+ScoresName+ "/" + "passedGBDT_"+ListName+"_"+ScoresName+"_allscores.csv"

data = pd.read_csv(GBDTScoresFileName,sep=',')

#data = pd.read_csv(GBDTScoresFileName,sep=' ',names=['run','subrun','event','trackid'
#                                             ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
#                                             ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
#                                             ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
#                                             ,'score' ])

if debug>0:
    print GBDTScoresFileName
    print "loaded %d tracks "%len(data)
    if debug>1:
        print data
        print data['score'] if debug<4 else  data['mscore_p']

NtracksTot = len(data)
score = []
purity = []
Ntracks = []

# loop to get purity. vs. score
for i in range(N):

    score.append(float(i)/N)
    #    purity.append(float(i)/N)

    data_pass = data[data.score > score[i]] if debug<4 else data[data.mscore_p > score[i]]

    purity.append(float(len(data_pass))/len(data))
    Ntracks.append(len(data_pass))
    
    if debug>1: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score[i],purity[i],len(data_pass),len(data))
    
    if debug>0 and N>10:
        if (i%(N/10)==0): print "[%.0f%%]"%(100.*float(i)/N)




# plot....
fig = pylab.figure()
fig1 = fig.add_subplot(111)
pylab.title("proton GBDT classification", fontsize=18)
pylab.plot( score , purity , "w")
pylab.xlabel(r'score', fontsize=22)

# yticks on left
locs,labels = pylab.yticks()
pylab.ylabel(r'$purity$', fontsize=22)
fig1.yaxis.set_major_formatter(ticker.FormatStrFormatter('%g'))

fig2 = fig1.twinx()
pylab.plot( score , Ntracks , "ok")

# yticks on right
locs,labels = pylab.yticks()
pylab.ylabel(r'$N_{tracks}$', fontsize=22 , labelpad=20 )
fig2.yaxis.set_major_formatter(ticker.FormatStrFormatter('%g'))
pylab.show()
fig.savefig("/Users/erezcohen/Desktop/"+ListName+"_"+ScoresName+"purity_vs_score.pdf")
