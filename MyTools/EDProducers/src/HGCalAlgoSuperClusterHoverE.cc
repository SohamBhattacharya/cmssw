# include "MyTools/EDProducers/interface/HGCalAlgoSuperClusterHoverE.h"


HGCalAlgoSuperClusterHoverE::HGCalAlgoSuperClusterHoverE(
    const edm::ParameterSet &iConfig
)
{
    coneDR_ = iConfig.getParameter <double>("coneDR");
    coneDR2_ = coneDR_*coneDR_;
    
    minClusE_ = iConfig.getParameter <double>("minClusE");
    minClusET_ = iConfig.getParameter <double>("minClusET");
    
    debug_ = iConfig.getParameter <bool>("debug");
}


double HGCalAlgoSuperClusterHoverE::getClusterBasedHoverE(
    const reco::SuperClusterRef &superClus,
    const std::vector <reco::CaloCluster> &layerClusters
)
{
    double HoverE = 0;
    
    double superClus_E = superClus->energy();
    double superClus_eta = superClus->eta();
    double superClus_phi = superClus->phi();
    
    for(auto &cluster : layerClusters)
    {
        // E cut
        if(cluster.energy() < minClusE_)
        {
            continue;
        }
        
        // HE layers
        if(!(cluster.seed().det() == DetId::HGCalHSi || cluster.seed().det() == DetId::HGCalHSc))
        {
            continue;
        }
        
        // ET cut
        double clusET = cluster.energy() * std::sin(cluster.position().theta());
        
        if(clusET < minClusET_)
        {
            continue;
        }
        
        // dR cut
        double dR2 = reco::deltaR2(superClus_eta, superClus_phi, cluster.eta(), cluster.phi());
        
        if(dR2 > coneDR2_)
        {
            continue;
        }
        
        HoverE += cluster.energy();
    }
    
    
    if(superClus_E)
    {
        HoverE /= superClus_E;
    }
    
    else
    {
        HoverE = std::numeric_limits<double>::max();
    }
    
    
    return HoverE;
}
