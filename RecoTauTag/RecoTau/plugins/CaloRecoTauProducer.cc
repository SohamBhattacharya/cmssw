/* class CaloRecoTauProducer
 * EDProducer of the CaloTauCollection, starting from the CaloTauTagInfoCollection, 
 * authors: Simone Gennai (simone.gennai@cern.ch), Ludovic Houchu (Ludovic.Houchu@cern.ch)
 */

#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"

#include "DataFormats/TauReco/interface/CaloTauTagInfo.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"

#include "TrackingTools/TransientTrack/interface/TransientTrackBuilder.h"
#include "TrackingTools/Records/interface/TransientTrackRecord.h"

#include "RecoTauTag/RecoTau/interface/CaloRecoTauAlgorithm.h"

#include "DataFormats/DetId/interface/DetIdCollection.h"

#include "CLHEP/Random/RandGauss.h"

#include <memory>

using namespace reco;
using namespace edm;
using namespace std;

class CaloRecoTauProducer : public EDProducer
{
    public:
    
    explicit CaloRecoTauProducer(const edm::ParameterSet& iConfig);
    ~CaloRecoTauProducer() override;
    void produce(edm::Event&,const edm::EventSetup&) override;
    
    
    private:
    
    //edm::InputTag CaloRecoTauTagInfoProducer_;
    edm::InputTag CaloRecoTauTagInfoProducerLabel;
    edm::EDGetTokenT <CaloTauTagInfoCollection> CaloRecoTauTagInfoProducerToken;
    
    //edm::InputTag PVProducer_;
    edm::InputTag PVProducerLabel;
    edm::EDGetTokenT <VertexCollection> PVProducerToken;
    
    
    double smearedPVsigmaX_;
    double smearedPVsigmaY_;
    double smearedPVsigmaZ_;
    double JetMinPt_;
    CaloRecoTauAlgorithm* CaloRecoTauAlgo_;
};

CaloRecoTauProducer::CaloRecoTauProducer(const edm::ParameterSet& iConfig)
{
    //CaloRecoTauTagInfoProducer_  = iConfig.getParameter<edm::InputTag>("CaloRecoTauTagInfoProducer");
    CaloRecoTauTagInfoProducerLabel = iConfig.getParameter<edm::InputTag>("CaloRecoTauTagInfoProducer");
    CaloRecoTauTagInfoProducerToken = consumes<CaloTauTagInfoCollection>(edm::InputTag(CaloRecoTauTagInfoProducerLabel));
    
    //PVProducer_                  = iConfig.getParameter<edm::InputTag>("PVProducer");
    PVProducerLabel = iConfig.getParameter<edm::InputTag>("PVProducer");
    PVProducerToken = consumes<VertexCollection>(edm::InputTag(PVProducerLabel));
    
    smearedPVsigmaX_             = iConfig.getParameter<double>("smearedPVsigmaX");
    smearedPVsigmaY_             = iConfig.getParameter<double>("smearedPVsigmaY");
    smearedPVsigmaZ_             = iConfig.getParameter<double>("smearedPVsigmaZ");	
    JetMinPt_                    = iConfig.getParameter<double>("JetPtMin");
    CaloRecoTauAlgo_=new CaloRecoTauAlgorithm(iConfig, consumesCollector());
    produces<CaloTauCollection>();
    produces<DetIdCollection>();
}

CaloRecoTauProducer::~CaloRecoTauProducer(){
  delete CaloRecoTauAlgo_;
}
  
void CaloRecoTauProducer::produce(edm::Event& iEvent,const edm::EventSetup& iSetup)
{
    //printf("Entering CaloRecoTauProducer::produce(...). \n");
    
    auto resultCaloTau = std::make_unique<CaloTauCollection>();
    auto selectedDetIds = std::make_unique<DetIdCollection>();
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 1.0 \n");
    
    edm::ESHandle<TransientTrackBuilder> myTransientTrackBuilder;
    iSetup.get<TransientTrackRecord>().get("TransientTrackBuilder",myTransientTrackBuilder);
    CaloRecoTauAlgo_->setTransientTrackBuilder(myTransientTrackBuilder.product());
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 2.0 \n");
    
    edm::ESHandle<MagneticField> myMF;
    iSetup.get<IdealMagneticFieldRecord>().get(myMF);
    CaloRecoTauAlgo_->setMagneticField(myMF.product());
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 3.0 \n");
    
    // query a rec/sim PV
    edm::Handle<VertexCollection> thePVs;
    //iEvent.getByLabel(PVProducer_,thePVs);
    iEvent.getByToken(PVProducerToken, thePVs);
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 4.0 \n");
    
    const VertexCollection vertCollection=*(thePVs.product());
    Vertex thePV;
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 5.0 \n");
    
    if(!vertCollection.empty()) thePV=*(vertCollection.begin());
    
    else
    {
        Vertex::Error SimPVError;
        SimPVError(0,0)=smearedPVsigmaX_*smearedPVsigmaX_;
        SimPVError(1,1)=smearedPVsigmaY_*smearedPVsigmaY_;
        SimPVError(2,2)=smearedPVsigmaZ_*smearedPVsigmaZ_;
        
        Vertex::Point SimPVPoint(
            CLHEP::RandGauss::shoot(0.,smearedPVsigmaX_),  
            CLHEP::RandGauss::shoot(0.,smearedPVsigmaY_),  
            CLHEP::RandGauss::shoot(0.,smearedPVsigmaZ_)
        );
        
        thePV=Vertex(SimPVPoint,SimPVError,1,1,1);    
    }
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 6.0 \n");
    
    edm::Handle<CaloTauTagInfoCollection> theCaloTauTagInfoCollection;
    //iEvent.getByLabel(CaloRecoTauTagInfoProducer_,theCaloTauTagInfoCollection);
    iEvent.getByToken(CaloRecoTauTagInfoProducerToken, theCaloTauTagInfoCollection);
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 7.0 \n");
    
    int iinfo=0;
    
    for(CaloTauTagInfoCollection::const_iterator i_info=theCaloTauTagInfoCollection->begin();i_info!=theCaloTauTagInfoCollection->end();i_info++)
    { 
        if(i_info->jetRef()->pt()>JetMinPt_)
        { 
            CaloTau myCaloTau=CaloRecoTauAlgo_->buildCaloTau(iEvent,iSetup,Ref<CaloTauTagInfoCollection>(theCaloTauTagInfoCollection,iinfo),thePV);
            resultCaloTau->push_back(myCaloTau);
        }
        ++iinfo;
    }
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 8.0 \n");
    
    for(unsigned int i =0;i<CaloRecoTauAlgo_->mySelectedDetId_.size();i++)
        selectedDetIds->push_back(CaloRecoTauAlgo_->mySelectedDetId_[i]);
    
    //printf("Inside CaloRecoTauProducer::produce(...). Stage 9.0 \n");
    
    iEvent.put(std::move(resultCaloTau));
    iEvent.put(std::move(selectedDetIds));
    
    //printf("Exiting CaloRecoTauProducer::produce(...). \n");
}

DEFINE_FWK_MODULE(CaloRecoTauProducer);
