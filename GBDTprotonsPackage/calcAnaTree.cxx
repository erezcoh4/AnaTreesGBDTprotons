#ifndef calcAnaTree_CXX
#define calcAnaTree_CXX

#include "calcAnaTree.h"


// main event loop
//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
bool calcAnaTree::get_bdt_tools (int entry){ // main event loop....
    
    InitEntry();
    InTree -> GetEntry(entry);

    GetInTimeFlashes();
    LoopPanNuTracks();
    
    OutTree -> Fill();
    return true;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
calcAnaTree::calcAnaTree( TTree * fInTree, TTree * fOutTree, TString fCSVFileName, int fdebug){
    
    SetInTree(fInTree);
    SetOutTree(fOutTree);
    SetDebug(fdebug);
    SetCSVFileName (fCSVFileName);
    InitInputTree();
    InitOutputTree();
    InitOutputCSV();
    
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::InitInputTree(){
    
    InTree -> SetBranchAddress("run"                                            , &run);
    InTree -> SetBranchAddress("subrun"                                         , &subrun);
    InTree -> SetBranchAddress("event"                                          , &event);

    InTree -> SetBranchAddress("ntracks_pandoraNu"                              , &ntracks_pandoraNu);
    InTree -> SetBranchAddress("trkId_pandoraNu"                                , &trkId_pandoraNu);
    InTree -> SetBranchAddress("trkg4id_pandoraNu"                              , &trkg4id_pandoraNu);
    InTree -> SetBranchAddress("trklen_pandoraNu"                               , &trklen_pandoraNu);
    InTree -> SetBranchAddress("trkstartx_pandoraNu"                            , &trkstartx_pandoraNu);
    InTree -> SetBranchAddress("trkstarty_pandoraNu"                            , &trkstarty_pandoraNu);
    InTree -> SetBranchAddress("trkstartz_pandoraNu"                            , &trkstartz_pandoraNu);
    InTree -> SetBranchAddress("trkendx_pandoraNu"                              , &trkendx_pandoraNu);
    InTree -> SetBranchAddress("trkendy_pandoraNu"                              , &trkendy_pandoraNu);
    InTree -> SetBranchAddress("trkendz_pandoraNu"                              , &trkendz_pandoraNu);
    InTree -> SetBranchAddress("trktheta_pandoraNu"                             , &trktheta_pandoraNu);
    InTree -> SetBranchAddress("trkphi_pandoraNu"                               , &trkphi_pandoraNu);
    InTree -> SetBranchAddress("ntrkhits_pandoraNu"                             , &ntrkhits_pandoraNu);
    InTree -> SetBranchAddress("trkdqdx_pandoraNu"                              , &trkdqdx_pandoraNu);
    InTree -> SetBranchAddress("trkresrg_pandoraNu"                             , &trkresrg_pandoraNu);
    InTree -> SetBranchAddress("trkxyz_pandoraNu"                               , &trkxyz_pandoraNu);
    InTree -> SetBranchAddress("trkncosmictags_tagger_pandoraNu"                , &trkncosmictags_tagger_pandoraNu);
    InTree -> SetBranchAddress("trkcosmicscore_tagger_pandoraNu"                , &trkcosmicscore_tagger_pandoraNu);
    InTree -> SetBranchAddress("trkcosmictype_tagger_pandoraNu"                 , &trkcosmictype_tagger_pandoraNu);
    InTree -> SetBranchAddress("trkcosmicscore_containmenttagger_pandoraNu"     , &trkcosmicscore_containmenttagger_pandoraNu);
    InTree -> SetBranchAddress("trkcosmictype_containmenttagger_pandoraNu"      , &trkcosmictype_containmenttagger_pandoraNu);
    InTree -> SetBranchAddress("trkpidchi_pandoraNu"                            , &trkpidchi_pandoraNu);
    InTree -> SetBranchAddress("trkpidpida_pandoraNu"                           , &trkpidpida_pandoraNu);
    InTree -> SetBranchAddress("trkpidbestplane_pandoraNu"                      , &trkpidbestplane_pandoraNu);

    InTree -> SetBranchAddress("no_hits"                                        , &no_hits);
    InTree -> SetBranchAddress("hit_plane"                                      , &hit_plane);
    InTree -> SetBranchAddress("hit_wire"                                       , &hit_wire);
    InTree -> SetBranchAddress("hit_peakT"                                      , &hit_peakT);
    InTree -> SetBranchAddress("hit_trkid"                                      , &hit_trkid);
    InTree -> SetBranchAddress("hit_trkKey"                                     , &hit_trkKey);

    InTree -> SetBranchAddress("no_flashes"                                     , &no_flashes);
    InTree -> SetBranchAddress("flash_time"                                     , &flash_time);
    InTree -> SetBranchAddress("flash_timewidth"                                , &flash_timewidth);
    InTree -> SetBranchAddress("flash_pe"                                       , &flash_pe);
    InTree -> SetBranchAddress("flash_ycenter"                                  , &flash_ycenter);
    InTree -> SetBranchAddress("flash_ywidth"                                   , &flash_ywidth);
    InTree -> SetBranchAddress("flash_zcenter"                                  , &flash_zcenter);
    InTree -> SetBranchAddress("flash_zwidth"                                   , &flash_zwidth);
    
    
    Nentries = InTree -> GetEntries();
    if(debug>1) cout << "calcAnaTree input-tree ready (" << InTree -> GetName() <<"), " <<  Nentries << " entries" << endl;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::InitOutputTree(){
    
    // Integer branches
    OutTree -> Branch("run"         ,&run               ,"run/I");
    OutTree -> Branch("subrun"      ,&subrun            ,"subrun/I");
    OutTree -> Branch("event"       ,&event             ,"event/I");
    OutTree -> Branch("Ntracks"     ,&Ntracks           ,"Ntracks/I"); // number of contained tracks, not ntracks_pandoraNu...
    
    
    // Float_t branches
    OutTree -> Branch("tracks"      ,&tracks);
    
    if(debug>1) cout << "calcAnaTree output-tree ready (" << OutTree -> GetTitle() << endl;
}


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::InitOutputCSV(){
    
    csvfile.open(CSVFileName);
    
    CSVHeader =
     TString("run,subrun,event,trackid")
    +TString(",flip,nhits,length")
    +TString(",startx,starty,startz")
    +TString(",endx,endy,endz")
    +TString(",theta,phi,distlenratio")
    +TString(",startdqdx,enddqdx")
    +TString(",dqdxdiff,dqdxratio,totaldqdx,averagedqdx")
    +TString(",cosmicscore,coscontscore,pidpida,pidchi")
    +TString(",cftime,cftimewidth,cfzcenter,cfzwidth")
    +TString(",cfycenter,cfywidth,cftotalpe,cfdistance")
    +TString(",U_start_wire,U_start_time,U_end_wire,U_end_time")
    +TString(",V_start_wire,V_start_time,V_end_wire,V_end_time")
    +TString(",Y_start_wire,Y_start_time,Y_end_wire,Y_end_time");

    csvfile << CSVHeader << endl;
}


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::InitEntry(){
    
    if (!goodflashidx.empty())  goodflashidx.clear();
    if (!tracks.empty())        tracks.clear();

    Ntracks = ntracks_pandoraNu = 0;
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::InitTrack(){
    totaldqdx  = startdqdx = enddqdx = nhits = 0;

}


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::GetInTimeFlashes(){
    if(debug>3) Printf("GetInTimeFlashes of %d flashes",no_flashes);
    // get a list of in-time flashes for the event
    if(no_flashes > 0) {
        if (!goodflashidx.empty())  goodflashidx.clear();
        if(debug>3) {SHOW(goodflashidx.size()); Printf("looping in if(no_flashes > 0) on no_flashes");}

        for(int i=0; i < no_flashes; i++){
            if(debug>4) {SHOW3(i,flash_time[i],flash_pe[i]);}
            if((0.0 < flash_time[i]) && (flash_time[i] < 10.0) && (6.5 < flash_pe[i])){
                goodflashidx.push_back(i);
                if(debug>3) {SHOW(i);SHOW(goodflashidx.size());}
            }
        }
    }
    if(debug>3) {
        if(!goodflashidx.empty()){
            PrintLine();
            SHOW(goodflashidx.size());
            SHOWstdVector(goodflashidx);
            PrintLine();
        }
    }
    
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::LoopPanNuTracks(){
    
    if (ntracks_pandoraNu==0 || ntracks_pandoraNu>100) return;
    if(debug>2) Printf("LoopPanNuTracks on %d tracks",ntracks_pandoraNu);
    
    
    
    // loop over all reconstructed tracks
    for(Int_t j=0; j < ntracks_pandoraNu; j++){
        
        InitTrack();
        if (!TrackContained(j)) continue;
        if(debug>3) Printf("track %d contained...",j);
        Ntracks ++ ;
        
        
        PandoraNuTrack cTrack(
                              run                                                                                // run
                              ,subrun                                                                            // subrun
                              ,event                                                                             // event
                              ,trkId_pandoraNu[j]                                                                // track id
                              ,TVector3(trkstartx_pandoraNu[j], trkstarty_pandoraNu[j], trkstartz_pandoraNu[j])  // start position
                              ,TVector3(trkendx_pandoraNu[j]  , trkendy_pandoraNu[j]  , trkendz_pandoraNu[j])    // end position
                              ,trklen_pandoraNu[j]                                                               // track length
                              ,trktheta_pandoraNu[j]                                                             // theta
                              ,trkphi_pandoraNu[j]                                                               // phi
                              );
        
        if(debug>3) Printf("created track %d...",j);
        
        // get flash info
        // compare reconstructed track to list of flashes in beam to find closest
        float tzcenter = (cTrack.start_pos.z() + cTrack.end_pos.z())/2.;
        if(debug>3) Printf("with tzcenter = %.2f, goodflashidx.size() = %lu",tzcenter,goodflashidx.size());

        if(goodflashidx.size() > 0) {
            int   minzi    = goodflashidx.at(0);
            float minzdiff = TMath::Abs(flash_zcenter[minzi] - tzcenter);
            if(debug>3) {SHOW(minzi);SHOW(minzdiff);}
            for(size_t k=0; k < goodflashidx.size(); k++)
            {
                int   fidx     = goodflashidx.at(k);
                float fzcenter = flash_zcenter[fidx];
                if(debug>3) {SHOW(fidx);SHOW(fzcenter);}
                if(TMath::Abs(fzcenter - tzcenter) < minzdiff)
                {
                    minzi    = fidx;
                    minzdiff = TMath::Abs(fzcenter = tzcenter);
                }
            }
            cftime      = flash_time[minzi];
            cftimewidth = flash_timewidth[minzi];
            cfzcenter   = flash_zcenter[minzi];
            cfzwidth    = flash_zwidth[minzi];
            cfycenter   = flash_ycenter[minzi];
            cfywidth    = flash_ywidth[minzi];
            cftotalpe   = flash_pe[minzi];
            cfdistance  = tzcenter - cfzcenter;
        }
        else {
            cftime = cftimewidth = cfzcenter = cfzwidth = cfycenter = cfywidth = cftotalpe = cfdistance = -9999;
        }
        cTrack.SetFlashInfo(cftime , cftimewidth , cfzcenter , cfzwidth , cfycenter , cfywidth , cftotalpe , cfdistance);
        if(debug>3) Printf("Set Flash Info...");

        
        // get cosmic scores
        cTrack.SetCosScores( trkcosmicscore_tagger_pandoraNu[j][0] , trkcosmicscore_containmenttagger_pandoraNu[j][0] );
        // get pid info
        cTrack.Set_pid_info( trkpidpida_pandoraNu[j][trkpidbestplane_pandoraNu[j]] , trkpidchi_pandoraNu[j][trkpidbestplane_pandoraNu[j]] );

        
        // get dqdx info: loop over range from end of track to find start and end
        int   rmin[3] , rmax[3];
        if(debug>3) Printf("before for(Int_t fr=0; fr<3;fr++) ...");
        for(Int_t fr=0; fr<3;fr++) {
            
            if(ntrkhits_pandoraNu[j][fr] >= 0) {
                
                nhits     += ntrkhits_pandoraNu[j][fr];
                rmin[fr]   = rmax[fr]   = trkresrg_pandoraNu[j][fr][0];
                totaldqdx += trkdqdx_pandoraNu[j][fr][0];
                int minidx = 0 , maxidx = 0;
                
                for(Int_t ridx=0; ridx < ntrkhits_pandoraNu[j][fr]; ridx++) {
                    if(trkresrg_pandoraNu[j][fr][ridx] < rmin[fr] && trkdqdx_pandoraNu[j][fr][ridx] != 0) {
                        rmin[fr] = trkresrg_pandoraNu[j][fr][ridx];
                        minidx   = ridx;
                    }
                    if(trkresrg_pandoraNu[j][fr][ridx] > rmax[fr]) {
                        rmax[fr] = trkresrg_pandoraNu[j][fr][ridx];
                        maxidx   = ridx;
                    }
                    totaldqdx += trkdqdx_pandoraNu[j][fr][ridx];
                }
                if(maxidx >= 3) {
                    startdqdx   += (trkdqdx_pandoraNu[j][fr][maxidx] + trkdqdx_pandoraNu[j][fr][maxidx-1]
                                    + trkdqdx_pandoraNu[j][fr][maxidx-2]);
                    enddqdx     += (trkdqdx_pandoraNu[j][fr][minidx] + trkdqdx_pandoraNu[j][fr][minidx+1]
                                    + trkdqdx_pandoraNu[j][fr][minidx+2]);
                } else {
                    startdqdx   += trkdqdx_pandoraNu[j][fr][maxidx];
                    enddqdx     += trkdqdx_pandoraNu[j][fr][minidx];
                }
            }
        }
        if(debug>3) Printf("after for(Int_t fr=0; fr<3;fr++) ...");
        cTrack.Set_dqdx( startdqdx , enddqdx , totaldqdx , nhits );
        if(debug>3) Printf("Set dq/dx ...");
        cTrack.CreateROIs();
        if(debug>3) Printf("Created ROIs...");
        cTrack.Calorimetry();
        if(debug>3) Printf("made some Calorimetry ...");
        cTrack.Straightness();
        if(debug>3) Printf("calculated the Straightness of the track ...");
        cTrack.Momentum();
        if(debug>3) Printf("calculated the Momentum of the track ...");
        tracks.push_back(cTrack);
        if(debug>3) Printf("pushed the track into tracks which now has a size %lu...",tracks.size());
    }
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
bool calcAnaTree::TrackContained(Int_t i){
    // check if contained
    if((trkstartx_pandoraNu[i] < 3.45   ) | (trkstartx_pandoraNu[i] > 249.8 )) return false;
    if((trkendx_pandoraNu[i]   < 3.45   ) | (trkendx_pandoraNu[i]   > 249.8 )) return false;
    if((trkstarty_pandoraNu[i] < -110.53) | (trkstarty_pandoraNu[i] > 112.47)) return false;
    if((trkendy_pandoraNu[i]   < -110.53) | (trkendy_pandoraNu[i]   > 112.47)) return false;
    if((trkstartz_pandoraNu[i] < 5.1    ) | (trkstartz_pandoraNu[i] > 1031.9)) return false;
    if((trkendz_pandoraNu[i]   < 5.1    ) | (trkendz_pandoraNu[i]   > 1031.9)) return false;
    return true;
}


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::PrintData(int entry){
    
    PrintLine();
    if (debug > 2) Printf("finally, printing data....");
    SHOW(entry);
    SHOW3(run , subrun , event);
    SHOWstdVector(goodflashidx);
    for (auto track:tracks) { track.Print(); }
    EndEventBlock();
    
}

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
void calcAnaTree::WriteTracks2CSV(){
    
    // run              , subrun            , event         , trackid
    // flip             , nhits             , length
    // startx           , starty            , startz
    // endx             , endy              , endz
    // theta            , phi               , distlenratio
    // startdqdx        , enddqdx
    // dqdxdiff         , dqdxratio         , totaldqdx     , averagedqdx
    // cosmicscore      , coscontscore      , pidpida       , pidchi
    // cftime           , cftimewidth       , cfzcenter     , cfzwidth
    // cfycenter        , cfywidth          , cftotalpe     , cfdistance
    // U_start_wire     , U_start_time      , U_end_wire  , U_end_time
    // V_start_wire     , V_start_time      , V_end_wire  , V_end_time
    // Y_start_wire     , Y_start_time      , Y_end_wire  , Y_end_time

    
    
    for (auto t:tracks){
        csvfile << t.run                       << "," << t.subrun             << "," << t.event              << "," << t.track_id
                << "," << t.is_flipped         << "," << t.nhits              << "," << t.length
                << "," << t.start_pos.x()      << "," << t.start_pos.y()      << "," << t.start_pos.z()
                << "," << t.end_pos.x()        << "," << t.end_pos.y()        << "," << t.end_pos.z()
                << "," << t.theta              << "," << t.phi                << "," << t.distlenratio
                << "," << t.start_dqdx         << "," << t.end_dqdx
                << "," << t.dqdx_diff          << "," << t.dqdx_ratio         << "," << t.tot_dqdx           << "," << t.avg_dqdx
                << "," << t.cosmicscore        << "," << t.coscontscore       << "," << t.pidpida            << "," << t.pidchi
                << "," << t.cftime             << "," << t.cftimewidth        << "," << t.cfzcenter          << "," << t.cfzwidth
                << "," << t.cfycenter          << "," << t.cfywidth           << "," << t.cftotalpe          << "," << t.cfdistance
                << "," << t.roi[0].start_wire  << "," << t.roi[0].start_time  << "," << t.roi[0].end_wire    << "," << t.roi[0].end_time
                << "," << t.roi[1].start_wire  << "," << t.roi[1].start_time  << "," << t.roi[1].end_wire    << "," << t.roi[1].end_time
                << "," << t.roi[2].start_wire  << "," << t.roi[2].start_time  << "," << t.roi[2].end_wire    << "," << t.roi[2].end_time
        << endl;

        if (debug>2) cout << "wrote track "<<t.track_id<<" to csv output file " << endl;
    };
}


#endif
