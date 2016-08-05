import ROOT , os , sys


Path = "/pnfs/uboone/persistent/users/aschu/MC_BNB_Cosmic/"
FileName = "prodgenie_bnb_nu_cosmic_uboone_v05_08_00_anatree.root"


operation = "draw Q2 for contained events"



InFile = ROOT.TFile(Path+"/"+FileName+".root")
InTree = InFile.Get("analysistree/anatree")



if operation == "draw Q2 for contained events":
