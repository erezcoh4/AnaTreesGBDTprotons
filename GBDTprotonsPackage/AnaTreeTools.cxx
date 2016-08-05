#ifndef ANATREETOOLS_CXX
#define ANATREETOOLS_CXX

#include "AnaTreeTools.h"



//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
std::vector<TTree*> AnaTreeTools::GetInputTrees (TString ListName){
    std::vector<TTree*> InputTrees;
    
    ifstream infile(ListName);
    
    string filename;
    while(infile >> filename)
    {
        //make filename into char array
        char* a = new char[filename.size() + 1];
        a[filename.size()] = 0;
        memcpy(a,filename.c_str(),filename.size());
        TFile* f = new TFile(a,"read");
        InputTrees.push_back((TTree*)f->Get("analysistree/anatree"));
    }
    
    return InputTrees;

}



#endif
