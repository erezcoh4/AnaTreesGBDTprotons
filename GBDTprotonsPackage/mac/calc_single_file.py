import ROOT , os , sys
from ROOT import calcAnaTree

print_every_entry = 100
evts_fraction = 1
debug = 1  # 0 - quiet, 1 - major functionality, 2 - print out all sorts of shit


Path = "$ANALYSISTREES_ANA"
FileName = "ana_hist_bnb"






InFile = ROOT.TFile(Path+"/example_AnaTrees/"+FileName+".root")
InTree = InFile.Get("analysistree/anatree")
OutFile = ROOT.TFile(Path + "/BDTanaFiles/"+"BDTana_"+FileName+".root","recreate")
OutTree = ROOT.TTree("GBDTTree","physical variables taken from pandoraNu tracking algorithm")


calc = calcAnaTree( InTree , OutTree , debug )


CSVfile = open(Path+"/CSVOutFiles/"+"features_"+FileName+".csv", "wb")
CSVfile.write(str(calc.GetCSVoutHeader()) + "\n")



for entry in range(int(evts_fraction*(calc.Nentries))):
    
    calc.get_bdt_tools( entry )
    
    if len(calc.tracks)>0:
        
        if (entry%print_every_entry == 0):
            calc.PrintData( entry )
        
        for feature in calc.GetCSVdata():
            CSVfile.write(str(feature) + ",")
        
        CSVfile.write("\n")


print "fille %d events from %s" % (OutTree.GetEntries(),file_name)
print "wrote root file " + OutFile.GetName() + ", with %d entries"%OutTree.GetEntries()
print "wrote csv file " + CSVfile.name

OutTree.Write()
OutFile.Close()


