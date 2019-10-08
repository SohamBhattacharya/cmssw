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
        
        std::vector <double> v_genEl_HGCalEEP_EsortedIndex;
        std::vector <double> v_genEl_HGCalEEM_EsortedIndex;
        
        std::vector <double> v_genEl_multiClus_totE;
        
        std::vector <double> v_genEl_multiClus_n;
        std::vector <double> v_genEl_nearestMultiClusEnRatio;
        std::vector <double> v_genEl_multiClusEnRatio;
        
        
        // Gen photon //
        int genPh_n;
        std::vector <double> v_genPh_E;
        std::vector <double> v_genPh_px;
        std::vector <double> v_genPh_py;
        std::vector <double> v_genPh_pz;
        std::vector <double> v_genPh_pT;
        std::vector <double> v_genPh_eta;
        std::vector <double> v_genPh_phi;
        
        std::vector <double> v_genPh_HGCalEEP_EsortedIndex;
        std::vector <double> v_genPh_HGCalEEM_EsortedIndex;
        
        std::vector <double> v_genPh_multiClus_totE;
        
        std::vector <double> v_genPh_HGCalEEP_deltaR;
        std::vector <double> v_genPh_HGCalEEM_deltaR;
        
        
        // HGCAL layer clusters //
        int HGCALlayerClus_n;
        std::vector <double> v_HGCALlayerClus_E;
        std::vector <double> v_HGCALlayerClus_x;
        std::vector <double> v_HGCALlayerClus_y;
        std::vector <double> v_HGCALlayerClus_z;
        std::vector <double> v_HGCALlayerClus_eta;
        std::vector <double> v_HGCALlayerClus_phi;
        std::vector <double> v_HGCALlayerClus_ET;
        std::vector <double> v_HGCALlayerClus_layer;
        
        std::vector <double> v_HGCALlayerClus_isInMultiClus;
        std::vector <double> v_HGCALlayerClus_sigRecHit_totE;
        std::vector <double> v_HGCALlayerClus_sigRecHit_Efraction;
        
        
        // MultiClusters //
        int multiClus_n;
        std::vector <double> v_multiClus_genElIndex;
        std::vector <double> v_multiClus_E;
        std::vector <double> v_multiClus_x;
        std::vector <double> v_multiClus_y;
        std::vector <double> v_multiClus_z;
        std::vector <double> v_multiClus_eta;
        std::vector <double> v_multiClus_phi;
        std::vector <double> v_multiClus_ET;
        
        std::vector <double> v_multiClus_dX;
        std::vector <double> v_multiClus_dY;
        std::vector <double> v_multiClus_dZ;
        
        std::vector <double> v_multiClus_dEta;
        std::vector <double> v_multiClus_dPhi;
        
        std::vector <double> v_multiClus_sigma2rr;
        std::vector <double> v_multiClus_sigma2etaEta;
        std::vector <double> v_multiClus_sigma2phiPhi;
        
        std::vector <double> v_multiClus_sigma2rEta;
        std::vector <double> v_multiClus_sigma2rPhi;
        std::vector <double> v_multiClus_sigma2etaPhi;
        
        std::vector <double> v_multiClus_sigma2diag1;
        std::vector <double> v_multiClus_sigma2diag2;
        std::vector <double> v_multiClus_sigma2diag3;
        
        std::vector <double> v_multiClus_EsortedIndex;
        std::vector <double> v_multiClus_HGCalEEP_EsortedIndex;
        std::vector <double> v_multiClus_HGCalEEM_EsortedIndex;
        
        std::vector <double> v_multiClus_clus_n;
        std::vector <double> v_multiClus_clus_startIndex;
        std::vector <double> v_multiClus_clus_E;
        std::vector <double> v_multiClus_clus_x;
        std::vector <double> v_multiClus_clus_y;
        std::vector <double> v_multiClus_clus_z;
        std::vector <double> v_multiClus_clus_eta;
        std::vector <double> v_multiClus_clus_phi;
        std::vector <double> v_multiClus_clus_ET;
        
        std::vector <double> v_multiClus_clus_layer;
        std::vector <double> v_multiClus_clus_multiplicity;
        std::vector <double> v_multiClus_clus_nHit;
        
        
        std::vector <double> v_multiClus_uniqueClus_n;
        std::vector <double> v_multiClus_uniqueClus_E;
        std::vector <double> v_multiClus_uniqueClus_x;
        std::vector <double> v_multiClus_uniqueClus_y;
        std::vector <double> v_multiClus_uniqueClus_z;
        std::vector <double> v_multiClus_uniqueClus_eta;
        std::vector <double> v_multiClus_uniqueClus_phi;
        std::vector <double> v_multiClus_uniqueClus_ET;
        
        std::vector <double> v_multiClus_uniqueClus_layer;
        std::vector <double> v_multiClus_uniqueClus_multiplicity;
        std::vector <double> v_multiClus_uniqueClus_nHit;
        
        
        //
        double multiClus_HGCalEEP_meanX;
        double multiClus_HGCalEEP_meanY;
        double multiClus_HGCalEEP_meanZ;
        
        double multiClus_HGCalEEP_meanDx;
        double multiClus_HGCalEEP_meanDy;
        double multiClus_HGCalEEP_meanDz;
        
        double multiClus_HGCalEEP_totE;
        double multiClus_HGCalEEP_totET;
        
        double multiClus_HGCalEEP_diag1;
        double multiClus_HGCalEEP_diag2;
        double multiClus_HGCalEEP_diag3;
        
        //
        double multiClus_HGCalEEM_meanX;
        double multiClus_HGCalEEM_meanY;
        double multiClus_HGCalEEM_meanZ;
        
        double multiClus_HGCalEEM_meanDx;
        double multiClus_HGCalEEM_meanDy;
        double multiClus_HGCalEEM_meanDz;
        
        double multiClus_HGCalEEM_totE;
        double multiClus_HGCalEEM_totET;
        
        double multiClus_HGCalEEM_diag1;
        double multiClus_HGCalEEM_diag2;
        double multiClus_HGCalEEM_diag3;
        
        
        double simHit_n;
        std::vector <double> v_simHit_E;
        std::vector <double> v_simHit_x;
        std::vector <double> v_simHit_y;
        std::vector <double> v_simHit_z;
        std::vector <double> v_simHit_eta;
        std::vector <double> v_simHit_phi;
        std::vector <double> v_simHit_ET;
        std::vector <double> v_simHit_layer;
        std::vector <double> v_simHit_zside;
        std::vector <double> v_simHit_isCaloParticleMatched;
        
        
        double recHit_n;
        std::vector <double> v_recHit_E;
        std::vector <double> v_recHit_x;
        std::vector <double> v_recHit_y;
        std::vector <double> v_recHit_z;
        std::vector <double> v_recHit_eta;
        std::vector <double> v_recHit_phi;
        std::vector <double> v_recHit_ET;
        std::vector <double> v_recHit_layer;
        std::vector <double> v_recHit_zside;
        std::vector <double> v_recHit_matchedSimHitIndex;
        std::vector <double> v_recHit_matchedHGCALlayerClusIndex;
        std::vector <double> v_recHit_isMultiClusMatched;
        std::vector <double> v_recHit_isCaloParticleMatched;
        
        std::vector <double> v_simHit_HGCalEEPlayer_totE;
        std::vector <double> v_recHit_HGCalEEPlayer_totE;
        
        std::vector <double> v_simHit_HGCalEEMlayer_totE;
        std::vector <double> v_recHit_HGCalEEMlayer_totE;
        
        
        double gsfEleFromMultiClus_n;
        std::vector <double> v_gsfEleFromMultiClus_E;
        std::vector <double> v_gsfEleFromMultiClus_px;
        std::vector <double> v_gsfEleFromMultiClus_py;
        std::vector <double> v_gsfEleFromMultiClus_pz;
        std::vector <double> v_gsfEleFromMultiClus_pT;
        std::vector <double> v_gsfEleFromMultiClus_eta;
        std::vector <double> v_gsfEleFromMultiClus_phi;
        
        
        double gsfEleFromTICL_n;
        std::vector <double> v_gsfEleFromTICL_E;
        std::vector <double> v_gsfEleFromTICL_px;
        std::vector <double> v_gsfEleFromTICL_py;
        std::vector <double> v_gsfEleFromTICL_pz;
        std::vector <double> v_gsfEleFromTICL_pT;
        std::vector <double> v_gsfEleFromTICL_eta;
        std::vector <double> v_gsfEleFromTICL_phi;
        
        std::vector <double> v_gsfEleFromTICL_superClus_nearestCellDist;
        
        
        double caloParticle_n;
        std::vector <double> v_caloParticle_E;
        std::vector <double> v_caloParticle_px;
        std::vector <double> v_caloParticle_py;
        std::vector <double> v_caloParticle_pz;
        std::vector <double> v_caloParticle_pT;
        std::vector <double> v_caloParticle_eta;
        std::vector <double> v_caloParticle_phi;
        std::vector <double> v_caloParticle_pdgid;
        
        char name[500];
        
        
        TreeOutput(std::string details, edm::Service<TFileService> fs)
        {
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
            
            sprintf(name, "genEl_HGCalEEP_EsortedIndex");
            tree->Branch(name, &v_genEl_HGCalEEP_EsortedIndex);
            
            sprintf(name, "genEl_HGCalEEM_EsortedIndex");
            tree->Branch(name, &v_genEl_HGCalEEM_EsortedIndex);
            
            sprintf(name, "genEl_multiClus_totE");
            tree->Branch(name, &v_genEl_multiClus_totE);
            
            sprintf(name, "genEl_multiClus_n");
            tree->Branch(name, &v_genEl_multiClus_n);
            
            sprintf(name, "genEl_nearestMultiClusEnRatio");
            tree->Branch(name, &v_genEl_nearestMultiClusEnRatio);
            
            sprintf(name, "genEl_multiClusEnRatio");
            tree->Branch(name, &v_genEl_multiClusEnRatio);
            
            
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
            
            sprintf(name, "genPh_HGCalEEP_EsortedIndex");
            tree->Branch(name, &v_genPh_HGCalEEP_EsortedIndex);
            
            sprintf(name, "genPh_HGCalEEM_EsortedIndex");
            tree->Branch(name, &v_genPh_HGCalEEM_EsortedIndex);
            
            sprintf(name, "genPh_multiClus_totE");
            tree->Branch(name, &v_genPh_multiClus_totE);
            
            sprintf(name, "genPh_HGCalEEP_deltaR");
            tree->Branch(name, &v_genPh_HGCalEEP_deltaR);
            
            sprintf(name, "genPh_HGCalEEM_deltaR");
            tree->Branch(name, &v_genPh_HGCalEEM_deltaR);
            
            
            // HGCalEE+
            v_simHit_HGCalEEPlayer_totE.resize(Constants::HGCalEE_nLayer, 0.0);
            
            for(int iLayer = 0; iLayer < Constants::HGCalEE_nLayer; iLayer++)
            {
                sprintf(name, "simHit_HGCalEEPlayer%d_totE", iLayer+1);
                tree->Branch(name, &v_simHit_HGCalEEPlayer_totE.at(iLayer));
            }
            
            v_recHit_HGCalEEPlayer_totE.resize(Constants::HGCalEE_nLayer, 0.0);
            
            for(int iLayer = 0; iLayer < Constants::HGCalEE_nLayer; iLayer++)
            {
                sprintf(name, "recHit_HGCalEEPlayer%d_totE", iLayer+1);
                tree->Branch(name, &v_recHit_HGCalEEPlayer_totE.at(iLayer));
            }
            
            // HGCalEE-
            v_simHit_HGCalEEMlayer_totE.resize(Constants::HGCalEE_nLayer, 0.0);
            
            for(int iLayer = 0; iLayer < Constants::HGCalEE_nLayer; iLayer++)
            {
                sprintf(name, "simHit_HGCalEEMlayer%d_totE", iLayer+1);
                tree->Branch(name, &v_simHit_HGCalEEMlayer_totE.at(iLayer));
            }
            
            v_recHit_HGCalEEMlayer_totE.resize(Constants::HGCalEE_nLayer, 0.0);
            
            for(int iLayer = 0; iLayer < Constants::HGCalEE_nLayer; iLayer++)
            {
                sprintf(name, "recHit_HGCalEEMlayer%d_totE", iLayer+1);
                tree->Branch(name, &v_recHit_HGCalEEMlayer_totE.at(iLayer));
            }
            
            
            // HGCAL layer clusters //
            sprintf(name, "HGCALlayerClus_n");
            tree->Branch(name, &HGCALlayerClus_n);
            
            sprintf(name, "HGCALlayerClus_E");
            tree->Branch(name, &v_HGCALlayerClus_E);
            
            sprintf(name, "HGCALlayerClus_x");
            tree->Branch(name, &v_HGCALlayerClus_x);
            
            sprintf(name, "HGCALlayerClus_y");
            tree->Branch(name, &v_HGCALlayerClus_y);
            
            sprintf(name, "HGCALlayerClus_z");
            tree->Branch(name, &v_HGCALlayerClus_z);
            
            sprintf(name, "HGCALlayerClus_eta");
            tree->Branch(name, &v_HGCALlayerClus_eta);
            
            sprintf(name, "HGCALlayerClus_phi");
            tree->Branch(name, &v_HGCALlayerClus_phi);
            
            sprintf(name, "HGCALlayerClus_ET");
            tree->Branch(name, &v_HGCALlayerClus_ET);
            
            sprintf(name, "HGCALlayerClus_layer");
            tree->Branch(name, &v_HGCALlayerClus_layer);
            
            sprintf(name, "HGCALlayerClus_isInMultiClus");
            tree->Branch(name, &v_HGCALlayerClus_isInMultiClus);
            
            sprintf(name, "HGCALlayerClus_sigRecHit_totE");
            tree->Branch(name, &v_HGCALlayerClus_sigRecHit_totE);
            
            sprintf(name, "HGCALlayerClus_sigRecHit_Efraction");
            tree->Branch(name, &v_HGCALlayerClus_sigRecHit_Efraction);
            
            
            // MultiClusters //
            sprintf(name, "multiClus_n");
            tree->Branch(name, &multiClus_n);
            
            sprintf(name, "multiClus_genElIndex");
            tree->Branch(name, &v_multiClus_genElIndex);
            
            sprintf(name, "multiClus_E");
            tree->Branch(name, &v_multiClus_E);
            
            sprintf(name, "multiClus_x");
            tree->Branch(name, &v_multiClus_x);
            
            sprintf(name, "multiClus_y");
            tree->Branch(name, &v_multiClus_y);
            
            sprintf(name, "multiClus_z");
            tree->Branch(name, &v_multiClus_z);
            
            sprintf(name, "multiClus_eta");
            tree->Branch(name, &v_multiClus_eta);
            
            sprintf(name, "multiClus_phi");
            tree->Branch(name, &v_multiClus_phi);
            
            sprintf(name, "multiClus_ET");
            tree->Branch(name, &v_multiClus_ET);
            
            sprintf(name, "multiClus_dX");
            tree->Branch(name, &v_multiClus_dX);
            
            sprintf(name, "multiClus_dY");
            tree->Branch(name, &v_multiClus_dY);
            
            sprintf(name, "multiClus_dZ");
            tree->Branch(name, &v_multiClus_dZ);
            
            sprintf(name, "multiClus_dEta");
            tree->Branch(name, &v_multiClus_dEta);
            
            sprintf(name, "multiClus_dPhi");
            tree->Branch(name, &v_multiClus_dPhi);
            
            sprintf(name, "multiClus_sigma2rr");
            tree->Branch(name, &v_multiClus_sigma2rr);
            
            sprintf(name, "multiClus_sigma2etaEta");
            tree->Branch(name, &v_multiClus_sigma2etaEta);
            
            sprintf(name, "multiClus_sigma2phiPhi");
            tree->Branch(name, &v_multiClus_sigma2phiPhi);
            
            sprintf(name, "multiClus_sigma2rEta");
            tree->Branch(name, &v_multiClus_sigma2rEta);
            
            sprintf(name, "multiClus_sigma2rPhi");
            tree->Branch(name, &v_multiClus_sigma2rPhi);
            
            sprintf(name, "multiClus_sigma2etaPhi");
            tree->Branch(name, &v_multiClus_sigma2etaPhi);
            
            sprintf(name, "multiClus_sigma2diag1");
            tree->Branch(name, &v_multiClus_sigma2diag1);
            
            sprintf(name, "multiClus_sigma2diag2");
            tree->Branch(name, &v_multiClus_sigma2diag2);
            
            sprintf(name, "multiClus_sigma2diag3");
            tree->Branch(name, &v_multiClus_sigma2diag3);
            
            sprintf(name, "multiClus_EsortedIndex");
            tree->Branch(name, &v_multiClus_EsortedIndex);
            
            sprintf(name, "multiClus_HGCalEEP_EsortedIndex");
            tree->Branch(name, &v_multiClus_HGCalEEP_EsortedIndex);
            
            sprintf(name, "multiClus_HGCalEEM_EsortedIndex");
            tree->Branch(name, &v_multiClus_HGCalEEM_EsortedIndex);
            
            
            //
            sprintf(name, "multiClus_clus_n");
            tree->Branch(name, &v_multiClus_clus_n);
            
            sprintf(name, "multiClus_clus_startIndex");
            tree->Branch(name, &v_multiClus_clus_startIndex);
            
            sprintf(name, "multiClus_clus_E");
            tree->Branch(name, &v_multiClus_clus_E);
            
            sprintf(name, "multiClus_clus_x");
            tree->Branch(name, &v_multiClus_clus_x);
            
            sprintf(name, "multiClus_clus_y");
            tree->Branch(name, &v_multiClus_clus_y);
            
            sprintf(name, "multiClus_clus_z");
            tree->Branch(name, &v_multiClus_clus_z);
            
            sprintf(name, "multiClus_clus_eta");
            tree->Branch(name, &v_multiClus_clus_eta);
            
            sprintf(name, "multiClus_clus_phi");
            tree->Branch(name, &v_multiClus_clus_phi);
            
            sprintf(name, "multiClus_clus_ET");
            tree->Branch(name, &v_multiClus_clus_ET);
            
            
            sprintf(name, "multiClus_clus_layer");
            tree->Branch(name, &v_multiClus_clus_layer);
            
            sprintf(name, "multiClus_clus_multiplicity");
            tree->Branch(name, &v_multiClus_clus_multiplicity);
            
            sprintf(name, "multiClus_clus_nHit");
            tree->Branch(name, &v_multiClus_clus_nHit);
            
            
            //
            sprintf(name, "multiClus_uniqueClus_n");
            tree->Branch(name, &v_multiClus_uniqueClus_n);
            
            sprintf(name, "multiClus_uniqueClus_E");
            tree->Branch(name, &v_multiClus_uniqueClus_E);
            
            sprintf(name, "multiClus_uniqueClus_x");
            tree->Branch(name, &v_multiClus_uniqueClus_x);
            
            sprintf(name, "multiClus_uniqueClus_y");
            tree->Branch(name, &v_multiClus_uniqueClus_y);
            
            sprintf(name, "multiClus_uniqueClus_z");
            tree->Branch(name, &v_multiClus_uniqueClus_z);
            
            sprintf(name, "multiClus_uniqueClus_eta");
            tree->Branch(name, &v_multiClus_uniqueClus_eta);
            
            sprintf(name, "multiClus_uniqueClus_phi");
            tree->Branch(name, &v_multiClus_uniqueClus_phi);
            
            sprintf(name, "multiClus_uniqueClus_ET");
            tree->Branch(name, &v_multiClus_uniqueClus_ET);
            
            
            sprintf(name, "multiClus_uniqueClus_layer");
            tree->Branch(name, &v_multiClus_uniqueClus_layer);
            
            sprintf(name, "multiClus_uniqueClus_multiplicity");
            tree->Branch(name, &v_multiClus_uniqueClus_multiplicity);
            
            sprintf(name, "multiClus_uniqueClus_nHit");
            tree->Branch(name, &v_multiClus_uniqueClus_nHit);
            
            
            //
            sprintf(name, "multiClus_HGCalEEP_meanX");
            tree->Branch(name, &multiClus_HGCalEEP_meanX);
            
            sprintf(name, "multiClus_HGCalEEP_meanY");
            tree->Branch(name, &multiClus_HGCalEEP_meanY);
            
            sprintf(name, "multiClus_HGCalEEP_meanZ");
            tree->Branch(name, &multiClus_HGCalEEP_meanZ);
            
            sprintf(name, "multiClus_HGCalEEP_meanDx");
            tree->Branch(name, &multiClus_HGCalEEP_meanDx);
            
            sprintf(name, "multiClus_HGCalEEP_meanDy");
            tree->Branch(name, &multiClus_HGCalEEP_meanDy);
            
            sprintf(name, "multiClus_HGCalEEP_meanDz");
            tree->Branch(name, &multiClus_HGCalEEP_meanDz);
            
            sprintf(name, "multiClus_HGCalEEP_totE");
            tree->Branch(name, &multiClus_HGCalEEP_totE);
            
            sprintf(name, "multiClus_HGCalEEP_totET");
            tree->Branch(name, &multiClus_HGCalEEP_totET);
            
            sprintf(name, "multiClus_HGCalEEP_diag1");
            tree->Branch(name, &multiClus_HGCalEEP_diag1);
            
            sprintf(name, "multiClus_HGCalEEP_diag2");
            tree->Branch(name, &multiClus_HGCalEEP_diag2);
            
            sprintf(name, "multiClus_HGCalEEP_diag3");
            tree->Branch(name, &multiClus_HGCalEEP_diag3);
            
            //
            sprintf(name, "multiClus_HGCalEEM_meanX");
            tree->Branch(name, &multiClus_HGCalEEM_meanX);
            
            sprintf(name, "multiClus_HGCalEEM_meanY");
            tree->Branch(name, &multiClus_HGCalEEM_meanY);
            
            sprintf(name, "multiClus_HGCalEEM_meanZ");
            tree->Branch(name, &multiClus_HGCalEEM_meanZ);
            
            sprintf(name, "multiClus_HGCalEEM_meanDx");
            tree->Branch(name, &multiClus_HGCalEEM_meanDx);
            
            sprintf(name, "multiClus_HGCalEEM_meanDy");
            tree->Branch(name, &multiClus_HGCalEEM_meanDy);
            
            sprintf(name, "multiClus_HGCalEEM_meanDz");
            tree->Branch(name, &multiClus_HGCalEEM_meanDz);
            
            sprintf(name, "multiClus_HGCalEEM_totE");
            tree->Branch(name, &multiClus_HGCalEEM_totE);
            
            sprintf(name, "multiClus_HGCalEEM_totET");
            tree->Branch(name, &multiClus_HGCalEEM_totET);
            
            sprintf(name, "multiClus_HGCalEEM_diag1");
            tree->Branch(name, &multiClus_HGCalEEM_diag1);
            
            sprintf(name, "multiClus_HGCalEEM_diag2");
            tree->Branch(name, &multiClus_HGCalEEM_diag2);
            
            sprintf(name, "multiClus_HGCalEEM_diag3");
            tree->Branch(name, &multiClus_HGCalEEM_diag3);
            
            
            //
            sprintf(name, "simHit_n");
            tree->Branch(name, &simHit_n);
            
            sprintf(name, "simHit_E");
            tree->Branch(name, &v_simHit_E);
            
            sprintf(name, "simHit_x");
            tree->Branch(name, &v_simHit_x);
            
            sprintf(name, "simHit_y");
            tree->Branch(name, &v_simHit_y);
            
            sprintf(name, "simHit_z");
            tree->Branch(name, &v_simHit_z);
            
            sprintf(name, "simHit_eta");
            tree->Branch(name, &v_simHit_eta);
            
            sprintf(name, "simHit_phi");
            tree->Branch(name, &v_simHit_phi);
            
            sprintf(name, "simHit_ET");
            tree->Branch(name, &v_simHit_ET);
            
            sprintf(name, "simHit_layer");
            tree->Branch(name, &v_simHit_layer);
            
            sprintf(name, "simHit_zside");
            tree->Branch(name, &v_simHit_zside);
            
            sprintf(name, "simHit_isCaloParticleMatched");
            tree->Branch(name, &v_simHit_isCaloParticleMatched);
            
            
            //
            sprintf(name, "recHit_n");
            tree->Branch(name, &recHit_n);
            
            sprintf(name, "recHit_E");
            tree->Branch(name, &v_recHit_E);
            
            sprintf(name, "recHit_x");
            tree->Branch(name, &v_recHit_x);
            
            sprintf(name, "recHit_y");
            tree->Branch(name, &v_recHit_y);
            
            sprintf(name, "recHit_z");
            tree->Branch(name, &v_recHit_z);
            
            sprintf(name, "recHit_eta");
            tree->Branch(name, &v_recHit_eta);
            
            sprintf(name, "recHit_phi");
            tree->Branch(name, &v_recHit_phi);
            
            sprintf(name, "recHit_ET");
            tree->Branch(name, &v_recHit_ET);
            
            sprintf(name, "recHit_layer");
            tree->Branch(name, &v_recHit_layer);
            
            sprintf(name, "recHit_zside");
            tree->Branch(name, &v_recHit_zside);
            
            sprintf(name, "recHit_matchedSimHitIndex");
            tree->Branch(name, &v_recHit_matchedSimHitIndex);
            
            sprintf(name, "recHit_matchedHGCALlayerClusIndex");
            tree->Branch(name, &v_recHit_matchedHGCALlayerClusIndex);
            
            sprintf(name, "recHit_isMultiClusMatched");
            tree->Branch(name, &v_recHit_isMultiClusMatched);
            
            sprintf(name, "recHit_isCaloParticleMatched");
            tree->Branch(name, &v_recHit_isCaloParticleMatched);
            
            
            //
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
            
            
            //
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
            
            sprintf(name, "gsfEleFromTICL_superClus_nearestCellDist");
            tree->Branch(name, &v_gsfEleFromTICL_superClus_nearestCellDist);
            
            
            //
            sprintf(name, "caloParticle_n");
            tree->Branch(name, &caloParticle_n);
            
            sprintf(name, "caloParticle_E");
            tree->Branch(name, &v_caloParticle_E);
            
            sprintf(name, "caloParticle_px");
            tree->Branch(name, &v_caloParticle_px);
            
            sprintf(name, "caloParticle_py");
            tree->Branch(name, &v_caloParticle_py);
            
            sprintf(name, "caloParticle_pz");
            tree->Branch(name, &v_caloParticle_pz);
            
            sprintf(name, "caloParticle_pT");
            tree->Branch(name, &v_caloParticle_pT);
            
            sprintf(name, "caloParticle_eta");
            tree->Branch(name, &v_caloParticle_eta);
            
            sprintf(name, "caloParticle_phi");
            tree->Branch(name, &v_caloParticle_phi);
            
            sprintf(name, "caloParticle_pdgid");
            tree->Branch(name, &v_caloParticle_pdgid);
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
            
            v_genEl_HGCalEEP_EsortedIndex.clear();
            v_genEl_HGCalEEM_EsortedIndex.clear();
            
            v_genEl_multiClus_totE.clear();
            
            v_genEl_multiClus_n.clear();
            v_genEl_nearestMultiClusEnRatio.clear();
            v_genEl_multiClusEnRatio.clear();
            
            
            // Gen photon //
            genPh_n = 0;
            v_genPh_E.clear();
            v_genPh_px.clear();
            v_genPh_py.clear();
            v_genPh_pz.clear();
            v_genPh_pT.clear();
            v_genPh_eta.clear();
            v_genPh_phi.clear();
            
            v_genPh_HGCalEEP_EsortedIndex.clear();
            v_genPh_HGCalEEM_EsortedIndex.clear();
            
            v_genPh_multiClus_totE.clear();
            
            v_genPh_HGCalEEP_deltaR.clear();
            v_genPh_HGCalEEM_deltaR.clear();
            
            
            // HGCAL layer clusters
            HGCALlayerClus_n = 0;
            v_HGCALlayerClus_E.clear();
            v_HGCALlayerClus_x.clear();
            v_HGCALlayerClus_y.clear();
            v_HGCALlayerClus_z.clear();
            v_HGCALlayerClus_eta.clear();
            v_HGCALlayerClus_phi.clear();
            v_HGCALlayerClus_ET.clear();
            v_HGCALlayerClus_layer.clear();
            
            v_HGCALlayerClus_isInMultiClus.clear();
            v_HGCALlayerClus_sigRecHit_totE.clear();
            v_HGCALlayerClus_sigRecHit_Efraction.clear();
            
            
            // MultiClusters
            multiClus_n = 0;
            v_multiClus_genElIndex.clear();
            v_multiClus_E.clear();
            v_multiClus_x.clear();
            v_multiClus_y.clear();
            v_multiClus_z.clear();
            v_multiClus_eta.clear();
            v_multiClus_phi.clear();
            v_multiClus_ET.clear();
            
            v_multiClus_dX.clear();
            v_multiClus_dY.clear();
            v_multiClus_dZ.clear();
            
            v_multiClus_dEta.clear();
            v_multiClus_dPhi.clear();
            
            v_multiClus_sigma2rr.clear();
            v_multiClus_sigma2etaEta.clear();
            v_multiClus_sigma2phiPhi.clear();
            
            v_multiClus_sigma2rEta.clear();
            v_multiClus_sigma2rPhi.clear();
            v_multiClus_sigma2etaPhi.clear();
            
            v_multiClus_sigma2diag1.clear();
            v_multiClus_sigma2diag2.clear();
            v_multiClus_sigma2diag3.clear();
            
            v_multiClus_EsortedIndex.clear();
            v_multiClus_HGCalEEP_EsortedIndex.clear();
            v_multiClus_HGCalEEM_EsortedIndex.clear();
            
            
            v_multiClus_clus_n.clear();
            v_multiClus_clus_startIndex.clear();
            v_multiClus_clus_E.clear();
            v_multiClus_clus_x.clear();
            v_multiClus_clus_y.clear();
            v_multiClus_clus_z.clear();
            v_multiClus_clus_eta.clear();
            v_multiClus_clus_phi.clear();
            v_multiClus_clus_ET.clear();
            
            v_multiClus_clus_layer.clear();
            v_multiClus_clus_multiplicity.clear();
            v_multiClus_clus_nHit.clear();
            
            
            v_multiClus_uniqueClus_n.clear();
            v_multiClus_uniqueClus_E.clear();
            v_multiClus_uniqueClus_x.clear();
            v_multiClus_uniqueClus_y.clear();
            v_multiClus_uniqueClus_z.clear();
            v_multiClus_uniqueClus_eta.clear();
            v_multiClus_uniqueClus_phi.clear();
            v_multiClus_uniqueClus_ET.clear();
            
            v_multiClus_uniqueClus_layer.clear();
            v_multiClus_uniqueClus_multiplicity.clear();
            v_multiClus_uniqueClus_nHit.clear();
            
            
            multiClus_HGCalEEP_meanX = 0;
            multiClus_HGCalEEP_meanY = 0;
            multiClus_HGCalEEP_meanZ = 0;
            multiClus_HGCalEEP_totE = 0;
            multiClus_HGCalEEP_totET = 0;
            
            multiClus_HGCalEEP_diag1 = 0;
            multiClus_HGCalEEP_diag2 = 0;
            multiClus_HGCalEEP_diag3 = 0;
            
            
            multiClus_HGCalEEM_meanX = 0;
            multiClus_HGCalEEM_meanY = 0;
            multiClus_HGCalEEM_meanZ = 0;
            multiClus_HGCalEEM_totE = 0;
            multiClus_HGCalEEM_totET = 0;
            
            multiClus_HGCalEEM_diag1 = 0;
            multiClus_HGCalEEM_diag2 = 0;
            multiClus_HGCalEEM_diag3 = 0;
            
            
            for(int iLayer = 0; iLayer < Constants::HGCalEE_nLayer; iLayer++)
            {
                v_simHit_HGCalEEPlayer_totE.at(iLayer) = 0;
                v_recHit_HGCalEEPlayer_totE.at(iLayer) = 0;
                
                v_simHit_HGCalEEMlayer_totE.at(iLayer) = 0;
                v_recHit_HGCalEEMlayer_totE.at(iLayer) = 0;
            }
            
            
            //
            simHit_n = 0;
            v_simHit_E.clear();
            v_simHit_x.clear();
            v_simHit_y.clear();
            v_simHit_z.clear();
            v_simHit_eta.clear();
            v_simHit_phi.clear();
            v_simHit_ET.clear();
            v_simHit_layer.clear();
            v_simHit_zside.clear();
            v_simHit_isCaloParticleMatched.clear();
            
            
            //
            recHit_n = 0;
            v_recHit_E.clear();
            v_recHit_x.clear();
            v_recHit_y.clear();
            v_recHit_z.clear();
            v_recHit_eta.clear();
            v_recHit_phi.clear();
            v_recHit_ET.clear();
            v_recHit_layer.clear();
            v_recHit_zside.clear();
            v_recHit_matchedSimHitIndex.clear();
            v_recHit_matchedHGCALlayerClusIndex.clear();
            v_recHit_isMultiClusMatched.clear();
            v_recHit_isCaloParticleMatched.clear();
            
            
            //
            gsfEleFromMultiClus_n = 0;
            v_gsfEleFromMultiClus_E.clear();
            v_gsfEleFromMultiClus_px.clear();
            v_gsfEleFromMultiClus_py.clear();
            v_gsfEleFromMultiClus_pz.clear();
            v_gsfEleFromMultiClus_pT.clear();
            v_gsfEleFromMultiClus_eta.clear();
            v_gsfEleFromMultiClus_phi.clear();
            
            
            //
            gsfEleFromTICL_n = 0;
            v_gsfEleFromTICL_E.clear();
            v_gsfEleFromTICL_px.clear();
            v_gsfEleFromTICL_py.clear();
            v_gsfEleFromTICL_pz.clear();
            v_gsfEleFromTICL_pT.clear();
            v_gsfEleFromTICL_eta.clear();
            v_gsfEleFromTICL_phi.clear();
            
            v_gsfEleFromTICL_superClus_nearestCellDist.clear();
            
            
            //
            caloParticle_n = 0;
            v_caloParticle_E.clear();
            v_caloParticle_px.clear();
            v_caloParticle_py.clear();
            v_caloParticle_pz.clear();
            v_caloParticle_pT.clear();
            v_caloParticle_eta.clear();
            v_caloParticle_phi.clear();
            v_caloParticle_pdgid.clear();
        }
    };
}


# endif
