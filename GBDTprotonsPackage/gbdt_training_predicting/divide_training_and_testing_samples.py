'''
    usage:
    ---------
    > python gbdt_training_predicting/divide_training_and_testing_samples.py -werez -v1
'''

import sys
import pandas as pd
import random
sys.path.insert(0, '/Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()




FileToDivide  = "openCOSMIC_MC_AnalysisTrees"
NumberToTrain = 200000

Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna" if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
DivideFileName = Path+"/FeaturesFiles/features_" + FileToDivide + ".csv"

data = pd.read_csv(DivideFileName)
Total = len(data)
TrainFileName = Path+"/TrainingSamples/trainsample_" + "%d_tracks_"%NumberToTrain + FileToDivide + ".csv"
TestFileName = Path+"/TestSamples/testsample_" + "%d_tracks_"%(Total-NumberToTrain) + FileToDivide + ".csv"
if (flags.verbose>0): print "\n%d events in the sample, dividing to %d for training and %d for testing\n"%(Total,NumberToTrain,Total-NumberToTrain)


rows         = random.sample( data.index, NumberToTrain )
data_train   = data.ix[rows]
data_test    = data.drop(rows)


data_train.to_csv(TrainFileName,index=False)
data_test.to_csv(TestFileName,index=False)

if (flags.verbose>0): print "done, generated the files: \n",TrainFileName,"\n",TestFileName

