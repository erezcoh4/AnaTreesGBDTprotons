'''
    usage:
    ---------
    > python gbdt_training_predicting/gbdt_plots.py --option=importances
'''

import sys
import pandas as pd
import xgboost as xgb
import operator
from matplotlib import pylab as plt
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()



feature_names = [
                 r'$N_{hits}$',r'$length$',r'$y_{start}$',r'$z_{start}$',r'$y_{end}$',r'$z_{end}$',r'$\theta$',r'$\phi$', r'${|\vec{d}|/l}$',
                 r'$dq/dx_{start}$',r'$dq/dx_{end}$',r'$\Delta dq/dx$',r'$dq/dx_{ratio}$',r'$dq/dx_{total}$',r'$dq/dx_{average}$',
                 r'$score_{cosmic}$',r'$score_{contained-cosmic}$',r'${PID_{a}}$',r'${PID_\chi}$'
                 ]

ModelName   = "cosmic_trained_only_on_mc"
model_path  = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna/GBDTmodels"

Booster = xgb.Booster(model_file = model_path + "/" + ModelName + ".bst")


if flags.option == "importances":

    outfile = open('xgb.fmap', 'w')
    i = 0
    for feat in feature_names:
        outfile.write('{0}\t{1}\tq\n'.format(i, feat))
        i = i + 1
    outfile.close()


    importance = Booster.get_fscore(fmap='xgb.fmap')
    importance = sorted(importance.items(), key=operator.itemgetter(1))

    df = pd.DataFrame(importance, columns=['feature', 'fscore'])
    df['fscore'] = df['fscore'] / df['fscore'].sum()

    plt.figure()
    df.plot()
    df.plot(kind='barh', x='feature', y='fscore', legend=False, figsize=(6, 10))
    plt.title('XGBoost Feature Importance',fontsize=22)
    plt.xlabel('relative importance',fontsize=22)
    plt.show()
    plt.gcf().savefig('/Users/erezcohen/Desktop/importances'+ModelName+'.pdf')