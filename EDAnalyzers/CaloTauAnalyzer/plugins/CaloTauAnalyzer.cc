// -*- C++ -*-
//
// Package:    EDAnalyzers/CaloTauAnalyzer
// Class:      CaloTauAnalyzer
//
/**\class CaloTauAnalyzer CaloTauAnalyzer.cc EDAnalyzers/CaloTauAnalyzer/plugins/CaloTauAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Mon, 16 Apr 2018 12:59:15 GMT
//
//


// system include files
# include <map>
# include <memory>
# include <string>
# include <vector>

// user include files
# include "CommonTools/UtilAlgos/interface/TFileService.h"
# include "DataFormats/HepMCCandidate/interface/GenParticle.h"
# include "DataFormats/JetReco/interface/PFJet.h"
# include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
# include "DataFormats/TauReco/interface/CaloTau.h"
# include "DataFormats/TauReco/interface/CaloTauDiscriminator.h"
# include "DataFormats/TauReco/interface/CaloTauTagInfo.h"
# include "DataFormats/TrackReco/interface/Track.h"
# include "DataFormats/TrackReco/interface/TrackFwd.h"
# include "DataFormats/VertexReco/interface/Vertex.h"
# include "FWCore/Framework/interface/Event.h"
# include "FWCore/Framework/interface/Frameworkfwd.h"
# include "FWCore/Framework/interface/MakerMacros.h"
# include "FWCore/Framework/interface/one/EDAnalyzer.h"
# include "FWCore/ParameterSet/interface/ParameterSet.h"
# include "FWCore/ServiceRegistry/interface/Service.h"
# include "FWCore/Utilities/interface/InputTag.h"
# include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

# include <CLHEP/Vector/LorentzVector.h>
# include <CLHEP/Vector/ThreeVector.h>

# include <TH1F.h>
# include <TH2F.h>
# include <TTree.h>

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.


//using reco::TrackCollection;


std::vector <double> v_tau_pTbin = {
    0, 10, 20, 30, 40, 50, 60, 70, 80,
    100,
    150, 200, 250, 300, 350, 400,
    500, 600, 700, 800,
    1000,
    1500, 2000
};


class TauMatchingOutput
{
    public :
    
    
    int nGenMatched;
    int nGenNotMatched;
    
    
    // Gen matched
    TH1F *h1_caloTau_genMatched_pT_reco;
    TH1F *h1_caloTau_genMatched_eta_reco;
    TH1F *h1_caloTau_genMatched_phi_reco;
    TH1F *h1_caloTau_genMatched_m_reco;
    TH1F *h1_caloTau_genMatched_decayMode_reco;
    
    TH1F *h1_caloTau_genMatched_pTresolution_reco;
    
    TH1F *h1_caloTau_genMatched_sigTrack_n_reco;
    TH1F *h1_caloTau_genMatched_isoTrack_n_reco;
    
    TH1F *h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_reco;
    TH1F *h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genMatched_maximumHCALhitEt_reco;
    TH1F *h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genMatched_maximumHCALhitEt_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genMatched_isolationECALhitsEtSum_reco;
    TH1F *h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genMatched_isolationECALhitsEtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genMatched_isolationTracksPtSum_reco;
    TH1F *h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genMatched_isolationTracksPtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genMatched_signalTracksInvariantMass_reco;
    TH1F *h1_caloTau_genMatched_TracksInvariantMass_reco;
    
    TH1F *h1_caloTau_genMatched_sigTrack1_deltaR_reco;
    TH1F *h1_caloTau_genMatched_isoTrack1_deltaR_reco;
    
    TH2F *h2_caloTau_genMatched_pT_vs_nPV_reco;
    TH2F *h2_caloTau_genMatched_decayMode_vs_m_reco;
    
    
    // Gen not matched
    TH1F *h1_caloTau_genNotMatched_pT_reco;
    TH1F *h1_caloTau_genNotMatched_eta_reco;
    TH1F *h1_caloTau_genNotMatched_phi_reco;
    TH1F *h1_caloTau_genNotMatched_m_reco;
    TH1F *h1_caloTau_genNotMatched_decayMode_reco;
    
    TH1F *h1_caloTau_genNotMatched_sigTrack_n_reco;
    TH1F *h1_caloTau_genNotMatched_isoTrack_n_reco;
    
    TH1F *h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_reco;
    TH1F *h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genNotMatched_maximumHCALhitEt_reco;
    TH1F *h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genNotMatched_maximumHCALhitEt_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genNotMatched_isolationECALhitsEtSum_reco;
    TH1F *h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genNotMatched_isolationTracksPtSum_reco;
    TH1F *h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrack1pT_reco;
    TH1F *h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrackHT_reco;
    TH1F *h1_caloTau_genNotMatched_isolationTracksPtSum_by_caloTauPt_reco;
    
    TH1F *h1_caloTau_genNotMatched_signalTracksInvariantMass_reco;
    TH1F *h1_caloTau_genNotMatched_TracksInvariantMass_reco;
    
    TH1F *h1_caloTau_genNotMatched_sigTrack1_deltaR_reco;
    TH1F *h1_caloTau_genNotMatched_isoTrack1_deltaR_reco;
    
    TH2F *h2_caloTau_genNotMatched_pT_vs_nPV_reco;
    TH2F *h2_caloTau_genNotMatched_decayMode_vs_m_reco;
    
    
    // Gen not matched, ak4PFjet matched
    TH1F *h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco;
    TH1F *h1_caloTau_genNotMatched_ak4PFjetMatched_eta_reco;
    TH1F *h1_caloTau_genNotMatched_ak4PFjetMatched_phi_reco;
    
    TH2F *h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco;
    
    //
    //TH2F *h2_caloTau_ROC_reco;
    
    char histName[500];
    char histTitle[500];
    
    
    TauMatchingOutput(std::string variableName, edm::Service<TFileService> fs)
    {
        nGenMatched = 0;
        nGenNotMatched = 0;
        
        
        // Gen matched
        sprintf(histName, "caloTau_genMatched_%s_pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_pT_reco", variableName.c_str());
        h1_caloTau_genMatched_pT_reco = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
        
        sprintf(histName, "caloTau_genMatched_%s_eta_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_eta_reco", variableName.c_str());
        h1_caloTau_genMatched_eta_reco = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
        
        sprintf(histName, "caloTau_genMatched_%s_phi_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_phi_reco", variableName.c_str());
        h1_caloTau_genMatched_phi_reco = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
        
        sprintf(histName, "caloTau_genMatched_%s_m_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_m_reco", variableName.c_str());
        h1_caloTau_genMatched_m_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        sprintf(histName, "caloTau_genMatched_%s_decayMode_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_decayMode_reco", variableName.c_str());
        h1_caloTau_genMatched_decayMode_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
        
        sprintf(histName, "caloTau_genMatched_%s_pTresolution_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_pTresolution_reco", variableName.c_str());
        h1_caloTau_genMatched_pTresolution_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        
        //
        sprintf(histName, "caloTau_genMatched_%s_sigTrack_n_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_sigTrack_n_reco", variableName.c_str());
        h1_caloTau_genMatched_sigTrack_n_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
        
        sprintf(histName, "caloTau_genMatched_%s_isoTrack_n_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isoTrack_n_reco", variableName.c_str());
        h1_caloTau_genMatched_isoTrack_n_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
    
        //
        sprintf(histName, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_reco", variableName.c_str());
        h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genMatched_%s_maximumHCALhitEt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_maximumHCALhitEt_reco", variableName.c_str());
        h1_caloTau_genMatched_maximumHCALhitEt_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genMatched_%s_maximumHCALhitEt_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_maximumHCALhitEt_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_maximumHCALhitEt_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_maximumHCALhitEt_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_maximumHCALhitEt_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_maximumHCALhitEt_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genMatched_maximumHCALhitEt_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genMatched_%s_isolationECALhitsEtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationECALhitsEtSum_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationECALhitsEtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationECALhitsEtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationECALhitsEtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genMatched_%s_isolationTracksPtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationTracksPtSum_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationTracksPtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationTracksPtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationTracksPtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationTracksPtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationTracksPtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_isolationTracksPtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isolationTracksPtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genMatched_isolationTracksPtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        
        //
        sprintf(histName, "caloTau_genMatched_%s_signalTracksInvariantMass_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_signalTracksInvariantMass_reco", variableName.c_str());
        h1_caloTau_genMatched_signalTracksInvariantMass_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        sprintf(histName, "caloTau_genMatched_%s_TracksInvariantMass_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_TracksInvariantMass_reco", variableName.c_str());
        h1_caloTau_genMatched_TracksInvariantMass_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        
        //
        sprintf(histName, "caloTau_genMatched_%s_sigTrack1_deltaR_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_sigTrack1_deltaR_reco", variableName.c_str());
        h1_caloTau_genMatched_sigTrack1_deltaR_reco = fs->make<TH1F>(histName, histTitle, 500, 0, 10);
        
        sprintf(histName, "caloTau_genMatched_%s_isoTrack1_deltaR_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_isoTrack1_deltaR_reco", variableName.c_str());
        h1_caloTau_genMatched_isoTrack1_deltaR_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        
        //
        sprintf(histName, "caloTau_genMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        h2_caloTau_genMatched_pT_vs_nPV_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 200, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
        
        sprintf(histName, "caloTau_genMatched_%s_decayMode_vs_m_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genMatched_%s_decayMode_vs_m_reco", variableName.c_str());
        h2_caloTau_genMatched_decayMode_vs_m_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 20, 20, 0, 20);
        
        
        // Gen not matched
        sprintf(histName, "caloTau_genNotMatched_%s_pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_pT_reco = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
        
        sprintf(histName, "caloTau_genNotMatched_%s_eta_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_eta_reco", variableName.c_str());
        h1_caloTau_genNotMatched_eta_reco = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
        
        sprintf(histName, "caloTau_genNotMatched_%s_phi_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_phi_reco", variableName.c_str());
        h1_caloTau_genNotMatched_phi_reco = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
        
        sprintf(histName, "caloTau_genNotMatched_%s_m_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_m_reco", variableName.c_str());
        h1_caloTau_genNotMatched_m_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        sprintf(histName, "caloTau_genNotMatched_%s_decayMode_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_decayMode_reco", variableName.c_str());
        h1_caloTau_genNotMatched_decayMode_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_sigTrack_n_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_sigTrack_n_reco", variableName.c_str());
        h1_caloTau_genNotMatched_sigTrack_n_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isoTrack_n_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isoTrack_n_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isoTrack_n_reco = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_reco", variableName.c_str());
        h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_maximumHCALhitEt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_maximumHCALhitEt_reco", variableName.c_str());
        h1_caloTau_genNotMatched_maximumHCALhitEt_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_maximumHCALhitEt_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genNotMatched_maximumHCALhitEt_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationECALhitsEtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationECALhitsEtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_isolationTracksPtSum_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationTracksPtSum_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationTracksPtSum_reco = fs->make<TH1F>(histName, histTitle, 2000, 0, 2000);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_sigTrack1pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_sigTrack1pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrack1pT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_sigTrackHT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_sigTrackHT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrackHT_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_caloTauPt_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isolationTracksPtSum_by_caloTauPt_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isolationTracksPtSum_by_caloTauPt_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_signalTracksInvariantMass_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_signalTracksInvariantMass_reco", variableName.c_str());
        h1_caloTau_genNotMatched_signalTracksInvariantMass_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        sprintf(histName, "caloTau_genNotMatched_%s_TracksInvariantMass_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_TracksInvariantMass_reco", variableName.c_str());
        h1_caloTau_genNotMatched_TracksInvariantMass_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_sigTrack1_deltaR_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_sigTrack1_deltaR_reco", variableName.c_str());
        h1_caloTau_genNotMatched_sigTrack1_deltaR_reco = fs->make<TH1F>(histName, histTitle, 500, 0, 10);
        
        sprintf(histName, "caloTau_genNotMatched_%s_isoTrack1_deltaR_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_isoTrack1_deltaR_reco", variableName.c_str());
        h1_caloTau_genNotMatched_isoTrack1_deltaR_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        h2_caloTau_genNotMatched_pT_vs_nPV_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 200, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
        
        sprintf(histName, "caloTau_genNotMatched_%s_decayMode_vs_m_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_%s_decayMode_vs_m_reco", variableName.c_str());
        h2_caloTau_genNotMatched_decayMode_vs_m_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 20, 20, 0, 20);
        
        //
        //sprintf(histName, "caloTau_%s_ROC_reco", variableName.c_str());
        //sprintf(histTitle, "caloTau_%s_ROC_reco", variableName.c_str());
        //h2_caloTau_genMatched_ROC_reco = fs->make<TH2F>(histName, histTitle, 40, 0, 2, 40, 0, 2);
        
        
        // Gen not matched, ak4PFjet matched
        sprintf(histName, "caloTau_genNotMatched_ak4PFjetMatched_%s_pT_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_ak4PFjetMatched_%s_pT_reco", variableName.c_str());
        h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
        
        sprintf(histName, "caloTau_genNotMatched_ak4PFjetMatched_%s_eta_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_ak4PFjetMatched_%s_eta_reco", variableName.c_str());
        h1_caloTau_genNotMatched_ak4PFjetMatched_eta_reco = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
        
        sprintf(histName, "caloTau_genNotMatched_ak4PFjetMatched_%s_phi_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_ak4PFjetMatched_%s_phi_reco", variableName.c_str());
        h1_caloTau_genNotMatched_ak4PFjetMatched_phi_reco = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
        
        
        //
        sprintf(histName, "caloTau_genNotMatched_ak4PFjetMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        sprintf(histTitle, "caloTau_genNotMatched_ak4PFjetMatched_%s_pT_vs_nPV_reco", variableName.c_str());
        h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 200, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    }
};


class CaloTauAnalyzer : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
    public:
    
    explicit CaloTauAnalyzer(const edm::ParameterSet&);
    ~CaloTauAnalyzer();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
    
    private:
    
    bool isLeptonicTau(const reco::GenParticle *tau);
    int getTauDecayMode(const reco::GenParticle *tau);
    CLHEP::HepLorentzVector getTau4momVisible(const reco::GenParticle *tau);
    int getNPU(edm::Handle <std::vector <PileupSummaryInfo> > v_pileUp);
    
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    
    // ----------member data ---------------------------
    //edm::EDGetTokenT<TrackCollection> tracksToken_;  //used to select what tracks to read from configuration file
    
    
    ////////////////////////////// GEN //////////////////////////////
    edm::EDGetTokenT <std::vector <reco::GenParticle> > tok_genParticle;
    
    
    TH1F *h1_tauh_pT_gen;
    TH1F *h1_tauh_eta_gen;
    TH1F *h1_tauh_phi_gen;
    TH1F *h1_tauh_m_gen;
    TH1F *h1_tauh_decayMode_gen;
    
    TH2F *h2_tauh_decayMode_vs_m_gen;
    
    
    ////////////////////////////// RECO //////////////////////////////
    edm::EDGetTokenT <std::vector <reco::Vertex> > tok_primaryVertex;
    edm::EDGetTokenT <std::vector <PileupSummaryInfo> > tok_pileUp;
    
    edm::EDGetTokenT <std::vector<reco::CaloTau> > tok_caloTau;
    edm::EDGetTokenT <std::vector<reco::CaloTauTagInfo> > tok_caloTauTagInfo;
    
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationAgainstElectron;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationAgainstMuon;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationByECALIsolation;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationByIsolation;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationByLeadingTrackFinding;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationByLeadingTrackPtCut;
    edm::EDGetTokenT <reco::CaloTauDiscriminator> tok_caloRecoTauDiscriminationByTrackIsolation;
    
    edm::EDGetTokenT <std::vector <reco::PFJet> > tok_ak4PFJet;
    
    
    //
    TH1F *h1_PV_n_reco;
    TH1F *h1_PU_n_reco;
    
    TH1F *h1_caloTau_pT_reco;
    TH1F *h1_caloTau_eta_reco;
    TH1F *h1_caloTau_phi_reco;
    TH1F *h1_caloTau_m_reco;
    TH1F *h1_caloTau_decayMode_reco;
    
    TH1F *h1_caloTau_nearestGenTauh_deltaR_reco;
    
    //
    TH1F *h1_ak4PFjet_pT_reco;
    TH1F *h1_ak4PFjet_eta_reco;
    TH1F *h1_ak4PFjet_phi_reco;
    
    TH1F *h1_caloTau_nearestAK4PFjet_deltaR_reco;
    
    //
    TH2F *h2_caloTau_decayMode_vs_m_reco;
    TH2F *h2_genTauh_pT_vs_nPV;
    
    //
    TH2F *h2_ak4PFjet_pT_vs_nPV;
    
    
    std::vector <std::string> v_caloTauDiscriminator_name;
    
    std::map <std::string, TauMatchingOutput*> m_TauMatchingOutput;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
CaloTauAnalyzer::CaloTauAnalyzer(const edm::ParameterSet& iConfig)
    //:
    //tracksToken_(consumes<TrackCollection>(iConfig.getUntrackedParameter<edm::InputTag>("tracks")))

{
    usesResource("TFileService");
    edm::Service<TFileService> fs;
    
    
    char histName[500];
    char histTitle[500];
    
    //TFile *f = TFile::Open("root://se01.indiacms.res.in//store/user/chatterj/RSGluonToTT_M-3000_TuneCUETP8M1_14TeV-pythia8/crab_crab_M3000_TTPU200_z05_b0_RSD3_PUPPI_nocor/180502_165332/0000/rootuple_RSD_Alphas_9.root", "READ");
    //f->ls();
    
    //now do what ever initialization is needed
    
    ////////////////////////////// GEN //////////////////////////////
    tok_genParticle = consumes <std::vector <reco::GenParticle> >(iConfig.getUntrackedParameter <edm::InputTag>("label_genParticle"));;
    
    
    sprintf(histName, "tauh_pT_gen");
    sprintf(histTitle, "tauh_pT_gen");
    h1_tauh_pT_gen = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    
    sprintf(histName, "tauh_eta_gen");
    sprintf(histTitle, "tauh_eta_gen");
    h1_tauh_eta_gen = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
    
    sprintf(histName, "tauh_phi_gen");
    sprintf(histTitle, "tauh_phi_gen");
    h1_tauh_phi_gen = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
    
    sprintf(histName, "tauh_m_gen");
    sprintf(histTitle, "tauh_m_gen");
    h1_tauh_m_gen = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
    
    sprintf(histName, "tauh_decayMode_gen");
    sprintf(histTitle, "tauh_decayMode_gen");
    h1_tauh_decayMode_gen = fs->make<TH1F>(histName, histTitle, 20, 0, 20);
    
    
    //
    sprintf(histName, "tauh_decayMode_vs_m_gen");
    sprintf(histTitle, "tauh_decayMode_vs_m_gen");
    h2_tauh_decayMode_vs_m_gen = fs->make<TH2F>(histName, histTitle, 200, 0, 20, 20, 0, 20);
    
    
    
    
    ////////////////////////////// RECO //////////////////////////////
    tok_primaryVertex = consumes <std::vector<reco::Vertex> >(iConfig.getUntrackedParameter <edm::InputTag>("label_primaryVertex"));
    tok_pileUp = consumes <std::vector<PileupSummaryInfo> >(iConfig.getUntrackedParameter <edm::InputTag>("label_pileUp"));
    
    tok_caloTau = consumes <std::vector<reco::CaloTau> >(iConfig.getUntrackedParameter <edm::InputTag>("label_caloTau"));
    tok_caloTauTagInfo = consumes <std::vector<reco::CaloTauTagInfo> >(iConfig.getUntrackedParameter <edm::InputTag>("label_caloTauTagInfo"));
    
    tok_caloRecoTauDiscriminationAgainstElectron = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationAgainstElectron"));
    tok_caloRecoTauDiscriminationAgainstMuon = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationAgainstMuon"));
    tok_caloRecoTauDiscriminationByECALIsolation = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationByECALIsolation"));
    tok_caloRecoTauDiscriminationByIsolation = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationByIsolation"));
    tok_caloRecoTauDiscriminationByLeadingTrackFinding = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationByLeadingTrackFinding"));
    tok_caloRecoTauDiscriminationByLeadingTrackPtCut = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationByLeadingTrackPtCut"));
    tok_caloRecoTauDiscriminationByTrackIsolation = consumes <reco::CaloTauDiscriminator>(iConfig.getUntrackedParameter <edm::InputTag>("label_caloRecoTauDiscriminationByTrackIsolation"));
    
    tok_ak4PFJet = consumes <std::vector <reco::PFJet> >(iConfig.getUntrackedParameter <edm::InputTag>("label_ak4PFJet"));
    
    
    
    //
    sprintf(histName, "PV_n_reco");
    sprintf(histTitle, "PV_n_reco");
    h1_PV_n_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 200);
    
    sprintf(histName, "PU_n_reco");
    sprintf(histTitle, "PU_n_reco");
    h1_PU_n_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 200);
    
    sprintf(histName, "caloTau_pT_reco");
    sprintf(histTitle, "caloTau_pT_reco");
    h1_caloTau_pT_reco = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    
    sprintf(histName, "caloTau_eta_reco");
    sprintf(histTitle, "caloTau_eta_reco");
    h1_caloTau_eta_reco = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
    
    sprintf(histName, "caloTau_phi_reco");
    sprintf(histTitle, "caloTau_phi_reco");
    h1_caloTau_phi_reco = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
    
    sprintf(histName, "caloTau_m_reco");
    sprintf(histTitle, "caloTau_m_reco");
    h1_caloTau_m_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
    
    sprintf(histName, "caloTau_decayMode_reco");
    sprintf(histTitle, "caloTau_decayMode_reco");
    h1_caloTau_decayMode_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 20);
    
    sprintf(histName, "caloTau_nearestGenTauh_deltaR_reco");
    sprintf(histTitle, "caloTau_nearestGenTauh_deltaR_reco");
    h1_caloTau_nearestGenTauh_deltaR_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
    
    //
    sprintf(histName, "ak4PFjet_pT_reco");
    sprintf(histTitle, "ak4PFjet_pT_reco");
    h1_ak4PFjet_pT_reco = fs->make<TH1F>(histName, histTitle, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    
    sprintf(histName, "ak4PFjet_eta_reco");
    sprintf(histTitle, "ak4PFjet_eta_reco");
    h1_ak4PFjet_eta_reco = fs->make<TH1F>(histName, histTitle, 60, -3, 3);
    
    sprintf(histName, "ak4PFjet_phi_reco");
    sprintf(histTitle, "ak4PFjet_phi_reco");
    h1_ak4PFjet_phi_reco = fs->make<TH1F>(histName, histTitle, 60, -M_PI, M_PI);
    
    sprintf(histName, "caloTau_nearestAK4PFjet_deltaR_reco");
    sprintf(histTitle, "caloTau_nearestAK4PFjet_deltaR_reco");
    h1_caloTau_nearestAK4PFjet_deltaR_reco = fs->make<TH1F>(histName, histTitle, 200, 0, 10);
    
    
    //
    sprintf(histName, "caloTau_decayMode_vs_m_reco");
    sprintf(histTitle, "caloTau_decayMode_vs_m_reco");
    h2_caloTau_decayMode_vs_m_reco = fs->make<TH2F>(histName, histTitle, 200, 0, 20, 20, 0, 20);
    
    sprintf(histName, "genTauh_pT_vs_nPV");
    sprintf(histTitle, "genTauh_pT_vs_nPV");
    h2_genTauh_pT_vs_nPV = fs->make<TH2F>(histName, histTitle, 200, 0, 200, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    
    //
    sprintf(histName, "ak4PFjet_pT_vs_nPV");
    sprintf(histTitle, "ak4PFjet_pT_vs_nPV");
    h2_ak4PFjet_pT_vs_nPV = fs->make<TH2F>(histName, histTitle, 200, 0, 200, v_tau_pTbin.size()-1, &v_tau_pTbin.at(0));
    
    
    v_caloTauDiscriminator_name = {
        "none",
        "againstElectron",
        "againstMuon",
        "byECALIsolation",
        "byIsolation",
        "byTrackIsolation",
        "byLeadingTrackPtCut"
    };
    
    for(int iDisc = 0; iDisc < (int) v_caloTauDiscriminator_name.size(); iDisc++)
    {
        m_TauMatchingOutput[v_caloTauDiscriminator_name.at(iDisc)] = new TauMatchingOutput(v_caloTauDiscriminator_name.at(iDisc), fs);
    }
}


CaloTauAnalyzer::~CaloTauAnalyzer()
{

    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    
    for(int iDisc = 0; iDisc < (int) v_caloTauDiscriminator_name.size(); iDisc++)
    {
        delete m_TauMatchingOutput[v_caloTauDiscriminator_name.at(iDisc)];
    }
}


//
// member functions
//


bool CaloTauAnalyzer::isLeptonicTau(const reco::GenParticle *tau)
{
    for(unsigned int iDaughter = 0; iDaughter < tau->numberOfDaughters(); iDaughter++)
    {
        const reco::GenParticle *daughter = tau->daughterRef(iDaughter).get();
        
        int daughterId = daughter->pdgId();
        
        // If the daugher is a tau, then recurse
        if(fabs(daughterId) == 15)
        {
            return isLeptonicTau(daughter);
        }
        
        // If any of the daughters is a lepton (except tau and tau neutrino), tau is leptonic
        if(fabs(daughterId) == 11 || fabs(daughterId) == 12 || fabs(daughterId) == 13 || fabs(daughterId) == 14)
        {
            return true;
        }
    }
    
    return false;
}


// Returns:
// -1: electron decay mode
// -2: muon decay mode
// 5*(nChHad-1) + nPi0: hadronic mode
int CaloTauAnalyzer::getTauDecayMode(const reco::GenParticle *tau)
{
    int nChHad = 0; // Charged hadrons
    int nPi0 = 0; // Neutral pions
    
    //CLHEP::HepLorentzVector tauh_4mom(0, 0, 0, 0);
    
    for(unsigned int iDaughter = 0; iDaughter < tau->numberOfDaughters(); iDaughter++)
    {
        const reco::GenParticle *daughter = tau->daughterRef(iDaughter).get();
        
        int daughterId = daughter->pdgId();
        
        // If the daughter is a tau, then recurse
        if(fabs(daughterId) == 15)
        {
            return getTauDecayMode(daughter);
        }
        
        // Leptonic decay: electron
        if(fabs(daughterId) == 11)
        {
            return -1;
        }
        
        // Leptonic decay: muon
        else if(fabs(daughterId) == 13)
        {
            return -2;
        }
        
        // Skip the neutrinos
        if(fabs(daughterId) == 12 || fabs(daughterId) == 14 || fabs(daughterId) == 16)
        {
            continue;
        }
        
        if(fabs(daughter->charge()) > 0)
        {
            nChHad++;
        }
        
        else
        {
            nPi0++;
        }
        
        //tauh_4mom.setT(tauh_4mom.getT() + daughter->energy());
        //tauh_4mom.setX(tauh_4mom.getX() + daughter->px());
        //tauh_4mom.setY(tauh_4mom.getY() + daughter->py());
        //tauh_4mom.setZ(tauh_4mom.getZ() + daughter->pz());
    }
    
    //printf("Inside CaloTauAnalyzer::getTauDecayMode(...): m %0.2f \n", tauh_4mom.m());
    
    int decayMode = 5*(nChHad-1) + nPi0;
    
    return decayMode;
}


CLHEP::HepLorentzVector CaloTauAnalyzer::getTau4momVisible(const reco::GenParticle *tau)
{
    CLHEP::HepLorentzVector tauh_4mom;
    
    tauh_4mom.setT(tau->energy());
    tauh_4mom.setX(tau->px());
    tauh_4mom.setY(tau->py());
    tauh_4mom.setZ(tau->pz());
    
    for(unsigned int iDaughter = 0; iDaughter < tau->numberOfDaughters(); iDaughter++)
    {
        const reco::GenParticle *daughter = tau->daughterRef(iDaughter).get();
        
        int daughterId = daughter->pdgId();
        
        // If the daughter is a tau, then recurse
        if(fabs(daughterId) == 15)
        {
            return getTau4momVisible(daughter);
        }
        
        // Subtract neutrino momentum
        if(fabs(daughterId) == 12 || fabs(daughterId) == 14 || fabs(daughterId) == 16)
        {
            tauh_4mom.setT(tauh_4mom.e() - daughter->energy());
            tauh_4mom.setX(tauh_4mom.px() - daughter->px());
            tauh_4mom.setY(tauh_4mom.py() - daughter->py());
            tauh_4mom.setZ(tauh_4mom.pz() - daughter->pz());
        }
    }
    
    return tauh_4mom;
}


int CaloTauAnalyzer::getNPU(edm::Handle <std::vector <PileupSummaryInfo> > v_pileUp)
{
    int nPU = -1;
    
    // Start from the end to reach the In-time bunch-crossing quicker
    for(int iPileUp = (int) v_pileUp->size() - 1; iPileUp >= 0; iPileUp--)
    {
        PileupSummaryInfo pileUpInfo = v_pileUp->at(iPileUp);
        
        int BX = pileUpInfo.getBunchCrossing();
        
        nPU = pileUpInfo.getPU_NumInteractions();
        //printf("BX %d: PU_NumInteractions %d, TrueNumInteractions %f \n", BX, nPU, pileUpInfo.getTrueNumInteractions());
        
        // In-time bunch-crossing pile-up
        if(BX == 0)
        {
            break;
        }
    }
    
    return nPU;
}


// ------------ method called for each event  ------------
void CaloTauAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    
    //Handle<TrackCollection> tracks;
    //iEvent.getByToken(tracksToken_, tracks);
    //for(TrackCollection::const_iterator itTrack = tracks->begin();
    //    itTrack != tracks->end();
    //    ++itTrack) {
    //  // do something with track parameters, e.g, plot the charge.
    //  // int charge = itTrack->charge();
    //}

    //#ifdef THIS_IS_AN_EVENT_EXAMPLE
    //Handle<ExampleData> pIn;
    //iEvent.getByLabel("example",pIn);
    //#endif
    //
    //#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
    //ESHandle<SetupData> pSetup;
    //iSetup.get<SetupRecord>().get(pSetup);
    //#endif
    
    printf("Event %llu \n", iEvent.id().event());
    
    
    ////////////////////////////// GEN //////////////////////////////
    
    edm::Handle <std::vector <reco::GenParticle> > v_genParticle;
    iEvent.getByToken(tok_genParticle, v_genParticle);
    
    
    ////////////////////////////// RECO //////////////////////////////
    
    edm::Handle <std::vector <reco::Vertex> > v_primaryVertex;
    iEvent.getByToken(tok_primaryVertex, v_primaryVertex);
    
    edm::Handle <std::vector <PileupSummaryInfo> > v_pileUp;
    iEvent.getByToken(tok_pileUp, v_pileUp);
    
    edm::Handle <std::vector <reco::CaloTau> > v_caloTau;
    iEvent.getByToken(tok_caloTau, v_caloTau);
    
    edm::Handle <std::vector <reco::CaloTauTagInfo> > v_caloTauTagInfo;
    iEvent.getByToken(tok_caloTauTagInfo, v_caloTauTagInfo);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationAgainstElectron;
    iEvent.getByToken(tok_caloRecoTauDiscriminationAgainstElectron, v_caloRecoTauDiscriminationAgainstElectron);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationAgainstMuon;
    iEvent.getByToken(tok_caloRecoTauDiscriminationAgainstMuon, v_caloRecoTauDiscriminationAgainstMuon);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationByECALIsolation;
    iEvent.getByToken(tok_caloRecoTauDiscriminationByECALIsolation, v_caloRecoTauDiscriminationByECALIsolation);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationByIsolation;
    iEvent.getByToken(tok_caloRecoTauDiscriminationByIsolation, v_caloRecoTauDiscriminationByIsolation);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationByLeadingTrackFinding;
    iEvent.getByToken(tok_caloRecoTauDiscriminationByLeadingTrackFinding, v_caloRecoTauDiscriminationByLeadingTrackFinding);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationByLeadingTrackPtCut;
    iEvent.getByToken(tok_caloRecoTauDiscriminationByLeadingTrackPtCut, v_caloRecoTauDiscriminationByLeadingTrackPtCut);
    
    edm::Handle <reco::CaloTauDiscriminator> v_caloRecoTauDiscriminationByTrackIsolation;
    iEvent.getByToken(tok_caloRecoTauDiscriminationByTrackIsolation, v_caloRecoTauDiscriminationByTrackIsolation);
    
    edm::Handle <std::vector <reco::PFJet> > v_ak4PFJet;
    iEvent.getByToken(tok_ak4PFJet, v_ak4PFJet);
    
    
    // Gen tauh
    std::vector <CLHEP::HepLorentzVector> v_tauh_4mom_gen;
    
    std::vector <bool> v_tauh_isSelected_gen;
    std::vector <bool> v_tauh_isUsed_gen;
    
    int nPV = v_primaryVertex->size();
    int nPU = getNPU(v_pileUp);
    
    for(unsigned int iPart = 0; iPart < v_genParticle->size(); iPart++)
    {
        reco::GenParticle part = v_genParticle->at(iPart);
        
        int pdgId = part.pdgId();
        
        if(abs(pdgId) == 15 && part.isLastCopy())
        {
            bool isHadronic = !isLeptonicTau(&part);
            
            int decayMode = getTauDecayMode(&part);
            CLHEP::HepLorentzVector tauh_4mom_gen = getTau4momVisible(&part);
            
            printf(
                "pdgId %d, status %d \n"
                "lep: E %0.2f, pT %0.2f, eta %0.2f, phi %0.2f, pz %0.2f, charge %d \n"
                "had: E %0.2f, pT %0.2f, eta %0.2f, phi %0.2f, pz %0.2f, m %0.2f \n"
                "hardProcess %d, lastCopy %d \n"
                "hadronic %d, decayMode %d \n",
                
                pdgId, part.status(),
                part.energy(), part.pt(), part.eta(), part.phi(), part.pz(), part.charge(),
                tauh_4mom_gen.e(), tauh_4mom_gen.perp(), tauh_4mom_gen.eta(), tauh_4mom_gen.phi(), tauh_4mom_gen.pz(), tauh_4mom_gen.m(),
                part.isHardProcess(), part.isLastCopy(),
                isHadronic, decayMode
            );
            
            printf("\n");
            
            // Select the hadronic modes
            if(!isHadronic)
            {
                continue;
            }
            
            v_tauh_4mom_gen.push_back(tauh_4mom_gen);
            
            v_tauh_isSelected_gen.push_back(false);
            v_tauh_isUsed_gen.push_back(false);
            
            if(tauh_4mom_gen.perp() > 20 && fabs(tauh_4mom_gen.eta()) < 2.4)
            //if(tauh_4mom_gen.perp() > 20)
            {
                v_tauh_isSelected_gen.at(v_tauh_isSelected_gen.size()-1) = true;
                
                h1_tauh_pT_gen->Fill(tauh_4mom_gen.perp());
                h1_tauh_eta_gen->Fill(tauh_4mom_gen.eta());
                h1_tauh_phi_gen->Fill(tauh_4mom_gen.phi());
                h1_tauh_m_gen->Fill(tauh_4mom_gen.m());
                h1_tauh_decayMode_gen->Fill(decayMode);
                
                h2_tauh_decayMode_vs_m_gen->Fill(tauh_4mom_gen.m(), decayMode);
                h2_genTauh_pT_vs_nPV->Fill(nPV, tauh_4mom_gen.perp());
            }
        }
    }
    
    
    // Primary vertices
    h1_PV_n_reco->Fill(nPV);
    h1_PU_n_reco->Fill(nPU);
    
    
    // AK4 PF jets
    std::vector <CLHEP::HepLorentzVector> v_ak4PFjet_4mom;
    
    std::vector <bool> v_ak4PFjet_isSelected(v_ak4PFJet->size(), false);
    std::vector <bool> v_ak4PFjet_isUsed(v_ak4PFJet->size(), false);
    
    for(int iAK4PFjet = 0; iAK4PFjet < (int) v_ak4PFJet->size(); iAK4PFjet++)
    {
        reco::PFJet ak4PFJet = v_ak4PFJet->at(iAK4PFjet);
        
        CLHEP::HepLorentzVector ak4PFJet_4mom;
        ak4PFJet_4mom.setT(ak4PFJet.energy());
        ak4PFJet_4mom.setX(ak4PFJet.px());
        ak4PFJet_4mom.setY(ak4PFJet.py());
        ak4PFJet_4mom.setZ(ak4PFJet.pz());
        
        v_ak4PFjet_4mom.push_back(ak4PFJet_4mom);
        
        if(ak4PFJet_4mom.perp() < 20 || fabs(ak4PFJet_4mom.eta()) > 2.4)
        //if(ak4PFJet_4mom.perp() < 20)
        {
            continue;
        }
        
        v_ak4PFjet_isSelected.at(iAK4PFjet) = true;
        
        
        h1_ak4PFjet_pT_reco->Fill(ak4PFJet_4mom.perp());
        h1_ak4PFjet_eta_reco->Fill(ak4PFJet_4mom.eta());
        h1_ak4PFjet_phi_reco->Fill(ak4PFJet_4mom.phi());
        
        h2_ak4PFjet_pT_vs_nPV->Fill(nPV, ak4PFJet_4mom.perp());
    }
    
    
    // Calo tau
    printf("nCaloTau %d, nCaloTauTagInfo %d \n", (int) v_caloTau->size(), (int) v_caloTauTagInfo->size());
    //printf("nDiscAgainstElectron %d \n", (int) v_caloRecoTauDiscriminationAgainstElectron->size());
    
    for(unsigned int iCaloTau = 0; iCaloTau < v_caloTau->size(); iCaloTau++)
    {
        reco::CaloTau caloTau = v_caloTau->at(iCaloTau);
        
        CLHEP::HepLorentzVector caloTau_4mom;
        caloTau_4mom.setT(caloTau.energy());
        caloTau_4mom.setX(caloTau.px());
        caloTau_4mom.setY(caloTau.py());
        caloTau_4mom.setZ(caloTau.pz());
        
        if(caloTau_4mom.perp() < 20 || fabs(caloTau_4mom.eta()) > 2.4)
        //if(caloTau_4mom.perp() < 20)
        {
            continue;
        }
        
        
        // Signal tracks
        reco::TrackRefVector v_caloTau_signalTrack = caloTau.signalTracks();
        
        int nSigTrack = v_caloTau_signalTrack.size();
        std::vector <int> v_signalTrack_pTsortedIndex;
        std::vector <double> v_signalTrack_caloTau_deltaR;
        std::vector <CLHEP::Hep3Vector> v_caloTau_signalTrack_3mom;
        
        CLHEP::Hep3Vector signalTrack1_3mom(0, 0, 0);
        
        double signalTrack_HT = 0;
        
        for(int iSigTrack = 0; iSigTrack < (int) nSigTrack; iSigTrack++)
        {
            CLHEP::Hep3Vector temp_3mom;
            temp_3mom.setX(v_caloTau_signalTrack.at(iSigTrack)->px());
            temp_3mom.setY(v_caloTau_signalTrack.at(iSigTrack)->py());
            temp_3mom.setZ(v_caloTau_signalTrack.at(iSigTrack)->pz());
            
            v_caloTau_signalTrack_3mom.push_back(temp_3mom);
            v_signalTrack_caloTau_deltaR.push_back(temp_3mom.deltaR(caloTau_4mom.vect()));
            v_signalTrack_pTsortedIndex.push_back(iSigTrack);
            
            //printf("sig track %d: pT %0.2f, dR %0.2f \n", iSigTrack+1, temp_3mom.perp(), temp_3mom.deltaR(caloTau_4mom.vect()));
            
            signalTrack_HT += temp_3mom.perp();
            
            // Sort by pT
            for(int iSortedIndex = 0; iSortedIndex < (int) v_signalTrack_pTsortedIndex.size(); iSortedIndex++)
            {
                if(temp_3mom.perp() > v_caloTau_signalTrack_3mom.at(v_signalTrack_pTsortedIndex.at(iSortedIndex)).perp())
                {
                    for(int jSortedIndex = v_signalTrack_pTsortedIndex.size()-1; jSortedIndex > iSortedIndex; jSortedIndex--)
                    {
                        v_signalTrack_pTsortedIndex.at(jSortedIndex) = v_signalTrack_pTsortedIndex.at(jSortedIndex-1);
                    }
                    
                    v_signalTrack_pTsortedIndex.at(iSortedIndex) = iSigTrack;
                    
                    break;
                }
            }
        }
        
        if(nSigTrack)
        {
            signalTrack1_3mom = v_caloTau_signalTrack_3mom.at(v_signalTrack_pTsortedIndex.at(0));
            
            //printf("sigTrk1: pT %0.2f %0.2f \n", signalTrack1_3mom.perp(), caloTau.leadTrack()->pt());
        }
        
        // Isolation tracks
        reco::TrackRefVector v_caloTau_isolationTrack = caloTau.isolationTracks();
        
        int nIsoTrack = v_caloTau_isolationTrack.size();
        std::vector <int> v_isolationTrack_pTsortedIndex;
        std::vector <double> v_isolationTrack_caloTau_deltaR;
        std::vector <CLHEP::Hep3Vector> v_caloTau_isolationTrack_3mom;
        
        for(int iIsoTrack = 0; iIsoTrack < (int) nIsoTrack; iIsoTrack++)
        {
            CLHEP::Hep3Vector temp_3mom;
            temp_3mom.setX(v_caloTau_isolationTrack.at(iIsoTrack)->px());
            temp_3mom.setY(v_caloTau_isolationTrack.at(iIsoTrack)->py());
            temp_3mom.setZ(v_caloTau_isolationTrack.at(iIsoTrack)->pz());
            
            v_caloTau_isolationTrack_3mom.push_back(temp_3mom);
            v_isolationTrack_caloTau_deltaR.push_back(temp_3mom.deltaR(caloTau_4mom.vect()));
            v_isolationTrack_pTsortedIndex.push_back(iIsoTrack);
            
            //printf("iso track %d: pT %0.2f, dR %0.2f \n", iIsoTrack+1, temp_3mom.perp(), temp_3mom.deltaR(caloTau_4mom.vect()));
            
            // Sort by pT
            for(int iSortedIndex = 0; iSortedIndex < (int) v_isolationTrack_pTsortedIndex.size(); iSortedIndex++)
            {
                if(temp_3mom.perp() > v_caloTau_isolationTrack_3mom.at(v_isolationTrack_pTsortedIndex.at(iSortedIndex)).perp())
                {
                    for(int jSortedIndex = v_isolationTrack_pTsortedIndex.size()-1; jSortedIndex > iSortedIndex; jSortedIndex--)
                    {
                        v_isolationTrack_pTsortedIndex.at(jSortedIndex) = v_isolationTrack_pTsortedIndex.at(jSortedIndex-1);
                    }
                    
                    v_isolationTrack_pTsortedIndex.at(iSortedIndex) = iIsoTrack;
                    
                    break;
                }
            }
        }
        
        //for(int iIsoTrack = 0; iIsoTrack < (int) v_isolationTrack_pTsortedIndex.size(); iIsoTrack++)
        //{
        //    printf(
        //        "pT sorted iso track %d (%d): pT %0.2f \n",
        //        iIsoTrack+1,
        //        v_isolationTrack_pTsortedIndex.at(iIsoTrack)+1,
        //        v_caloTau_isolationTrack_3mom.at(v_isolationTrack_pTsortedIndex.at(iIsoTrack)).perp());
        //}
        
        printf(
            "nPV %d, nPU %d \n"
            
            "tau %d: pT %0.2f, eta %0.2f, phi %0.2f, pz %0.2f \n"
            
            "nSigTrk %d, nIsoTrk %d, neutralECALBasicClusters %d %d \n"
            
            "antiEle %0.2f, antiMu %0.2f \n"
            
            "byECALiso %0.2f, byIso %0.2f \n"
            "byLeadTrkFinding %0.2f, byLeadTrkPt %0.2f \n"
            "byTrackIso %0.2f \n"
            
            "isolationECALhitsEtSum %0.2f, isolationTracksPtSum %0.2f \n"
            "leadTrackHCAL3x3hitsEtSum %0.2f, leadTrackHCAL3x3hottesthitDEta %0.2f, leadTracksignedSipt %0.2f \n"
            "maximumHCALhitEt %0.2f \n",
            
            nPV, nPU,
            
            iCaloTau+1, caloTau.pt(), caloTau.eta(), caloTau.phi(), caloTau.pz(),
            
            nSigTrack, nIsoTrack, (int) caloTau.caloTauTagInfoRef().get()->neutralECALBasicClusters().size(), (int) v_caloTauTagInfo->at(iCaloTau).neutralECALBasicClusters().size(),
            
            v_caloRecoTauDiscriminationAgainstElectron->value(iCaloTau), v_caloRecoTauDiscriminationAgainstMuon->value(iCaloTau),
            
            v_caloRecoTauDiscriminationByECALIsolation->value(iCaloTau), v_caloRecoTauDiscriminationByIsolation->value(iCaloTau),
            v_caloRecoTauDiscriminationByLeadingTrackFinding->value(iCaloTau), v_caloRecoTauDiscriminationByLeadingTrackPtCut->value(iCaloTau),
            v_caloRecoTauDiscriminationByTrackIsolation->value(iCaloTau),
            
            caloTau.isolationECALhitsEtSum(), caloTau.isolationTracksPtSum(),
            caloTau.leadTrackHCAL3x3hitsEtSum(), caloTau.leadTrackHCAL3x3hottesthitDEta(), caloTau.leadTracksignedSipt(),
            caloTau.maximumHCALhitEt()
        );
        
        printf("\n");
        
        h1_caloTau_pT_reco->Fill(caloTau_4mom.perp());
        h1_caloTau_eta_reco->Fill(caloTau_4mom.eta());
        h1_caloTau_phi_reco->Fill(caloTau_4mom.phi());
        h1_caloTau_m_reco->Fill(caloTau_4mom.m());
        //h2_caloTau_decayMode_vs_m_reco->Fill(caloTau_4mom.m(), caloTau.decayMode());
        
        
        // AK4 PF jet matching
        bool caloTau_isAK4PFjetMatched = false;
        int caloTau_matchedAK4PFjet_index = -1;
        double caloTau_nearestAK4PFjet_deltaR = 9999;
        CLHEP::HepLorentzVector caloTau_matchedAK4PFjet_4mom(0, 0, 0, 0);
        
        for(int iAK4PFjet = 0; iAK4PFjet < (int) v_ak4PFJet->size(); iAK4PFjet++)
        {
            if(!v_ak4PFjet_isSelected.at(iAK4PFjet))
            {
                continue;
            }
            
            double deltaR = v_ak4PFjet_4mom.at(iAK4PFjet).deltaR(caloTau_4mom);
            
            if(deltaR < caloTau_nearestAK4PFjet_deltaR)
            {
                caloTau_matchedAK4PFjet_index = iAK4PFjet;
                caloTau_nearestAK4PFjet_deltaR = deltaR;
            }
        }
        
        printf("caloTau_nearestAK4PFjet_deltaR %0.2f (%d) \n", caloTau_nearestAK4PFjet_deltaR, caloTau_matchedAK4PFjet_index);
        h1_caloTau_nearestAK4PFjet_deltaR_reco->Fill(caloTau_nearestAK4PFjet_deltaR);
        
        if(caloTau_nearestAK4PFjet_deltaR < 0.4)
        {
            caloTau_isAK4PFjetMatched = true;
            caloTau_matchedAK4PFjet_4mom = v_ak4PFjet_4mom.at(caloTau_matchedAK4PFjet_index);
        }
        
        
        // Gen tauh matching
        bool caloTau_isGenMatched = false;
        int caloTau_matchedGenTauh_index = -1;
        double caloTau_nearestGenTauh_deltaR = 9999;
        CLHEP::HepLorentzVector caloTau_matchedGenTauh_4mom(0, 0, 0, 0);
        
        for(int iTauh_gen = 0; iTauh_gen < (int) v_tauh_4mom_gen.size(); iTauh_gen++)
        {
            if(!v_tauh_isSelected_gen.at(iTauh_gen))
            {
                continue;
            }
            
            // Reject if already used for matching
            if(v_tauh_isUsed_gen.at(iTauh_gen))
            {
                continue;
            }
            
            double deltaR = v_tauh_4mom_gen.at(iTauh_gen).deltaR(caloTau_4mom);
            //printf("deltaR %0.2f \n", deltaR);
            
            if(deltaR < caloTau_nearestGenTauh_deltaR)
            {
                caloTau_matchedGenTauh_index = iTauh_gen;
                caloTau_nearestGenTauh_deltaR = deltaR;
            }
        }
        
        printf("caloTau_nearestGenTauh_deltaR %0.2f (%d) \n", caloTau_nearestGenTauh_deltaR, caloTau_matchedGenTauh_index);
        h1_caloTau_nearestGenTauh_deltaR_reco->Fill(caloTau_nearestGenTauh_deltaR);
        
        if(caloTau_nearestGenTauh_deltaR < 0.3)
        {
            v_tauh_isUsed_gen.at(caloTau_matchedGenTauh_index) = true;
            
            caloTau_isGenMatched = true;
            caloTau_matchedGenTauh_4mom = v_tauh_4mom_gen.at(caloTau_matchedGenTauh_index);
        }
        
        
        // Discriminators
        
        std::vector <double> v_caloTauDiscriminator = {
            1,
            v_caloRecoTauDiscriminationAgainstElectron->value(iCaloTau),
            v_caloRecoTauDiscriminationAgainstMuon->value(iCaloTau),
            v_caloRecoTauDiscriminationByECALIsolation->value(iCaloTau),
            v_caloRecoTauDiscriminationByIsolation->value(iCaloTau),
            v_caloRecoTauDiscriminationByTrackIsolation->value(iCaloTau),
            v_caloRecoTauDiscriminationByLeadingTrackPtCut->value(iCaloTau),
        };
        
        for(int iDisc = 0; iDisc < (int) v_caloTauDiscriminator_name.size(); iDisc++)
        {
            std::string discriminatorName = v_caloTauDiscriminator_name.at(iDisc);
            
            if(v_caloTauDiscriminator.at(iDisc))
            {
                if(caloTau_isGenMatched)
                {
                    m_TauMatchingOutput[discriminatorName]->nGenMatched++;
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_pT_reco->Fill(caloTau_matchedGenTauh_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_eta_reco->Fill(caloTau_matchedGenTauh_4mom.eta());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_phi_reco->Fill(caloTau_matchedGenTauh_4mom.phi());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_m_reco->Fill(caloTau_matchedGenTauh_4mom.m());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_pTresolution_reco->Fill(caloTau_4mom.perp()/caloTau_matchedGenTauh_4mom.perp());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_sigTrack_n_reco->Fill(nSigTrack);
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isoTrack_n_reco->Fill(nIsoTrack);
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_reco->Fill(caloTau.leadTrackHCAL3x3hitsEtSum());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_maximumHCALhitEt_reco->Fill(caloTau.maximumHCALhitEt());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationECALhitsEtSum_reco->Fill(caloTau.isolationECALhitsEtSum());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationTracksPtSum_reco->Fill(caloTau.isolationTracksPtSum());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco->Fill(caloTau.leadTrackHCAL3x3hitsEtSum() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_maximumHCALhitEt_by_caloTauPt_reco->Fill(caloTau.maximumHCALhitEt() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationECALhitsEtSum_by_caloTauPt_reco->Fill(caloTau.isolationECALhitsEtSum() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationTracksPtSum_by_caloTauPt_reco->Fill(caloTau.isolationTracksPtSum() / caloTau_4mom.perp());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_signalTracksInvariantMass_reco->Fill(caloTau.signalTracksInvariantMass());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_TracksInvariantMass_reco->Fill(caloTau.TracksInvariantMass());
                    
                    if(nSigTrack)
                    {
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.leadTrackHCAL3x3hitsEtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco->Fill(
                            caloTau.leadTrackHCAL3x3hitsEtSum() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrack1pT_reco->Fill(
                            caloTau.maximumHCALhitEt() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_maximumHCALhitEt_by_sigTrackHT_reco->Fill(
                            caloTau.maximumHCALhitEt() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.isolationECALhitsEtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationECALhitsEtSum_by_sigTrackHT_reco->Fill(
                            caloTau.isolationECALhitsEtSum() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.isolationTracksPtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isolationTracksPtSum_by_sigTrackHT_reco->Fill(
                            caloTau.isolationTracksPtSum() / signalTrack_HT
                        );
                        
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_sigTrack1_deltaR_reco->Fill(
                            v_signalTrack_caloTau_deltaR.at(v_signalTrack_pTsortedIndex.at(0))
                        );
                    }
                    
                    if(nIsoTrack)
                    {
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genMatched_isoTrack1_deltaR_reco->Fill(
                            v_isolationTrack_caloTau_deltaR.at(v_isolationTrack_pTsortedIndex.at(0))
                        );
                    }
                    
                    //m_TauMatchingOutput[discriminatorName]->h2_caloTau_genMatched_decayMode_vs_m_reco->Fill(caloTau_matchedGenTauh_4mom.m(), caloTau.decayMode());
                    m_TauMatchingOutput[discriminatorName]->h2_caloTau_genMatched_pT_vs_nPV_reco->Fill(nPV, caloTau_matchedGenTauh_4mom.perp());
                }
                
                else
                {
                    m_TauMatchingOutput[discriminatorName]->nGenNotMatched++;
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_pT_reco->Fill(caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_eta_reco->Fill(caloTau_4mom.eta());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_phi_reco->Fill(caloTau_4mom.phi());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_m_reco->Fill(caloTau_4mom.m());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_sigTrack_n_reco->Fill(nSigTrack);
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isoTrack_n_reco->Fill(nIsoTrack);
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_reco->Fill(caloTau.leadTrackHCAL3x3hitsEtSum());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_maximumHCALhitEt_reco->Fill(caloTau.maximumHCALhitEt());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationECALhitsEtSum_reco->Fill(caloTau.isolationECALhitsEtSum());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationTracksPtSum_reco->Fill(caloTau.isolationTracksPtSum());
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_caloTauPt_reco->Fill(caloTau.leadTrackHCAL3x3hitsEtSum() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_maximumHCALhitEt_by_caloTauPt_reco->Fill(caloTau.maximumHCALhitEt() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_caloTauPt_reco->Fill(caloTau.isolationECALhitsEtSum() / caloTau_4mom.perp());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationTracksPtSum_by_caloTauPt_reco->Fill(caloTau.isolationTracksPtSum() / caloTau_4mom.perp());
                    
                    
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_signalTracksInvariantMass_reco->Fill(caloTau.signalTracksInvariantMass());
                    m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_TracksInvariantMass_reco->Fill(caloTau.TracksInvariantMass());
                    
                    if(nSigTrack)
                    {
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.leadTrackHCAL3x3hitsEtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_leadTrackHCAL3x3hitsEtSum_by_sigTrackHT_reco->Fill(
                            caloTau.leadTrackHCAL3x3hitsEtSum() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrack1pT_reco->Fill(
                            caloTau.maximumHCALhitEt() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_maximumHCALhitEt_by_sigTrackHT_reco->Fill(
                            caloTau.maximumHCALhitEt() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.isolationECALhitsEtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationECALhitsEtSum_by_sigTrackHT_reco->Fill(
                            caloTau.isolationECALhitsEtSum() / signalTrack_HT
                        );
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrack1pT_reco->Fill(
                            caloTau.isolationTracksPtSum() / signalTrack1_3mom.perp()
                        );
                        
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isolationTracksPtSum_by_sigTrackHT_reco->Fill(
                            caloTau.isolationTracksPtSum() / signalTrack_HT
                        );
                        
                        
                        //
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_sigTrack1_deltaR_reco->Fill(
                            v_signalTrack_caloTau_deltaR.at(v_signalTrack_pTsortedIndex.at(0))
                        );
                    }
                    
                    if(nIsoTrack)
                    {
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_isoTrack1_deltaR_reco->Fill(
                            v_isolationTrack_caloTau_deltaR.at(v_isolationTrack_pTsortedIndex.at(0))
                        );
                    }
                    
                    //m_TauMatchingOutput[discriminatorName]->h2_caloTau_genNotMatched_decayMode_vs_m_reco->Fill(caloTau_4mom.m(), caloTau.decayMode());
                    m_TauMatchingOutput[discriminatorName]->h2_caloTau_genNotMatched_pT_vs_nPV_reco->Fill(nPV, caloTau_4mom.perp());
                    
                    
                    if(caloTau_isAK4PFjetMatched)
                    {
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco->Fill(caloTau_matchedAK4PFjet_4mom.perp());
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_ak4PFjetMatched_eta_reco->Fill(caloTau_matchedAK4PFjet_4mom.eta());
                        m_TauMatchingOutput[discriminatorName]->h1_caloTau_genNotMatched_ak4PFjetMatched_phi_reco->Fill(caloTau_matchedAK4PFjet_4mom.phi());
                        
                        m_TauMatchingOutput[discriminatorName]->h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco->Fill(nPV, caloTau_matchedAK4PFjet_4mom.perp());
                    }
                }
            }
        }
    }
    
    printf("\n\n");
}


// ------------ method called once each job just before starting event loop  ------------
void
CaloTauAnalyzer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void CaloTauAnalyzer::endJob()
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
CaloTauAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);

  //Specify that only 'tracks' is allowed
  //To use, remove the default given above and uncomment below
  //ParameterSetDescription desc;
  //desc.addUntracked<edm::InputTag>("tracks","ctfWithMaterialTracks");
  //descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(CaloTauAnalyzer);
