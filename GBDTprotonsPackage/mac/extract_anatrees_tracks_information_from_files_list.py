import ROOT , os , sys, larlite, argparse
from ROOT import *
from ROOT import calcAnaTree
from ROOT import AnaTreeTools
sys.path.insert(0, '../../mySoftware/MySoftwarePackage/mac')
import input_flags
flags = input_flags.get_args()


Path            = "/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna"    if flags.worker=="erez" else "/uboone/app/users/ecohen/AnalysisTreesAna"
ListsPath       = Path+"/lists"
AnaPath         = Path+"/BDTanaFiles"
CSVFilesPath    = Path+"/FeaturesFiles"
ListName        = "openCOSMIC_MC_AnalysisTrees"                         if flags.DataType=='MC' else "extBNB_AnalysisTrees"
MCmode          = True if flags.DataType=='MC' else False
#"small_20_files_extBNB_AnalysisTrees" # "extBNB_AnalysisTrees" # openCOSMIC_MC_AnalysisTrees
tools           = AnaTreeTools()


if flags.verbose>0: print "\nreading list of files..."
with open(ListsPath + "/" + ListName + ".list") as f:
    files = f.read().splitlines()
if flags.verbose>4: print files




CSVfileName = CSVFilesPath+"/"+"features_"+ListName+".csv"
AnafileName = AnaPath + "/"+"BDTana_" + ListName + ".root"



in_chain = ROOT.TChain("analysistree/anatree");


for i in range(int(flags.files_frac*len(files))):
    if flags.verbose>1: print "file %d size is %.2f MB"%(i,float(os.path.getsize(files[i])/1048576))
    if float(os.path.getsize(files[i])/1048576) > 0.1 :
        in_chain.Add(files[i])
if flags.verbose>0: print "input chain entries from",int(flags.files_frac*len(files)),"files: ", in_chain.GetEntries()


Nentries = in_chain.GetEntries()


OutFile     = ROOT.TFile(AnafileName,"recreate")
OutTree     = ROOT.TTree("GBDTTree","physical variables per event")
TracksTree  = ROOT.TTree("TacksTree","pandoraNu tracks")


if flags.verbose>1: print in_chain,OutTree,TracksTree
    
calc = calcAnaTree( in_chain , OutTree , TracksTree , CSVfileName , flags.verbose , MCmode )

counter = 0
for entry in range(int(flags.evnts_frac*(Nentries))):
        
    calc.get_bdt_tools( entry )
        
        
    if calc.Ntracks>0:
        counter += calc.Ntracks
        
        if (entry%flags.print_mod == 0):
            calc.PrintData( entry )
        
        calc.WriteTracks2CSV();

        if flags.verbose>1: print "wrote %d more contained tracks (%d tracks in total) to features csv file"%(calc.Ntracks,counter)



    
if flags.verbose>0: print "extracted %d events\nout-tree has %d events\n\n" % (int(flags.evnts_frac*(Nentries)),OutTree.GetEntries())

TracksTree.Write()
OutTree.Write()
OutFile.Close()


print "wrote csv file with %d tracks (%.2f MB):\n"%(counter,float(os.path.getsize(CSVfileName)/1048576.0)) + CSVfileName
print "wrote root file  (%.2f MB):\n"%float(os.path.getsize(AnafileName)/1048576.0) + AnafileName


