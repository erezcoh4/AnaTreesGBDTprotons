'''
    usage:
    ---------
    python gbdt_training_predicting/calc_all_gbdt_scores.py -werez -v1
'''
from definitions import *

SampleFileName      = Path + "/FeaturesFiles/features_" + ListName + ".csv"

# create a directory for the BDT model
dirname = Path+"/PassedGBDTFiles/"+ModelName
try:
    os.makedirs( dirname )
except OSError, e:
    if e.errno != 17:
        raise


if flags.verbose>0: print "loading data from %s"%SampleFileName

data = pd.read_csv( SampleFileName )
if flags.verbose>0: print "loaded %d tracks"%len(data)

data_scores = predict_cosmic.predict_data( data , model_path + "/" + ModelName + ".bst"  , feature_names )
if flags.verbose>0: print "predicted to %d tracks"%len(data)


# all features + scores
data_scores.to_csv( PassedGBDTScoresFeatures , header=True )
print "wrote csv file of all features and all scores:\n" + PassedGBDTScoresFeatures

# run/sub/event - input to larsoft filter, or for plotting the p-score vs. number of classified tracks
data_scores[ features_names_only_scores ].to_csv( PassedGBDTAllScores , header=True )

print "wrote csv file of only r/s/e and all scores:\n" + PassedGBDTAllScores
