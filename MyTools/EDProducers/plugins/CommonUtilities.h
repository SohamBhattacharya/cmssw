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
    
    
    // Shamelessly copied from:
    // https://stackoverflow.com/questions/12015195/how-to-call-member-function-only-if-object-happens-to-have-it
    /*! The template `has_void_foo_no_args_const<T>` exports a
        boolean constant `value` that is true iff `T` provides
        `void foo() const`
    
        It also provides `static void eval(T const & t)`, which
        invokes void `T::foo() const` upon `t` if such a public member
        function exists and is a no-op if there is no such member.
    */ 
    template< typename T>
    struct RecHitTools_has_getEventSetup
    {
        /* SFINAE foo-has-correct-sig :) */
        template<typename A>
        static std::true_type test(void (A::*)() const) {
            return std::true_type();
        }
        
        /* SFINAE getEventSetup-exists :) */
        template <typename A> 
        static decltype(test(&A::getEventSetup)) 
        test(decltype(&A::getEventSetup),void *) {
            /* getEventSetup exists. What about sig? */
            typedef decltype(test(&A::getEventSetup)) return_type; 
            return return_type();
        }
        
        /* SFINAE game over :( */
        template<typename A>
        static std::false_type test(...) {
            return std::false_type(); 
        }
        
        /* This will be either `std::true_type` or `std::false_type` */
        typedef decltype(test<T>(0,0)) type;
        
        static const bool value = type::value; /* Which is it? */
        
        /*  `eval(T const &,std::true_type)` 
            delegates to `T::getEventSetup()` when `type` == `std::true_type`
        */
        static void eval(T const & t, const edm::EventSetup *iSetup, std::true_type) {
            t.getEventSetup(*iSetup);
        }
        /* `eval(...)` is a no-op for otherwise unmatched arguments */ 
        static void eval(...){
            // This output for demo purposes. Delete
            //std::cout << "T::getEventSetup() not called" << std::endl;        
        }
    
        /* `eval(T const & t)` delegates to :-
            - `eval(t,type()` when `type` == `std::true_type`
            - `eval(...)` otherwise
        */  
        static void eval(T const & t, const edm::EventSetup *iSetup) {
            eval(t, iSetup, type());
        }
    };
    
    // This is the desired implementation of `void f(T const& val)` 
    void initRecHitTools(
        hgcal::RecHitTools &recHitTools,
        const edm::EventSetup *iSetup
    );
    
    
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
