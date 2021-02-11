// -*- C++ -*-
//
// Package:    MyTools/PhotonMVAIDProducerHGCal
// Class:      PhotonMVAIDProducerHGCal
//
/**\class PhotonMVAIDProducerHGCal PhotonMVAIDProducerHGCal.cc MyTools/PhotonMVAIDProducerHGCal/plugins/PhotonMVAIDProducerHGCal.cc

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
# include "CommonTools/MVAUtils/interface/TMVAEvaluator.h"
# include "DataFormats/CaloRecHit/interface/CaloCluster.h"
# include "DataFormats/Common/interface/MapOfVectors.h"
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
# include "RecoEcal/EgammaCoreTools/interface/EcalClusterLazyTools.h"
# include "RecoEgamma/EgammaTools/interface/HGCalClusterTools.h"
# include "RecoEgamma/EgammaTools/interface/HGCalShowerShapeHelper.h"
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "RecoParticleFlow/PFClusterProducer/interface/InitialClusteringStepBase.h"

# include <CLHEP/Vector/LorentzVector.h>
# include <Math/VectorUtil.h>

# include <TVectorD.h>

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

class PhotonMVAIDProducerHGCal : public edm::stream::EDProducer<>
{
    public:
    
    explicit PhotonMVAIDProducerHGCal(const edm::ParameterSet&);
    ~PhotonMVAIDProducerHGCal();
    
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
    
    edm::EDGetTokenT <std::vector <reco::Photon> > tok_photon_;
    edm::EDGetTokenT <std::vector <reco::PFRecHit> > tok_PFRecHit_;
    edm::EDGetTokenT <double> tok_rho_;
    edm::EDGetTokenT <edm::MapOfVectors <std::string, double> > tok_varMap_;
    
    TMVAEvaluator tmvaEval;
    
    std::string options_ ;
    std::string method_ ;
    std::string weightFile_;
    
    std::vector<std::string> variables_;
    std::vector<std::string> spectators_;
    
    HGCalClusterTools algo_iso_;
    HGCalShowerShapeHelper showerShapeHelper_;
    
    std::map<std::string, std::string> mapKey;
    
    bool useGBRForest_;
    bool useAdaBoost_;
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
PhotonMVAIDProducerHGCal::PhotonMVAIDProducerHGCal(const edm::ParameterSet& iConfig)
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
    
    tok_photon_ = consumes <std::vector <reco::Photon> >(iConfig.getParameter <edm::InputTag>("photons"));
    tok_PFRecHit_ = consumes <std::vector <reco::PFRecHit> >(iConfig.getParameter <edm::InputTag>("PFRecHits"));
    tok_rho_ = consumes <double>(iConfig.getParameter <edm::InputTag>("rho"));
    tok_varMap_ = consumes <edm::MapOfVectors <std::string, double> >(iConfig.getParameter <edm::InputTag>("varMap"));
    
    minPt_ = iConfig.getParameter <double>("minPt");
    
    debug_ = iConfig.getParameter <bool>("debug");
    
    options_ = "";
    method_ = "BDT::BDT";
    
    variables_ = {
        "sc_rawET",
        "sc_absEta",
        "sc_nClus",
        "sc_nHit",
        "sc_hit1_enFrac",
        "sc_hit2_enFrac",
        "sc_R2p8",
        "sc_sUU",
        "sc_sVV",
        "sc_sWW",
        "sc_seed_dEta",
        "sc_seed_dPhi",
        "sc_seed_enFrac",
        "clusIsoDR0p2",
        "hByEdR0p15",
        "rho",
    };
    
    
    
    mapKey["sc_R2p8"]       = "TICLphoRvarProducer_HGCalPhotonRvar";
    mapKey["sc_sUU"]        = "TICLphoPCAProducer_HGCalPhotonPCASigma2UU";
    mapKey["sc_sVV"]        = "TICLphoPCAProducer_HGCalPhotonPCASigma2VV";
    mapKey["sc_sWW"]        = "TICLphoPCAProducer_HGCalPhotonPCASigma2WW";
    mapKey["clusIsoDR0p2"]  = "TICLphoClusIsoProducer_HGCalPhotonClusIso";
    mapKey["hByEdR0p15"]    = "TICLphoHoverEProducer_HGCalPhotonHoverE";
    
    spectators_ = {
    };
    
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

PhotonMVAIDProducerHGCal::~PhotonMVAIDProducerHGCal() {
  // do anything here that needs to be done at destruction time
  // (e.g. close files, deallocate resources etc.)
  //
  // please remove this method altogether if it would be left empty
}

//
// member functions
//

// ------------ method called to produce the data  ------------
void PhotonMVAIDProducerHGCal::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
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
    
    long long eventNumber = iEvent.id().event();
    
    
    edm::Handle <double> handle_rho;
    iEvent.getByToken(tok_rho_, handle_rho);
    double rho = *handle_rho;
    
    edm::Handle <std::vector <reco::PFRecHit> > h_PFRecHit;
    iEvent.getByToken(tok_PFRecHit_, h_PFRecHit);
    auto recHits = *h_PFRecHit;
    
    showerShapeHelper_.initPerEvent(
        iSetup,
        recHits
    );
    
    
    edm::Handle <std::vector <reco::Photon> > h_photon;
    iEvent.getByToken(tok_photon_, h_photon);
    auto photons = *h_photon;
    
    edm::Handle <edm::MapOfVectors <std::string, double> > h_varMap;
    iEvent.getByToken(tok_varMap_, h_varMap);
    edm::MapOfVectors <std::string, double> varMap = *h_varMap;
    
    int iPho = -1;
    int nPho = h_photon->size();
    
    std::map <std::string, float> inputs;
    std::vector <double> v_photonID;
    
    for(auto &pho : photons)
    {
        iPho++;
        
        if(pho.pt() < minPt_)
        {
            v_photonID.push_back(-99);
            continue;
        }
        
        if(debug_)
        {
            printf("[%llu] In PhotonMVAIDProducerHGCal --> Pho %d/%d: \n", eventNumber, iPho+1, nPho);
            printf(
                "    "
                "pT %0.4f, "
                "eta %+0.4f, "
                "phi %+0.4f, "
                "scE %+0.8f, "
                "scEta %+0.8f, "
                ,
                pho.pt(),
                pho.eta(),
                pho.phi(),
                pho.superCluster()->energy(),
                pho.superCluster()->eta()
            );
            printf("\n");
        }
        
        auto sc = pho.superCluster();
        math::XYZPoint superClus_xyz = sc->position();
        
        showerShapeHelper_.initPerObject(
            sc->hitsAndFractions()
        );
        
        std::vector <double> superClus_maxhitE = showerShapeHelper_.getEnergyHighestHits(2, true);
        
        inputs["sc_rawET"           ] = sc->rawEnergy() * std::sin(superClus_xyz.theta());
        inputs["sc_absEta"          ] = std::fabs(sc->eta());
        inputs["sc_nClus"           ] = sc->clusters().size();
        inputs["sc_nHit"            ] = sc->hitsAndFractions().size();
        inputs["sc_hit1_enFrac"     ] = superClus_maxhitE.at(0) / sc->rawEnergy();
        inputs["sc_hit2_enFrac"     ] = superClus_maxhitE.at(1) / sc->rawEnergy();
        inputs["sc_seed_dEta"       ] = sc->eta() - sc->seed().get()->eta();
        inputs["sc_seed_dPhi"       ] = ROOT::Math::VectorUtil::Phi_mpi_pi(sc->phi() - sc->seed().get()->phi());
        inputs["sc_seed_enFrac"     ] = sc->seed().get()->energy() / sc->rawEnergy();
        inputs["rho"                ]  = rho;
        
        for(auto const& iter : mapKey)
        {
            const std::string &key = iter.second;
            
            //if(debug_)
            //{
            //    printf("Adding to TMVA reader: %s. \n", key.c_str());
            //}
            
            if(varMap.find(key) == varMap.emptyRange())
            {
                printf("Error: Cannot find key \"%s\" in variable map. \n", key.c_str());
                exit(EXIT_FAILURE);
            }
            
            inputs[iter.first] = varMap.find(key)[iPho];
        }
        
        
        float mvaVal = tmvaEval.evaluateTMVA(inputs, false);
        
        if(debug_)
        {
            for(auto &key : variables_)
            {
                printf("    %s %0.8f \n", key.c_str(), inputs.at(key));
            }
            
            printf("    MVA: %0.8f \n", mvaVal);
        }
        
        v_photonID.push_back(mvaVal);
    }
    
    
    iEvent.put(
       std::make_unique <std::vector <double> >(v_photonID),
       instanceName_
    );
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void PhotonMVAIDProducerHGCal::beginStream(edm::StreamID) {
  // please remove this method if not needed
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void PhotonMVAIDProducerHGCal::endStream() {
  // please remove this method if not needed
}

// ------------ method called when starting to processes a run  ------------
/*
void
PhotonMVAIDProducerHGCal::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
PhotonMVAIDProducerHGCal::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
PhotonMVAIDProducerHGCal::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
PhotonMVAIDProducerHGCal::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void PhotonMVAIDProducerHGCal::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(PhotonMVAIDProducerHGCal);
