// -*- C++ -*-
//
// Package:    EDAnalyzers/TreeMaker
// Class:      TreeMaker
//
/**\class TreeMaker TreeMaker.cc EDAnalyzers/TreeMaker/plugins/TreeMaker.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Sat, 11 May 2019 13:14:55 GMT
//
//


// system include files
# include <algorithm>
# include <list>
# include <memory>
# include <numeric>

// user include files



# include "CommonTools/UtilAlgos/interface/TFileService.h"
# include "DataFormats/CaloTowers/interface/CaloTowerDefs.h"
# include "DataFormats/Common/interface/MapOfVectors.h"
# include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
# include "DataFormats/EgammaCandidates/interface/Photon.h"
# include "DataFormats/ForwardDetId/interface/HGCEEDetId.h"
# include "DataFormats/ForwardDetId/interface/HGCalDetId.h"
# include "DataFormats/FWLite/interface/ESHandle.h"
# include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
# include "DataFormats/HGCalReco/interface/Trackster.h"
# include "DataFormats/HGCRecHit/interface/HGCRecHit.h"
# include "DataFormats/HepMCCandidate/interface/GenParticle.h"
# include "DataFormats/JetReco/interface/PFJet.h"
# include "DataFormats/Math/interface/LorentzVector.h"
# include "DataFormats/ParticleFlowReco/interface/HGCalMultiCluster.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
# include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
# include "DataFormats/TrackReco/interface/Track.h"
# include "DataFormats/TrackReco/interface/TrackFwd.h"
# include "DataFormats/VertexReco/interface/Vertex.h"
# include "FWCore/Framework/interface/Event.h"
# include "FWCore/Framework/interface/ESHandle.h"
# include "FWCore/Framework/interface/Frameworkfwd.h"
# include "FWCore/Framework/interface/MakerMacros.h"
# include "FWCore/Framework/interface/one/EDAnalyzer.h"
# include "FWCore/ParameterSet/interface/ParameterSet.h"
# include "FWCore/ServiceRegistry/interface/Service.h"
# include "FWCore/Utilities/interface/InputTag.h"
# include "Geometry/CaloTopology/interface/HGCalTopology.h"
# include "Geometry/Records/interface/CaloGeometryRecord.h"
# include "Geometry/Records/interface/IdealGeometryRecord.h"
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "SimDataFormats/CaloAnalysis/interface/CaloParticle.h"
# include "SimDataFormats/CaloAnalysis/interface/SimCluster.h"
# include "SimDataFormats/CaloHit/interface/PCaloHit.h"
# include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
# include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

# include "EDAnalyzers/TreeMaker/interface/Common.h"
# include "EDAnalyzers/TreeMaker/interface/Constants.h"
# include "EDAnalyzers/TreeMaker/interface/TreeOutputInfo.h"

# include <CLHEP/Matrix/Matrix.h>
# include <CLHEP/Vector/ThreeVector.h>
# include <CLHEP/Vector/ThreeVector.h>

# include <Compression.h>
# include <TH1F.h>
# include <TH2F.h>
# include <TMatrixD.h>
# include <TTree.h> 
# include <TVector2.h> 
# include <TVectorD.h> 

//
// class declaration
//

// If the analyzer does not use TFileService, please remove
// the template argument to the base class so the class inherits
// from  edm::one::EDAnalyzer<>
// This will improve performance in multithreaded jobs.



double HGCal_minEta = 1.479;
double HGCal_maxEta = 3.1;

double el_minPt = 10; //15;
double el_maxPt = 99999; //30;

double ph_minPt = 10; //15;
double ph_maxPt = 99999; //30;

double _largeVal = 999999999;


class TreeMaker : public edm::one::EDAnalyzer<edm::one::SharedResources>
{
    public:
    
    explicit TreeMaker(const edm::ParameterSet&);
    ~TreeMaker();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
    
    private:
    
    virtual void beginJob() override;
    virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
    virtual void endJob() override;
    
    double getDeltaPhi(double phi1, double phi2);
    
    std::tuple <TMatrixD, TMatrixD, TVectorD> getMultiClusterPC(
        reco::HGCalMultiCluster *multiCluster,
        std::map <DetId, const HGCRecHit*> m_recHit
    );
    
    
    int minLayer;
    int maxLayer;
    
    
    TreeOutputInfo::TreeOutput *treeOutput;
    
    
    // My stuff //
    bool debug;
    bool isGunSample;
    
    bool storeSimHit;
    bool storeRecHit;
    bool storeHGCALlayerClus;
    bool storeSuperClusTICLclus;
    
    double TICLeleGenMatchDR;
    double TICLphoGenMatchDR;
    
    
    // Gen particles //
    edm::EDGetTokenT <std::vector <reco::GenParticle> > tok_genParticle;
    
    
    // Pileup //
    edm::EDGetTokenT <std::vector <PileupSummaryInfo> > tok_pileup;
    
    
    // Rho //
    edm::EDGetTokenT <double> tok_rho;
    
    
    // HGCAL layer clusters //
    edm::EDGetTokenT <std::vector <reco::CaloCluster> > tok_HGCALlayerCluster;
    
    
    // TICL //
    edm::EDGetTokenT <std::vector <ticl::Trackster> > tok_TICLtrackster;
    edm::EDGetTokenT <std::vector <reco::HGCalMultiCluster> > tok_TICLmultiCluster;
    
    
    // Gsf electrons from Multiclus //
    edm::EDGetTokenT <std::vector <reco::GsfElectron> > tok_gsfEleFromMultiClus;
    
    
    // Gsf electrons from TICL //
    edm::EDGetTokenT <std::vector <reco::GsfElectron> > tok_gsfEleFromTICL;
    edm::EDGetTokenT <edm::MapOfVectors <std::string, double> > tok_gsfEleFromTICLvarMap;
    
    
    // Photons from Multiclus //
    edm::EDGetTokenT <std::vector <reco::Photon> > tok_phoFromMultiClus;
    
    
    // Photons from TICL //
    edm::EDGetTokenT <std::vector <reco::Photon> > tok_phoFromTICL;
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
TreeMaker::TreeMaker(const edm::ParameterSet& iConfig)
{
    usesResource("TFileService");
    edm::Service<TFileService> fs;
    
    // Compression
    //fs->file().SetCompressionAlgorithm(ROOT::kLZMA);
    //fs->file().SetCompressionLevel(8);
    
    
    treeOutput = new TreeOutputInfo::TreeOutput("tree", fs);
    
    
    minLayer = +9999;
    maxLayer = -9999;
    
    
    // My stuff //
    debug = iConfig.getParameter <bool>("debug");
    isGunSample = iConfig.getParameter <bool>("isGunSample");
    
    storeSimHit = iConfig.getParameter <bool>("storeSimHit");
    storeRecHit = iConfig.getParameter <bool>("storeRecHit");
    storeHGCALlayerClus = iConfig.getParameter <bool>("storeHGCALlayerClus");
    storeSuperClusTICLclus = iConfig.getParameter <bool>("storeSuperClusTICLclus");
    
    TICLeleGenMatchDR = iConfig.getParameter <double>("TICLeleGenMatchDR");
    TICLphoGenMatchDR = iConfig.getParameter <double>("TICLphoGenMatchDR");
    
    
    // Gen particles //
    tok_genParticle = consumes <std::vector <reco::GenParticle> >(iConfig.getParameter <edm::InputTag>("label_genParticle"));
    
    
    // Pileup //
    tok_pileup = consumes <std::vector <PileupSummaryInfo> >(iConfig.getParameter <edm::InputTag>("label_pileup"));
    
    
    // Rho //
    tok_rho = consumes <double>(iConfig.getParameter <edm::InputTag>("label_rho"));
    
    
    // TICL //
    tok_TICLtrackster = consumes <std::vector <ticl::Trackster> >(iConfig.getParameter <edm::InputTag>("label_TICLtrackster"));
    tok_TICLmultiCluster = consumes <std::vector <reco::HGCalMultiCluster> >(iConfig.getParameter <edm::InputTag>("label_TICLmultiCluster"));
    
    
    // Gsf electrons from Multiclus //
    tok_gsfEleFromMultiClus = consumes <std::vector <reco::GsfElectron> >(iConfig.getParameter <edm::InputTag>("label_gsfEleFromMultiClus"));
    
    
    // Gsf electrons from TICL //
    tok_gsfEleFromTICL = consumes <std::vector <reco::GsfElectron> >(iConfig.getParameter <edm::InputTag>("label_gsfEleFromTICL"));
    tok_gsfEleFromTICLvarMap = consumes <edm::MapOfVectors <std::string, double> >(iConfig.getParameter <edm::InputTag>("label_gsfEleFromTICLvarMap"));
    
    
    // Photons from MultiClus //
    tok_phoFromMultiClus = consumes <std::vector <reco::Photon> >(iConfig.getParameter <edm::InputTag>("label_phoFromMultiClus"));
    
    
    // Photons from TICL //
    tok_phoFromTICL = consumes <std::vector <reco::Photon> >(iConfig.getParameter <edm::InputTag>("label_phoFromTICL"));
}


TreeMaker::~TreeMaker()
{
    // do anything here that needs to be done at desctruction time
    // (e.g. close files, deallocate resources etc.)
    
    delete treeOutput;
}


//
// member functions
//


// ------------ method called for each event  ------------
void TreeMaker::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    
    long long eventNumber = iEvent.id().event();
    //printf("Event %llu \n", eventNumber);
    
    
    treeOutput->clear();
    
    //recHitTools.getEventSetup(iSetup);
    
    
    //////////////////// Run info ////////////////////
    treeOutput->runNumber = iEvent.id().run();
    treeOutput->eventNumber = iEvent.id().event();
    treeOutput->luminosityNumber = iEvent.id().luminosityBlock();
    treeOutput->bunchCrossingNumber = iEvent.bunchCrossing();
    
    
    //////////////////// Gen particle ////////////////////
    edm::Handle <std::vector <reco::GenParticle> > v_genParticle;
    iEvent.getByToken(tok_genParticle, v_genParticle);
    
    std::vector <CLHEP::HepLorentzVector> v_genEl_4mom;
    std::vector <CLHEP::HepLorentzVector> v_genPh_4mom;
    
    
    for(int iPart = 0; iPart < (int) v_genParticle->size(); iPart++)
    {
        reco::GenParticle part = v_genParticle->at(iPart);
        
        int pdgId = part.pdgId();
        int status = part.status();
        
        // Gen ele
        //if(abs(pdgId) == 11 && status == 1)
        //if(abs(pdgId) == 11 && (part.isHardProcess() || status == 1))
        if(
            abs(pdgId) == 11 && (
                (isGunSample && status == 1) ||
                (!isGunSample && part.isHardProcess())
            )
        )
        {
            //printf("[%llu] Gen electron found: E %0.2f, pT %0.2f, eta %+0.2f \n", eventNumber, part.energy(), part.pt(), part.eta());
            
            printf(
                "[%llu] "
                "Gen-ele found: E %0.2f, pT %0.2f, eta %+0.2f, pz %+0.2f, "
                "\n",
                eventNumber,
                part.energy(), part.pt(), part.eta(), part.pz()
            );
            
            if(fabs(part.eta()) > HGCal_minEta && fabs(part.eta()) < HGCal_maxEta && part.pt() > el_minPt && part.pt() < el_maxPt)
            {
                CLHEP::HepLorentzVector genEl_4mom;
                
                genEl_4mom.setT(part.energy());
                genEl_4mom.setX(part.px());
                genEl_4mom.setY(part.py());
                genEl_4mom.setZ(part.pz());
                
                v_genEl_4mom.push_back(genEl_4mom);
                
                treeOutput->v_genEl_E.push_back(genEl_4mom.e());
                treeOutput->v_genEl_px.push_back(genEl_4mom.px());
                treeOutput->v_genEl_py.push_back(genEl_4mom.py());
                treeOutput->v_genEl_pz.push_back(genEl_4mom.pz());
                treeOutput->v_genEl_pT.push_back(genEl_4mom.perp());
                treeOutput->v_genEl_eta.push_back(genEl_4mom.eta());
                treeOutput->v_genEl_phi.push_back(genEl_4mom.phi());
                
                treeOutput->genEl_n++;
            }
        }
        
        else if(
            abs(pdgId) == 22 && (
                (isGunSample && status == 1) ||
                (!isGunSample && part.isHardProcess())
            )
        )
        {
            //printf("[%llu] Gen electron found: E %0.2f, pT %0.2f, eta %+0.2f \n", eventNumber, part.energy(), part.pt(), part.eta());
            
            printf(
                "[%llu] "
                "Gen-pho found: E %0.2f, pT %0.2f, eta %+0.2f, pz %+0.2f, "
                "\n",
                eventNumber,
                part.energy(), part.pt(), part.eta(), part.pz()
            );
            
            if(fabs(part.eta()) > HGCal_minEta && fabs(part.eta()) < HGCal_maxEta && part.pt() > ph_minPt && part.pt() < ph_maxPt)
            {
                CLHEP::HepLorentzVector genPh_4mom;
                
                genPh_4mom.setT(part.energy());
                genPh_4mom.setX(part.px());
                genPh_4mom.setY(part.py());
                genPh_4mom.setZ(part.pz());
                
                v_genPh_4mom.push_back(genPh_4mom);
                
                treeOutput->v_genPh_E.push_back(genPh_4mom.e());
                treeOutput->v_genPh_px.push_back(genPh_4mom.px());
                treeOutput->v_genPh_py.push_back(genPh_4mom.py());
                treeOutput->v_genPh_pz.push_back(genPh_4mom.pz());
                treeOutput->v_genPh_pT.push_back(genPh_4mom.perp());
                treeOutput->v_genPh_eta.push_back(genPh_4mom.eta());
                treeOutput->v_genPh_phi.push_back(genPh_4mom.phi());
                
                treeOutput->genPh_n++;
            }
        }
    }
    
    
    // Pileup
    edm::Handle <std::vector <PileupSummaryInfo> > pileUps_reco;
    iEvent.getByToken(tok_pileup, pileUps_reco);
    treeOutput->pileup_n = Common::getPileup(pileUps_reco);
    
    
    // Rho
    edm::Handle <double> handle_rho;
    iEvent.getByToken(tok_rho, handle_rho);
    double rho = *handle_rho;
    
    treeOutput->rho = rho;
    
    
    
    //////////////////////////////////////////////////////////////////////
    //////////////////// Gsf electrons from MultiClus ////////////////////
    //////////////////////////////////////////////////////////////////////
    
    edm::Handle <std::vector <reco::GsfElectron> > v_gsfEleFromMultiClus;
    
    try
    {
        
        iEvent.getByToken(tok_gsfEleFromMultiClus, v_gsfEleFromMultiClus);
    }
    
    catch(...)
    {
    }
    
    if(v_gsfEleFromMultiClus.isValid())
    {
        int nEleFromMultiClus = v_gsfEleFromMultiClus->size();
        
        std::vector <CLHEP::HepLorentzVector> v_gsfEleFromMultiClus_4mom;
        
        
        for(int iEle = 0; iEle < nEleFromMultiClus; iEle++)
        {
            reco::GsfElectron gsfEle = v_gsfEleFromMultiClus->at(iEle);
            
            CLHEP::HepLorentzVector gsfEleFromMultiClus_4mom;
            gsfEleFromMultiClus_4mom.setT(gsfEle.energy());
            gsfEleFromMultiClus_4mom.setX(gsfEle.px());
            gsfEleFromMultiClus_4mom.setY(gsfEle.py());
            gsfEleFromMultiClus_4mom.setZ(gsfEle.pz());
            
            v_gsfEleFromMultiClus_4mom.push_back(gsfEleFromMultiClus_4mom);
        }
        
        
        // MultiClus-ele gen-matching
        TMatrixD mat_gsfEleFromMultiClus_genEl_deltaR;
        
        std::vector <int> v_gsfEleFromMultiClus_matchedGenEl_idx;
        
        std::vector <double> v_gsfEleFromMultiClus_genEl_minDeltaR = Common::getMinDeltaR(
            v_gsfEleFromMultiClus_4mom,
            v_genEl_4mom,
            mat_gsfEleFromMultiClus_genEl_deltaR,
            v_gsfEleFromMultiClus_matchedGenEl_idx
        );
        
        
        for(int iEle = 0; iEle < nEleFromMultiClus; iEle++)
        {
            reco::GsfElectron gsfEle = v_gsfEleFromMultiClus->at(iEle);
            CLHEP::HepLorentzVector gsfEleFromMultiClus_4mom = v_gsfEleFromMultiClus_4mom.at(iEle);
            
            
            if(gsfEle.pt() < el_minPt || fabs(gsfEle.eta()) < HGCal_minEta || fabs(gsfEle.eta()) > HGCal_maxEta)
            {
                continue;
            }
            
            
            double matchedGenEl_deltaR = v_gsfEleFromMultiClus_genEl_minDeltaR.at(iEle);
            
            if(matchedGenEl_deltaR > TICLeleGenMatchDR)
            {
                continue;
            }
            
            printf(
                "[%llu] "
                
                "gsfEleFromMultiClus %d/%d: "
                "E %0.4f, "
                "pT %0.2f, "
                "eta %+0.2f, "
                "\n",
                
                eventNumber,
                
                iEle+1, nEleFromMultiClus,
                gsfEle.energy(),
                gsfEle.pt(),
                gsfEle.eta()
            );
            
            int matchedGenEl_idx = v_gsfEleFromMultiClus_matchedGenEl_idx.at(iEle);
            
            treeOutput->v_gsfEleFromMultiClus_genEl_minDeltaR.push_back(matchedGenEl_deltaR);
            treeOutput->v_gsfEleFromMultiClus_nearestGenEl_idx.push_back(matchedGenEl_idx);
            
            double matchedGenEl_energy = -99;
            double matchedGenEl_pT = -99;
            double matchedGenEl_eta = -99;
            double matchedGenEl_phi = -99;
            
            if(matchedGenEl_idx >= 0)
            {
                matchedGenEl_energy = v_genEl_4mom.at(matchedGenEl_idx).e();
                matchedGenEl_pT = v_genEl_4mom.at(matchedGenEl_idx).perp();
                matchedGenEl_eta = v_genEl_4mom.at(matchedGenEl_idx).eta();
                matchedGenEl_phi = v_genEl_4mom.at(matchedGenEl_idx).phi();
            }
            
            treeOutput->v_gsfEleFromMultiClus_matchedGenEl_E.push_back(matchedGenEl_energy);
            treeOutput->v_gsfEleFromMultiClus_matchedGenEl_pT.push_back(matchedGenEl_pT);
            treeOutput->v_gsfEleFromMultiClus_matchedGenEl_eta.push_back(matchedGenEl_eta);
            treeOutput->v_gsfEleFromMultiClus_matchedGenEl_phi.push_back(matchedGenEl_phi);
            
            
            treeOutput->v_gsfEleFromMultiClus_E.push_back(gsfEle.energy());
            treeOutput->v_gsfEleFromMultiClus_px.push_back(gsfEle.px());
            treeOutput->v_gsfEleFromMultiClus_py.push_back(gsfEle.py());
            treeOutput->v_gsfEleFromMultiClus_pz.push_back(gsfEle.pz());
            
            treeOutput->v_gsfEleFromMultiClus_pT.push_back(gsfEle.pt());
            treeOutput->v_gsfEleFromMultiClus_eta.push_back(gsfEle.eta());
            treeOutput->v_gsfEleFromMultiClus_phi.push_back(gsfEle.phi());
            
            treeOutput->v_gsfEleFromMultiClus_ET.push_back(gsfEle.et());
            
            treeOutput->gsfEleFromMultiClus_n++;
        }
    }
    
    
    
    /////////////////////////////////////////////////////////////////
    //////////////////// Gsf electrons from TICL ////////////////////
    /////////////////////////////////////////////////////////////////
    edm::Handle <std::vector <reco::GsfElectron> > v_gsfEleFromTICL;
    
    try
    {
        
        iEvent.getByToken(tok_gsfEleFromTICL, v_gsfEleFromTICL);
    }
    
    catch(...)
    {
    }
    
    if(v_gsfEleFromTICL.isValid())
    {
        //edm::Handle <edm::MapOfVectors <std::string, double> > m_gsfEleFromTICLvarMap;
        //iEvent.getByToken(tok_gsfEleFromTICLvarMap, m_gsfEleFromTICLvarMap);
        
        int nEleFromTICL = v_gsfEleFromTICL->size();
        
        std::vector <CLHEP::HepLorentzVector> v_gsfEleFromTICL_4mom;
        
        
        for(int iEle = 0; iEle < nEleFromTICL; iEle++)
        {
            reco::GsfElectron gsfEle = v_gsfEleFromTICL->at(iEle);
            
            CLHEP::HepLorentzVector gsfEleFromTICL_4mom;
            gsfEleFromTICL_4mom.setT(gsfEle.energy());
            gsfEleFromTICL_4mom.setX(gsfEle.px());
            gsfEleFromTICL_4mom.setY(gsfEle.py());
            gsfEleFromTICL_4mom.setZ(gsfEle.pz());
            
            v_gsfEleFromTICL_4mom.push_back(gsfEleFromTICL_4mom);
        }
        
        
        // TICL-ele gen-matching
        TMatrixD mat_gsfEleFromTICL_genEl_deltaR;
        
        std::vector <int> v_gsfEleFromTICL_matchedGenEl_idx;
        
        std::vector <double> v_gsfEleFromTICL_genEl_minDeltaR = Common::getMinDeltaR(
            v_gsfEleFromTICL_4mom,
            v_genEl_4mom,
            mat_gsfEleFromTICL_genEl_deltaR,
            v_gsfEleFromTICL_matchedGenEl_idx
        );
        
        
        for(int iEle = 0; iEle < nEleFromTICL; iEle++)
        {
            reco::GsfElectron gsfEle = v_gsfEleFromTICL->at(iEle);
            CLHEP::HepLorentzVector gsfEleFromTICL_4mom = v_gsfEleFromTICL_4mom.at(iEle);
            
            
            if(gsfEle.pt() < el_minPt || fabs(gsfEle.eta()) < HGCal_minEta || fabs(gsfEle.eta()) > HGCal_maxEta)
            {
                continue;
            }
            
            
            double matchedGenEl_deltaR = v_gsfEleFromTICL_genEl_minDeltaR.at(iEle);
            
            if(matchedGenEl_deltaR > TICLeleGenMatchDR)
            {
                continue;
            }
            
            printf(
                "[%llu] "
                
                "gsfEleFromTICL %d/%d: "
                "E %0.4f, "
                "pT %0.2f, "
                "eta %+0.2f, "
                
                "dR(w.r.t. gen) %0.4e, "
                
                //"\n"
                "superClus E %0.2f, "
                "superClus nClus %d, "
                //"R2.8 %0.2f, "
                
                "\n",
                
                eventNumber,
                
                iEle+1, nEleFromTICL,
                gsfEle.energy(),
                gsfEle.pt(),
                gsfEle.eta(),
                
                matchedGenEl_deltaR,
                
                gsfEle.superCluster()->energy(),
                (int) gsfEle.superCluster()->clusters().size()
                
                //m_gsfEleFromTICLvarMap->find("HGCalElectronRvar_HGCalElectronRvar")[iEle]
            );
            
            int matchedGenEl_idx = v_gsfEleFromTICL_matchedGenEl_idx.at(iEle);
            
            treeOutput->v_gsfEleFromTICL_genEl_minDeltaR.push_back(matchedGenEl_deltaR);
            treeOutput->v_gsfEleFromTICL_nearestGenEl_idx.push_back(matchedGenEl_idx);
            
            double matchedGenEl_energy = -99;
            double matchedGenEl_pT = -99;
            double matchedGenEl_eta = -99;
            double matchedGenEl_phi = -99;
            
            if(matchedGenEl_idx >= 0)
            {
                matchedGenEl_energy = v_genEl_4mom.at(matchedGenEl_idx).e();
                matchedGenEl_pT = v_genEl_4mom.at(matchedGenEl_idx).perp();
                matchedGenEl_eta = v_genEl_4mom.at(matchedGenEl_idx).eta();
                matchedGenEl_phi = v_genEl_4mom.at(matchedGenEl_idx).phi();
            }
            
            treeOutput->v_gsfEleFromTICL_matchedGenEl_E.push_back(matchedGenEl_energy);
            treeOutput->v_gsfEleFromTICL_matchedGenEl_pT.push_back(matchedGenEl_pT);
            treeOutput->v_gsfEleFromTICL_matchedGenEl_eta.push_back(matchedGenEl_eta);
            treeOutput->v_gsfEleFromTICL_matchedGenEl_phi.push_back(matchedGenEl_phi);
            
            
            treeOutput->v_gsfEleFromTICL_E.push_back(gsfEle.energy());
            treeOutput->v_gsfEleFromTICL_px.push_back(gsfEle.px());
            treeOutput->v_gsfEleFromTICL_py.push_back(gsfEle.py());
            treeOutput->v_gsfEleFromTICL_pz.push_back(gsfEle.pz());
            
            treeOutput->v_gsfEleFromTICL_pT.push_back(gsfEle.pt());
            treeOutput->v_gsfEleFromTICL_eta.push_back(gsfEle.eta());
            treeOutput->v_gsfEleFromTICL_phi.push_back(gsfEle.phi());
            
            treeOutput->v_gsfEleFromTICL_ET.push_back(gsfEle.et());
            
            treeOutput->gsfEleFromTICL_n++;
            
            int gsfEle_superClus_nClus = gsfEle.superCluster()->clusters().size();
            treeOutput->v_gsfEleFromTICL_superClus_nClus.push_back(gsfEle_superClus_nClus);
            
            edm::PtrVector <reco::CaloCluster> v_superClus_clus = gsfEle.superCluster()->clusters();
            
            std::vector <int> v_superClus_clus_sortedIdx(gsfEle_superClus_nClus);
            std::iota(v_superClus_clus_sortedIdx.begin(), v_superClus_clus_sortedIdx.end(), 0);
            
            std::sort(
                v_superClus_clus_sortedIdx.begin(), v_superClus_clus_sortedIdx.end(),
                [&](int idx1, int idx2)
                {
                    return (v_superClus_clus[idx1].get()->energy() > v_superClus_clus[idx2].get()->energy());
                }
            );
            
            std::vector <double> v_gsfEleFromTICL_superClus_clus_eleIdx;
            std::vector <double> v_gsfEleFromTICL_superClus_clus_idx;
            std::vector <double> v_gsfEleFromTICL_superClus_clus_E;
            std::vector <double> v_gsfEleFromTICL_superClus_clus_ET;
            
            int iClus = -1;
            
            for(auto idx : v_superClus_clus_sortedIdx)
            {
                iClus++;
                
                const reco::CaloCluster cluster = *v_superClus_clus[idx].get();
                
                v_gsfEleFromTICL_superClus_clus_eleIdx.push_back(treeOutput->gsfEleFromTICL_n-1);
                v_gsfEleFromTICL_superClus_clus_idx.push_back(iClus);
                v_gsfEleFromTICL_superClus_clus_E.push_back(cluster.energy());
                v_gsfEleFromTICL_superClus_clus_ET.push_back(cluster.energy() * std::sin(cluster.position().theta()));
            }
            
            treeOutput->vv_gsfEleFromTICL_superClus_clus_eleIdx.push_back(v_gsfEleFromTICL_superClus_clus_eleIdx);
            treeOutput->vv_gsfEleFromTICL_superClus_clus_idx.push_back(v_gsfEleFromTICL_superClus_clus_idx);
            treeOutput->vv_gsfEleFromTICL_superClus_clus_E.push_back(v_gsfEleFromTICL_superClus_clus_E);
            treeOutput->vv_gsfEleFromTICL_superClus_clus_ET.push_back(v_gsfEleFromTICL_superClus_clus_ET);
            
            printf("SC clus E (%d): ", gsfEle_superClus_nClus);
            iClus = -1;
            for(auto E : treeOutput->vv_gsfEleFromTICL_superClus_clus_E.back())
            {
                iClus++;
                printf("(%d) %0.2f, ", iClus+1, E);
            }
            printf("\n");
            
            //treeOutput->v_gsfEleFromTICL_R2p8.push_back(m_gsfEleFromTICLvarMap->find("HGCalElectronRvar_HGCalElectronRvarProducer")[iEle]);
            //
            //treeOutput->v_gsfEleFromTICL_sigma2uu.push_back(m_gsfEleFromTICLvarMap->find("HGCalElectronPCA_HGCalElectronPCAProducerSigma2UU")[iEle]);
            //treeOutput->v_gsfEleFromTICL_sigma2vv.push_back(m_gsfEleFromTICLvarMap->find("HGCalElectronPCA_HGCalElectronPCAProducerSigma2VV")[iEle]);
            //treeOutput->v_gsfEleFromTICL_sigma2ww.push_back(m_gsfEleFromTICLvarMap->find("HGCalElectronPCA_HGCalElectronPCAProducerSigma2WW")[iEle]);
            
            
            //std::vector <DetId> v_SC_seedId = gsfEle.superCluster()->getSeedIds();
            //
            //printf("SC_nCluster %d, SC_nSeed %d \n", (int) gsfEle.superCluster()->clusters().size(), (int) v_SC_seedId.size());
            //printf("SC_seedIds: ");
            //
            //for(int iSeed = 0; iSeed < (int) v_SC_seedId.size(); iSeed++)
            //{
            //    printf("[%u] ", v_SC_seedId.at(iSeed).rawId());
            //}
            //
            //printf("\n");
            
            //edm::PtrVector <reco::CaloCluster> v_superClus_clus = gsfEle.superCluster()->clusters();
            //
            //printf("SC_clusterIds: ");
            //
            //for(int iCluster = 0; iCluster < (int) v_superClus_clus.size(); iCluster++)
            //{
            //    const reco::CaloCluster *cluster = v_superClus_clus[iCluster].get();
            //    
            //    printf("[%u] ", cluster->seed().rawId());
            //}
            //
            //printf("\n");
        }
    }
    
    
    
    ////////////////////////////////////////////////////////////////
    //////////////////// Photons from MultiClus ////////////////////
    ////////////////////////////////////////////////////////////////
    edm::Handle <std::vector <reco::Photon> > v_phoFromMultiClus;
    
    try
    {
        iEvent.getByToken(tok_phoFromMultiClus, v_phoFromMultiClus);
    }
    
    catch(...)
    {
    }
    
    if(v_phoFromMultiClus.isValid())
    {
        int nPhoFromMultiClus = v_phoFromMultiClus->size();
        
        std::vector <CLHEP::HepLorentzVector> v_phoFromMultiClus_4mom;
        
        
        for(int iPho = 0; iPho < nPhoFromMultiClus; iPho++)
        {
            reco::Photon pho = v_phoFromMultiClus->at(iPho);
            
            CLHEP::HepLorentzVector phoFromMultiClus_4mom;
            phoFromMultiClus_4mom.setT(pho.energy());
            phoFromMultiClus_4mom.setX(pho.px());
            phoFromMultiClus_4mom.setY(pho.py());
            phoFromMultiClus_4mom.setZ(pho.pz());
            
            v_phoFromMultiClus_4mom.push_back(phoFromMultiClus_4mom);
        }
        
        
        // MultiClus-pho gen-matching
        TMatrixD mat_phoFromMultiClus_genPh_deltaR;
        
        std::vector <int> v_phoFromMultiClus_matchedGenPh_idx;
        
        std::vector <double> v_phoFromMultiClus_genPh_minDeltaR = Common::getMinDeltaR(
            v_phoFromMultiClus_4mom,
            v_genPh_4mom,
            mat_phoFromMultiClus_genPh_deltaR,
            v_phoFromMultiClus_matchedGenPh_idx
        );
        
        
        for(int iPho = 0; iPho < nPhoFromMultiClus; iPho++)
        {
            reco::Photon pho = v_phoFromMultiClus->at(iPho);
            CLHEP::HepLorentzVector phoFromMultiClus_4mom = v_phoFromMultiClus_4mom.at(iPho);
            
            
            if(pho.pt() < el_minPt || fabs(pho.eta()) < HGCal_minEta || fabs(pho.eta()) > HGCal_maxEta)
            {
                continue;
            }
            
            
            double matchedGenPh_deltaR = v_phoFromMultiClus_genPh_minDeltaR.at(iPho);
            
            if(matchedGenPh_deltaR > TICLphoGenMatchDR)
            {
                continue;
            }
            
            printf(
                "[%llu] "
                
                "phoFromMultiClus %d/%d: "
                "E %0.4f, "
                "pT %0.2f, "
                "eta %+0.2f, "
                
                "\n",
                
                eventNumber,
                
                iPho+1, nPhoFromMultiClus,
                pho.energy(),
                pho.pt(),
                pho.eta()
            );
            
            int matchedGenPh_idx = v_phoFromMultiClus_matchedGenPh_idx.at(iPho);
            
            treeOutput->v_phoFromMultiClus_genPh_minDeltaR.push_back(matchedGenPh_deltaR);
            treeOutput->v_phoFromMultiClus_nearestGenPh_idx.push_back(matchedGenPh_idx);
            
            double matchedGenPh_energy = -99;
            double matchedGenPh_pT = -99;
            double matchedGenPh_eta = -99;
            double matchedGenPh_phi = -99;
            
            if(matchedGenPh_idx >= 0)
            {
                matchedGenPh_energy = v_genPh_4mom.at(matchedGenPh_idx).e();
                matchedGenPh_pT = v_genPh_4mom.at(matchedGenPh_idx).perp();
                matchedGenPh_eta = v_genPh_4mom.at(matchedGenPh_idx).eta();
                matchedGenPh_phi = v_genPh_4mom.at(matchedGenPh_idx).phi();
            }
            
            treeOutput->v_phoFromMultiClus_matchedGenPh_E.push_back(matchedGenPh_energy);
            treeOutput->v_phoFromMultiClus_matchedGenPh_pT.push_back(matchedGenPh_pT);
            treeOutput->v_phoFromMultiClus_matchedGenPh_eta.push_back(matchedGenPh_eta);
            treeOutput->v_phoFromMultiClus_matchedGenPh_phi.push_back(matchedGenPh_phi);
            
            
            treeOutput->v_phoFromMultiClus_E.push_back(pho.energy());
            treeOutput->v_phoFromMultiClus_px.push_back(pho.px());
            treeOutput->v_phoFromMultiClus_py.push_back(pho.py());
            treeOutput->v_phoFromMultiClus_pz.push_back(pho.pz());
            
            treeOutput->v_phoFromMultiClus_pT.push_back(pho.pt());
            treeOutput->v_phoFromMultiClus_eta.push_back(pho.eta());
            treeOutput->v_phoFromMultiClus_phi.push_back(pho.phi());
            
            treeOutput->v_phoFromMultiClus_ET.push_back(pho.et());
            
            treeOutput->phoFromMultiClus_n++;
        }
    }
    
    
    
    ///////////////////////////////////////////////////////////
    //////////////////// Photons from TICL ////////////////////
    ///////////////////////////////////////////////////////////
    edm::Handle <std::vector <reco::Photon> > v_phoFromTICL;
    
    try
    {
        iEvent.getByToken(tok_phoFromTICL, v_phoFromTICL);
    }
    
    catch(...)
    {
    }
    
    if(v_phoFromTICL.isValid())
    {
        int nPhoFromTICL = v_phoFromTICL->size();
        
        std::vector <CLHEP::HepLorentzVector> v_phoFromTICL_4mom;
        
        
        for(int iPho = 0; iPho < nPhoFromTICL; iPho++)
        {
            reco::Photon pho = v_phoFromTICL->at(iPho);
            
            CLHEP::HepLorentzVector phoFromTICL_4mom;
            phoFromTICL_4mom.setT(pho.energy());
            phoFromTICL_4mom.setX(pho.px());
            phoFromTICL_4mom.setY(pho.py());
            phoFromTICL_4mom.setZ(pho.pz());
            
            v_phoFromTICL_4mom.push_back(phoFromTICL_4mom);
        }
        
        
        // TICL-pho gen-matching
        TMatrixD mat_phoFromTICL_genPh_deltaR;
        
        std::vector <int> v_phoFromTICL_matchedGenPh_idx;
        
        std::vector <double> v_phoFromTICL_genPh_minDeltaR = Common::getMinDeltaR(
            v_phoFromTICL_4mom,
            v_genPh_4mom,
            mat_phoFromTICL_genPh_deltaR,
            v_phoFromTICL_matchedGenPh_idx
        );
        
        
        for(int iPho = 0; iPho < nPhoFromTICL; iPho++)
        {
            reco::Photon pho = v_phoFromTICL->at(iPho);
            CLHEP::HepLorentzVector phoFromTICL_4mom = v_phoFromTICL_4mom.at(iPho);
            
            
            if(pho.pt() < el_minPt || fabs(pho.eta()) < HGCal_minEta || fabs(pho.eta()) > HGCal_maxEta)
            {
                continue;
            }
            
            
            double matchedGenPh_deltaR = v_phoFromTICL_genPh_minDeltaR.at(iPho);
            
            if(matchedGenPh_deltaR > TICLphoGenMatchDR)
            {
                continue;
            }
            
            printf(
                "[%llu] "
                
                "phoFromTICL %d/%d: "
                "E %0.4f, "
                "pT %0.2f, "
                "eta %+0.2f, "
                "superClus E %0.2f, "
                
                "\n",
                
                eventNumber,
                
                iPho+1, nPhoFromTICL,
                pho.energy(),
                pho.pt(),
                pho.eta(),
                pho.superCluster()->energy()
            );
            
            int matchedGenPh_idx = v_phoFromTICL_matchedGenPh_idx.at(iPho);
            
            treeOutput->v_phoFromTICL_genPh_minDeltaR.push_back(matchedGenPh_deltaR);
            treeOutput->v_phoFromTICL_nearestGenPh_idx.push_back(matchedGenPh_idx);
            
            double matchedGenPh_energy = -99;
            double matchedGenPh_pT = -99;
            double matchedGenPh_eta = -99;
            double matchedGenPh_phi = -99;
            
            if(matchedGenPh_idx >= 0)
            {
                matchedGenPh_energy = v_genPh_4mom.at(matchedGenPh_idx).e();
                matchedGenPh_pT = v_genPh_4mom.at(matchedGenPh_idx).perp();
                matchedGenPh_eta = v_genPh_4mom.at(matchedGenPh_idx).eta();
                matchedGenPh_phi = v_genPh_4mom.at(matchedGenPh_idx).phi();
            }
            
            treeOutput->v_phoFromTICL_matchedGenPh_E.push_back(matchedGenPh_energy);
            treeOutput->v_phoFromTICL_matchedGenPh_pT.push_back(matchedGenPh_pT);
            treeOutput->v_phoFromTICL_matchedGenPh_eta.push_back(matchedGenPh_eta);
            treeOutput->v_phoFromTICL_matchedGenPh_phi.push_back(matchedGenPh_phi);
            
            
            treeOutput->v_phoFromTICL_E.push_back(pho.energy());
            treeOutput->v_phoFromTICL_px.push_back(pho.px());
            treeOutput->v_phoFromTICL_py.push_back(pho.py());
            treeOutput->v_phoFromTICL_pz.push_back(pho.pz());
            
            treeOutput->v_phoFromTICL_pT.push_back(pho.pt());
            treeOutput->v_phoFromTICL_eta.push_back(pho.eta());
            treeOutput->v_phoFromTICL_phi.push_back(pho.phi());
            
            treeOutput->v_phoFromTICL_ET.push_back(pho.et());
            
            treeOutput->phoFromTICL_n++;
        }
    }
    
    
    // Fill tree
    treeOutput->fill();
    
    //#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
    //ESHandle<SetupData> pSetup;
    //iSetup.get<SetupRecord>().get(pSetup);
    //#endif
    
    printf("\n\n");
    
    fflush(stdout);
    fflush(stderr);
}


double TreeMaker::getDeltaPhi(double phi1, double phi2)
{
    double deltaPhi = phi1 - phi2;
    
    deltaPhi = (deltaPhi > +M_PI)? (deltaPhi - 2*M_PI): deltaPhi;
    deltaPhi = (deltaPhi < -M_PI)? (deltaPhi + 2*M_PI): deltaPhi;
    
    //deltaPhi = (deltaPhi > +M_PI)? (2*M_PI - deltaPhi): deltaPhi;
    //deltaPhi = (deltaPhi < -M_PI)? (2*M_PI + deltaPhi): deltaPhi;
    
    return deltaPhi;
}


// ------------ method called once each job just before starting event loop  ------------
void
TreeMaker::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
TreeMaker::endJob()
{
    
    printf("minLayer = %d, maxLayer = %d \n", minLayer, maxLayer);
    
    
    fflush(stdout);
    fflush(stderr);
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TreeMaker::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
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
DEFINE_FWK_MODULE(TreeMaker);
