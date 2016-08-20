'''
    usage:
    ---------
    > python gbdt_training_predicting/plot_gdbt_scores_distribution.py -werez
'''

import ROOT ,os, sys , math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab
import matplotlib.ticker as ticker
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()


N = 1000 # number of efficiency vs. score points

ModelName   = "cosmic_trained_only_on_mc"




Path            = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"

if flags.verbose>4: # just a small sample for flags.verboseing

    ListName    = "small_20_files_extBNB_AnalysisTrees"
    ModelName   = "CORSIKAtraining"
    GBDTScoresFileName = Path+"/PassedGBDTFiles/"+ListName+"_"+ModelName+"/passedGBDT_"+ListName+"_"+ModelName+"_allscores.csv"
    data        = pd.read_csv(GBDTScoresFileName,sep=' ',names=['run','subrun','event','trackid'
                                                         ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
                                                         ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
                                                        ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
                                                         ,'score' ])
else:

    ListName    = "extBNB_AnalysisTrees"
    GBDTScoresFileName = Path+"/PassedGBDTFiles/"+ListName+"_"+ModelName+"/passedGBDT_"+ListName+"_"+ModelName+"_allscores.csv"
#    data        = pd.read_csv(GBDTScoresFileName,sep=',')
    data        = pd.read_csv(GBDTScoresFileName,sep=' ',names=['run','subrun','event','trackid'
                                                            ,'U_start_wire','U_end_wire','U_start_time','U_end_time'
                                                            ,'V_start_wire','V_end_wire','V_start_time','V_end_time'
                                                            ,'Y_start_wire','Y_end_wire','Y_start_time','Y_end_time'
                                                            ,'score' ])




print "from \n" + GBDTScoresFileName
print "loaded %d tracks "%len(data)
if flags.verbose>1: print data

NtracksTot = len(data)
score = []
purity = []
Ntracks = []

# loop to get purity. vs. score
for i in range(N):

    score.append(float(i)/N)
    #    purity.append(float(i)/N)

    data_pass = data[data.score > score[i]]

    purity.append(float(len(data_pass))/len(data))
    Ntracks.append(len(data_pass))
    
    if flags.verbose>6: print "purity for score %.2f is %.4f (left w/ %d tracks out of %d)"%(score[i],purity[i],len(data_pass),len(data))
    
    if flags.verbose>0 and N>10:
        if (i%(N/10)==0): print "[%.0f%%]"%(100.*float(i)/N)

print "[%.0f%%]"%(100.*float(i)/N)


# plot....
#fig, ax  = pylab.figure()
fig, ax = plt.subplots()
fig1 = fig.add_subplot(111)
pylab.title("proton GBDT classification", fontsize=18)
pylab.plot( score , purity , 'w')
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



# inset
axins = inset_axes(fig2,width="50%", height="50%", loc=1)

fig2.plot( score , Ntracks , "r." )
axins.plot( score , Ntracks , "ro" )

index90 = score.index(0.90)
tracks90 = Ntracks[index90]
print "index of score 0.9: ",index90
print "number of tracks for score 0.9: ",tracks90


x1, x2, y1, y2 =  0.90, 1.0, 0, tracks90
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)


mark_inset(fig2, axins, loc1=3, loc2=4, fc="none", ec="0.5")

plt.draw()
plt.show()
fig.savefig("/Users/erezcohen/Desktop/"+ListName+"_"+ModelName+"purity_vs_score.pdf")




