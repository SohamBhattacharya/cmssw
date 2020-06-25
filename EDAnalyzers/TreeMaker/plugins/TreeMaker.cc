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
    
    void fill_Ele_sigVar(
        TreeOutputInfo::TreeOutput::Ele_sigVarContent *sigVarContent,
        edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate,
        std::vector <int> *v_pfCand_ETsortedIdx,
        pat::Electron *ele,
        reco::Vertex *pmVtx4D
    );
    
    void fill_Ele_isoVar(
        TreeOutputInfo::TreeOutput::Ele_isoVarContent *isoVarContent,
        edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate,
        std::vector <int> *v_pfCand_ETsortedIdx,
        pat::Electron *ele,
        reco::Vertex *pmVtx4D,
        double ET_min = 0.0,
        double dR_max = 9999,
        double dz_max = 9999,
        double dtSigni_max = 9999,
        bool wrtVtx = true
    );
    
    
    hgcal::RecHitTools recHitTools;
    
    int minLayer;
    int maxLayer;
    
    
    TreeOutputInfo::TreeOutput *treeOutput;
    
    
    // My stuff //
    bool debug;
    bool isGunSample;
    
    double eleGenMatchDR;
    
    
    // Gen particles //
    edm::EDGetTokenT <std::vector <reco::GenParticle> > tok_genParticle;
    
    
    // Primary vertices
    edm::EDGetTokenT <vector <reco::Vertex> > tok_primaryVertex;
    edm::EDGetTokenT <vector <reco::Vertex> > tok_primaryVertex4D;
    
    
    // Pileup //
    edm::EDGetTokenT <std::vector <PileupSummaryInfo> > tok_pileup;
    
    
    // Rho //
    edm::EDGetTokenT <double> tok_rho;
    
    
    // Slimmed electrons //
    edm::EDGetTokenT <std::vector <pat::Electron> > tok_slimmedEle;
    
    edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17IsoV2Values;
    edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
    
    edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
    edm::EDGetTokenT <edm::ValueMap <float> > tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
    
    
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
    
    
    minLayer = +9999;
    maxLayer = -9999;
    
    
    //now do what ever initialization is needed
    
    treeOutput = new TreeOutputInfo::TreeOutput("tree", fs);
    
    treeOutput->init_Ele_sigVarContent("all");
    
    treeOutput->init_Ele_isoVarContent("dR0p3");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5");
    
    treeOutput->init_Ele_isoVarContent("dR0p3_dTsigniLt2");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt2");
    
    treeOutput->init_Ele_isoVarContent("dR0p3_dTsigniLt3");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt3");
    
    treeOutput->init_Ele_isoVarContent("dR0p3_dTsigniLt4");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt4");
    
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt5");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt6");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt10");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt20");
    treeOutput->init_Ele_isoVarContent("dR0p3_dzLt0p5_dTsigniLt30");
    
    
    // My stuff //
    debug = iConfig.getParameter <bool>("debug");
    isGunSample = iConfig.getParameter <bool>("isGunSample");
    
    eleGenMatchDR = iConfig.getParameter <double>("eleGenMatchDR");
    
    
    // Gen particles //
    tok_genParticle = consumes <std::vector <reco::GenParticle> >(iConfig.getUntrackedParameter <edm::InputTag>("label_genParticle"));
    
    
    // Primary vertices
    tok_primaryVertex = consumes <std::vector <reco::Vertex> >(iConfig.getUntrackedParameter <edm::InputTag>("label_primaryVertex"));
    tok_primaryVertex4D = consumes <std::vector <reco::Vertex> >(iConfig.getUntrackedParameter <edm::InputTag>("label_primaryVertex4D"));
    
    
    // Pileup //
    tok_pileup = consumes <std::vector <PileupSummaryInfo> >(iConfig.getUntrackedParameter <edm::InputTag>("label_pileup"));
    
    
    // Rho //
    tok_rho = consumes <double>(iConfig.getUntrackedParameter <edm::InputTag>("label_rho"));
    
    
    // Slimmed electrons //
    tok_slimmedEle = consumes <std::vector <pat::Electron> >(iConfig.getUntrackedParameter <edm::InputTag>("label_slimmedEle"));
    
    tok_ElectronMVAEstimatorRun2Fall17IsoV2Values = consumes <edm::ValueMap <float> >(iConfig.getUntrackedParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17IsoV2Values"));
    tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues = consumes <edm::ValueMap <float> >(iConfig.getUntrackedParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17IsoV2RawValues"));
    
    tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values = consumes <edm::ValueMap <float> >(iConfig.getUntrackedParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17NoIsoV2Values"));
    tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues = consumes <edm::ValueMap <float> >(iConfig.getUntrackedParameter <edm::InputTag>("label_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"));
    
    
    // PF candidates  //
    tok_pfCandidate = consumes <std::vector <pat::PackedCandidate> >(iConfig.getUntrackedParameter <edm::InputTag>("label_pfCandidate"));
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


void TreeMaker::fill_Ele_sigVar(
    TreeOutputInfo::TreeOutput::Ele_sigVarContent *sigVarContent,
    edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate,
    std::vector <int> *v_pfCand_ETsortedIdx,
    pat::Electron *ele,
    reco::Vertex *pmVtx4D
)
{
    edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele->associatedPackedPFCandidates();
    
    std::map <const pat::PackedCandidate*, int> m_elePFcand_idx;
    
    for(int iCand = 0; iCand < (int) elePFcandidates.size(); iCand++)
    {
        const pat::PackedCandidate *cand = elePFcandidates.at(iCand).get();
        
        m_elePFcand_idx[cand] = iCand;
        
        //int pfCand_idx = -1;
        //
        //if(m_pfCand_idx.find(cand) != m_pfCand_idx.end())
        //{
        //    pfCand_idx = m_pfCand_idx.at(cand);
        //}
        //
        //printf(
        //    "\t"
        //    "Ele PF cand %02d/%02d: "
        //    "PF idx %d/%d "
        //    //"time %0.4f, timeErr %0.4f"
        //    "E %0.4f, ET %0.4f, pt %0.4f"
        //    "\n",
        //    
        //    iCand+1, (int) elePFcandidates.size(),
        //    pfCand_idx+1, nPFcand,
        //    //cand->time(), cand->timeError()
        //    cand->energy(), cand->et(), cand->pt()
        //);
    }
    
    
    int nPFcand = v_pfCandidate->size();
    
    int nPFcand_isTimeValid = 0;
    int nPFcand_hasTrackDetails = 0;
    
    int sig_pfCand_n = 0;
    
    double sig_pfCand1_PV_dtSigni = -9;
    double sig_pfCand2_PV_dtSigni = -9;
    
    double sig_pfCand_PV_dtSigniMean = 0;
    double sig_pfCand_PV_dtSigniMean_ETwtd = 0;
    
    double sig_pfCand1_PV_dz = -9;
    double sig_pfCand2_PV_dz = -9;
    
    double sig_pfCand_PV_dzMean = 0;
    double sig_pfCand_PV_dzMean_ETwtd = 0;
    
    double ET_sum_isTimeValid = 0;
    double ET_sum_hasTrackDetails = 0;
    
    
    for(int iCand = 0; iCand < (int) nPFcand; iCand++)
    {
        const pat::PackedCandidate *cand = &v_pfCandidate->at(v_pfCand_ETsortedIdx->at(iCand));
        
        if(iCand < 10)
        {
            //printf(
            //    "PF cand %d/%d: "
            //    //"time %0.4f, timeErr %0.4f"
            //    "chg %+d, "
            //    "E %0.2f, ET %0.2f, pt %0.2f, "
            //    //"dz %0.2e, dz(%d) %0.2e, dzAssociatedPV %0.2e, "
            //    "pmVtx4D_z %0.2e, candVtx_z %0.2e "
            //    "\n",
            //    
            //    iCand+1, nPFcand,
            //    cand->charge(),
            //    cand->energy(), cand->et(), cand->pt(),
            //    //cand->dz(), pmVtx_idx, cand->dz(pmVtx_idx), cand->dzAssociatedPV(),
            //    pmVtx4D->z(), cand->vertex().z()
            //);
        }
        
        // Skip the iso candidates
        if(m_elePFcand_idx.find(cand) == m_elePFcand_idx.end())
        {
            continue;
        }
        
        
        sig_pfCand_n++;
        
        
        //
        bool isTimeValid = (cand->timeError() > 0 && pmVtx4D->tError() > 0);
        
        if(isTimeValid)
        {
            nPFcand_isTimeValid++;
            
            double dt = std::fabs(cand->time() - pmVtx4D->t());
            double dtSigni = dt / std::sqrt(cand->timeError()*cand->timeError() + pmVtx4D->tError()*pmVtx4D->tError());
            
            if(sig_pfCand1_PV_dtSigni < 0)
            {
                sig_pfCand1_PV_dtSigni = dtSigni;
            }
            
            else if(sig_pfCand2_PV_dtSigni < 0)
            {
                sig_pfCand2_PV_dtSigni = dtSigni;
            }
            
            sig_pfCand_PV_dtSigniMean += dtSigni;
            sig_pfCand_PV_dtSigniMean_ETwtd += dtSigni;
            
            ET_sum_isTimeValid += cand->et();
        }
        
        
        //
        if(cand->hasTrackDetails())
        {
            nPFcand_hasTrackDetails++;
            
            double dz = fabs(cand->dz());
            //double dzSigni = dz / cand->dzError();
            
            if(sig_pfCand1_PV_dz < 0)
            {
                sig_pfCand1_PV_dz = dz;
            }
            
            else if(sig_pfCand2_PV_dz < 0)
            {
                sig_pfCand2_PV_dz = dz;
            }
            
            sig_pfCand_PV_dzMean += dz;
            sig_pfCand_PV_dzMean_ETwtd += dz;
            
            ET_sum_hasTrackDetails += cand->et();
        }
    }
    
    
    if(nPFcand_isTimeValid)
    {
        sig_pfCand_PV_dtSigniMean /= (double) nPFcand_isTimeValid;
        
        sig_pfCand_PV_dtSigniMean_ETwtd /= ET_sum_isTimeValid;
    }
    
    if(nPFcand_hasTrackDetails)
    {
        sig_pfCand_PV_dzMean /= (double) nPFcand_hasTrackDetails;
        
        sig_pfCand_PV_dzMean_ETwtd /= ET_sum_hasTrackDetails;
    }
    
    
    //
    sigVarContent->v_slimmedEle_sig_pfCand_n.push_back(sig_pfCand_n);
    
    //
    sigVarContent->v_slimmedEle_sig_pfCand1_PV_dtSigni.push_back(sig_pfCand1_PV_dtSigni);
    sigVarContent->v_slimmedEle_sig_pfCand2_PV_dtSigni.push_back(sig_pfCand2_PV_dtSigni);
    
    sigVarContent->v_slimmedEle_sig_pfCand_PV_dtSigniMean.push_back(sig_pfCand_PV_dtSigniMean);
    sigVarContent->v_slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd.push_back(sig_pfCand_PV_dtSigniMean_ETwtd);
    
    //
    sigVarContent->v_slimmedEle_sig_pfCand1_PV_dz.push_back(sig_pfCand1_PV_dz);
    sigVarContent->v_slimmedEle_sig_pfCand2_PV_dz.push_back(sig_pfCand2_PV_dz);
    
    sigVarContent->v_slimmedEle_sig_pfCand_PV_dzMean.push_back(sig_pfCand_PV_dzMean);
    sigVarContent->v_slimmedEle_sig_pfCand_PV_dzMean_ETwtd.push_back(sig_pfCand_PV_dzMean_ETwtd);
}


void TreeMaker::fill_Ele_isoVar(
    TreeOutputInfo::TreeOutput::Ele_isoVarContent *isoVarContent,
    edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate,
    std::vector <int> *v_pfCand_ETsortedIdx,
    pat::Electron *ele,
    reco::Vertex *pmVtx4D,
    double ET_min,
    double dR_max,
    double dz_max,
    double dtSigni_max,
    bool wrtVtx
)
{
    edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele->associatedPackedPFCandidates();
    
    std::map <const pat::PackedCandidate*, int> m_elePFcand_idx;
    
    for(int iCand = 0; iCand < (int) elePFcandidates.size(); iCand++)
    {
        const pat::PackedCandidate *cand = elePFcandidates.at(iCand).get();
        
        m_elePFcand_idx[cand] = iCand;
        
        //int pfCand_idx = -1;
        //
        //if(m_pfCand_idx.find(cand) != m_pfCand_idx.end())
        //{
        //    pfCand_idx = m_pfCand_idx.at(cand);
        //}
        //
        //printf(
        //    "\t"
        //    "Ele PF cand %02d/%02d: "
        //    "PF idx %d/%d "
        //    //"time %0.4f, timeErr %0.4f"
        //    "E %0.4f, ET %0.4f, pt %0.4f"
        //    "\n",
        //    
        //    iCand+1, (int) elePFcandidates.size(),
        //    pfCand_idx+1, nPFcand,
        //    //cand->time(), cand->timeError()
        //    cand->energy(), cand->et(), cand->pt()
        //);
    }
    
    
    int nPFcand = v_pfCandidate->size();
    
    int nPFcand_isTimeValid = 0;
    int nPFcand_hasTrackDetails = 0;
    
    int iso_pfCand_n = 0;
    
    double iso_sumETratio = 0;
    double iso_sumETratio_charged = 0;
    double iso_sumETratio_neutral = 0;
    double iso_sumETratio_ecal = 0;
    double iso_sumETratio_hcal = 0;
    
    double iso_pfCand1_PV_dtSigni = -9;
    double iso_pfCand2_PV_dtSigni = -9;
    
    double iso_pfCand_PV_dtSigniMean = 0;
    double iso_pfCand_PV_dtSigniMean_ETwtd = 0;
    
    double iso_pfCand1_PV_dz = -9;
    double iso_pfCand2_PV_dz = -9;
    
    double iso_pfCand_PV_dzMean = 0;
    double iso_pfCand_PV_dzMean_ETwtd = 0;
    
    double ET_sum_isTimeValid = 0;
    double ET_sum_hasTrackDetails = 0;
    
    
    for(int iCand = 0; iCand < (int) nPFcand; iCand++)
    {
        const pat::PackedCandidate *cand = &v_pfCandidate->at(v_pfCand_ETsortedIdx->at(iCand));
        
        if(cand->et() < ET_min)
        {
            continue;
        }
        
        if(iCand < 10)
        {
            //printf(
            //    "PF cand %d/%d: "
            //    //"time %0.4f, timeErr %0.4f"
            //    "chg %+d, "
            //    "E %0.2f, ET %0.2f, pt %0.2f, "
            //    //"dz %0.2e, dz(%d) %0.2e, dzAssociatedPV %0.2e, "
            //    "ele_dz-isoCand_dz %0.2e, "
            //    "ele_vz-isoCand_vz %0.2e (%0.5e, %0.5e), "
            //    "pmVtx4D_z %0.5e, "
            //    "\n",
            //    
            //    iCand+1, nPFcand,
            //    cand->charge(),
            //    cand->energy(), cand->et(), cand->pt(),
            //    //cand->dz(), pmVtx_idx, cand->dz(pmVtx_idx), cand->dzAssociatedPV()
            //    (double) cand->hasTrackDetails() * (ele->bestTrack()->dz() - cand->dz()),
            //    (double) (ele->bestTrackRef().isNonnull() && cand->vertexRef().isNonnull()) * (ele->vz() - cand->vz()),
            //    ele->vz(), cand->vz(),
            //    pmVtx4D->z()
            //);
        }
        
        // Skip the signal candidates
        if(m_elePFcand_idx.find(cand) != m_elePFcand_idx.end())
        {
            continue;
        }
        
        
        //
        double dEta = ele->eta() - cand->eta();
        double dPhi = getDeltaPhi(ele->phi(), cand->phi());
        
        double dR = std::sqrt(dEta*dEta + dPhi*dPhi);
        
        bool isTimeValid = (cand->timeError() > 0 && pmVtx4D->tError() > 0);
        
        double dt = -9;
        double dtSigni = -9;
        
        if(isTimeValid)
        {
            dt = std::fabs(cand->time() - pmVtx4D->t());
            dtSigni = dt / std::sqrt(cand->timeError()*cand->timeError() + pmVtx4D->tError()*pmVtx4D->tError());
        }
        
        bool passed_dR = (dR < dR_max);
        
        bool passed_dz = (
            !cand->hasTrackDetails() ||
            (cand->hasTrackDetails() && fabs(cand->dz()) < dz_max)
        );
        
        bool passed_dtSigni = (
            !isTimeValid ||
            (isTimeValid && dtSigni < dtSigni_max)
        );
        
        bool passed_all = (
            passed_dR &&
            passed_dtSigni &&
            passed_dz
        );
        
        
        if(!passed_all)
        {
            continue;
        }
        
        
        iso_pfCand_n++;
        
        
        //
        if(isTimeValid)
        {
            nPFcand_isTimeValid++;
            
            if(iso_pfCand1_PV_dtSigni < 0)
            {
                iso_pfCand1_PV_dtSigni = dtSigni;
            }
            
            else if(iso_pfCand2_PV_dtSigni < 0)
            {
                iso_pfCand2_PV_dtSigni = dtSigni;
            }
            
            iso_pfCand_PV_dtSigniMean += dtSigni;
            iso_pfCand_PV_dtSigniMean_ETwtd += dtSigni * cand->et();
            
            ET_sum_isTimeValid += cand->et();
        }
        
        
        //
        if(cand->hasTrackDetails())
        {
            nPFcand_hasTrackDetails++;
            
            double dz = fabs(cand->dz());
            //double dzSigni = dz / cand->dzError();
            
            if(iso_pfCand1_PV_dz < 0)
            {
                iso_pfCand1_PV_dz = dz;
            }
            
            else if(iso_pfCand2_PV_dz < 0)
            {
                iso_pfCand2_PV_dz = dz;
            }
            
            iso_pfCand_PV_dzMean += dz;
            iso_pfCand_PV_dzMean_ETwtd += dz * cand->et();
            
            ET_sum_hasTrackDetails += cand->et();
        }
        
        
        // caloFraction = (ECAL+HCAL)/E
        // hcalFraction = HCAL/(ECAL+HCAL)
        double hcalFrac = cand->hcalFraction() * cand->caloFraction();
        double ecalFrac = cand->caloFraction() - hcalFrac;
        
        bool isCharged = cand->charge() != 0;
        bool isNeutral = cand->charge() == 0;
        
        iso_sumETratio += cand->et();
        
        iso_sumETratio_charged += cand->et() * isCharged;
        iso_sumETratio_neutral += cand->et() * isNeutral;
        iso_sumETratio_ecal += cand->et() * ecalFrac;
        iso_sumETratio_hcal += cand->et() * hcalFrac;
    }
    
    
    if(nPFcand_isTimeValid)
    {
        iso_pfCand_PV_dtSigniMean /= (double) nPFcand_isTimeValid;
        
        iso_pfCand_PV_dtSigniMean_ETwtd /= ET_sum_isTimeValid;
    }
    
    if(nPFcand_hasTrackDetails)
    {
        iso_pfCand_PV_dzMean /= (double) nPFcand_hasTrackDetails;
        
        iso_pfCand_PV_dzMean_ETwtd /= ET_sum_hasTrackDetails;
    }
    
    iso_sumETratio /= ele->et();
    iso_sumETratio_charged /= ele->et();
    iso_sumETratio_neutral /= ele->et();
    iso_sumETratio_ecal /= ele->et();
    iso_sumETratio_hcal /= ele->et();
    
    
    //
    isoVarContent->v_slimmedEle_iso_pfCand_n.push_back(iso_pfCand_n);
    
    //
    isoVarContent->v_slimmedEle_iso_pfCand1_PV_dtSigni.push_back(iso_pfCand1_PV_dtSigni);
    isoVarContent->v_slimmedEle_iso_pfCand2_PV_dtSigni.push_back(iso_pfCand2_PV_dtSigni);
    
    isoVarContent->v_slimmedEle_iso_pfCand_PV_dtSigniMean.push_back(iso_pfCand_PV_dtSigniMean);
    isoVarContent->v_slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd.push_back(iso_pfCand_PV_dtSigniMean_ETwtd);
    
    //
    isoVarContent->v_slimmedEle_iso_pfCand1_PV_dz.push_back(iso_pfCand1_PV_dz);
    isoVarContent->v_slimmedEle_iso_pfCand2_PV_dz.push_back(iso_pfCand2_PV_dz);
    
    isoVarContent->v_slimmedEle_iso_pfCand_PV_dzMean.push_back(iso_pfCand_PV_dzMean);
    isoVarContent->v_slimmedEle_iso_pfCand_PV_dzMean_ETwtd.push_back(iso_pfCand_PV_dzMean_ETwtd);
    
    //
    isoVarContent->v_slimmedEle_iso_sumETratio.push_back(iso_sumETratio);
    isoVarContent->v_slimmedEle_iso_sumETratio_charged.push_back(iso_sumETratio_charged);
    isoVarContent->v_slimmedEle_iso_sumETratio_neutral.push_back(iso_sumETratio_neutral);
    isoVarContent->v_slimmedEle_iso_sumETratio_ecal.push_back(iso_sumETratio_ecal);
    isoVarContent->v_slimmedEle_iso_sumETratio_hcal.push_back(iso_sumETratio_hcal);
}


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
    }
    
    
    //if(!treeOutput->genEl_n)
    //{
    //    return;
    //}
    
    
    //////////////////// Pileup ////////////////////
    edm::Handle <std::vector <PileupSummaryInfo> > pileUps_reco;
    iEvent.getByToken(tok_pileup, pileUps_reco);
    treeOutput->pileup_n = Common::getPileup(pileUps_reco);
    
    
    //////////////////// Rho ////////////////////
    edm::Handle <double> handle_rho;
    iEvent.getByToken(tok_rho, handle_rho);
    double rho = *handle_rho;
    
    treeOutput->rho = rho;
    
    
    //////////////////// PF candidates ////////////////////
    edm::Handle <std::vector <pat::PackedCandidate> > v_pfCandidate;
    iEvent.getByToken(tok_pfCandidate, v_pfCandidate);
    
    int nPFcand = v_pfCandidate->size();
    
    std::vector <int> v_pfCand_ETsortedIdx;
    std::map <const pat::PackedCandidate*, int> m_pfCand_idx;
    
    for(int iCand = 0; iCand < (int) nPFcand; iCand++)
    {
        const pat::PackedCandidate *cand = &v_pfCandidate->at(iCand);
        
        v_pfCand_ETsortedIdx.push_back(iCand);
        
        m_pfCand_idx[cand] = iCand;
        
        //if(iCand < 10)
        //{
        //    printf(
        //        "PF cand %d/%d: "
        //        //"time %0.3f, timeErr %0.3f, "
        //        "ID %+d, "
        //        "E %0.3f, ET %0.3f, pt %0.3f, "
        //        "charge %+d, "
        //        //"caloFrac %0.3f, hcalFrac %0.3f, "
        //        "dz %0.2e, dz(%d) %0.2e, dzAssociatedPV %0.2e, "
        //        "\n",
        //        
        //        iCand+1, nPFcand,
        //        cand->pdgId(),
        //        cand->energy(), cand->et(), cand->pt(),
        //        cand->charge(),
        //        //cand->caloFraction(), cand->hcalFraction()
        //        cand->dz(), pmVtx_idx, cand->dz(pmVtx_idx), cand->dzAssociatedPV()
        //    );
        //}
    }
    
    std::sort(
        v_pfCand_ETsortedIdx.begin(), v_pfCand_ETsortedIdx.end(),
        [&](int iCand1, int iCand2)
        {
            return (
                (&v_pfCandidate->at(iCand1))->et() > (&v_pfCandidate->at(iCand2))->et()
            );
        }
    );
    
    
    //////////////////// Slimmed electrons ////////////////////
    edm::Handle <std::vector <pat::Electron> > v_slimmedEle;
    iEvent.getByToken(tok_slimmedEle, v_slimmedEle);
    
    edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17IsoV2Values;
    iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17IsoV2Values, ElectronMVAEstimatorRun2Fall17IsoV2Values);
    
    edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
    iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17IsoV2RawValues, ElectronMVAEstimatorRun2Fall17IsoV2RawValues);
    
    edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
    iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17NoIsoV2Values, ElectronMVAEstimatorRun2Fall17NoIsoV2Values);
    
    edm::Handle <edm::ValueMap <float> > ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
    iEvent.getByToken(tok_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues, ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues);
    
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
    TMatrixD mat_slimmedEle_gelEl_deltaR;
    
    std::vector <int> v_slimmedEle_matchedGenEl_index;
    
    std::vector <double> v_slimmedEle_gelEl_minDeltaR = Common::getMinDeltaR(
        v_slimmedEle_4mom,
        v_genEl_4mom,
        mat_slimmedEle_gelEl_deltaR,
        v_slimmedEle_matchedGenEl_index
    );
    
    for(int iEle = 0; iEle < (int) v_slimmedEle_gelEl_minDeltaR.size(); iEle++)
    {
        double deltaR = v_slimmedEle_gelEl_minDeltaR.at(iEle);
        
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
        if(v_slimmedEle_gelEl_minDeltaR.at(iEle) > eleGenMatchDR)
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
        
        treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values.push_back((*ElectronMVAEstimatorRun2Fall17IsoV2Values)[ele_ptr]);
        treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues.push_back((*ElectronMVAEstimatorRun2Fall17IsoV2RawValues)[ele_ptr]);
        
        treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values.push_back((*ElectronMVAEstimatorRun2Fall17NoIsoV2Values)[ele_ptr]);
        treeOutput->v_slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues.push_back((*ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues)[ele_ptr]);
        
        treeOutput->v_slimmedEle_idx.push_back(treeOutput->slimmedEle_n);
        treeOutput->slimmedEle_n++;
        
        
        edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele.associatedPackedPFCandidates();
        //edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele.associatedPackedPFCandidates().reference;
        //edm::RefVector <pat::PackedCandidateCollection> elePFcandidates = ele.associatedPackedPFCandidates().refVector();
        
        const reco::GenParticle *linkedGenPart = ele.genParticle();
        
        //int linkedGenPart_pdgId = 0;
        //double linkedGenPart_pT = -99;
        //double linkedGenPart_eta = -99;
        //
        //if(linkedGenPart)
        //{
        //    linkedGenPart_pdgId = linkedGenPart->pdgId();
        //    
        //    linkedGenPart_pT = linkedGenPart->pt();
        //    linkedGenPart_eta = linkedGenPart->eta();
        //}
        
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
        
        
        fill_Ele_sigVar(
            treeOutput->m_Ele_sigVarContent.at("all"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            9999.0, // dz_max
            9999.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            9999.0 // dtSigni_max
        );
        
        //
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dTsigniLt2"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            9999.0, // dz_max
            2.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt2"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            2.0 // dtSigni_max
        );
        
        //
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dTsigniLt3"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            9999.0, // dz_max
            3.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt3"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            3.0 // dtSigni_max
        );
        
        //
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dTsigniLt4"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            9999.0, // dz_max
            4.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt4"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            4.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt5"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            5.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt6"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            6.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt10"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            10.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt20"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            20.0 // dtSigni_max
        );
        
        fill_Ele_isoVar(
            treeOutput->m_Ele_isoVarContent.at("dR0p3_dzLt0p5_dTsigniLt30"),
            v_pfCandidate,
            &v_pfCand_ETsortedIdx,
            &ele,
            &pmVtx4D,
            0.5, // ET_min
            0.3, // dR_max
            0.5, // dz_max
            30.0 // dtSigni_max
        );
        
        
        std::map <const pat::PackedCandidate*, int> m_elePFcand_idx;
        
        for(int iCand = 0; iCand < (int) elePFcandidates.size(); iCand++)
        //for(auto cand = elePFcandidates.begin(); cand != elePFcandidates.end(); cand++)
        {
            const pat::PackedCandidate *cand = elePFcandidates.at(iCand).get();
            
            m_elePFcand_idx[cand] = iCand;
            
            //int pfCand_idx = -1;
            //
            //if(m_pfCand_idx.find(cand) != m_pfCand_idx.end())
            //{
            //    pfCand_idx = m_pfCand_idx.at(cand);
            //}
            //
            //printf(
            //    "\t"
            //    "Ele PF cand %02d/%02d: "
            //    "PF idx %d/%d "
            //    //"time %0.4f, timeErr %0.4f"
            //    "E %0.4f, ET %0.4f, pt %0.4f"
            //    "\n",
            //    
            //    iCand+1, (int) elePFcandidates.size(),
            //    pfCand_idx+1, nPFcand,
            //    //cand->time(), cand->timeError()
            //    cand->energy(), cand->et(), cand->pt()
            //);
        }
        
        //
        //double isoDR0p3_sumETratio = 0;
        //double isoDR0p3_sumETratio_charged = 0;
        //double isoDR0p3_sumETratio_neutral = 0;
        //double isoDR0p3_sumETratio_ecal = 0;
        //double isoDR0p3_sumETratio_hcal = 0;
        //
        //double isoDR0p3_sumETratio_cleanedDT3sigma = 0;
        //double isoDR0p3_sumETratio_charged_cleanedDT3sigma = 0;
        //double isoDR0p3_sumETratio_neutral_cleanedDT3sigma = 0;
        //double isoDR0p3_sumETratio_ecal_cleanedDT3sigma = 0;
        //double isoDR0p3_sumETratio_hcal_cleanedDT3sigma = 0;
        //
        //double isoDR0p3_sumETratio_dzLt0p5 = 0;
        //double isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma = 0;
        //
        //double sig_pfCand1_PV_dtSigni = -9;
        //double sig_pfCand2_PV_dtSigni = -9;
        //
        //double isoDR0p3_pfCand1_PV_dtSigni = -9;
        //double isoDR0p3_pfCand2_PV_dtSigni = -9;
        //
        //double sig_pfCand_PV_dtSigniMean = 0;
        //double isoDR0p3_pfCand_PV_dtSigniMean = 0;
        
        
        std::vector <double> v_slimmedEle_sig_pfCand_eleIdx;
        
        std::vector <double> v_slimmedEle_sig_pfCand_charge;
        std::vector <double> v_slimmedEle_sig_pfCand_ET;
        
        std::vector <double> v_slimmedEle_sig_pfCand_t;
        std::vector <double> v_slimmedEle_sig_pfCand_tErr;
        
        std::vector <double> v_slimmedEle_sig_pfCand_PV_dt;
        std::vector <double> v_slimmedEle_sig_pfCand_PV_dtSigni;
        
        std::vector <double> v_slimmedEle_sig_pfCand_PV_dz;
        std::vector <double> v_slimmedEle_sig_pfCand_PV_dzSigni;
        
        
        //
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_eleIdx;
        
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_charge;
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_ET;
        
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_t;
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_tErr;
        
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_PV_dt;
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_PV_dtSigni;
        
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_PV_dz;
        std::vector <double> v_slimmedEle_isoDR0p3_pfCand_PV_dzSigni;
        
        
        for(int iCand = 0; iCand < (int) nPFcand; iCand++)
        {
            //const pat::PackedCandidate *cand = &v_pfCandidate->at(iCand);
            const pat::PackedCandidate *cand = &v_pfCandidate->at(v_pfCand_ETsortedIdx.at(iCand));
            
            if(iCand < 10)
            {
                //printf(
                //    "PF cand %d/%d: "
                //    //"time %0.4f, timeErr %0.4f"
                //    "chg %+d, "
                //    "E %0.2f, ET %0.2f, pt %0.2f, "
                //    //"dz %0.2e, dz(%d) %0.2e, dzAssociatedPV %0.2e, "
                //    "\n",
                //    
                //    iCand+1, nPFcand,
                //    cand->charge(),
                //    cand->energy(), cand->et(), cand->pt()
                //    //cand->dz(), pmVtx_idx, cand->dz(pmVtx_idx), cand->dzAssociatedPV()
                //);
            }
            
            // Skip the candidates with an invalid time measurement
            //if(cand->timeError() < 0)
            //{
            //    continue;
            //}
            
            double cand_t = -9;
            double cand_tErr = 9;
            
            double dt = -9;
            double dtSigni = -9;
            
            bool isTimeValid = (cand->timeError() > 0 && pmVtx4D.tError() > 0);
            
            double cand_dz = -9;
            double cand_dzErr = 9;
            double cand_dzSigni = 9;
            
            bool isCharged = cand->charge() != 0;
            bool isNeutral = cand->charge() == 0;
            
            const reco::Track *track = cand->bestTrack();
            
            if(isTimeValid)
            {
                cand_t = cand->time();
                cand_tErr = cand->timeError();
                
                dt = std::fabs(cand->time() - pmVtx4D.t());
                dtSigni = dt / std::sqrt(cand->timeError()*cand->timeError() + pmVtx4D.tError()*pmVtx4D.tError());
            }
            
            if(cand->hasTrackDetails())
            {
                cand_dz = fabs(cand->dz());
                cand_dzErr = cand->dzError();
                cand_dzSigni = cand_dz / cand_dzErr;
            }
            
            //else
            //{
            //    printf("cand->timeError() %f, pmVtx4D.tError() %f \n", cand->timeError(), pmVtx4D.tError());
            //}
            
            // Skip the signal candidates
            if(m_elePFcand_idx.find(cand) != m_elePFcand_idx.end())
            {
                //if(isTimeValid)
                {
                    //sig_pfCand_PV_dtSigniMean += dtSigni;
                    
                    v_slimmedEle_sig_pfCand_eleIdx.push_back(treeOutput->slimmedEle_n-1);
                    
                    v_slimmedEle_sig_pfCand_charge.push_back(cand->charge());
                    v_slimmedEle_sig_pfCand_ET.push_back(cand->et());
                    
                    v_slimmedEle_sig_pfCand_t.push_back(cand_t);
                    v_slimmedEle_sig_pfCand_tErr.push_back(cand_tErr);
                    
                    v_slimmedEle_sig_pfCand_PV_dt.push_back(dt);
                    v_slimmedEle_sig_pfCand_PV_dtSigni.push_back(dtSigni);
                    
                    
                    //if(sig_pfCand1_PV_dtSigni < 0)
                    //{
                    //    sig_pfCand1_PV_dtSigni = dtSigni;
                    //}
                    //
                    //else if(sig_pfCand2_PV_dtSigni < 0)
                    //{
                    //    sig_pfCand2_PV_dtSigni = dtSigni;
                    //}
                }
                
                ////if(isCharged)
                ////if(track != nullptr)
                //if(cand->hasTrackDetails())
                {
                    v_slimmedEle_sig_pfCand_PV_dz.push_back(cand_dz);
                    v_slimmedEle_sig_pfCand_PV_dzSigni.push_back(cand_dzSigni);
                    
                    //v_slimmedEle_sig_pfCand_PV_dz.push_back(fabs(track->dz()));
                    //v_slimmedEle_sig_pfCand_PV_dzSigni.push_back(fabs(track->dz()) / track->dzError());
                }
                
                continue;
            }
            
            
            double dEta = ele.eta() - cand->eta();
            double dPhi = getDeltaPhi(ele.phi(), cand->phi());
            
            double dR = std::sqrt(dEta*dEta + dPhi*dPhi);
            
            // caloFraction = (ECAL+HCAL)/E
            // hcalFraction = HCAL/(ECAL+HCAL)
            double hcalFrac = cand->hcalFraction() * cand->caloFraction();
            double ecalFrac = cand->caloFraction() - hcalFrac;
            
            bool passed_dz = (
                !cand->hasTrackDetails() ||
                (cand->hasTrackDetails() && fabs(cand->dz()) < 0.5)
            );
            
            if(dR < 0.3)
            {
                //if(isTimeValid)
                {
                    //isoDR0p3_pfCand_PV_dtSigniMean += dtSigni;
                    
                    v_slimmedEle_isoDR0p3_pfCand_eleIdx.push_back(treeOutput->slimmedEle_n-1);
                    
                    v_slimmedEle_isoDR0p3_pfCand_charge.push_back(cand->charge());
                    v_slimmedEle_isoDR0p3_pfCand_ET.push_back(cand->et());
                    
                    v_slimmedEle_isoDR0p3_pfCand_t.push_back(cand_t);
                    v_slimmedEle_isoDR0p3_pfCand_tErr.push_back(cand_tErr);
                    
                    v_slimmedEle_isoDR0p3_pfCand_PV_dt.push_back(dt);
                    v_slimmedEle_isoDR0p3_pfCand_PV_dtSigni.push_back(dtSigni);
                    
                    
                    //if(isoDR0p3_pfCand1_PV_dtSigni < 0)
                    //{
                    //    isoDR0p3_pfCand1_PV_dtSigni = dtSigni;
                    //}
                    //
                    //else if(isoDR0p3_pfCand2_PV_dtSigni < 0)
                    //{
                    //    isoDR0p3_pfCand2_PV_dtSigni = dtSigni;
                    //}
                }
                
                ////if(isCharged)
                ////if(track != nullptr)
                //if(cand->hasTrackDetails())
                {
                    v_slimmedEle_isoDR0p3_pfCand_PV_dz.push_back(cand_dz);
                    v_slimmedEle_isoDR0p3_pfCand_PV_dzSigni.push_back(cand_dzSigni);
                    
                    //v_slimmedEle_isoDR0p3_pfCand_PV_dz.push_back(fabs(track->dz()));
                    //v_slimmedEle_isoDR0p3_pfCand_PV_dzSigni.push_back(fabs(track->dz()) / track->dzError());
                }
                
                //isoDR0p3_sumETratio += cand->et();
                //
                //isoDR0p3_sumETratio_charged += cand->et() * isCharged;
                //isoDR0p3_sumETratio_neutral += cand->et() * isNeutral;
                //isoDR0p3_sumETratio_ecal += cand->et() * ecalFrac;
                //isoDR0p3_sumETratio_hcal += cand->et() * hcalFrac;
                //
                //isoDR0p3_sumETratio_dzLt0p5 += cand->et() * passed_dz;
                //
                //
                //if(dtSigni < 3)
                //{
                //    isoDR0p3_sumETratio_cleanedDT3sigma += cand->et();
                //    
                //    isoDR0p3_sumETratio_charged_cleanedDT3sigma += cand->et() * isCharged;
                //    isoDR0p3_sumETratio_neutral_cleanedDT3sigma += cand->et() * isNeutral;
                //    isoDR0p3_sumETratio_ecal_cleanedDT3sigma += cand->et() * ecalFrac;
                //    isoDR0p3_sumETratio_hcal_cleanedDT3sigma += cand->et() * hcalFrac;
                //    
                //    isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma += cand->et() * passed_dz;
                //}
            }
        }
        
        //isoDR0p3_sumETratio /= ele.et();
        //isoDR0p3_sumETratio_charged /= ele.et();
        //isoDR0p3_sumETratio_neutral /= ele.et();
        //isoDR0p3_sumETratio_ecal /= ele.et();
        //isoDR0p3_sumETratio_hcal /= ele.et();
        //
        //isoDR0p3_sumETratio_cleanedDT3sigma /= ele.et();
        //isoDR0p3_sumETratio_charged_cleanedDT3sigma /= ele.et();
        //isoDR0p3_sumETratio_neutral_cleanedDT3sigma /= ele.et();
        //isoDR0p3_sumETratio_ecal_cleanedDT3sigma /= ele.et();
        //isoDR0p3_sumETratio_hcal_cleanedDT3sigma /= ele.et();
        //
        //isoDR0p3_sumETratio_dzLt0p5 /= ele.et();
        //isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma /= ele.et();
        //
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio.push_back(isoDR0p3_sumETratio);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_charged.push_back(isoDR0p3_sumETratio_charged);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_neutral.push_back(isoDR0p3_sumETratio_neutral);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_ecal.push_back(isoDR0p3_sumETratio_ecal);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_hcal.push_back(isoDR0p3_sumETratio_hcal);
        //
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_cleanedDT3sigma);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_charged_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_charged_cleanedDT3sigma);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_neutral_cleanedDT3sigma);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_ecal_cleanedDT3sigma);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_hcal_cleanedDT3sigma);
        //
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5.push_back(isoDR0p3_sumETratio_dzLt0p5);
        //treeOutput->v_slimmedEle_isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma.push_back(isoDR0p3_sumETratio_dzLt0p5_cleanedDT3sigma);
        //
        //
        ////
        //if(v_slimmedEle_sig_pfCand_t.size())
        //{
        //    sig_pfCand_PV_dtSigniMean /= (double) v_slimmedEle_sig_pfCand_t.size();
        //}
        //
        //if(v_slimmedEle_isoDR0p3_pfCand_t.size())
        //{
        //    isoDR0p3_pfCand_PV_dtSigniMean /= (double) v_slimmedEle_isoDR0p3_pfCand_t.size();
        //}
        //
        //treeOutput->v_slimmedEle_sig_pfCand1_PV_dtSigni.push_back(sig_pfCand1_PV_dtSigni);
        //treeOutput->v_slimmedEle_sig_pfCand2_PV_dtSigni.push_back(sig_pfCand2_PV_dtSigni);
        //
        //treeOutput->v_slimmedEle_isoDR0p3_pfCand1_PV_dtSigni.push_back(isoDR0p3_pfCand1_PV_dtSigni);
        //treeOutput->v_slimmedEle_isoDR0p3_pfCand2_PV_dtSigni.push_back(isoDR0p3_pfCand2_PV_dtSigni);
        //
        //treeOutput->v_slimmedEle_sig_pfCand_PV_dtSigniMean.push_back(sig_pfCand_PV_dtSigniMean);
        //treeOutput->v_slimmedEle_isoDR0p3_pfCand_PV_dtSigniMean.push_back(isoDR0p3_pfCand_PV_dtSigniMean);
        
        
        //
        treeOutput->vv_slimmedEle_sig_pfCand_eleIdx.push_back(v_slimmedEle_sig_pfCand_eleIdx);
        
        treeOutput->vv_slimmedEle_sig_pfCand_charge.push_back(v_slimmedEle_sig_pfCand_charge);
        treeOutput->vv_slimmedEle_sig_pfCand_ET.push_back(v_slimmedEle_sig_pfCand_ET);
        
        treeOutput->vv_slimmedEle_sig_pfCand_t.push_back(v_slimmedEle_sig_pfCand_t);
        treeOutput->vv_slimmedEle_sig_pfCand_tErr.push_back(v_slimmedEle_sig_pfCand_tErr);
        
        treeOutput->vv_slimmedEle_sig_pfCand_PV_dt.push_back(v_slimmedEle_sig_pfCand_PV_dt);
        treeOutput->vv_slimmedEle_sig_pfCand_PV_dtSigni.push_back(v_slimmedEle_sig_pfCand_PV_dtSigni);
        
        treeOutput->vv_slimmedEle_sig_pfCand_PV_dz.push_back(v_slimmedEle_sig_pfCand_PV_dz);
        treeOutput->vv_slimmedEle_sig_pfCand_PV_dzSigni.push_back(v_slimmedEle_sig_pfCand_PV_dzSigni);
        
        //
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_eleIdx.push_back(v_slimmedEle_isoDR0p3_pfCand_eleIdx);
        
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_charge.push_back(v_slimmedEle_isoDR0p3_pfCand_charge);
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_ET.push_back(v_slimmedEle_isoDR0p3_pfCand_ET);
        
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_t.push_back(v_slimmedEle_isoDR0p3_pfCand_t);
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_tErr.push_back(v_slimmedEle_isoDR0p3_pfCand_tErr);
        
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_PV_dt.push_back(v_slimmedEle_isoDR0p3_pfCand_PV_dt);
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_PV_dtSigni.push_back(v_slimmedEle_isoDR0p3_pfCand_PV_dtSigni);
        
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_PV_dz.push_back(v_slimmedEle_isoDR0p3_pfCand_PV_dz);
        treeOutput->vv_slimmedEle_isoDR0p3_pfCand_PV_dzSigni.push_back(v_slimmedEle_isoDR0p3_pfCand_PV_dzSigni);
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
