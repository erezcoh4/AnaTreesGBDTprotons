'''
    usage:
    ---------
    python gbdt_training_predicting/join_passedGBDTprotons_with_selection2muons.py
'''

import ROOT ,os, sys , math, pandas as pd,  csv
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()

score               = 0.90
ModelName           = "cosmic_trained_only_on_mc"
ListName            = "extBNB_AnalysisTrees"
PassedGBDTPath      = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"
PassedGBDTListName  = PassedGBDTPath + "/PassedGBDTFiles" + "/" +ListName +"_"+ModelName+ "/" + "passedGBDT_"+ListName+"_"+ModelName+"_score_%.2f_just_events.csv"%score
NuSelectionPath     = "/Users/erezcohen/Desktop/uBoone/Lists/NeutrinoSelection2"
NuSelectionListName = NuSelectionPath + "/BeamOffData_pandoraNu_pandoraNu.csv"
IntersectionPath    = "/Users/erezcohen/Desktop/uBoone/Lists/muon_proton_intersection"
IntersectionListName= IntersectionPath + "/mu_p_score_%.2f_intersection.csv"%score


with open(PassedGBDTListName, 'rb') as PassedGBDTcsvfile:
    reader = csv.reader(PassedGBDTcsvfile, delimiter=' ', skipinitialspace=True)
    header = next(reader)
    PassedGBDTEventsList = [dict(zip(header, map(int, row))) for row in reader]


with open(NuSelectionListName, 'rb') as NuSelectioncsvfile:
    reader = csv.reader(NuSelectioncsvfile, delimiter=' ', skipinitialspace=True)
    header = next(reader)
    NuSelectionEventsList = [dict(zip(header, map(int, row))) for row in reader]


def search(list,run,subrun,event):
    for e in list:
        if e['run'] == run and e['subrun'] == subrun and e['event'] == event:
            return e
    return False


f = open(IntersectionListName,'w')
f.write("run subrun event ivtx-NuSel itrk-NuSelMuon itrk-GBDTproton \n")

for event_with_proton in PassedGBDTEventsList:
    event_with_muon = search (NuSelectionEventsList , event_with_proton['run'] , event_with_proton['subrun'] , event_with_proton['event'])
    if (event_with_muon):
        data_string = "%d %d %d %d %d %d\n"%(event_with_proton['run'] , event_with_proton['subrun'] , event_with_proton['event'] ,
                                             event_with_muon['ivtx'] , event_with_muon['trkindex[ivtx][itrk]'] , event_with_proton['trackid'])
        f.write( data_string )
        print "written to file: ",data_string

print "done, written file \n"+IntersectionListName
