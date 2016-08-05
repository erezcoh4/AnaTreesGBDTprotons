# take csv data and predict proton scores

import ROOT ,os, sys , math
sys.path.insert(0, "/Users/erezcohen/larlite/UserDev/AnaTreesGBDTprotons/GBDTprotonsPackage/python_gbdt")
import boost_predict
import input_flags

flags = input_flags.get_args()
[debug,print_every_entry,files_fraction,evts_fraction,worker] = [flags.verbose,flags.print_mod,flags.files_frac,flags.ev_frac,flags.worker]


ListName   = "small_20_files_extBNB_AnalysisTrees"

#            [cos  , pion , muon , em   ]
des_scores = [0.0095 , 0.0095 , 0.0095 , 0.0095 ]

Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
CSVFilesPath = Path+"/CSVOutFiles"

# data is now pandas dataframe with all of the scores predicted
data = boost_predict.predict_data(CSVFilesPath+"/"+"features_"+ListName+".csv")


if debug>1:
    print data[['score_cosmic','score_piminus','score_muminus','score_electron']]
    print "loaded %d events from %s"%(len(data) , CSVFilesPath+"/"+"features_"+ListName+".csv")



# get pandas dataframe that is a subset of tracks that pass cuts
# choose a 95% cut for all 4 classifiers
data_pass = boost_predict.score_cut(data,des_scores[0],des_scores[1],des_scores[2],des_scores[3])





# now dump the run and event number to csv to use as input to larsoft filter
data_pass[['run','subrun','event']].to_csv(CSVFilesPath + "/" +"passedGBDT_"+ListName+".csv")
print "done, wrote csv file " + CSVFilesPath + "/" +"passedGBDT_"+ListName+".csv" + "\nwith %d p-candidate tracks of scores [%.2f,%.2f,%.2f,%.2f]"%(len(data_pass),des_scores[0],des_scores[1],des_scores[2],des_scores[3])
