#ifndef MYLARTOOLS_CXX
#define MYLARTOOLS_CXX

#include "MyLArTools.h"

//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
MyLArTools::MyLArTools(){
    
    Float_t Range_grampercm_proton[31] =
    {1.887E-1, 3.823E-1, 6.335E-1, 1.296, 2.159, 7.375, 1.092E1,
        2.215E1, 3.627E1, 5.282E1, 7.144E1, 9.184E1, 1.138E2,
        1.370E2, 1.614E2, 1.869E2, 2.132E2, 2.403E2, 2.681E2,
        2.965E2, 3.254E2, 3.548E2, 3.846E2, 4.148E2, 4.454E2,
        7.626E2, 1.090E3, 1.418E3, 1.745E3, 2.391E3, 3.022E3
    };
    Float_t KE_MeV_proton[31] =
    {10, 15, 20, 30, 40, 80, 100, 150, 200, 250, 300, 350, 400,
        450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000,
        1500, 2000, 2500, 3000, 4000, 5000
    };
    double LAr_density = 1.396; //g/cm^3
    
    
    Float_t Range_grampercm_proton_LAr[31];
    Float_t p_MeVc_proton[31];
    for (int i = 0 ; i < 31; i++) {
        Range_grampercm_proton_LAr[i] = Range_grampercm_proton[i] * LAr_density;
        E = 938.272 + KE_MeV_proton[i];
        p_MeVc_proton[i] = sqrt(E*E - 938.272*938.272);
    }
    
        KE_vs_range_proton = new TGraph(31, Range_grampercm_proton_LAr, KE_MeV_proton);
        KE_vs_range_proton_s3 = new TSpline3("KE_vs_range_proton", KE_vs_range_proton);
        p_vs_range_proton = new TGraph(31, Range_grampercm_proton_LAr, p_MeVc_proton);
        p_vs_range_proton_s3 = new TSpline3("p_vs_range_proton", p_vs_range_proton);

}


//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
TCanvas * MyLArTools::Plot_proton_range_in_LAr(TString type){
   
    
    TCanvas * c = new TCanvas(type,type);
    if (type == "kinetic energy") {
        KE_vs_range_proton_s3 -> Draw();
    }
    else if (type == "momentum"){
        p_vs_range_proton_s3 -> Draw();
    }
    c->SaveAs("~/Desktop/"+type+"proton_range.pdf");
    return c;

}



//....oooOO0OOooo........oooOO0OOooo........oooOO0OOooo........oooOO0OOooo......
double MyLArTools::GetMomentumFromRange( float range ){
    return p_vs_range_proton_s3 -> Eval(range);
}

#endif
