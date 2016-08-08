import ROOT ,os, sys , math
import matplotlib.pyplot as plt
import pandas as pd
import input_flags
from pprint import pprint
flags = input_flags.get_args()
from ipywidgets import interact

plt.rcParams.update({'font.size': 20, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})

"features_openCOSMIC_MC_AnalysisTrees.csv"

ListName = "openCOSMIC_MC_AnalysisTrees"
Path = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"

inputCSVFileName = Path+"/CSVOutFiles"+"/"+"features_"+ListName+".csv"

if flags.verbose>0: print "loading data from %s"%inputCSVFileName
data = pd.read_csv(inputCSVFileName)
if flags.verbose>0: print "loaded %d tracks"%len(data)

grouped=data.groupby(['MCpdgCode'])
pprint(type(grouped))
pprint(grouped)

series=grouped.size()

print(type(series))
print(series)
print
print ("protons data")
protons=series[2212]
print(type(protons))
print("Size of protons data:"+str(protons))



def by_particle(code=2212):
    status_counts = df.groupby(['MCpdgCode']).size().ix[code]
    
    cmap = plt.cm.summer
    colors = cmap(np.linspace(0., 1., len(status_counts)))
    
    fig, ax = plt.subplots(figsize=(10.0, 10.0))
    
    ax.pie(status_counts, autopct=lambda p: '{0:.1f}% ({1:})'. format(p, int(p * sum(status_counts) / 100)),
    labels=status_counts.index, colors=colors)
    fig.suptitle("{}".format(code))
    plt.show()


i = interact(by_particle, code=list(data['MCpdgCode'].dropna().unique()))
