/**
 * \file calcAnaTree.h
 *
 * \ingroup GBDTprotonsPackage
 *
 * \brief Class def header for a class calcAnaTree, tools for analysis of AnalysisTree information
 *
 * @author erez c. and katherine w.
 */

/** \addtogroup GBDTprotonsPackage
 
 @{*/
#ifndef calcAnaTree_H
#define calcAnaTree_H
#include "AnaTreeTools.h"
#include "PandoraNuTrack.h"
#include <ostream>
#include "TChain.h"
#define MAX_tracks 1000
#define MAX_hits 50000

/**
 \class calcAnaTree
 User defined class calcAnaTree ... these comments are used to generate
 doxygen documentation!
 */

class calcAnaTree{
    
public:
    
    // constructors
    calcAnaTree(){}
    ~calcAnaTree(){csvfile.close();}
    
    // construct w/ input and output TTree-s
    calcAnaTree (TTree * fInTree, TTree * fOutTree, TString fCSVFileName, int fdebug=0, bool fMCmode=false);
    calcAnaTree (TChain * fInChain, TTree * fOutTree, TString fCSVFileName, int fdebug=0, bool fMCmode=false){calcAnaTree((TTree*) fInChain, fOutTree, fCSVFileName,fdebug,fMCmode);};
    
    
    
 
    
    // setters
    
    void        SetInTree (TTree * tree)    {InTree = tree;};
    void       SetOutTree (TTree * tree)    {OutTree = tree;};
    void   SetCSVFileName (TString name)    {CSVFileName = name;};
    void         SetDebug (int _debug)      {debug = _debug;};
    void        SetMCMode (bool _mc_mode)   {MCmode = _mc_mode;};
    
    // getters
    TTree*          GetInTree (){return InTree;};
    TTree*         GetOutTree (){return OutTree;};
    TString   GetCSVoutHeader (){return CSVHeader;};
   
    // initializations
    void    InitInputTree ();
    void   InitOutputTree ();
    void    InitOutputCSV ();
    void        InitEntry ();
    void        InitTrack ();
    
    
    // running
    bool    get_bdt_tools (int);
    void GetInTimeFlashes ();
    void  LoopPanNuTracks ();
    bool   TrackContained (Int_t);
    void        PrintData (int);
    void releaseAddresses (){ OutTree->SetBranchStatus("*",0); };
    
    
    // csv output
    void  WriteTracks2CSV ();
    
    
    
  
    // variables
    TTree       * InTree    , * OutTree;
    TString     CSVFileName , CSVHeader;
    ofstream    csvfile;

    int         debug;  // 0 - quiet, 1 - major functionality, 2 - print out all sorts of shit
    bool        MCmode;
    
    Short_t     trkId_pandoraNu[MAX_tracks] , ntrkhits_pandoraNu[MAX_tracks][3]   , trkncosmictags_tagger_pandoraNu[MAX_tracks];
    Short_t     trkcosmictype_tagger_pandoraNu[MAX_tracks][10]  , trkncosmictags_containmenttagger_pandoraNu[MAX_tracks];
    Short_t     trkcosmictype_containmenttagger_pandoraNu[MAX_tracks][10]   , trkpidbestplane_pandoraNu[MAX_tracks];
    Short_t     hit_trkid[MAX_hits] , hit_trkKey[MAX_hits]  , hit_plane[MAX_hits]   , hit_wire[MAX_hits];
    Short_t     ntracks_pandoraNu;
    
    
    Int_t       run         , subrun    , event , primary ;
    Int_t       Nentries    , entry     , nhits;
    Int_t       Ntracks     ;
    Int_t       trkg4id_pandoraNu[MAX_tracks];
    Int_t       no_hits     , no_flashes;
    
    // MC information
    Int_t       geant_list_size         , truth_pdg[MAX_tracks];
    
    Float_t     startdqdx , enddqdx     , totaldqdx;
    Float_t     cftime    , cftimewidth , cfzcenter , cfzwidth, cfycenter , cfywidth  , cftotalpe , cfdistance;
    Float_t     trklen_pandoraNu[MAX_tracks], trkstartx_pandoraNu[MAX_tracks]   , trkstarty_pandoraNu[MAX_tracks];
    Float_t     trkstartz_pandoraNu[MAX_tracks] , trkendx_pandoraNu[MAX_tracks] , trkendy_pandoraNu[MAX_tracks];
    Float_t     trkendz_pandoraNu[MAX_tracks]   , trktheta_pandoraNu[MAX_tracks], trkphi_pandoraNu[MAX_tracks];
    Float_t     trkdqdx_pandoraNu[MAX_tracks][3][MAX_hits]  , trkresrg_pandoraNu[MAX_tracks][3][MAX_hits]   , trkxyz_pandoraNu[MAX_tracks][3][MAX_hits][3];
    Float_t     trkcosmicscore_tagger_pandoraNu[MAX_tracks][10] , trkcosmicscore_containmenttagger_pandoraNu[MAX_tracks][10];
    Float_t     trkpidchi_pandoraNu[MAX_tracks][3]  , trkpidpida_pandoraNu[MAX_tracks][3]   , flash_time[MAX_hits]  , flash_timewidth[MAX_hits] , flash_pe[MAX_hits];
    Float_t     hit_peakT[MAX_hits]     , flash_ycenter[MAX_hits]   , flash_ywidth[MAX_hits]    , flash_zcenter[MAX_hits]   , flash_zwidth[MAX_hits];
    
    
  
    
    
    
    
    
    
    // std::vector-s
    std::vector<int> goodflashidx;
    
    std::vector<PandoraNuTrack> tracks;
   
    
};

#endif
/** @} */ // end of doxygen group

