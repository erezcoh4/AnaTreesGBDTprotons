import ROOT
import os, sys , math , os.path
from ROOT import TPlots
import larlite
from ROOT import PandoraNuTrack
from rootpy.interactive import wait
sys.path.insert(0, '/Users/erezcohen/larlite/UserDev/mySoftware/MySoftwarePackage/mac')
import Initiation as init , GeneralPlot as gp, input_flags
init.createnewdir()
flags = input_flags.get_args()

#ROOT.gStyle.SetOptStat(0000)

ana = TPlots("/Users/erezcohen/Desktop/uBoone/AnalysisTreesAna/BDTanaFiles/BDTana_openCOSMIC_MC_AnalysisTrees.root","GBDTTree")
var = flags.variable
cut = flags.cut


if flags.operation == 12:
    
    print "usage: \npython ana_COSMICMCtracks.py -var=<default='NNeighborTracks'> --operation=<default='short-tracks'>\n\n"
    flags.operation = 'short-tracks'
if var == 12:
    
    print "usage: \npython ana_COSMICMCtracks.py -var=<default='NNeighborTracks'> --operation=<default='short-tracks'>\n\n"
    var = 'NNeighborTracks'


c   = ana.CreateCanvas(var)


def draw_protons_vs_else (nbins , xlow , xup , xtit , log_scale = False ):
    
        hAll        = ana.H1( 'tracks.'+ var , cut , "hist" , nbins , xlow , xup , "" , xtit , "" , 1 , 1 , 3005 )
    
        hProtons    = ana.H1( 'tracks.'+ var , ROOT.TCut("tracks.MCpdgCode==2212") , "hist same" , nbins , xlow , xup , "" , xtit , "" , 4 , 38 , 3001 )
    
        h9999       = ana.H1( 'tracks.'+ var , ROOT.TCut("tracks.MCpdgCode==-9999") , "hist same" , nbins , xlow , xup , "" , xtit , "" , 2 , 46 , 3007 )

        if log_scale: c.SetLogy()

        ana.AddLegend(hAll , "all" , hProtons , "protons" , h9999 , "-9999" , "f")

        return c


def draw_2d (vx , nbinsx , xlow , xup , xtit , vy , nbinsy , ylow , yup , ytit ):

        c.Divide(3,1)
        
        c.cd(1)
        hAll        = ana.H2( 'tracks.'+ vx , 'tracks.'+ vy , cut , "col"
                             , nbinsx , xlow , xup , nbinsy , ylow , yup , "all" , xtit , ytit , 1 , 20 , 0.1 )
                             
        c.cd(2)
        hProtons    = ana.H2( 'tracks.'+ vx , 'tracks.'+ vy , ROOT.TCut("tracks.MCpdgCode==2212") , "col"
                                 , nbinsx , xlow , xup , nbinsy , ylow , yup , "protons" , xtit , ytit , 4 , 20 , 0.3 )

        c.cd(3)
        h9999       = ana.H2( 'tracks.'+ vx , 'tracks.'+ vy , ROOT.TCut("tracks.MCpdgCode==-9999") , "col"
                     , nbinsx , xlow , xup , nbinsy , ylow , yup , "-9999" , xtit , ytit , 2 , 21 , 0.3 )







if flags.operation == 'short-tracks':
    
    
    
    if var == 'NNeighborTracks':
        
        c = draw_protons_vs_else ( 40 , -1 , 11 , "number of neighboring tracks" , True )


    elif var == 'NeighborTracksAngles':
     
        c = draw_protons_vs_else ( 100 , -1 , 181 , "angles of neighboring tracks [deg.]" )


    elif var == 'NeighborTracksDistance':

        c = draw_protons_vs_else ( 60 , 0 , 10 , "distance of neighboring tracks [cm]" )


    elif var == 'NeighborTracksDistanceVsAngles':
    
        draw_2d ( 'NeighborTracksDistance' , 60 , 0 , 10 , "distance of neighboring tracks [cm]"
                 , 'NeighborTracksAngles' , 100 , -1 , 181 , "angles of neighboring tracks [deg.]" )
    
    
    elif var == 'Ntracks':
        
        ana.H1( var , cut , "hist" , 100 , -1 , 20 , "" , "number of reconstructed tracks in event" )
        c.SetLogy()

    c.Update()
    wait()
    c.SaveAs(init.dirname()+"/cosmic_mc_tracks_"+var+".pdf")
