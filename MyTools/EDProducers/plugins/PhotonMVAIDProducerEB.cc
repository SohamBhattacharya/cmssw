// -*- C++ -*-
//
// Package:    MyTools/PhotonMVAIDProducerEB
// Class:      PhotonMVAIDProducerEB
//
/**\class PhotonMVAIDProducerEB PhotonMVAIDProducerEB.cc MyTools/PhotonMVAIDProducerEB/plugins/PhotonMVAIDProducerEB.cc

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
# include "DataFormats/CaloRecHit/interface/CaloCluster.h"
# include "DataFormats/EgammaCandidates/interface/Photon.h"
# include "DataFormats/FWLite/interface/ESHandle.h"
# include "DataFormats/ForwardDetId/interface/HGCEEDetId.h"
# include "DataFormats/ForwardDetId/interface/HGCalDetId.h"
# include "DataFormats/GsfTrackReco/interface/GsfTrack.h"
# include "DataFormats/HGCRecHit/interface/HGCRecHit.h"
# include "DataFormats/Math/interface/LorentzVector.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHit.h"
# include "DataFormats/ParticleFlowReco/interface/PFRecHitFraction.h"
# include "DataFormats/PatCandidates/interface/Photon.h"
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
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "RecoParticleFlow/PFClusterProducer/interface/InitialClusteringStepBase.h"

# include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"

# include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"

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

class PhotonMVAIDProducerEB : public edm::stream::EDProducer<>
{
    public:
    
    explicit PhotonMVAIDProducerEB(const edm::ParameterSet&);
    ~PhotonMVAIDProducerEB();
    
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
    
    edm::EDGetTokenT <std::vector <pat::Photon> > tok_photon_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitEB_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitEE_;
    edm::EDGetTokenT <EcalRecHitCollection> tok_recHitES_;
    
    edm::EDGetTokenT <double> tok_rho;
    
    TMVAEvaluator tmvaEval;
    
    std::string options_ ;
    std::string method_ ;
    std::string weightFile_;
    
    std::vector<std::string> variables_;
    std::vector<std::string> spectators_;
    
    bool useGBRForest_;
    bool useAdaBoost_;
    
    const noZS::EcalClusterLazyTools::ESGetTokens ecalClusterToolsESGetTokens_;
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
PhotonMVAIDProducerEB::PhotonMVAIDProducerEB(const edm::ParameterSet& iConfig) :
    ecalClusterToolsESGetTokens_{consumesCollector()}
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
    weightFile_ = iConfig.getParameter <std::string>("weightFile");
    
    tok_photon_ = consumes <std::vector <pat::Photon> >(iConfig.getParameter <edm::InputTag>("photons"));
    
    tok_recHitEB_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsEB"));;
    tok_recHitEE_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsEE"));;
    tok_recHitES_ = consumes <EcalRecHitCollection>(iConfig.getParameter <edm::InputTag>("recHitsES"));;
    
    tok_rho = consumes <double>(iConfig.getParameter <edm::InputTag>("rho"));
    
    minPt_ = iConfig.getParameter <double>("minPt");
    
    debug_ = iConfig.getParameter <bool>("debug");
    
    options_ = "";
    method_ = "BDT::BDTG";
    
    variables_ = {
        "scRawE",
        "r9",
        "sigmaIetaIeta",
        "etaWidth",
        "phiWidth",
        "covIEtaIPhi",
        "s4",
        "phoIso03",
        "chgIsoWrtChosenVtx",
        "chgIsoWrtWorstVtx",
        "scEta",
        "rho"
    };
    
    spectators_ = {};
    
    useGBRForest_ = false;
    useAdaBoost_ = false;
    
    tmvaEval.initialize(
        options_,
        method_,
        weightFile_,
        variables_,
        spectators_,
        useGBRForest_,
        useAdaBoost_
    );
    
    std::srand(std::time(nullptr));
    
    
    produces <std::vector <double> > (instanceName_);
}

PhotonMVAIDProducerEB::~PhotonMVAIDProducerEB() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void PhotonMVAIDProducerEB::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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
    
    edm::Handle <std::vector <pat::Photon> > h_photon;
    iEvent.getByToken(tok_photon_, h_photon);
    auto photons = *h_photon;
    
    int iPho = -1;
    int nPho = h_photon->size();
    
    std::map <std::string, float> inputs;
    std::vector <double> v_photonID;
    
    for(auto &pho : photons)
    {
        iPho++;
        
        if(pho.pt() < minPt_)
        {
            //v_Rvar.push_back(-99);
            continue;
        }
        
        std::vector <float> covariances = lazyToolnoZS.localCovariances(*(pho.superCluster()->seed()));                                                                                                          
        
        inputs["scRawE"] = pho.superCluster()->rawEnergy();
        inputs["r9"] = pho.full5x5_r9();
        inputs["sigmaIetaIeta"] = pho.full5x5_sigmaIetaIeta();
        inputs["etaWidth"] = pho.superCluster()->etaWidth();
        inputs["phiWidth"] = pho.superCluster()->phiWidth();
        inputs["covIEtaIPhi"] = covariances[1];
        inputs["s4"] = lazyToolnoZS.e2x2(*(pho.superCluster()->seed())) / pho.full5x5_e5x5();
        inputs["phoIso03"] = pho.photonIso();
        inputs["chgIsoWrtChosenVtx"] = pho.chargedHadronIso();
        inputs["chgIsoWrtWorstVtx"] = pho.chargedHadronWorstVtxIso();
        inputs["scEta"] = pho.superCluster()->eta();
        inputs["rho"] = rho;
        
        float mvaVal = tmvaEval.evaluateTMVA(inputs, false);
        
        if(debug_)
        {
            printf("In PhotonMVAIDProducerEB --> Pho %d/%d: \n", iPho+1, nPho);
            printf(
                "MVA val: %0.4f, "
                ,
                mvaVal
            );
            printf("\n");
        }
        
        // https://github.com/Prasant1993/EGMObjectDumper/blob/master/egmNtuplizer/plugins/egmNtuplizer_photons.cc#L191
        
        v_photonID.push_back(mvaVal);
    }
    
    
    iEvent.put(
       std::make_unique <std::vector <double> >(v_photonID),
       instanceName_
    );
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void PhotonMVAIDProducerEB::beginStream(edm::StreamID) {
  // please remove this method if not needed
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void PhotonMVAIDProducerEB::endStream() {
  // please remove this method if not needed
}

// ------------ method called when starting to processes a run  ------------
/*
void
PhotonMVAIDProducerEB::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
PhotonMVAIDProducerEB::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
PhotonMVAIDProducerEB::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
PhotonMVAIDProducerEB::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PhotonMVAIDProducerEB::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PhotonMVAIDProducerEB);
