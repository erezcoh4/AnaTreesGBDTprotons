import ROOT ,os, sys , math

sys.path.insert(0, '../../protonid')
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab
import matplotlib.ticker as ticker
import input_flags
import boost_cosmic
import predict_cosmic

from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from prompter import yesno
from my_tools import * 

flags = input_flags.get_args()



# The features that we want to use for the GBDT
# -------------------------
feature_names = [
                 'nhits','length','starty','startz','endy','endz','theta','phi', 'distlenratio'    # geometry
                 ,'startdqdx','enddqdx','dqdxdiff','dqdxratio','totaldqdx','averagedqdx'            # calorimetry
                 ,'cosmicscore','coscontscore','pidpida','pidchi'                                    # uboonecode tagging and PID
                 ,'cfdistance'                                                                       # optical information - unused for open cosmic MC
                 ]

features_scores_roi = [
                       'run','subrun','event','trackid'
                        ,'U_start_wire','U_start_time','U_end_wire','U_end_time'
                        ,'V_start_wire','V_start_time','V_end_wire','V_end_time'
                        ,'Y_start_wire','Y_start_time','Y_end_wire','Y_end_time'
                        ,'p_score'
                        ]

features_only_scores = [
                        'run','subrun','event','trackid','p_score'
                        ]

'''
    
    application on beam-off data, training on cosmic MC
    ----------------------------------------------------
    ListName        = "extBNB_AnalysisTrees"
    ModelName       = "cosmic_trained_only_on_mc"
    TrainingSample  = "200000_tracks_openCOSMIC_MC"
    TestSample      = "55650_tracks_openCOSMIC_MC_AnalysisTrees"
    
    application on beam-on data, training only on MC-BNB
    ----------------------------------------------------
    ListName        = "BNB_5e19POT_AnalysisTrees"
    ModelName       = "BNB_TrainedOn_only_MC_BNB"
    TrainingSample  = "300000_tracks_MC_BNB"
    TestSample      = "87789_tracks_MC_BNB"
    
    just a small sample for debugging
    ----------------------------------------------------
    ListName    = "small_20_files_extBNB_AnalysisTrees"
    ModelName   = "CORSIKAtraining"
    
'''



# samples names
# -------------------------
TrainingSample  = "300000_tracks_MC_BNB"
TestSample      = "87789_tracks_MC_BNB"
ListName        = "BNB_5e19POT_AnalysisTrees"
ModelName       = "BNB_TrainedOn_only_MC_BNB"




# paths
# -------------------------
if flags.worker=="erez":
    
    Path            = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"
    PlotPath        = "/Users/erezcohen/Desktop/"

elif flags.worker=="uboone":
    
    Path            = "/uboone/app/users/ecohen/AnalysisTreesAna"
    PlotPath        = "/uboone/app/users/ecohen/"


model_path = Path + "/GBDTmodels"
dirname    = Path+"/PassedGBDTFiles/"+ModelName
passedGBDTpath = Path + "/PassedGBDTFiles" 



# files names
# -------------------------
PassedGBDTAllScores         = Path+"/PassedGBDTFiles" + "/" +ModelName + "/" + "passedGBDT_"+ListName+"_"+ModelName+"_allscores_only_rse.csv"
PassedGBDTScoresFeatures    = Path+"/PassedGBDTFiles" + "/" +ModelName + "/" + "passedGBDT_"+ListName+"_"+ModelName+"_allscores_features.csv"

