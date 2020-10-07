# ifndef TreeOutputInfo_H
# define TreeOutputInfo_H


# include <iostream>
# include <map>
# include <stdlib.h>
# include <string>
# include <type_traits>
# include <utility>
# include <vector>

# include <TH1F.h>
# include <TH2F.h>
# include <TMatrixD.h>
# include <TROOT.h>
# include <TTree.h> 
# include <TVectorD.h> 

# include "EDAnalyzers/TreeMaker/interface/Constants.h"


namespace TreeOutputInfo
{
    class TreeOutput
    {
        public :
        
        
        TTree *tree;
        
        
        // Run info //
        ULong64_t runNumber;
        ULong64_t eventNumber;
        ULong64_t luminosityNumber;
        ULong64_t bunchCrossingNumber;
        
        
        // Gen electron //
        int genEl_n;
        std::vector <double> v_genEl_E;
        std::vector <double> v_genEl_px;
        std::vector <double> v_genEl_py;
        std::vector <double> v_genEl_pz;
        std::vector <double> v_genEl_pT;
        std::vector <double> v_genEl_eta;
        std::vector <double> v_genEl_phi;
        
        
        // Gen photon //
        int genPh_n;
        std::vector <double> v_genPh_E;
        std::vector <double> v_genPh_px;
        std::vector <double> v_genPh_py;
        std::vector <double> v_genPh_pz;
        std::vector <double> v_genPh_pT;
        std::vector <double> v_genPh_eta;
        std::vector <double> v_genPh_phi;
        
        
        // Pileup //
        int pileup_n;
        
        
        // Rho //
        double rho;
        
        
        // Tracksters //
        int trackster_n;
        std::vector <double> v_trackster_E;
        std::vector <double> v_trackster_x;
        std::vector <double> v_trackster_y;
        std::vector <double> v_trackster_z;
        std::vector <double> v_trackster_eta;
        std::vector <double> v_trackster_phi;
        std::vector <double> v_trackster_ET;
        
        
        // MultiClus ele //
        double gsfEleFromMultiClus_n;
        std::vector <double> v_gsfEleFromMultiClus_E;
        std::vector <double> v_gsfEleFromMultiClus_px;
        std::vector <double> v_gsfEleFromMultiClus_py;
        std::vector <double> v_gsfEleFromMultiClus_pz;
        std::vector <double> v_gsfEleFromMultiClus_pT;
        std::vector <double> v_gsfEleFromMultiClus_eta;
        std::vector <double> v_gsfEleFromMultiClus_phi;
        std::vector <double> v_gsfEleFromMultiClus_ET;
        
        std::vector <double> v_gsfEleFromMultiClus_genEl_minDeltaR;
        std::vector <double> v_gsfEleFromMultiClus_nearestGenEl_idx;
        std::vector <double> v_gsfEleFromMultiClus_matchedGenEl_E;
        std::vector <double> v_gsfEleFromMultiClus_matchedGenEl_pT;
        std::vector <double> v_gsfEleFromMultiClus_matchedGenEl_eta;
        std::vector <double> v_gsfEleFromMultiClus_matchedGenEl_phi;
        
        
        // TICL ele //
        double gsfEleFromTICL_n;
        std::vector <double> v_gsfEleFromTICL_E;
        std::vector <double> v_gsfEleFromTICL_px;
        std::vector <double> v_gsfEleFromTICL_py;
        std::vector <double> v_gsfEleFromTICL_pz;
        std::vector <double> v_gsfEleFromTICL_pT;
        std::vector <double> v_gsfEleFromTICL_eta;
        std::vector <double> v_gsfEleFromTICL_phi;
        std::vector <double> v_gsfEleFromTICL_ET;
        
        std::vector <double> v_gsfEleFromTICL_genEl_minDeltaR;
        std::vector <double> v_gsfEleFromTICL_nearestGenEl_idx;
        std::vector <double> v_gsfEleFromTICL_matchedGenEl_E;
        std::vector <double> v_gsfEleFromTICL_matchedGenEl_pT;
        std::vector <double> v_gsfEleFromTICL_matchedGenEl_eta;
        std::vector <double> v_gsfEleFromTICL_matchedGenEl_phi;
        
        std::vector <double> v_gsfEleFromTICL_superClus_nClus;
        std::vector <std::vector <double> > vv_gsfEleFromTICL_superClus_clus_eleIdx;
        std::vector <std::vector <double> > vv_gsfEleFromTICL_superClus_clus_idx;
        std::vector <std::vector <double> > vv_gsfEleFromTICL_superClus_clus_E;
        std::vector <std::vector <double> > vv_gsfEleFromTICL_superClus_clus_ET;
        
        std::vector <double> v_gsfEleFromTICL_R2p8;
        
        std::vector <double> v_gsfEleFromTICL_sigma2uu;
        std::vector <double> v_gsfEleFromTICL_sigma2vv;
        std::vector <double> v_gsfEleFromTICL_sigma2ww;
        
        
        // MultiClus pho //
        double phoFromMultiClus_n;
        std::vector <double> v_phoFromMultiClus_E;
        std::vector <double> v_phoFromMultiClus_px;
        std::vector <double> v_phoFromMultiClus_py;
        std::vector <double> v_phoFromMultiClus_pz;
        std::vector <double> v_phoFromMultiClus_pT;
        std::vector <double> v_phoFromMultiClus_eta;
        std::vector <double> v_phoFromMultiClus_phi;
        std::vector <double> v_phoFromMultiClus_ET;
        
        std::vector <double> v_phoFromMultiClus_genPh_minDeltaR;
        std::vector <double> v_phoFromMultiClus_nearestGenPh_idx;
        std::vector <double> v_phoFromMultiClus_matchedGenPh_E;
        std::vector <double> v_phoFromMultiClus_matchedGenPh_pT;
        std::vector <double> v_phoFromMultiClus_matchedGenPh_eta;
        std::vector <double> v_phoFromMultiClus_matchedGenPh_phi;
        
        
        // TICL pho //
        double phoFromTICL_n;
        std::vector <double> v_phoFromTICL_E;
        std::vector <double> v_phoFromTICL_px;
        std::vector <double> v_phoFromTICL_py;
        std::vector <double> v_phoFromTICL_pz;
        std::vector <double> v_phoFromTICL_pT;
        std::vector <double> v_phoFromTICL_eta;
        std::vector <double> v_phoFromTICL_phi;
        std::vector <double> v_phoFromTICL_ET;
        
        std::vector <double> v_phoFromTICL_genPh_minDeltaR;
        std::vector <double> v_phoFromTICL_nearestGenPh_idx;
        std::vector <double> v_phoFromTICL_matchedGenPh_E;
        std::vector <double> v_phoFromTICL_matchedGenPh_pT;
        std::vector <double> v_phoFromTICL_matchedGenPh_eta;
        std::vector <double> v_phoFromTICL_matchedGenPh_phi;
        
        
        char name[500];
        
        
        TreeOutput(std::string details, edm::Service<TFileService> fs)
        {
            printf("Loading custom ROOT dictionaries. \n");
            gROOT->ProcessLine(".L EDAnalyzers/TreeMaker/interface/CustomRootDict.cc+");
            printf("Loaded custom ROOT dictionaries. \n");
            
            tree = fs->make<TTree>(details.c_str(), details.c_str());
            
            
            // Run info //
            tree->Branch("runNumber", &runNumber);
            tree->Branch("eventNumber", &eventNumber);
            tree->Branch("luminosityNumber", &luminosityNumber);
            tree->Branch("bunchCrossingNumber", &bunchCrossingNumber);
            
            
            // Gen electron //
            sprintf(name, "genEl_n");
            tree->Branch(name, &genEl_n);
            
            sprintf(name, "genEl_E");
            tree->Branch(name, &v_genEl_E);
            
            sprintf(name, "genEl_px");
            tree->Branch(name, &v_genEl_px);
            
            sprintf(name, "genEl_py");
            tree->Branch(name, &v_genEl_py);
            
            sprintf(name, "genEl_pz");
            tree->Branch(name, &v_genEl_pz);
            
            sprintf(name, "genEl_pT");
            tree->Branch(name, &v_genEl_pT);
            
            sprintf(name, "genEl_eta");
            tree->Branch(name, &v_genEl_eta);
            
            sprintf(name, "genEl_phi");
            tree->Branch(name, &v_genEl_phi);
            
            
            // Gen photon //
            sprintf(name, "genPh_n");
            tree->Branch(name, &genPh_n);
            
            sprintf(name, "genPh_E");
            tree->Branch(name, &v_genPh_E);
            
            sprintf(name, "genPh_px");
            tree->Branch(name, &v_genPh_px);
            
            sprintf(name, "genPh_py");
            tree->Branch(name, &v_genPh_py);
            
            sprintf(name, "genPh_pz");
            tree->Branch(name, &v_genPh_pz);
            
            sprintf(name, "genPh_pT");
            tree->Branch(name, &v_genPh_pT);
            
            sprintf(name, "genPh_eta");
            tree->Branch(name, &v_genPh_eta);
            
            sprintf(name, "genPh_phi");
            tree->Branch(name, &v_genPh_phi);
            
            
            // Pileup //
            sprintf(name, "pileup_n");
            tree->Branch(name, &pileup_n);
            
            
            // Rho //
            sprintf(name, "rho");
            tree->Branch(name, &rho);
            
            
            // MultiClus ele
            sprintf(name, "gsfEleFromMultiClus_n");
            tree->Branch(name, &gsfEleFromMultiClus_n);
            
            sprintf(name, "gsfEleFromMultiClus_E");
            tree->Branch(name, &v_gsfEleFromMultiClus_E);
            
            sprintf(name, "gsfEleFromMultiClus_px");
            tree->Branch(name, &v_gsfEleFromMultiClus_px);
            
            sprintf(name, "gsfEleFromMultiClus_py");
            tree->Branch(name, &v_gsfEleFromMultiClus_py);
            
            sprintf(name, "gsfEleFromMultiClus_pz");
            tree->Branch(name, &v_gsfEleFromMultiClus_pz);
            
            sprintf(name, "gsfEleFromMultiClus_pT");
            tree->Branch(name, &v_gsfEleFromMultiClus_pT);
            
            sprintf(name, "gsfEleFromMultiClus_eta");
            tree->Branch(name, &v_gsfEleFromMultiClus_eta);
            
            sprintf(name, "gsfEleFromMultiClus_phi");
            tree->Branch(name, &v_gsfEleFromMultiClus_phi);
            
            sprintf(name, "gsfEleFromMultiClus_ET");
            tree->Branch(name, &v_gsfEleFromMultiClus_ET);
            
            sprintf(name, "gsfEleFromMultiClus_genEl_minDeltaR");
            tree->Branch(name, &v_gsfEleFromMultiClus_genEl_minDeltaR);
            
            sprintf(name, "gsfEleFromMultiClus_nearestGenEl_idx");
            tree->Branch(name, &v_gsfEleFromMultiClus_nearestGenEl_idx);
            
            sprintf(name, "gsfEleFromMultiClus_matchedGenEl_E");
            tree->Branch(name, &v_gsfEleFromMultiClus_matchedGenEl_E);
            
            sprintf(name, "gsfEleFromMultiClus_matchedGenEl_pT");
            tree->Branch(name, &v_gsfEleFromMultiClus_matchedGenEl_pT);
            
            sprintf(name, "gsfEleFromMultiClus_matchedGenEl_eta");
            tree->Branch(name, &v_gsfEleFromMultiClus_matchedGenEl_eta);
            
            sprintf(name, "gsfEleFromMultiClus_matchedGenEl_phi");
            tree->Branch(name, &v_gsfEleFromMultiClus_matchedGenEl_phi);
            
            
            // TICL ele
            sprintf(name, "gsfEleFromTICL_n");
            tree->Branch(name, &gsfEleFromTICL_n);
            
            sprintf(name, "gsfEleFromTICL_E");
            tree->Branch(name, &v_gsfEleFromTICL_E);
            
            sprintf(name, "gsfEleFromTICL_px");
            tree->Branch(name, &v_gsfEleFromTICL_px);
            
            sprintf(name, "gsfEleFromTICL_py");
            tree->Branch(name, &v_gsfEleFromTICL_py);
            
            sprintf(name, "gsfEleFromTICL_pz");
            tree->Branch(name, &v_gsfEleFromTICL_pz);
            
            sprintf(name, "gsfEleFromTICL_pT");
            tree->Branch(name, &v_gsfEleFromTICL_pT);
            
            sprintf(name, "gsfEleFromTICL_eta");
            tree->Branch(name, &v_gsfEleFromTICL_eta);
            
            sprintf(name, "gsfEleFromTICL_phi");
            tree->Branch(name, &v_gsfEleFromTICL_phi);
            
            sprintf(name, "gsfEleFromTICL_ET");
            tree->Branch(name, &v_gsfEleFromTICL_ET);
            
            sprintf(name, "gsfEleFromTICL_genEl_minDeltaR");
            tree->Branch(name, &v_gsfEleFromTICL_genEl_minDeltaR);
            
            sprintf(name, "gsfEleFromTICL_nearestGenEl_idx");
            tree->Branch(name, &v_gsfEleFromTICL_nearestGenEl_idx);
            
            sprintf(name, "gsfEleFromTICL_matchedGenEl_E");
            tree->Branch(name, &v_gsfEleFromTICL_matchedGenEl_E);
            
            sprintf(name, "gsfEleFromTICL_matchedGenEl_pT");
            tree->Branch(name, &v_gsfEleFromTICL_matchedGenEl_pT);
            
            sprintf(name, "gsfEleFromTICL_matchedGenEl_eta");
            tree->Branch(name, &v_gsfEleFromTICL_matchedGenEl_eta);
            
            sprintf(name, "gsfEleFromTICL_matchedGenEl_phi");
            tree->Branch(name, &v_gsfEleFromTICL_matchedGenEl_phi);
            
            //
            sprintf(name, "gsfEleFromTICL_superClus_nClus");
            tree->Branch(name, &v_gsfEleFromTICL_superClus_nClus);
            
            sprintf(name, "gsfEleFromTICL_superClus_clus_eleIdx");
            tree->Branch(name, &vv_gsfEleFromTICL_superClus_clus_eleIdx);
            
            sprintf(name, "gsfEleFromTICL_superClus_clus_idx");
            tree->Branch(name, &vv_gsfEleFromTICL_superClus_clus_idx);
            
            sprintf(name, "gsfEleFromTICL_superClus_clus_E");
            tree->Branch(name, &vv_gsfEleFromTICL_superClus_clus_E);
            
            sprintf(name, "gsfEleFromTICL_superClus_clus_ET");
            tree->Branch(name, &vv_gsfEleFromTICL_superClus_clus_ET);
            
            //
            sprintf(name, "gsfEleFromTICL_R2p8");
            tree->Branch(name, &v_gsfEleFromTICL_R2p8);
            
            sprintf(name, "gsfEleFromTICL_sigma2uu");
            tree->Branch(name, &v_gsfEleFromTICL_sigma2uu);
            
            sprintf(name, "gsfEleFromTICL_sigma2vv");
            tree->Branch(name, &v_gsfEleFromTICL_sigma2vv);
            
            sprintf(name, "gsfEleFromTICL_sigma2ww");
            tree->Branch(name, &v_gsfEleFromTICL_sigma2ww);
            
            
            // MultiClus pho
            sprintf(name, "phoFromMultiClus_n");
            tree->Branch(name, &phoFromMultiClus_n);
            
            sprintf(name, "phoFromMultiClus_E");
            tree->Branch(name, &v_phoFromMultiClus_E);
            
            sprintf(name, "phoFromMultiClus_px");
            tree->Branch(name, &v_phoFromMultiClus_px);
            
            sprintf(name, "phoFromMultiClus_py");
            tree->Branch(name, &v_phoFromMultiClus_py);
            
            sprintf(name, "phoFromMultiClus_pz");
            tree->Branch(name, &v_phoFromMultiClus_pz);
            
            sprintf(name, "phoFromMultiClus_pT");
            tree->Branch(name, &v_phoFromMultiClus_pT);
            
            sprintf(name, "phoFromMultiClus_eta");
            tree->Branch(name, &v_phoFromMultiClus_eta);
            
            sprintf(name, "phoFromMultiClus_phi");
            tree->Branch(name, &v_phoFromMultiClus_phi);
            
            sprintf(name, "phoFromMultiClus_ET");
            tree->Branch(name, &v_phoFromMultiClus_ET);
            
            sprintf(name, "phoFromMultiClus_genPh_minDeltaR");
            tree->Branch(name, &v_phoFromMultiClus_genPh_minDeltaR);
            
            sprintf(name, "phoFromMultiClus_nearestGenPh_idx");
            tree->Branch(name, &v_phoFromMultiClus_nearestGenPh_idx);
            
            sprintf(name, "phoFromMultiClus_matchedGenPh_E");
            tree->Branch(name, &v_phoFromMultiClus_matchedGenPh_E);
            
            sprintf(name, "phoFromMultiClus_matchedGenPh_pT");
            tree->Branch(name, &v_phoFromMultiClus_matchedGenPh_pT);
            
            sprintf(name, "phoFromMultiClus_matchedGenPh_eta");
            tree->Branch(name, &v_phoFromMultiClus_matchedGenPh_eta);
            
            sprintf(name, "phoFromMultiClus_matchedGenPh_phi");
            tree->Branch(name, &v_phoFromMultiClus_matchedGenPh_phi);
            
            
            // TICL pho
            sprintf(name, "phoFromTICL_n");
            tree->Branch(name, &phoFromTICL_n);
            
            sprintf(name, "phoFromTICL_E");
            tree->Branch(name, &v_phoFromTICL_E);
            
            sprintf(name, "phoFromTICL_px");
            tree->Branch(name, &v_phoFromTICL_px);
            
            sprintf(name, "phoFromTICL_py");
            tree->Branch(name, &v_phoFromTICL_py);
            
            sprintf(name, "phoFromTICL_pz");
            tree->Branch(name, &v_phoFromTICL_pz);
            
            sprintf(name, "phoFromTICL_pT");
            tree->Branch(name, &v_phoFromTICL_pT);
            
            sprintf(name, "phoFromTICL_eta");
            tree->Branch(name, &v_phoFromTICL_eta);
            
            sprintf(name, "phoFromTICL_phi");
            tree->Branch(name, &v_phoFromTICL_phi);
            
            sprintf(name, "phoFromTICL_ET");
            tree->Branch(name, &v_phoFromTICL_ET);
            
            sprintf(name, "phoFromTICL_genPh_minDeltaR");
            tree->Branch(name, &v_phoFromTICL_genPh_minDeltaR);
            
            sprintf(name, "phoFromTICL_nearestGenPh_idx");
            tree->Branch(name, &v_phoFromTICL_nearestGenPh_idx);
            
            sprintf(name, "phoFromTICL_matchedGenPh_E");
            tree->Branch(name, &v_phoFromTICL_matchedGenPh_E);
            
            sprintf(name, "phoFromTICL_matchedGenPh_pT");
            tree->Branch(name, &v_phoFromTICL_matchedGenPh_pT);
            
            sprintf(name, "phoFromTICL_matchedGenPh_eta");
            tree->Branch(name, &v_phoFromTICL_matchedGenPh_eta);
            
            sprintf(name, "phoFromTICL_matchedGenPh_phi");
            tree->Branch(name, &v_phoFromTICL_matchedGenPh_phi);
        }
        
        
        void fill()
        {
            tree->Fill();
        }
        
        
        void clear()
        {
            // Gen electron //
            genEl_n = 0;
            v_genEl_E.clear();
            v_genEl_px.clear();
            v_genEl_py.clear();
            v_genEl_pz.clear();
            v_genEl_pT.clear();
            v_genEl_eta.clear();
            v_genEl_phi.clear();
            
            
            // Gen photon //
            genPh_n = 0;
            v_genPh_E.clear();
            v_genPh_px.clear();
            v_genPh_py.clear();
            v_genPh_pz.clear();
            v_genPh_pT.clear();
            v_genPh_eta.clear();
            v_genPh_phi.clear();
            
            
            // Pileup //
            pileup_n = 0;
            
            
            // Rho //
            rho = 0;
            
            
            // MultiClus ele
            gsfEleFromMultiClus_n = 0;
            v_gsfEleFromMultiClus_E.clear();
            v_gsfEleFromMultiClus_px.clear();
            v_gsfEleFromMultiClus_py.clear();
            v_gsfEleFromMultiClus_pz.clear();
            v_gsfEleFromMultiClus_pT.clear();
            v_gsfEleFromMultiClus_eta.clear();
            v_gsfEleFromMultiClus_phi.clear();
            v_gsfEleFromMultiClus_ET.clear();
            
            v_gsfEleFromMultiClus_genEl_minDeltaR.clear();
            v_gsfEleFromMultiClus_nearestGenEl_idx.clear();
            v_gsfEleFromMultiClus_matchedGenEl_E.clear();
            v_gsfEleFromMultiClus_matchedGenEl_pT.clear();
            v_gsfEleFromMultiClus_matchedGenEl_eta.clear();
            v_gsfEleFromMultiClus_matchedGenEl_phi.clear();
            
            
            // TICL ele
            gsfEleFromTICL_n = 0;
            v_gsfEleFromTICL_E.clear();
            v_gsfEleFromTICL_px.clear();
            v_gsfEleFromTICL_py.clear();
            v_gsfEleFromTICL_pz.clear();
            v_gsfEleFromTICL_pT.clear();
            v_gsfEleFromTICL_eta.clear();
            v_gsfEleFromTICL_phi.clear();
            v_gsfEleFromTICL_ET.clear();
            
            v_gsfEleFromTICL_genEl_minDeltaR.clear();
            v_gsfEleFromTICL_nearestGenEl_idx.clear();
            v_gsfEleFromTICL_matchedGenEl_E.clear();
            v_gsfEleFromTICL_matchedGenEl_pT.clear();
            v_gsfEleFromTICL_matchedGenEl_eta.clear();
            v_gsfEleFromTICL_matchedGenEl_phi.clear();
            
            v_gsfEleFromTICL_superClus_nClus.clear();
            vv_gsfEleFromTICL_superClus_clus_eleIdx.clear();
            vv_gsfEleFromTICL_superClus_clus_idx.clear();
            vv_gsfEleFromTICL_superClus_clus_E.clear();
            vv_gsfEleFromTICL_superClus_clus_ET.clear();
            
            v_gsfEleFromTICL_R2p8.clear();
            
            v_gsfEleFromTICL_sigma2uu.clear();
            v_gsfEleFromTICL_sigma2vv.clear();
            v_gsfEleFromTICL_sigma2ww.clear();
            
            
            // MultiClus pho
            phoFromMultiClus_n = 0;
            v_phoFromMultiClus_E.clear();
            v_phoFromMultiClus_px.clear();
            v_phoFromMultiClus_py.clear();
            v_phoFromMultiClus_pz.clear();
            v_phoFromMultiClus_pT.clear();
            v_phoFromMultiClus_eta.clear();
            v_phoFromMultiClus_phi.clear();
            v_phoFromMultiClus_ET.clear();
            
            v_phoFromMultiClus_genPh_minDeltaR.clear();
            v_phoFromMultiClus_nearestGenPh_idx.clear();
            v_phoFromMultiClus_matchedGenPh_E.clear();
            v_phoFromMultiClus_matchedGenPh_pT.clear();
            v_phoFromMultiClus_matchedGenPh_eta.clear();
            v_phoFromMultiClus_matchedGenPh_phi.clear();
            
            
            // TICL pho
            phoFromTICL_n = 0;
            v_phoFromTICL_E.clear();
            v_phoFromTICL_px.clear();
            v_phoFromTICL_py.clear();
            v_phoFromTICL_pz.clear();
            v_phoFromTICL_pT.clear();
            v_phoFromTICL_eta.clear();
            v_phoFromTICL_phi.clear();
            v_phoFromTICL_ET.clear();
            
            v_phoFromTICL_genPh_minDeltaR.clear();
            v_phoFromTICL_nearestGenPh_idx.clear();
            v_phoFromTICL_matchedGenPh_E.clear();
            v_phoFromTICL_matchedGenPh_pT.clear();
            v_phoFromTICL_matchedGenPh_eta.clear();
            v_phoFromTICL_matchedGenPh_phi.clear();
        }
    };
}


# endif
