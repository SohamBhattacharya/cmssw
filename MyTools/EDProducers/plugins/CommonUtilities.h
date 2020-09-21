# ifndef CommonUtilities_H
# define CommonUtilities_H

# include "CommonTools/UtilAlgos/interface/TFileService.h"
# include "DataFormats/CaloTowers/interface/CaloTowerDefs.h"
# include "DataFormats/EgammaCandidates/interface/GsfElectron.h"
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
# include "FWCore/ParameterSet/interface/ParameterSet.h"
# include "FWCore/ServiceRegistry/interface/Service.h"
# include "FWCore/Utilities/interface/InputTag.h"
# include "Geometry/CaloTopology/interface/HGCalTopology.h"
# include "Geometry/Records/interface/IdealGeometryRecord.h"
# include "RecoLocalCalo/HGCalRecAlgos/interface/RecHitTools.h"
# include "SimDataFormats/CaloAnalysis/interface/CaloParticle.h"
# include "SimDataFormats/CaloAnalysis/interface/SimCluster.h"
# include "SimDataFormats/CaloHit/interface/PCaloHit.h"
# include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
# include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

# include <algorithm>
//# include <iostream>
# include <map>
# include <stdlib.h>
# include <string>
# include <type_traits>
# include <utility>
# include <vector>

# include <TH1F.h>
# include <TH2F.h>
# include <TMatrixD.h>
# include <TTree.h>
# include <TVectorD.h>
# include <Math/Point3D.h>
# include <Math/Point3Dfwd.h>



namespace CommonUtilities
{
    // SFINAE test
    // From https://stackoverflow.com/questions/257288/templated-check-for-the-existence-of-a-class-member-function
    //template <typename T>
    //class RecHitTools_has_getEventSetup
    //{
    //    private :
    //    
    //    typedef char one;
    //    
    //    struct two
    //    {
    //        char x[2];
    //    };
    //    
    //    template <typename C> static one test(decltype(&C::getEventSetup));
    //    template <typename C> static two test(...);
    //    
    //    
    //    public:
    //    
    //    enum
    //    {
    //        value = sizeof(test<T>(0)) == sizeof(char)
    //    };
    //};
    //
    //template<class T>
    //auto runFunction(T* obj)
    //-> decltype(  obj->toString()  )
    //{
    //    return     obj->toString();
    //}
    //auto optionalToString(...) -> string
    //{
    //    return "toString not defined";
    //}
    
    
    //typedef std::map <std::string, std::vector <double> > MyVarMap;
    
    
    std::map <DetId, int> getPFRecHitIndexMap(
        edm::Handle <std::vector <reco::PFRecHit> > v_recHit
    );
    
    
    std::map <DetId, const HGCRecHit*> getHGCRecHitPtrMap(
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCEERecHit,
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCHEFRecHit,
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCHEBRecHit
    );
}


# endif
