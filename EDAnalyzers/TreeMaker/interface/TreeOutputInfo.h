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
        
        
        // Pileup //
        int pileup_n;
        
        
        // Rho //
        double rho;
        
        
        // PV //
        double PV_t;
        double PV_tErr;
        
        
        // Slimmed electron //
        double slimmedEle_n;
        std::vector <double> v_slimmedEle_idx;
        
        std::vector <double> v_slimmedEle_E;
        std::vector <double> v_slimmedEle_px;
        std::vector <double> v_slimmedEle_py;
        std::vector <double> v_slimmedEle_pz;
        std::vector <double> v_slimmedEle_pT;
        std::vector <double> v_slimmedEle_eta;
        std::vector <double> v_slimmedEle_phi;
        std::vector <double> v_slimmedEle_ET;
        
        std::vector <double> v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values;
        std::vector <double> v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
        
        std::vector <double> v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
        std::vector <double> v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
        
        std::vector <double> v_slimmedEle_genEl_minDeltaR;
        std::vector <double> v_slimmedEle_nearestGenEl_idx;
        std::vector <double> v_slimmedEle_matchedGenEl_E;
        std::vector <double> v_slimmedEle_matchedGenEl_pT;
        std::vector <double> v_slimmedEle_matchedGenEl_eta;
        std::vector <double> v_slimmedEle_matchedGenEl_phi;
        
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_charged;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_neutral;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_ecal;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_hcal;
        //
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_charged_cleanedDT3sigma;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma;
        //
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5;
        //std::vector <double> v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma;
        //
        //std::vector <double> v_slimmedEle_sig_pfCand1_PV_dtSigni;
        //std::vector <double> v_slimmedEle_sig_pfCand2_PV_dtSigni;
        //
        //std::vector <double> v_slimmedEle_isoDR0p3_pfCand1_PV_dtSigni;
        //std::vector <double> v_slimmedEle_isoDR0p3_pfCand2_PV_dtSigni;
        //
        //std::vector <double> v_slimmedEle_sig_pfCand_PV_dtSigniMean;
        //std::vector <double> v_slimmedEle_isoDR0p3_pfCand_PV_dtSigniMean;
        
        struct Ele_sigVarContent
        {
            std::vector <double> v_slimmedEle_sig_pfCand_n;
            
            std::vector <double> v_slimmedEle_sig_pfCand1_PV_dtSigni;
            std::vector <double> v_slimmedEle_sig_pfCand2_PV_dtSigni;
            
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dtSigniMean;
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd;
            
            std::vector <double> v_slimmedEle_sig_pfCand1_PV_dz;
            std::vector <double> v_slimmedEle_sig_pfCand2_PV_dz;
            
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dzMean;
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dzMean_ETwtd;
            
            
            void clear()
            {
                v_slimmedEle_sig_pfCand_n.clear();
                
                v_slimmedEle_sig_pfCand1_PV_dtSigni.clear();
                v_slimmedEle_sig_pfCand2_PV_dtSigni.clear();
                
                v_slimmedEle_sig_pfCand_PV_dtSigniMean.clear();
                v_slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd.clear();
                
                v_slimmedEle_sig_pfCand1_PV_dz.clear();
                v_slimmedEle_sig_pfCand2_PV_dz.clear();
                
                v_slimmedEle_sig_pfCand_PV_dzMean.clear();
                v_slimmedEle_sig_pfCand_PV_dzMean_ETwtd.clear();
            }
        };
        
        std::map <std::string, Ele_sigVarContent*> m_Ele_sigVarContent;
        
        struct Ele_isoVarContent
        {
            std::vector <double> v_slimmedEle_iso_pfCand_n;
            
            std::vector <double> v_slimmedEle_iso_sumETratio;
            std::vector <double> v_slimmedEle_iso_sumETratio_charged;
            std::vector <double> v_slimmedEle_iso_sumETratio_neutral;
            std::vector <double> v_slimmedEle_iso_sumETratio_ecal;
            std::vector <double> v_slimmedEle_iso_sumETratio_hcal;
            
            std::vector <double> v_slimmedEle_iso_pfCand1_PV_dtSigni;
            std::vector <double> v_slimmedEle_iso_pfCand2_PV_dtSigni;
            
            std::vector <double> v_slimmedEle_iso_pfCand_PV_dtSigniMean;
            std::vector <double> v_slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd;
            
            std::vector <double> v_slimmedEle_iso_pfCand1_PV_dz;
            std::vector <double> v_slimmedEle_iso_pfCand2_PV_dz;
            
            std::vector <double> v_slimmedEle_iso_pfCand_PV_dzMean;
            std::vector <double> v_slimmedEle_iso_pfCand_PV_dzMean_ETwtd;
            
            
            void clear()
            {
                v_slimmedEle_iso_pfCand_n.clear();
                
                v_slimmedEle_iso_sumETratio.clear();
                v_slimmedEle_iso_sumETratio_charged.clear();
                v_slimmedEle_iso_sumETratio_neutral.clear();
                v_slimmedEle_iso_sumETratio_ecal.clear();
                v_slimmedEle_iso_sumETratio_hcal.clear();
                
                v_slimmedEle_iso_pfCand1_PV_dtSigni.clear();
                v_slimmedEle_iso_pfCand2_PV_dtSigni.clear();
                
                v_slimmedEle_iso_pfCand_PV_dtSigniMean.clear();
                v_slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd.clear();
                
                v_slimmedEle_iso_pfCand1_PV_dz.clear();
                v_slimmedEle_iso_pfCand2_PV_dz.clear();
                
                v_slimmedEle_iso_pfCand_PV_dzMean.clear();
                v_slimmedEle_iso_pfCand_PV_dzMean_ETwtd.clear();
            }
        };
        
        std::map <std::string, Ele_isoVarContent*> m_Ele_isoVarContent;
        
        
        //
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_eleIdx;
        
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_charge;
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_ET;
        
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_t;
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_tErr;
        
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_PV_dt;
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_PV_dtSigni;
        
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_PV_dz;
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_PV_dzSigni;
        
        //
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_eleIdx;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_charge;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_ET;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_t;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_tErr;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dt;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dz;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni;
        
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
            
            
            // Pileup //
            sprintf(name, "pileup_n");
            tree->Branch(name, &pileup_n);
            
            
            // Rho //
            sprintf(name, "rho");
            tree->Branch(name, &rho);
            
            
            // PV //
            sprintf(name, "PV_t");
            tree->Branch(name, &PV_t);
            
            sprintf(name, "PV_tErr");
            tree->Branch(name, &PV_tErr);
            
            
            // Slimmed electron //
            sprintf(name, "slimmedEle_n");
            tree->Branch(name, &slimmedEle_n);
            
            sprintf(name, "slimmedEle_idx");
            tree->Branch(name, &v_slimmedEle_idx);
            
            sprintf(name, "slimmedEle_E");
            tree->Branch(name, &v_slimmedEle_E);
            
            sprintf(name, "slimmedEle_px");
            tree->Branch(name, &v_slimmedEle_px);
            
            sprintf(name, "slimmedEle_py");
            tree->Branch(name, &v_slimmedEle_py);
            
            sprintf(name, "slimmedEle_pz");
            tree->Branch(name, &v_slimmedEle_pz);
            
            sprintf(name, "slimmedEle_pT");
            tree->Branch(name, &v_slimmedEle_pT);
            
            sprintf(name, "slimmedEle_eta");
            tree->Branch(name, &v_slimmedEle_eta);
            
            sprintf(name, "slimmedEle_phi");
            tree->Branch(name, &v_slimmedEle_phi);
            
            sprintf(name, "slimmedEle_ET");
            tree->Branch(name, &v_slimmedEle_ET);
            
            //
            sprintf(name, "slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values");
            tree->Branch(name, &v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values);
            
            sprintf(name, "slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues");
            tree->Branch(name, &v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues);
            
            sprintf(name, "slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values");
            tree->Branch(name, &v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values);
            
            sprintf(name, "slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues");
            tree->Branch(name, &v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues);
            
            //
            sprintf(name, "slimmedEle_genEl_minDeltaR");
            tree->Branch(name, &v_slimmedEle_genEl_minDeltaR);
            
            sprintf(name, "slimmedEle_nearestGenEl_idx");
            tree->Branch(name, &v_slimmedEle_nearestGenEl_idx);
            
            sprintf(name, "slimmedEle_matchedGenEl_E");
            tree->Branch(name, &v_slimmedEle_matchedGenEl_E);
            
            sprintf(name, "slimmedEle_matchedGenEl_pT");
            tree->Branch(name, &v_slimmedEle_matchedGenEl_pT);
            
            sprintf(name, "slimmedEle_matchedGenEl_eta");
            tree->Branch(name, &v_slimmedEle_matchedGenEl_eta);
            
            sprintf(name, "slimmedEle_matchedGenEl_phi");
            tree->Branch(name, &v_slimmedEle_matchedGenEl_phi);
            
            ////
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_charged");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_charged);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_neutral");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_neutral);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_ecal");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_ecal);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_hcal");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_hcal);
            //
            ////
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_charged_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_charged_cleanedDT3sigma);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma);
            //
            ////
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_dzLt0p5");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma);
            //
            ////
            //sprintf(name, "slimmedEle_sig_pfCand1_PV_dtSigni");
            //tree->Branch(name, &v_slimmedEle_sig_pfCand1_PV_dtSigni);
            //
            //sprintf(name, "slimmedEle_sig_pfCand2_PV_dtSigni");
            //tree->Branch(name, &v_slimmedEle_sig_pfCand2_PV_dtSigni);
            //
            ////
            //sprintf(name, "slimmedEle_isoDR0p3_pfCand1_PV_dtSigni");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_pfCand1_PV_dtSigni);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_pfCand2_PV_dtSigni");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_pfCand2_PV_dtSigni);
            //
            ////
            //sprintf(name, "slimmedEle_sig_pfCand_PV_dtSigniMean");
            //tree->Branch(name, &v_slimmedEle_sig_pfCand_PV_dtSigniMean);
            //
            //sprintf(name, "slimmedEle_isoDR0p3_pfCand_PV_dtSigniMean");
            //tree->Branch(name, &v_slimmedEle_isoDR0p3_pfCand_PV_dtSigniMean);
            
            //
            sprintf(name, "slimmedEle_sig_pfCand_eleIdx");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_eleIdx);
            
            sprintf(name, "slimmedEle_sig_pfCand_charge");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_charge);
            
            sprintf(name, "slimmedEle_sig_pfCand_ET");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_ET);
            
            sprintf(name, "slimmedEle_sig_pfCand_t");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_t);
            
            sprintf(name, "slimmedEle_sig_pfCand_tErr");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_tErr);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dt");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_PV_dt);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dtSigni");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_PV_dtSigni);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dz");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_PV_dz);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dzSigni");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_PV_dzSigni);
            
            //
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_eleIdx");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_eleIdx);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_charge");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_charge);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_ET");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_ET);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_t");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_t);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_tErr");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_tErr);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_PV_dt");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_PV_dt);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_PV_dtSigni");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_PV_dz");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_PV_dz);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_PV_dzSigni");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni);
        }
        
        
        void init_Ele_sigVarContent(std::string key)
        {
            if(!key.length())
            {
                printf("Error in TreeOutput::init_Ele_sigVar(...): Argument \"key\" cannot be empty. \n");
                printf("Exiting... \n");
                
                exit(EXIT_FAILURE);
            }
            
            Ele_sigVarContent *sigVarContent = new Ele_sigVarContent();
            
            
            sprintf(name, "slimmedEle_sig_pfCand_n_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand_n);
            
            //
            sprintf(name, "slimmedEle_sig_pfCand1_PV_dtSigni_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand1_PV_dtSigni);
            
            sprintf(name, "slimmedEle_sig_pfCand2_PV_dtSigni_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand2_PV_dtSigni);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dtSigniMean_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand_PV_dtSigniMean);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd);
            
            //
            sprintf(name, "slimmedEle_sig_pfCand1_PV_dz_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand1_PV_dz);
            
            sprintf(name, "slimmedEle_sig_pfCand2_PV_dz_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand2_PV_dz);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dzMean_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand_PV_dzMean);
            
            sprintf(name, "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand_PV_dzMean_ETwtd);
            
            
            // Add to the map
            m_Ele_sigVarContent[key] = sigVarContent;
        }
        
        
        void init_Ele_isoVarContent(std::string key)
        {
            if(!key.length())
            {
                printf("Error in TreeOutput::init_Ele_isoVar(...): Argument \"key\" cannot be empty. \n");
                printf("Exiting... \n");
                
                exit(EXIT_FAILURE);
            }
            
            Ele_isoVarContent *isoVarContent = new Ele_isoVarContent();
            
            
            sprintf(name, "slimmedEle_iso_pfCand_n_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand_n);
            
            //
            sprintf(name, "slimmedEle_iso_sumETratio_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_sumETratio);
            
            sprintf(name, "slimmedEle_iso_sumETratio_charged_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_sumETratio_charged);
            
            sprintf(name, "slimmedEle_iso_sumETratio_neutral_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_sumETratio_neutral);
            
            sprintf(name, "slimmedEle_iso_sumETratio_ecal_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_sumETratio_ecal);
            
            sprintf(name, "slimmedEle_iso_sumETratio_hcal_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_sumETratio_hcal);
            
            //
            sprintf(name, "slimmedEle_iso_pfCand1_PV_dtSigni_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand1_PV_dtSigni);
            
            sprintf(name, "slimmedEle_iso_pfCand2_PV_dtSigni_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand2_PV_dtSigni);
            
            sprintf(name, "slimmedEle_iso_pfCand_PV_dtSigniMean_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand_PV_dtSigniMean);
            
            sprintf(name, "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd);
            
            //
            sprintf(name, "slimmedEle_iso_pfCand1_PV_dz_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand1_PV_dz);
            
            sprintf(name, "slimmedEle_iso_pfCand2_PV_dz_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand2_PV_dz);
            
            sprintf(name, "slimmedEle_iso_pfCand_PV_dzMean_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand_PV_dzMean);
            
            sprintf(name, "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_%s", key.c_str());
            tree->Branch(name, &isoVarContent->v_slimmedEle_iso_pfCand_PV_dzMean_ETwtd);
            
            
            // Add to the map
            m_Ele_isoVarContent[key] = isoVarContent;
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
            
            
            // Pileup //
            pileup_n = 0;
            
            
            // Rho //
            rho = 0;
            
            
            // PV //
            PV_t = 0;
            PV_tErr = 0;
            
            
            // Slimmed electron //
            slimmedEle_n = 0;
            
            v_slimmedEle_idx.clear();
            
            v_slimmedEle_E.clear();
            v_slimmedEle_px.clear();
            v_slimmedEle_py.clear();
            v_slimmedEle_pz.clear();
            v_slimmedEle_pT.clear();
            v_slimmedEle_eta.clear();
            v_slimmedEle_phi.clear();
            v_slimmedEle_ET.clear();
            
            v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values.clear();
            v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues.clear();
            
            v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values.clear();
            v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues.clear();
            
            v_slimmedEle_genEl_minDeltaR.clear();
            v_slimmedEle_nearestGenEl_idx.clear();
            v_slimmedEle_matchedGenEl_E.clear();
            v_slimmedEle_matchedGenEl_pT.clear();
            v_slimmedEle_matchedGenEl_eta.clear();
            v_slimmedEle_matchedGenEl_phi.clear();
            
            //v_slimmedEle_isoDR0p3_sumETratio.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_charged.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_neutral.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_ecal.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_hcal.clear();
            //
            //v_slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_charged_cleanedDT3sigma.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma.clear();
            //
            //v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5.clear();
            //v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma.clear();
            //
            //v_slimmedEle_sig_pfCand1_PV_dtSigni.clear();
            //v_slimmedEle_sig_pfCand2_PV_dtSigni.clear();
            //
            //v_slimmedEle_isoDR0p3_pfCand1_PV_dtSigni.clear();
            //v_slimmedEle_isoDR0p3_pfCand2_PV_dtSigni.clear();
            //
            //v_slimmedEle_sig_pfCand_PV_dtSigniMean.clear();
            //v_slimmedEle_isoDR0p3_pfCand_PV_dtSigniMean.clear();
            
            //
            vv_slimmedEle_sig_pfCand_eleIdx.clear();
            
            vv_slimmedEle_sig_pfCand_charge.clear();
            vv_slimmedEle_sig_pfCand_ET.clear();
            
            vv_slimmedEle_sig_pfCand_t.clear();
            vv_slimmedEle_sig_pfCand_tErr.clear();
            
            vv_slimmedEle_sig_pfCand_PV_dt.clear();
            vv_slimmedEle_sig_pfCand_PV_dtSigni.clear();
            
            vv_slimmedEle_sig_pfCand_PV_dz.clear();
            vv_slimmedEle_sig_pfCand_PV_dzSigni.clear();
            
            //
            vv_slimmedEle_isoDR0p3_pfCand_eleIdx.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_charge.clear();
            vv_slimmedEle_isoDR0p3_pfCand_ET.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_t.clear();
            vv_slimmedEle_isoDR0p3_pfCand_tErr.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_PV_dt.clear();
            vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_PV_dz.clear();
            vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni.clear();
            
            
            for(auto iter = m_Ele_sigVarContent.begin(); iter != m_Ele_sigVarContent.end(); iter++)
            {
                iter->second->clear();
            }
            
            for(auto iter = m_Ele_isoVarContent.begin(); iter != m_Ele_isoVarContent.end(); iter++)
            {
                iter->second->clear();
            }
        }
    };
}


# endif
