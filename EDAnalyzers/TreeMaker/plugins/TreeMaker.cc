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
# include <memory>

// user include files




# include "CommonTools/UtilAlgos/interface/TFileService.h"
# include "DataFormats/CaloTowers/interface/CaloTowerDefs.h"
# include "DataFormats/Common/interface/TriggerResults.h"
# include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
# include "DataFormats/FWLite/interface/ESHandle.h"
# include "DataFormats/ForwardDetId/interface/HGCEEDetId.h"
# include "DataFormats/ForwardDetId/interface/HGCalDetId.h"
# include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
# include "DataFormats/HGCRecHit/interface/HGCRecHit.h"
# include "DataFormats/HGCalReco/interface/Trackster.h"
# include "DataFormats/HLTReco/interface/TriggerObject.h"
# include "DataFormats/HepMCCandidate/interface/GenParticle.h"
# include "DataFormats/JetReco/interface/GenJet.h"
# include "DataFormats/JetReco/interface/PFJet.h"
# include "DataFormats/Math/interface/LorentzVector.h"
# include "DataFormats/ParticleFlowReco/interface/HGCalMultiCluster.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
# include "DataFormats/PatCandidates/interface/Electron.h"
# include "DataFormats/PatCandidates/interface/Jet.h"
# include "DataFormats/PatCandidates/interface/MET.h"
# include "DataFormats/PatCandidates/interface/Muon.h"
# include "DataFormats/PatCandidates/interface/PackedCandidate.h"
# include "DataFormats/PatCandidates/interface/Photon.h"
# include "DataFormats/PatCandidates/interface/Tau.h"
# include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
# include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
# include "DataFormats/TrackReco/interface/Track.h"
# include "DataFormats/TrackReco/interface/TrackFwd.h"
# include "DataFormats/VertexReco/interface/Vertex.h"
# include "FWCore/Common/interface/TriggerNames.h"
# include "FWCore/Framework/interface/ESHandle.h"
# include "FWCore/Framework/interface/Event.h"
# include "FWCore/Framework/interface/Frameworkfwd.h"
# include "FWCore/Framework/interface/LuminosityBlock.h"
# include "FWCore/Framework/interface/MakerMacros.h"
# include "FWCore/Framework/interface/one/EDAnalyzer.h"
# include "FWCore/ParameterSet/interface/FileInPath.h"
# include "FWCore/ParameterSet/interface/ParameterSet.h"
# include "FWCore/ServiceRegistry/interface/Service.h"
# include "FWCore/Utilities/interface/InputTag.h"
# include "Geometry/CaloTopology/interface/HGCalTopology.h"
# include "Geometry/Records/interface/IdealGeometryRecord.h"
# include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
# include "HLTrigger/HLTcore/interface/HLTPrescaleProvider.h"
# include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
# include "JetMETCorrections/Objects/interface/JetCorrector.h"
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "SimDataFormats/CaloAnalysis/interface/CaloParticle.h"
# include "SimDataFormats/CaloAnalysis/interface/SimCluster.h"
# include "SimDataFormats/CaloHit/interface/PCaloHit.h"
# include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
# include "SimDataFormats/GeneratorProducts/interface/GenLumiInfoHeader.h"
# include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
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



double minEta = 0.0;
double maxEta = 1.479;

double el_minPt = 0; //15;
double el_maxPt = 99999; //30;

double ph_minPt = 0; //15;
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
    
    hgcal::RecHitTools recHitTools;
    
    TreeOutputInfo::TreeOutput *treeOutput;
    
    
    // My stuff //
    bool debug;
    bool isGunSample;
    
    double eleGenMatchDR;
    double phoGenMatchDR;
    
    
    // Gen particles //
    edm::EDGetTokenT <std::vector <reco::GenParticle> > tok_genParticle;
    edm::EDGetTokenT <std::vector <reco::GenJet> > tok_genJet;
    
    
    // Primary vertices
    edm::EDGetTokenT <vector <reco::Vertex> > tok_primaryVertex;
    edm::EDGetTokenT <vector <reco::Vertex> > tok_primaryVertex4D;
    
    
    // Pileup //
    edm::EDGetTokenT <std::vector <PileupSummaryInfo> > tok_pileup;
    
    
    // Rho //
    edm::EDGetTokenT <double> tok_rho;
    
    
    // Slimmed electrons //
    edm::EDGetTokenT <std::vector <pat::Electron> > tok_slimmedEle;
    //
    //edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17IsoV2Values;
    //edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
    //
    //edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
    //edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
    
    
    // Slimmed photons //
    edm::EDGetTokenT <std::vector <pat::Photon> > tok_slimmedPho;
    edm::EDGetTokenT <std::vector <double> > tok_photonPhaseIImvaIdEB;
    
    
    // PF candidates //
    edm::EDGetTokenT <std::vector <pat::PackedCandidate> > tok_pfCandidate;
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
    
    
    //now do what ever initialization is needed
    
    treeOutput = new TreeOutputInfo::TreeOutput("tree", fs);
    
    
    // My stuff //
    debug = iConfig.getParameter <bool>("debug");
    isGunSample = iConfig.getParameter <bool>("isGunSample");
    
    eleGenMatchDR = iConfig.getParameter <double>("eleGenMatchDR");
    phoGenMatchDR = iConfig.getParameter <double>("phoGenMatchDR");
    
    
    // Gen particles //
    tok_genParticle = consumes <std::vector <reco::GenParticle> >(iConfig.getParameter <edm::InputTag>("label_genParticle"));
    
    
    // Gen jets //
    tok_genJet = consumes <std::vector <reco::GenJet> >(iConfig.getParameter <edm::InputTag>("label_genJet"));
    
    
    // Primary vertices
    tok_primaryVertex = consumes <std::vector <reco::Vertex> >(iConfig.getParameter <edm::InputTag>("label_primaryVertex"));
    tok_primaryVertex4D = consumes <std::vector <reco::Vertex> >(iConfig.getParameter <edm::InputTag>("label_primaryVertex4D"));
    
    
    // Pileup //
    tok_pileup = consumes <std::vector <PileupSummaryInfo> >(iConfig.getParameter <edm::InputTag>("label_pileup"));
    
    
    // Rho //
    tok_rho = consumes <double>(iConfig.getParameter <edm::InputTag>("label_rho"));
    
    
    // Slimmed electrons //
    tok_slimmedEle = consumes <std::vector <pat::Electron> >(iConfig.getParameter <edm::InputTag>("label_slimmedEle"));
    
    //tok_ElectronMVAEstimatorRun2Fall17IsoV2Values = consumes <edm::ValueMap <float> >(iConfig.getParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17IsoV2Values"));
    //tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues = consumes <edm::ValueMap <float> >(iConfig.getParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17IsoV2RawValues"));
    //
    //tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values = consumes <edm::ValueMap <float> >(iConfig.getParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17NoIsoV2Values"));
    //tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues = consumes <edm::ValueMap <float> >(iConfig.getParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"));
    
    
    // Slimmed photons //
    tok_slimmedPho = consumes <std::vector <pat::Photon> >(iConfig.getParameter <edm::InputTag>("label_slimmedPho"));
    
    tok_photonPhaseIImvaIdEB = consumes <std::vector <double> >(iConfig.getParameter <edm::InputTag>("label_photonPhaseIImvaIdEB"));
    
    
    // PF candidates  //
    tok_pfCandidate = consumes <std::vector <pat::PackedCandidate> >(iConfig.getParameter <edm::InputTag>("label_pfCandidate"));
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
    
    
    //////////////////// Primary vertices ////////////////////
    edm::Handle <std::vector <reco::Vertex> > v_primaryVertex;
    iEvent.getByToken(tok_primaryVertex, v_primaryVertex);
    
    int pmVtx_idx = -1;
    reco::Vertex pmVtx;
    
    int nGoodVertex = 0;
    
    for(int iVtx = 0; iVtx < (int) v_primaryVertex->size(); iVtx++)
    {
        reco::Vertex vertex = v_primaryVertex->at(iVtx);
        
        bool isGoodVertex = (
            !vertex.isFake() &&
            vertex.ndof() >= 4 //&&
            //fabs(vertex.z()) <= 24.0 &&
            //fabs(vertex.position().rho()) <= 2.0
        );
        
        nGoodVertex += (int) isGoodVertex;
        
        if(pmVtx_idx < 0)
        {
            pmVtx_idx = iVtx;
            pmVtx = vertex;
        }
    }
    
    if(nGoodVertex)
    {
        printf(
            "[%llu] "
            "PV found: idx %d, "
            "x %0.5e, y %0.5e, z %0.5e, "
            "\n",
            
            eventNumber,
            pmVtx_idx,
            pmVtx.x(), pmVtx.y(), pmVtx.z()
        );
    }
    
    
    edm::Handle <std::vector <reco::Vertex> > v_primaryVertex4D;
    iEvent.getByToken(tok_primaryVertex4D, v_primaryVertex4D);
    
    int pmVtx4D_idx = -1;
    reco::Vertex pmVtx4D;
    
    int nGoodVertex4D = 0;
    
    for(int iVtx = 0; iVtx < (int) v_primaryVertex4D->size(); iVtx++)
    {
        reco::Vertex vertex = v_primaryVertex4D->at(iVtx);
        
        bool isGoodVertex = (
            !vertex.isFake() &&
            vertex.ndof() >= 4 //&&
            //fabs(vertex.z()) <= 24.0 &&
            //fabs(vertex.position().rho()) <= 2.0
        );
        
        nGoodVertex4D += (int) isGoodVertex;
        
        if(pmVtx4D_idx < 0)
        {
            pmVtx4D_idx = iVtx;
            pmVtx4D = vertex;
        }
    }
    
    if(nGoodVertex4D)
    {
        printf(
            "[%llu] "
            "PV4D found: idx %d, "
            "x %0.5e, y %0.5e, z %0.5e, "
            "\n",
            
            eventNumber,
            pmVtx4D_idx,
            pmVtx4D.x(), pmVtx4D.y(), pmVtx4D.z()
        );
    }
    
    
    // At least one PV
    if(!nGoodVertex4D)
    {
        printf("Skipping event: no primary vertex found. \n");
        
        fflush(stdout);
        fflush(stderr);
        
        return;
    }
    
    treeOutput->PV_t = pmVtx4D.t();
    treeOutput->PV_tErr = pmVtx4D.tError();
    
    
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
                
                "Gen-ele found (%+d): "
                "E %0.2f, pT %0.2f, eta %+0.2f, pz %+0.2f, "
                
                //"\n\t"
                //"mother %d/%d: id %+d"
                
                "\n",
                
                eventNumber,
                
                pdgId, part.energy(), part.pt(), part.eta(), part.pz()
                
                //1, (int) part.numberOfMothers(), part.motherRef(0).get()->pdgId()
            );
            
            //if(fabs(part.eta()) > HGCal_minEta && fabs(part.eta()) < HGCal_maxEta && part.pt() > el_minPt && part.pt() < el_maxPt)
            if(part.pt() > el_minPt && part.pt() < el_maxPt)
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
        
        
        // Gen pho
        if(
            abs(pdgId) == 22 && (
                (isGunSample && status == 1) ||
                (!isGunSample && part.isHardProcess())
            )
        )
        {
            //printf("[%llu] Gen electron found: E %0.2f, pT %0.2f, eta %+0.2f \n", eventNumber, part.energy(), part.pt(), part.eta());
            
            printf(
                "[%llu] "
                
                "Gen-pho found (%+d): "
                "E %0.2f, pT %0.2f, eta %+0.2f, pz %+0.2f, "
                
                //"\n\t"
                //"mother %d/%d: id %+d"
                
                "\n",
                
                eventNumber,
                
                pdgId, part.energy(), part.pt(), part.eta(), part.pz()
                
                //1, (int) part.numberOfMothers(), part.motherRef(0).get()->pdgId()
            );
            
            if(part.pt() > ph_minPt && part.pt() < ph_maxPt)
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
    
    
    //if(!treeOutput->genEl_n)
    //{
    //    return;
    //}
    
    
    //////////////////// Gen jet ////////////////////
    edm::Handle <std::vector <reco::GenJet> > v_genJet;
    iEvent.getByToken(tok_genJet, v_genJet);
    
    //for(int iJet = 0; iJet < (int) v_genJet->size(); iJet++)
    //{
    //    reco::GenJet jet = v_genJet->at(iJet);
    //    
    //    printf(
    //        "GenJet %02d/%02d: "
    //        "%0.2f, %+0.2f, "
    //        "\n",
    //        
    //        iJet+1, (int) v_genJet->size(),
    //        jet.pt(), jet.eta()
    //    );
    //    
    //    //std::vector <const reco::GenParticle*> v_consti = jet.getGenConstituents();
    //    
    //    for(int iConsti = 0; iConsti < (int) jet.getGenConstituents().size(); iConsti++)
    //    {
    //        //const reco::GenParticle *consti = (const reco::GenParticle) v_consti.at(iConsti);
    //        
    //        printf(
    //            "\tconsti %02d/%02d: "
    //            "id %+d, "
    //            "%0.2f, %+0.2f, "
    //            "\n",
    //            
    //            iConsti+1, (int) jet.getGenConstituents().size(),
    //            jet.getGenConstituents().at(iConsti)->pdgId(),
    //            jet.getGenConstituents().at(iConsti)->pt(), jet.getGenConstituents().at(iConsti)->eta()
    //        );
    //    }
    //}
    
    
    
    //////////////////// Pileup ////////////////////
    edm::Handle <std::vector <PileupSummaryInfo> > pileUps_reco;
    iEvent.getByToken(tok_pileup, pileUps_reco);
    treeOutput->pileup_n = Common::getPileup(pileUps_reco);
    
    treeOutput->pileupDensity = Common::getPileupDesity(pileUps_reco, &pmVtx4D);
    
    for(int iPileUp = (int) pileUps_reco->size() - 1; iPileUp >= 0; iPileUp--)
    {
        PileupSummaryInfo pileUpInfo = (*pileUps_reco)[iPileUp];
        
        int bunchCrossingNumber = pileUpInfo.getBunchCrossing();
        
        // In-time bunch-crossing pile-up
        if(bunchCrossingNumber != 0)
        {
            continue;
        }
        
        for (int iZ = 0; iZ < (int) pileUpInfo.getPU_zpositions().size(); iZ++)
        {
            double PU_z = pileUpInfo.getPU_zpositions().at(iZ);
            
            treeOutput->PU_n++;
            treeOutput->v_PU_z.push_back(PU_z);
        }
    }
    
    
    
    //////////////////// Rho ////////////////////
    edm::Handle <double> handle_rho;
    iEvent.getByToken(tok_rho, handle_rho);
    double rho = *handle_rho;
    
    treeOutput->rho = rho;
    
    
    // //////////////////// PF candidates ////////////////////
    //edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate;
    //iEvent.getByToken(tok_pfCandidate, v_pfCandidate);
    //
    //int nPFcand = v_pfCandidate->size();
    //
    //std::vector <int> v_pfCand_ETsortedIdx;
    //std::map <const pat::PackedCandidate*, int> m_pfCand_idx;
    //
    //for(int iCand = 0; iCand < (int) nPFcand; iCand++)
    //{
    //    const pat::PackedCandidate *cand = &v_pfCandidate->at(iCand);
    //    
    //    v_pfCand_ETsortedIdx.push_back(iCand);
    //    
    //    m_pfCand_idx[cand] = iCand;
    //    
    //    //if(iCand < 10)
    //    //{
    //    //    printf(
    //    //        "PF cand %d/%d: "
    //    //        //"time %0.3f, timeErr %0.3f, "
    //    //        "ID %+d, "
    //    //        "E %0.3f, ET %0.3f, pt %0.3f, "
    //    //        "charge %+d, "
    //    //        //"caloFrac %0.3f, hcalFrac %0.3f, "
    //    //        "dz %0.2e, dz(%d) %0.2e, dzAssociatedPV %0.2e, "
    //    //        "\n",
    //    //        
    //    //        iCand+1, nPFcand,
    //    //        cand->pdgId(),
    //    //        cand->energy(), cand->et(), cand->pt(),
    //    //        cand->charge(),
    //    //        //cand->caloFraction(), cand->hcalFraction()
    //    //        cand->dz(), pmVtx_idx, cand->dz(pmVtx_idx), cand->dzAssociatedPV()
    //    //    );
    //    //}
    //}
    //
    //std::sort(
    //    v_pfCand_ETsortedIdx.begin(), v_pfCand_ETsortedIdx.end(),
    //    [&](int iCand1, int iCand2)
    //    {
    //        return (
    //            (&v_pfCandidate->at(iCand1))->et() > (&v_pfCandidate->at(iCand2))->et()
    //        );
    //    }
    //);
    
    
    //////////////////// Slimmed electrons ////////////////////
    edm::Handle <std::vector <pat::Electron> > v_slimmedEle;
    iEvent.getByToken(tok_slimmedEle, v_slimmedEle);
    
    //edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17IsoV2Values;
    //iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17IsoV2Values, ElectronMVAEstimatorRun2Fall17IsoV2Values);
    //
    //edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
    //iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues, ElectronMVAEstimatorRun2Fall17IsoV2RawValues);
    //
    //edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
    //iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values, ElectronMVAEstimatorRun2Fall17NoIsoV2Values);
    //
    //edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
    //iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues, ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues);
    
    int nSlimmedEle = v_slimmedEle->size();
    
    std::map <reco::SuperClusterRef, int> m_gsfEle_superClus;
    
    std::vector <CLHEP::HepLorentzVector> v_slimmedEle_4mom;
    
    
    for(int iEle = 0; iEle < nSlimmedEle; iEle++)
    {
        pat::Electron ele = v_slimmedEle->at(iEle);
        
        CLHEP::HepLorentzVector slimmedEle_4mom;
        slimmedEle_4mom.setT(ele.energy());
        slimmedEle_4mom.setX(ele.px());
        slimmedEle_4mom.setY(ele.py());
        slimmedEle_4mom.setZ(ele.pz());
        
        v_slimmedEle_4mom.push_back(slimmedEle_4mom);
    }
    
    
    // Electron gen-matching
    TMatrixD mat_slimmedEle_genEl_deltaR;
    
    std::vector <int> v_slimmedEle_matchedGenEl_index;
    
    std::vector <double> v_slimmedEle_genEl_minDeltaR = Common::getMinDeltaR(
        v_slimmedEle_4mom,
        v_genEl_4mom,
        mat_slimmedEle_genEl_deltaR,
        v_slimmedEle_matchedGenEl_index
    );
    
    for(int iEle = 0; iEle < (int) v_slimmedEle_genEl_minDeltaR.size(); iEle++)
    {
        double deltaR = v_slimmedEle_genEl_minDeltaR.at(iEle);
        
        if(deltaR > eleGenMatchDR)
        {
            continue;
        }
        
        int index = v_slimmedEle_matchedGenEl_index.at(iEle);
        
        treeOutput->v_slimmedEle_genEl_minDeltaR.push_back(deltaR);
        treeOutput->v_slimmedEle_nearestGenEl_idx.push_back(index);
        
        double energy = -99;
        double pT = -99;
        double eta = -99;
        double phi = -99;
        
        if(index >= 0)
        {
            energy = v_genEl_4mom.at(index).e();
            pT = v_genEl_4mom.at(index).perp();
            eta = v_genEl_4mom.at(index).eta();
            phi = v_genEl_4mom.at(index).phi();
        }
        
        treeOutput->v_slimmedEle_matchedGenEl_E.push_back(energy);
        treeOutput->v_slimmedEle_matchedGenEl_pT.push_back(pT);
        treeOutput->v_slimmedEle_matchedGenEl_eta.push_back(eta);
        treeOutput->v_slimmedEle_matchedGenEl_phi.push_back(phi);
    }
    
    
    for(int iEle = 0; iEle < nSlimmedEle; iEle++)
    {
        if(v_slimmedEle_genEl_minDeltaR.at(iEle) > eleGenMatchDR)
        {
            continue;
        }
        
        pat::Electron ele = v_slimmedEle->at(iEle);
        
        edm::Ptr <pat::Electron> ele_ptr(v_slimmedEle, iEle);
        
        CLHEP::HepLorentzVector slimmedEle_4mom = v_slimmedEle_4mom.at(iEle);
        
        
        treeOutput->v_slimmedEle_E.push_back(ele.energy());
        treeOutput->v_slimmedEle_px.push_back(ele.px());
        treeOutput->v_slimmedEle_py.push_back(ele.py());
        treeOutput->v_slimmedEle_pz.push_back(ele.pz());
        
        treeOutput->v_slimmedEle_pT.push_back(ele.pt());
        treeOutput->v_slimmedEle_eta.push_back(ele.eta());
        treeOutput->v_slimmedEle_phi.push_back(ele.phi());
        
        treeOutput->v_slimmedEle_ET.push_back(ele.et());
        
        //treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values.push_back((*ElectronMVAEstimatorRun2Fall17IsoV2Values)[ele_ptr]);
        //treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues.push_back((*ElectronMVAEstimatorRun2Fall17IsoV2RawValues)[ele_ptr]);
        //
        //treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values.push_back((*ElectronMVAEstimatorRun2Fall17NoIsoV2Values)[ele_ptr]);
        //treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues.push_back((*ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues)[ele_ptr]);
        
        treeOutput->v_slimmedEle_idx.push_back(treeOutput->slimmedEle_n);
        treeOutput->slimmedEle_n++;
        
        treeOutput->v_slimmedEle_chargedHadronIso.push_back(ele.pfIsolationVariables().sumChargedHadronPt);
        
        
        edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele.associatedPackedPFCandidates();
        const reco::GenParticle *linkedGenPart = ele.genParticle();
        
        printf(
            "[%llu] "
            
            "slimmedEle %d/%d: "
            "E %0.2f, "
            "eta %+0.2f, "
            
            //"\n\t"
            //"genPart %d/%d: "
            //"id %+d, pT %0.2f, eta %0.2f, "
            
            //"IsoV2 (valueMap) %0.3f, IsoV2 %0.3f, "
            
            "\n",
            
            eventNumber,
            
            iEle+1, nSlimmedEle,
            ele.energy(),
            ele.eta()
            
            //1, (int) ele.genParticlesSize(),
            //linkedGenPart_pdgId, linkedGenPart_pT, linkedGenPart_eta
            
            //(*ElectronMVAEstimatorRun2Fall17IsoV2Values)[ele_ptr], ele.userFloat("ElectronMVAEstimatorRun2Fall17IsoV2Values")
        );
    }
    
    
    
    //////////////////// Slimmed photons ////////////////////
    edm::Handle <std::vector <pat::Photon> > v_slimmedPho;
    iEvent.getByToken(tok_slimmedPho, v_slimmedPho);
    
    edm::Handle <std::vector <double> > v_photonPhaseIImvaIdEB;
    iEvent.getByToken(tok_photonPhaseIImvaIdEB, v_photonPhaseIImvaIdEB);
    
    int nSlimmedPho = v_slimmedPho->size();
    
    std::map <reco::SuperClusterRef, int> m_gsfPho_superClus;
    
    std::vector <CLHEP::HepLorentzVector> v_slimmedPho_4mom;
    
    
    for(int iPho = 0; iPho < nSlimmedPho; iPho++)
    {
        pat::Photon ele = v_slimmedPho->at(iPho);
        
        CLHEP::HepLorentzVector slimmedPho_4mom;
        slimmedPho_4mom.setT(ele.energy());
        slimmedPho_4mom.setX(ele.px());
        slimmedPho_4mom.setY(ele.py());
        slimmedPho_4mom.setZ(ele.pz());
        
        v_slimmedPho_4mom.push_back(slimmedPho_4mom);
    }
    
    
    // Photon gen-matching
    TMatrixD mat_slimmedPho_genPh_deltaR;
    
    std::vector <int> v_slimmedPho_matchedGenPh_index;
    
    std::vector <double> v_slimmedPho_genPh_minDeltaR = Common::getMinDeltaR(
        v_slimmedPho_4mom,
        v_genPh_4mom,
        mat_slimmedPho_genPh_deltaR,
        v_slimmedPho_matchedGenPh_index
    );
    
    for(int iPho = 0; iPho < (int) v_slimmedPho_genPh_minDeltaR.size(); iPho++)
    {
        double deltaR = v_slimmedPho_genPh_minDeltaR.at(iPho);
        
        if(deltaR > phoGenMatchDR)
        {
            continue;
        }
        
        int index = v_slimmedPho_matchedGenPh_index.at(iPho);
        
        treeOutput->v_slimmedPho_genPh_minDeltaR.push_back(deltaR);
        treeOutput->v_slimmedPho_nearestGenPh_idx.push_back(index);
        
        double energy = -99;
        double pT = -99;
        double eta = -99;
        double phi = -99;
        
        if(index >= 0)
        {
            energy = v_genPh_4mom.at(index).e();
            pT = v_genPh_4mom.at(index).perp();
            eta = v_genPh_4mom.at(index).eta();
            phi = v_genPh_4mom.at(index).phi();
        }
        
        treeOutput->v_slimmedPho_matchedGenPh_E.push_back(energy);
        treeOutput->v_slimmedPho_matchedGenPh_pT.push_back(pT);
        treeOutput->v_slimmedPho_matchedGenPh_eta.push_back(eta);
        treeOutput->v_slimmedPho_matchedGenPh_phi.push_back(phi);
    }
    
    
    for(int iPho = 0; iPho < nSlimmedPho; iPho++)
    {
        if(v_slimmedPho_genPh_minDeltaR.at(iPho) > phoGenMatchDR)
        {
            continue;
        }
        
        pat::Photon pho = v_slimmedPho->at(iPho);
        
        edm::Ptr <pat::Photon> pho_ptr(v_slimmedPho, iPho);
        
        CLHEP::HepLorentzVector slimmedPho_4mom = v_slimmedPho_4mom.at(iPho);
        
        
        treeOutput->v_slimmedPho_E.push_back(pho.energy());
        treeOutput->v_slimmedPho_px.push_back(pho.px());
        treeOutput->v_slimmedPho_py.push_back(pho.py());
        treeOutput->v_slimmedPho_pz.push_back(pho.pz());
        
        treeOutput->v_slimmedPho_pT.push_back(pho.pt());
        treeOutput->v_slimmedPho_eta.push_back(pho.eta());
        treeOutput->v_slimmedPho_phi.push_back(pho.phi());
        
        treeOutput->v_slimmedPho_ET.push_back(pho.et());
        
        treeOutput->v_slimmedPho_idx.push_back(treeOutput->slimmedPho_n);
        treeOutput->slimmedPho_n++;
        
        treeOutput->v_slimmedPho_chargedHadronIso.push_back(pho.getPflowIsolationVariables().chargedHadronIso);
        treeOutput->v_slimmedPho_neutralHadronIso.push_back(pho.getPflowIsolationVariables().neutralHadronIso);
        treeOutput->v_slimmedPho_photonIso.push_back(pho.getPflowIsolationVariables().photonIso);
        
        
        const reco::GenParticle *linkedGenPart = pho.genParticle();
        
        int linkedGenPart_pdgId = 0;
        double linkedGenPart_pT = -99;
        double linkedGenPart_eta = -99;
        
        if(linkedGenPart)
        {
            linkedGenPart_pdgId = linkedGenPart->pdgId();
            
            linkedGenPart_pT = linkedGenPart->pt();
            linkedGenPart_eta = linkedGenPart->eta();
        }
        
        treeOutput->v_slimmedPho_linkedGenPart_pdgId.push_back(linkedGenPart_pdgId);
        
        printf(
            "[%llu] "
            
            "slimmedPho %d/%d: "
            "E %0.2f, "
            "pT %0.2f, eta %+0.2f, "
            "chHadIso %0.2f, "
            "pfIso.chHadIso %0.2f, "
            
            //"\n\t"
            //"genPart %d/%d: "
            "(linked gen id %+d, pT %0.2f, eta %0.2f), "
            
            "MVA %0.4f, "
            
            "\n",
            
            eventNumber,
            
            iPho+1, nSlimmedPho,
            pho.energy(),
            pho.pt(), pho.eta(),
            
            pho.chargedHadronIso(),
            pho.getPflowIsolationVariables().chargedHadronIso,
            
            //1, (int) pho.genParticlesSize(),
            linkedGenPart_pdgId, linkedGenPart_pT, linkedGenPart_eta,
            
            v_photonPhaseIImvaIdEB->at(iPho)
        );
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
