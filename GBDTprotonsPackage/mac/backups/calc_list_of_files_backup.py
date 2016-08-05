import ROOT , os , sys, larlite
from ROOT import *
from ROOT import calcAnaTree
from ROOT import AnaTreeTools


print_every_entry = 1
evts_fraction = 0.01
debug = 1  # 0 - quiet, 1 - major functionality, 2 - print out all sorts of shit

Path = "/uboone/app/users/ecohen/AnalysisTreesAna"
ListsPath = Path+"/lists"
AnaPath = Path+"/BDTanaFiles"
CSVFilesPath = Path+"/CSVOutFiles"
ListName = "example_list_of_mcc7_anatrees_uboone"

tools = AnaTreeTools()
with open(ListsPath + "/" + ListName + ".list") as f:
    files = f.read().splitlines()

OutFile = ROOT.TFile(AnaPath + "/"+"BDTana_" + ListName + ".root","recreate")
OutTree = ROOT.TTree("GBDTTree","physical variables taken from pandoraNu tracking algorithm")
OutTree.Write()
OutFile.Close()

print files
print OutFile



c = calcAnaTree()
CSVfile = open(CSVFilesPath+"/"+"features_"+ListName+".csv", "wb")
CSVfile.write(str(c.GetCSVoutHeader()) + "\n")



for i in range(len(files)):
    print "file: ", files[i]
    in_file = ROOT.TFile(files[i])

    in_tree = in_file.Get("analysistree/anatree")
    out_file = ROOT.TFile(AnaPath + "/"+"BDTana_" + ListName + ".root","update")
    out_tree = out_file.Get("GBDTTree")
 
    print in_tree,out_tree,debug

    calc = calcAnaTree( in_tree , out_tree , debug )
    for entry in range(int(evts_fraction*(calc.Nentries))):

        calc.get_bdt_tools( entry )
    

        if calc.ntracks_pandoraNu>0:


            if (entry%print_every_entry == 1):
                calc.PrintData( entry )

            for feature in calc.GetCSVdata():
                CSVfile.write(str(feature) + ",")
        
            CSVfile.write("\n")

    calc.releaseAddresses()


    if debug>0: print "filled %d events from %s\nout_tree has %d entries\n---------------------" % (in_tree.GetEntries(),files[i],out_tree.GetEntries())
    out_tree.Write()
    out_file.Close()
    in_file.Close()


print "wrote csv file " + CSVfile.name



