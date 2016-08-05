/**
 * \file AnaTreeTools.h
 *
 * \ingroup GBDTprotonsPackage
 * 
 * \brief Class def header for a class AnaTreeTools
 *
 * @author erezcohen
 */

/** \addtogroup GBDTprotonsPackage

    @{*/
#ifndef ANATREETOOLS_H
#define ANATREETOOLS_H



#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <fstream>
#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TVector3.h"
#include "TMath.h"


using namespace std;


// monitoring....
#define EndEventBlock() cout << "\033[32m"<< "....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......" << "\033[0m"<< endl;
#define PrintLine() cout << "-------------------------------" << endl;
#define SHOW(a) cout  << #a << ": " << (a) << endl;
#define SHOW3(a,b,c) cout  << "\033[36m"<<#a<<": "<<(a)<<"," << #b <<": "<<(b)<<","<<#c<<": "<<(c)<< "\033[0m"<< endl;
#define SHOWstdVector(v){ if (v.size()<1) {cout << #v << " is empty" << endl;} else {cout << #v << "( " << v.size() << " entries):\t"; for (auto it:v) cout << it << ",\t"; cout << endl;}}
#define SHOWTVector3(v){ cout << #v << ": (" << v.X() << "," << v.Y() << "," << v.Z() << "), |" << #v << "| = " << v.Mag() << endl;}


/**
   \class AnaTreeTools
   User defined class AnaTreeTools ... these comments are used to generate
   doxygen documentation!
 */
class AnaTreeTools{

public:

  /// Default constructor
  AnaTreeTools(){}

  /// Default destructor
  ~AnaTreeTools(){}
    
    
  std::vector<TTree*> GetInputTrees (TString ListName);

};

#endif
/** @} */ // end of doxygen group 

