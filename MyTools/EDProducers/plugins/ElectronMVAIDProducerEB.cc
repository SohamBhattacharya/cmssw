// -*- C++ -*-
//
// Package:    MyTools/ElectronMVAIDProducerEB
// Class:      ElectronMVAIDProducerEB
//
/**\class ElectronMVAIDProducerEB ElectronMVAIDProducerEB.cc MyTools/ElectronMVAIDProducerEB/plugins/ElectronMVAIDProducerEB.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Soham Bhattacharya
//         Created:  Wed, 16 Sep 2020 14:18:20 GMT
//
//

// system include files
#include <memory>

// user include files
# include "CommonTools/Egamma/interface/ConversionTools.h"
# include "CommonTools/Egamma/interface/EffectiveAreas.h"
# include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"
# include "DataFormats/CaloRecHit/interface/CaloCluster.h"
# include "DataFormats/EgammaCandidates/interface/Conversion.h"
# include "DataFormats/EgammaCandidates/interface/ConversionFwd.h"
# include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
# include "DataFormats/FWLite/interface/ESHandle.h"
# include "DataFormats/ForwardDetId/interface/HGCEEDetId.h"
# include "DataFormats/ForwardDetId/interface/HGCalDetId.h"
# include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
# include "DataFormats/HGCRecHit/interface/HGCRecHit.h"
# include "DataFormats/Math/interface/LorentzVector.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHitFraction.h"
# include "DataFormats/PatCandidates/interface/Electron.h"
# include "DataFormats/TrackReco/interface/Track.h"
# include "DataFormats/TrackReco/interface/TrackFwd.h"
# include "FWCore/Framework/interface/Event.h"
# include "FWCore/Framework/interface/Frameworkfwd.h"
# include "FWCore/Framework/interface/MakerMacros.h"
# include "FWCore/Framework/interface/stream/EDProducer.h"
# include "FWCore/ParameterSet/interface/ParameterSet.h"
# include "FWCore/Utilities/interface/StreamID.h"
# include "Geometry/CaloTopology/interface/HGCalTopology.h"
# include "Geometry/Records/interface/IdealGeometryRecord.h"
# include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "RecoParticleFlow/PFClusterProducer/interface/InitialClusteringStepBase.h"

# include <CLHEP/Vector/LorentzVector.h>
# include <Math/VectorUtil.h>

# include <algorithm>
# include <ctime>
# include <iostream>
# include <map>
# include <stdlib.h>
# include <string>
# include <type_traits>
# include <utility>
# include <vector>


//
// class declaration
//

class ElectronMVAIDProducerEB : public edm::stream::EDProducer<>
{
    public:
    
    explicit ElectronMVAIDProducerEB(const edm::ParameterSet&);
    ~ElectronMVAIDProducerEB();
    
    static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);
    
    
    private:
    
    void beginStream(edm::StreamID) override;
    void produce(edm::Event&, const edm::EventSetup&) override;
    void endStream() override;
    
    //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
    //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
    //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
    //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
    
    // ----------member data ---------------------------
    
    std::string instanceName_;
    
    double minPt_;
    bool debug_;
    
    edm::EDGetTokenT <std::vector <pat::Electron> > tok_electron_;
    edm::EDGetTokenT <reco::BeamSpot> tok_beamSpot_;
    edm::EDGetTokenT <reco::ConversionCollection> tok_conversions_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitEB_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitEE_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitES_;
    
    edm::EDGetTokenT <double> tok_rho;
    
    std::vector <std::string> variables_;
    
    const noZS::EcalClusterLazyTools::ESGetTokens ecalClusterToolsESGetTokens_;
    
    EffectiveAreas effectiveAreas_;
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
ElectronMVAIDProducerEB::ElectronMVAIDProducerEB(const edm::ParameterSet& iConfig) :
    ecalClusterToolsESGetTokens_{consumesCollector()},
    effectiveAreas_(iConfig.getParameter <std::string>("effAreaFile"))
{
    //register your products
    /* Examples
    produces<ExampleData2>();
    
    //if do put with a label
    produces<ExampleData2>("label");
    
    //if you want to put into the Run
    produces<ExampleData2,InRun>();
    */
    //now do what ever other initialization is needed
    
    instanceName_ = iConfig.getParameter <std::string>("instanceName");
    
    tok_electron_ = consumes <std::vector <pat::Electron> >(iConfig.getParameter <edm::InputTag>("electrons"));
    
    tok_beamSpot_ = consumes <reco::BeamSpot>(iConfig.getParameter <edm::InputTag>("beamSpot"));
    tok_conversions_ = consumes <reco::ConversionCollection>(iConfig.getParameter <edm::InputTag>("conversions"));
    
    tok_recHitEB_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsEB"));;
    tok_recHitEE_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsEE"));;
    tok_recHitES_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsES"));;
    
    tok_rho = consumes <double>(iConfig.getParameter <edm::InputTag>("rho"));
    
    minPt_ = iConfig.getParameter <double>("minPt");
    
    debug_ = iConfig.getParameter <bool>("debug");
    
    variables_ = {
        "full5x5_sigmaIetaIeta",
        "dEtaSeed",
        "dPhiIn",
        "hOverE",
        "relCombIsoWithEA",
        "ooEmooP",
        "missingInnerHits",
        "passConvVeto",
    };
    
    
    produces <std::vector <bool> > (instanceName_+"VetoWP");
    produces <std::vector <bool> > (instanceName_+"LooseWP");
    produces <std::vector <bool> > (instanceName_+"MediumWP");
    produces <std::vector <bool> > (instanceName_+"TightWP");
}

ElectronMVAIDProducerEB::~ElectronMVAIDProducerEB() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void ElectronMVAIDProducerEB::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    /* This is an event example
    //Read 'ExampleData' from the Event
    ExampleData const& in = iEvent.get(inToken_);
    
    //Use the ExampleData to create an ExampleData2 which 
    // is put into the Event
    iEvent.put(std::make_unique<ExampleData2>(in));
    */
    
    /* this is an EventSetup example
    //Read SetupData from the SetupRecord in the EventSetup
    SetupData& setup = iSetup.getData(setupToken_);
    */
    
    
    edm::Handle <double> handle_rho;
    iEvent.getByToken(tok_rho, handle_rho);
    double rho = *handle_rho;
    
    edm::Handle <EcalRecHitCollection> h_recHitEB;
    edm::Handle <EcalRecHitCollection> h_recHitEE;
    edm::Handle <EcalRecHitCollection> h_recHitES;
    
    //iEvent.getByToken(tok_recHitEB_, h_recHitEB);
    //iEvent.getByToken(tok_recHitEE_, h_recHitEE);
    //iEvent.getByToken(tok_recHitES_, h_recHitES);
    
    //noZS::EcalClusterLazyTools lazyToolnoZS(iEvent, iSetup, h_recHitEB, h_recHitEE, h_recHitES);
    //noZS::EcalClusterLazyTools lazyToolnoZS(iEvent, ecalClusterToolsESGetTokens_.get(iSetup), tok_recHitEB_, tok_recHitEE_, tok_recHitES_);
    noZS::EcalClusterLazyTools lazyToolnoZS(iEvent, ecalClusterToolsESGetTokens_.get(iSetup), tok_recHitEB_, tok_recHitEE_);
    
    edm::Handle <std::vector <pat::Electron> > h_electron;
    iEvent.getByToken(tok_electron_, h_electron);
    auto electrons = *h_electron;
    
    edm::Handle<reco::BeamSpot> h_beamSpot;
    iEvent.getByToken(tok_beamSpot_, h_beamSpot);
    auto beamSpot = *h_beamSpot;
    
    edm::Handle <reco::ConversionCollection> h_conversion;
    iEvent.getByToken(tok_conversions_, h_conversion);
    auto conversions = *h_conversion;
    
    int iEle = -1;
    int nEle = h_electron->size();
    
    std::map <std::string, float> inputs;
    
    std::vector <bool> v_electronVetoWP(nEle, false);
    std::vector <bool> v_electronLooseWP(nEle, false);
    std::vector <bool> v_electronMediumWP(nEle, false);
    std::vector <bool> v_electronTightWP(nEle, false);
    
    for(auto &ele : electrons)
    {
        iEle++;
        
        if(ele.pt() < minPt_)
        {
            continue;
        }
        
        double effArea = effectiveAreas_.getEffectiveArea(std::fabs(ele.superCluster()->eta()));
        auto const &pfIso = ele.pfIsolationVariables();
        
        double full5x5_sigmaIetaIeta = ele.full5x5_sigmaIetaIeta();
        double dEtaSeed = (ele.superCluster().isNonnull() && ele.superCluster()->seed().isNonnull())? std::fabs(ele.deltaEtaSuperClusterTrackAtVtx() - ele.superCluster()->eta() + ele.superCluster()->seed()->eta()) : std::numeric_limits<float>::max();
        double dPhiIn = std::fabs(ele.deltaPhiSuperClusterTrackAtVtx());
        double hOverE = ele.hcalOverEcal();
        double relCombIsoWithEA = (pfIso.sumChargedHadronPt + std::max(0.0, pfIso.sumNeutralHadronEt + pfIso.sumPhotonEt - effArea*rho)) / ele.pt();
        double ooEmooP = (ele.ecalEnergy() == 0 || !std::isfinite(ele.ecalEnergy()))? 1e30 : std::fabs(1.0/ele.ecalEnergy() - ele.eSuperClusterOverP()/ele.ecalEnergy());
        
        int missingInnerHits = ele.gsfTrack()->hitPattern().numberOfLostHits(reco::HitPattern::MISSING_INNER_HITS);
        bool passConvVeto = !ConversionTools::hasMatchedConversion(ele, conversions, beamSpot.position());
        
        
        inputs["full5x5_sigmaIetaIeta"] = full5x5_sigmaIetaIeta;
        inputs["dEtaSeed"             ] = dEtaSeed;
        inputs["dPhiIn"               ] = dPhiIn;
        inputs["hOverE"               ] = hOverE;
        inputs["relCombIsoWithEA"     ] = relCombIsoWithEA;
        inputs["ooEmooP"              ] = ooEmooP;
        inputs["missingInnerHits"     ] = missingInnerHits;
        inputs["passConvVeto"         ] = passConvVeto;
        
        // ABSOLUTELY TERRIBLE HARDCODING!!! Change later...
        bool passVetoWP = (
               full5x5_sigmaIetaIeta <  0.0181
            && dEtaSeed              <  0.00548
            && dPhiIn                <  0.197
            && hOverE                <  0.313
            && relCombIsoWithEA      <  0.284
            && ooEmooP               <  0.203
            && missingInnerHits      <= 2
            && passConvVeto          == true
        );
        
        bool passLooseWP = (
               full5x5_sigmaIetaIeta <  0.0162
            && dEtaSeed              <  0.00409
            && dPhiIn                <  0.0679
            && hOverE                <  0.222
            && relCombIsoWithEA      <  0.223
            && ooEmooP               <  0.0747
            && missingInnerHits      <= 1
            && passConvVeto          == true
        );
        
        bool passMediumWP = (
               full5x5_sigmaIetaIeta <  0.0156
            && dEtaSeed              <  0.00326
            && dPhiIn                <  0.0434
            && hOverE                <  0.138
            && relCombIsoWithEA      <  0.159
            && ooEmooP               <  0.0735
            && missingInnerHits      <= 1
            && passConvVeto          == true
        );
        
        bool passTightWP = (
               full5x5_sigmaIetaIeta <  0.0137
            && dEtaSeed              <  0.00325
            && dPhiIn                <  0.0365
            && hOverE                <  0.103
            && relCombIsoWithEA      <  0.121
            && ooEmooP               <  0.0161
            && missingInnerHits      <= 1
            && passConvVeto          == true
        );
        
        v_electronVetoWP.at(iEle) = passVetoWP;
        v_electronLooseWP.at(iEle) = passLooseWP;
        v_electronMediumWP.at(iEle) = passMediumWP;
        v_electronTightWP.at(iEle) = passTightWP;
        
        if(debug_)
        {
            printf("In ElectronMVAIDProducerEB --> Ele %d/%d: \n", iEle+1, nEle);
        }
        
        if(debug_)
        {
            for(auto &key : variables_)
            {
                printf("    %s %0.8f \n", key.c_str(), inputs.at(key));
            }
            
            printf("    Veto: %d, L: %d, M: %d, T: %d \n", passVetoWP, passLooseWP, passMediumWP, passTightWP);
        }
    }
    
    
    iEvent.put(std::make_unique <std::vector <bool> >(v_electronVetoWP),   instanceName_+"VetoWP");
    iEvent.put(std::make_unique <std::vector <bool> >(v_electronLooseWP),  instanceName_+"LooseWP");
    iEvent.put(std::make_unique <std::vector <bool> >(v_electronMediumWP), instanceName_+"MediumWP");
    iEvent.put(std::make_unique <std::vector <bool> >(v_electronTightWP),  instanceName_+"TightWP");
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void ElectronMVAIDProducerEB::beginStream(edm::StreamID) {
  // please remove this method if not needed
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void ElectronMVAIDProducerEB::endStream() {
  // please remove this method if not needed
}

// ------------ method called when starting to processes a run  ------------
/*
void
ElectronMVAIDProducerEB::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
ElectronMVAIDProducerEB::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
ElectronMVAIDProducerEB::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
ElectronMVAIDProducerEB::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void ElectronMVAIDProducerEB::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(ElectronMVAIDProducerEB);
