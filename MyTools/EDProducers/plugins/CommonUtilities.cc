# include "MyTools/EDProducers/plugins/CommonUtilities.h"



namespace CommonUtilities
{
    std::map <DetId, int> getPFRecHitIndexMap(edm::Handle <std::vector <reco::PFRecHit> > v_recHit)
    {
        std::map <DetId, int> m_recHitIdx;
        
        int nHit = v_recHit->size();
        
        for(int iHit = 0; iHit < nHit; iHit++)
        {
            const reco::PFRecHit recHit = v_recHit->at(iHit);
            
            DetId hitId(recHit.detId());
            
            m_recHitIdx[hitId] = iHit;
        }
        
        return m_recHitIdx;
    }
    
    
    std::map <DetId, const HGCRecHit*> getHGCRecHitPtrMap(
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCEERecHit,
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCHEFRecHit,
        edm::Handle <edm::SortedCollection <HGCRecHit,edm::StrictWeakOrdering <HGCRecHit> > > v_HGCHEBRecHit
    )
    {
        std::map <DetId, const HGCRecHit*> m_recHit;
        
        int nHGCEERecHit = v_HGCEERecHit->size();
        
        for(int iRecHit = 0; iRecHit < nHGCEERecHit; iRecHit++)
        {
            const HGCRecHit *recHit = &(*v_HGCEERecHit)[iRecHit];
            
            m_recHit[recHit->id()] = recHit;
        }
        
        
        //
        int nHGCHEFRecHit = v_HGCHEFRecHit->size();
        
        for(int iRecHit = 0; iRecHit < nHGCHEFRecHit; iRecHit++)
        {
            const HGCRecHit *recHit = &(*v_HGCHEFRecHit)[iRecHit];
            
            m_recHit[recHit->id()] = recHit;
        }
        
        
        //
        int nHGCHEBRecHit = v_HGCHEBRecHit->size();
        
        for(int iRecHit = 0; iRecHit < nHGCHEBRecHit; iRecHit++)
        {
            const HGCRecHit *recHit = &(*v_HGCHEBRecHit)[iRecHit];
            
            m_recHit[recHit->id()] = recHit;
        }
        
        
        return m_recHit;
    }
}
