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
        
        
        // Rho //
        double pileupDensity;
        
        
        // PV //
        double PV_t;
        double PV_tErr;
        
        
        int PV4D_n;
        std::vector <double> v_PV4D_x;
        std::vector <double> v_PV4D_y;
        std::vector <double> v_PV4D_z;
        
        int PU_n;
        std::vector <double> v_PU_x;
        std::vector <double> v_PU_y;
        std::vector <double> v_PU_z;
        
        
        struct IsoVarContent
        {
            std::vector <double> v_iso_pfCand_n;
            
            std::vector <double> v_iso_sumETratio;
            std::vector <double> v_iso_sumETratio_charged;
            std::vector <double> v_iso_sumETratio_neutral;
            std::vector <double> v_iso_sumETratio_ecal;
            std::vector <double> v_iso_sumETratio_hcal;
            
            //
            std::vector <double> v_iso_pfCand1_sig_dt;
            std::vector <double> v_iso_pfCand2_sig_dt;
            
            std::vector <double> v_iso_pfCand_sig_dtMean;
            std::vector <double> v_iso_pfCand_sig_dtMean_ETwtd;
            
            //
            std::vector <double> v_iso_pfCand1_sig_dtSigni;
            std::vector <double> v_iso_pfCand2_sig_dtSigni;
            
            std::vector <double> v_iso_pfCand_sig_dtSigniMean;
            std::vector <double> v_iso_pfCand_sig_dtSigniMean_ETwtd;
            
            //
            std::vector <double> v_iso_pfCand1_PV_dt;
            std::vector <double> v_iso_pfCand2_PV_dt;
            
            std::vector <double> v_iso_pfCand_PV_dtMean;
            std::vector <double> v_iso_pfCand_PV_dtMean_ETwtd;
            
            //
            std::vector <double> v_iso_pfCand1_PV_dtSigni;
            std::vector <double> v_iso_pfCand2_PV_dtSigni;
            
            std::vector <double> v_iso_pfCand_PV_dtSigniMean;
            std::vector <double> v_iso_pfCand_PV_dtSigniMean_ETwtd;
            
            //
            std::vector <double> v_iso_pfCand1_sig_dz;
            std::vector <double> v_iso_pfCand2_sig_dz;
            
            std::vector <double> v_iso_pfCand_sig_dzMean;
            std::vector <double> v_iso_pfCand_sig_dzMean_ETwtd;
            
            //
            std::vector <double> v_iso_pfCand1_PV_dz;
            std::vector <double> v_iso_pfCand2_PV_dz;
            
            std::vector <double> v_iso_pfCand_PV_dzMean;
            std::vector <double> v_iso_pfCand_PV_dzMean_ETwtd;
            
            
            void clear()
            {
                v_iso_pfCand_n.clear();
                
                v_iso_sumETratio.clear();
                v_iso_sumETratio_charged.clear();
                v_iso_sumETratio_neutral.clear();
                v_iso_sumETratio_ecal.clear();
                v_iso_sumETratio_hcal.clear();
                
                //
                v_iso_pfCand1_sig_dt.clear();
                v_iso_pfCand2_sig_dt.clear();
                
                v_iso_pfCand_sig_dtMean.clear();
                v_iso_pfCand_sig_dtMean_ETwtd.clear();
                
                v_iso_pfCand1_sig_dtSigni.clear();
                v_iso_pfCand2_sig_dtSigni.clear();
                
                v_iso_pfCand_sig_dtSigniMean.clear();
                v_iso_pfCand_sig_dtSigniMean_ETwtd.clear();
                
                //
                v_iso_pfCand1_PV_dt.clear();
                v_iso_pfCand2_PV_dt.clear();
                
                v_iso_pfCand_PV_dtMean.clear();
                v_iso_pfCand_PV_dtMean_ETwtd.clear();
                
                v_iso_pfCand1_PV_dtSigni.clear();
                v_iso_pfCand2_PV_dtSigni.clear();
                
                v_iso_pfCand_PV_dtSigniMean.clear();
                v_iso_pfCand_PV_dtSigniMean_ETwtd.clear();
                
                //
                v_iso_pfCand1_sig_dz.clear();
                v_iso_pfCand2_sig_dz.clear();
                
                v_iso_pfCand_sig_dzMean.clear();
                v_iso_pfCand_sig_dzMean_ETwtd.clear();
                
                //
                v_iso_pfCand1_PV_dz.clear();
                v_iso_pfCand2_PV_dz.clear();
                
                v_iso_pfCand_PV_dzMean.clear();
                v_iso_pfCand_PV_dzMean_ETwtd.clear();
            }
        };
        
        
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
        
        std::vector <double> v_slimmedEle_chargedHadronIso;
        
        struct Ele_sigVarContent
        {
            std::vector <double> v_slimmedEle_sig_pfCand_n;
            
            std::vector <double> v_slimmedEle_sig_pfCand1_PV_dt;
            std::vector <double> v_slimmedEle_sig_pfCand2_PV_dt;
            
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dtMean;
            std::vector <double> v_slimmedEle_sig_pfCand_PV_dtMean_ETwtd;
            
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
                
                v_slimmedEle_sig_pfCand1_PV_dt.clear();
                v_slimmedEle_sig_pfCand2_PV_dt.clear();
                
                v_slimmedEle_sig_pfCand_PV_dtMean.clear();
                v_slimmedEle_sig_pfCand_PV_dtMean_ETwtd.clear();
                
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
        
        
        //
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_eleIdx;
        
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_charge;
        std::vector <std::vector <double> > vv_slimmedEle_sig_pfCand_pT;
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
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_pT;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_ET;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_t;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_tErr;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_sig_dt;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_sig_dtSigni;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dt;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_sig_dz;
        
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dz;
        std::vector <std::vector <double> > vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni;
        
        
        // Slimmed photon //
        double slimmedPho_n;
        std::vector <double> v_slimmedPho_idx;
        
        std::vector <double> v_slimmedPho_E;
        std::vector <double> v_slimmedPho_px;
        std::vector <double> v_slimmedPho_py;
        std::vector <double> v_slimmedPho_pz;
        std::vector <double> v_slimmedPho_pT;
        std::vector <double> v_slimmedPho_eta;
        std::vector <double> v_slimmedPho_phi;
        std::vector <double> v_slimmedPho_ET;
        
        std::vector <double> v_slimmedPho_linkedGenPart_pdgId;
        
        std::vector <double> v_slimmedPho_genPh_minDeltaR;
        std::vector <double> v_slimmedPho_nearestGenPh_idx;
        std::vector <double> v_slimmedPho_matchedGenPh_E;
        std::vector <double> v_slimmedPho_matchedGenPh_pT;
        std::vector <double> v_slimmedPho_matchedGenPh_eta;
        std::vector <double> v_slimmedPho_matchedGenPh_phi;
        
        std::vector <double> v_slimmedPho_chargedHadronIso;
        std::vector <double> v_slimmedPho_neutralHadronIso;
        std::vector <double> v_slimmedPho_photonIso;
        
        
        // Isolation
        std::map <std::string, IsoVarContent*> m_IsoVarContent;
        
        
        
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
            
            
            // Gen electron //
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
            
            
            // Pileup //
            sprintf(name, "pileup_n");
            tree->Branch(name, &pileup_n);
            
            
            // Rho //
            sprintf(name, "rho");
            tree->Branch(name, &rho);
            
            
            // PU density //
            sprintf(name, "pileupDensity");
            tree->Branch(name, &pileupDensity);
            
            
            // PV //
            sprintf(name, "PV_t");
            tree->Branch(name, &PV_t);
            
            sprintf(name, "PV_tErr");
            tree->Branch(name, &PV_tErr);
            
            
            sprintf(name, "PV4D_n");
            tree->Branch(name, &PV4D_n);
            
            sprintf(name, "PV4D_x");
            tree->Branch(name, &v_PV4D_x);
            
            sprintf(name, "PV4D_y");
            tree->Branch(name, &v_PV4D_y);
            
            sprintf(name, "PV4D_z");
            tree->Branch(name, &v_PV4D_z);
            
            
            sprintf(name, "PU_n");
            tree->Branch(name, &PU_n);
            
            sprintf(name, "PU_x");
            tree->Branch(name, &v_PU_x);
            
            sprintf(name, "PU_y");
            tree->Branch(name, &v_PU_y);
            
            sprintf(name, "PU_z");
            tree->Branch(name, &v_PU_z);
            
            
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
            
            //
            sprintf(name, "slimmedEle_chargedHadronIso");
            tree->Branch(name, &v_slimmedEle_chargedHadronIso);
            
            
            //
            sprintf(name, "slimmedEle_sig_pfCand_eleIdx");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_eleIdx);
            
            sprintf(name, "slimmedEle_sig_pfCand_charge");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_charge);
            
            sprintf(name, "slimmedEle_sig_pfCand_pT");
            tree->Branch(name, &vv_slimmedEle_sig_pfCand_pT);
            
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
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_pT");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_pT);
            
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
            
            //
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_sig_dt");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_sig_dt);
            
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_sig_dtSigni");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_sig_dtSigni);
            
            //
            sprintf(name, "slimmedEle_isoDR0p3_pfCand_sig_dz");
            tree->Branch(name, &vv_slimmedEle_isoDR0p3_pfCand_sig_dz);
            
            
            // Slimmed photon //
            sprintf(name, "slimmedPho_n");
            tree->Branch(name, &slimmedPho_n);
            
            sprintf(name, "slimmedPho_idx");
            tree->Branch(name, &v_slimmedPho_idx);
            
            sprintf(name, "slimmedPho_E");
            tree->Branch(name, &v_slimmedPho_E);
            
            sprintf(name, "slimmedPho_px");
            tree->Branch(name, &v_slimmedPho_px);
            
            sprintf(name, "slimmedPho_py");
            tree->Branch(name, &v_slimmedPho_py);
            
            sprintf(name, "slimmedPho_pz");
            tree->Branch(name, &v_slimmedPho_pz);
            
            sprintf(name, "slimmedPho_pT");
            tree->Branch(name, &v_slimmedPho_pT);
            
            sprintf(name, "slimmedPho_eta");
            tree->Branch(name, &v_slimmedPho_eta);
            
            sprintf(name, "slimmedPho_phi");
            tree->Branch(name, &v_slimmedPho_phi);
            
            sprintf(name, "slimmedPho_ET");
            tree->Branch(name, &v_slimmedPho_ET);
            
            //
            sprintf(name, "slimmedPho_linkedGenPart_pdgId");
            tree->Branch(name, &v_slimmedPho_linkedGenPart_pdgId);
            
            //
            sprintf(name, "slimmedPho_genPh_minDeltaR");
            tree->Branch(name, &v_slimmedPho_genPh_minDeltaR);
            
            sprintf(name, "slimmedPho_nearestGenPh_idx");
            tree->Branch(name, &v_slimmedPho_nearestGenPh_idx);
            
            sprintf(name, "slimmedPho_matchedGenPh_E");
            tree->Branch(name, &v_slimmedPho_matchedGenPh_E);
            
            sprintf(name, "slimmedPho_matchedGenPh_pT");
            tree->Branch(name, &v_slimmedPho_matchedGenPh_pT);
            
            sprintf(name, "slimmedPho_matchedGenPh_eta");
            tree->Branch(name, &v_slimmedPho_matchedGenPh_eta);
            
            sprintf(name, "slimmedPho_matchedGenPh_phi");
            tree->Branch(name, &v_slimmedPho_matchedGenPh_phi);
            
            //
            sprintf(name, "slimmedPho_chargedHadronIso");
            tree->Branch(name, &v_slimmedPho_chargedHadronIso);
            
            sprintf(name, "slimmedPho_neutralHadronIso");
            tree->Branch(name, &v_slimmedPho_neutralHadronIso);
            
            sprintf(name, "slimmedPho_photonIso");
            tree->Branch(name, &v_slimmedPho_photonIso);
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
            sprintf(name, "slimmedEle_sig_pfCand1_PV_dt_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand1_PV_dt);
            
            sprintf(name, "slimmedEle_sig_pfCand2_PV_dt_%s", key.c_str());
            tree->Branch(name, &sigVarContent->v_slimmedEle_sig_pfCand2_PV_dt);
            
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
        
        
        void init_IsoVarContent(std::string objName, std::string suffix)
        {
            if(!objName.length())
            {
                printf("Error in TreeOutput::init_IsoVarContent(...): Argument \"objName\" cannot be empty. \n");
                printf("Exiting... \n");
                
                exit(EXIT_FAILURE);
            }
            
            if(!suffix.length())
            {
                printf("Error in TreeOutput::init_IsoVarContent(...): Argument \"suffix\" cannot be empty. \n");
                printf("Exiting... \n");
                
                exit(EXIT_FAILURE);
            }
            
            std::string key = objName + "_" + suffix;
            
            IsoVarContent *isoVarContent = new IsoVarContent();
            
            
            sprintf(name, "%s_iso_pfCand_n_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_n);
            
            //
            sprintf(name, "%s_iso_sumETratio_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_sumETratio);
            
            sprintf(name, "%s_iso_sumETratio_charged_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_sumETratio_charged);
            
            sprintf(name, "%s_iso_sumETratio_neutral_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_sumETratio_neutral);
            
            sprintf(name, "%s_iso_sumETratio_ecal_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_sumETratio_ecal);
            
            sprintf(name, "%s_iso_sumETratio_hcal_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_sumETratio_hcal);
            
            //
            sprintf(name, "%s_iso_pfCand1_sig_dt_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_sig_dt);
            
            sprintf(name, "%s_iso_pfCand2_sig_dt_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_sig_dt);
            
            sprintf(name, "%s_iso_pfCand_sig_dtMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dtMean);
            
            sprintf(name, "%s_iso_pfCand_sig_dtMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dtMean_ETwtd);
            
            sprintf(name, "%s_iso_pfCand1_sig_dtSigni_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_sig_dtSigni);
            
            sprintf(name, "%s_iso_pfCand2_sig_dtSigni_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_sig_dtSigni);
            
            sprintf(name, "%s_iso_pfCand_sig_dtSigniMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dtSigniMean);
            
            sprintf(name, "%s_iso_pfCand_sig_dtSigniMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dtSigniMean_ETwtd);
            
            //
            sprintf(name, "%s_iso_pfCand1_PV_dt_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_PV_dt);
            
            sprintf(name, "%s_iso_pfCand2_PV_dt_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_PV_dt);
            
            sprintf(name, "%s_iso_pfCand_PV_dtMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dtMean);
            
            sprintf(name, "%s_iso_pfCand_PV_dtMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dtMean_ETwtd);
            
            sprintf(name, "%s_iso_pfCand1_PV_dtSigni_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_PV_dtSigni);
            
            sprintf(name, "%s_iso_pfCand2_PV_dtSigni_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_PV_dtSigni);
            
            sprintf(name, "%s_iso_pfCand_PV_dtSigniMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dtSigniMean);
            
            sprintf(name, "%s_iso_pfCand_PV_dtSigniMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dtSigniMean_ETwtd);
            
            //
            sprintf(name, "%s_iso_pfCand1_sig_dz_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_sig_dz);
            
            sprintf(name, "%s_iso_pfCand2_sig_dz_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_sig_dz);
            
            sprintf(name, "%s_iso_pfCand_sig_dzMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dzMean);
            
            sprintf(name, "%s_iso_pfCand_sig_dzMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_sig_dzMean_ETwtd);
            
            //
            sprintf(name, "%s_iso_pfCand1_PV_dz_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand1_PV_dz);
            
            sprintf(name, "%s_iso_pfCand2_PV_dz_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand2_PV_dz);
            
            sprintf(name, "%s_iso_pfCand_PV_dzMean_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dzMean);
            
            sprintf(name, "%s_iso_pfCand_PV_dzMean_ETwtd_%s", objName.c_str(), suffix.c_str());
            tree->Branch(name, &isoVarContent->v_iso_pfCand_PV_dzMean_ETwtd);
            
            
            // Add to the map
            m_IsoVarContent[key] = isoVarContent;
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
            
            
            // PU density //
            pileupDensity = 0;
            
            
            // PV //
            PV_t = 0;
            PV_tErr = 0;
            
            
            //
            PV4D_n = 0;
            v_PV4D_x.clear();
            v_PV4D_y.clear();
            v_PV4D_z.clear();
            
            PU_n = 0;
            v_PU_x.clear();
            v_PU_y.clear();
            v_PU_z.clear();
            
            
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
            
            v_slimmedEle_chargedHadronIso.clear();
            
            
            //
            vv_slimmedEle_sig_pfCand_eleIdx.clear();
            
            vv_slimmedEle_sig_pfCand_charge.clear();
            vv_slimmedEle_sig_pfCand_pT.clear();
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
            vv_slimmedEle_isoDR0p3_pfCand_pT.clear();
            vv_slimmedEle_isoDR0p3_pfCand_ET.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_t.clear();
            vv_slimmedEle_isoDR0p3_pfCand_tErr.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_PV_dt.clear();
            vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_PV_dz.clear();
            vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_sig_dt.clear();
            vv_slimmedEle_isoDR0p3_pfCand_sig_dtSigni.clear();
            
            vv_slimmedEle_isoDR0p3_pfCand_sig_dz.clear();
            
            
            for(auto iter = m_Ele_sigVarContent.begin(); iter != m_Ele_sigVarContent.end(); iter++)
            {
                iter->second->clear();
            }
            
            for(auto iter = m_IsoVarContent.begin(); iter != m_IsoVarContent.end(); iter++)
            {
                iter->second->clear();
            }
            
            
            // Slimmed photon //
            slimmedPho_n = 0;
            
            v_slimmedPho_idx.clear();
            
            v_slimmedPho_E.clear();
            v_slimmedPho_px.clear();
            v_slimmedPho_py.clear();
            v_slimmedPho_pz.clear();
            v_slimmedPho_pT.clear();
            v_slimmedPho_eta.clear();
            v_slimmedPho_phi.clear();
            v_slimmedPho_ET.clear();
            
            v_slimmedPho_linkedGenPart_pdgId.clear();
            
            v_slimmedPho_genPh_minDeltaR.clear();
            v_slimmedPho_nearestGenPh_idx.clear();
            v_slimmedPho_matchedGenPh_E.clear();
            v_slimmedPho_matchedGenPh_pT.clear();
            v_slimmedPho_matchedGenPh_eta.clear();
            v_slimmedPho_matchedGenPh_phi.clear();
            
            v_slimmedPho_chargedHadronIso.clear();
            v_slimmedPho_neutralHadronIso.clear();
            v_slimmedPho_photonIso.clear();
        }
    };
}


# endif
