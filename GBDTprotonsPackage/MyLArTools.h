/**
 * \file MyLArTools.h
 *
 * \ingroup MyPackage
 *
 * \brief Class def header for a class MyLArTools
 *
 * @author erezcohen
 */

/** \addtogroup MyPackage
 
 @{*/
#ifndef MYLARTOOLS_H
#define MYLARTOOLS_H

#include <iostream>
#include "TGraph.h"
#include "TSpline.h"
#include "TCanvas.h"

using namespace std;
/**
 \class MyLArTools
 User defined class MyLArTools ... these comments are used to generate
 doxygen documentation!
 */
class MyLArTools{
    
public:

    double E;
    
    
    
    
    /// Default constructor
    MyLArTools();
    
    /// Default destructor
    ~MyLArTools(){}
    
    TGraph *KE_vs_range_proton , *p_vs_range_proton;
    TSpline3 *KE_vs_range_proton_s3 , *p_vs_range_proton_s3;
    
    TCanvas * Plot_proton_range_in_LAr(TString type = "kinetic energy");
    double GetMomentumFromRange( float range );

};

#endif
/** @} */ // end of doxygen group

