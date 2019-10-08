# ifndef Common_H
# define Common_H


# include <algorithm>
# include <iostream>
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


namespace Common
{
    template <typename T1, typename T2> std::vector <int> associateRecToSimHit(
        T1 simHitCollPtr,
        T2 recHitCollPtr
    )
    {
        int nSimHit = simHitCollPtr->size();
        int nRecHit = recHitCollPtr->size();
        
        std::vector <int> v_matchedSimHitIndex(nRecHit, -1);
        
        # pragma omp parallel for
        for(int iRecHit = 0; iRecHit < nRecHit; iRecHit++)
        {
            auto recHit = (*recHitCollPtr)[iRecHit];
            
            unsigned int recHitId = recHit.id();
            
            for(int iSimHit = 0; iSimHit < nSimHit; iSimHit++)
            {
                auto simHit = (*simHitCollPtr)[iSimHit];
                
                unsigned int simHitId = simHit.id();
                
                if(recHitId == simHitId)
                {
                    v_matchedSimHitIndex.at(iRecHit) = iSimHit;
                    
                    break;
                }
            }
        }
        
        fflush(stdout);
        fflush(stderr);
        
        return v_matchedSimHitIndex;
    }
    
    
    // PCA
    // Returns <(r, eta, phi) cov matrix, eigen vector matrix, eigen values>
    std::tuple <TMatrixD, TMatrixD, TVectorD> getMultiClusterPCAinfo(
        reco::HGCalMultiCluster *multiCluster,
        std::map <DetId, const HGCRecHit*> m_recHit,
        hgcal::RecHitTools *recHitTools,
        bool debug = false
    )
    {
        double recHit_meanDrSq = 0;
        double recHit_meanDetaSq = 0;
        double recHit_meanDphiSq = 0;
        
        double recHit_meanDrDeta = 0;
        double recHit_meanDrDphi = 0;
        double recHit_meanDetaDphi = 0;
        
        edm::PtrVector <reco::CaloCluster> v_cluster = multiCluster->clusters();
        
        int nCluster = v_cluster.size();
        
        CLHEP::Hep3Vector multiCluster_3mom(
            multiCluster->x(),
            multiCluster->y(),
            multiCluster->z()
        );
        
        int nHitTotal = 0;
        double totE = 0;
        
        for(int iCluster = 0; iCluster < nCluster; iCluster++)
        {
            auto cluster = v_cluster[iCluster].get();
            std::vector <std::pair <DetId, float> > v_clusterHit = cluster->hitsAndFractions();
            
            int nClusterHit = v_clusterHit.size();
            
            for(int iClusterHit = 0; iClusterHit < nClusterHit; iClusterHit++)
            {
                if(m_recHit.find(v_clusterHit.at(iClusterHit).first) == m_recHit.end())
                {
                    printf("Warning in Common::getMultiClusterPCAinfo(...): Cluster-hit not in rec-hit map. \n");
                    //exit(EXIT_FAILURE);
                    continue;
                }
                
                const HGCRecHit *recHit = m_recHit[v_clusterHit.at(iClusterHit).first];
                
                auto position = recHitTools->getPosition(recHit->id());
                
                CLHEP::Hep3Vector recHit_3mom(
                    position.x(),
                    position.y(),
                    position.z()
                );
                
                double dR = multiCluster_3mom.r() - recHit_3mom.r();
                double dEta = multiCluster_3mom.eta() - recHit_3mom.eta();
                double dPhi = multiCluster_3mom.deltaPhi(recHit_3mom);
                
                recHit_meanDrSq   += recHit->energy() * dR*dR;
                recHit_meanDetaSq += recHit->energy() * dEta*dEta;
                recHit_meanDphiSq += recHit->energy() * dPhi*dPhi;
                
                recHit_meanDrDeta   += recHit->energy() * dR*dEta;
                recHit_meanDrDphi   += recHit->energy() * dR*dPhi;
                recHit_meanDetaDphi += recHit->energy() * dEta*dPhi;
                
                nHitTotal++;
                totE += recHit->energy();
            }
        }
        
        if(totE > 0)
        {
            recHit_meanDrSq /= totE;
            recHit_meanDetaSq /= totE;
            recHit_meanDphiSq /= totE;
            
            recHit_meanDrDeta /= totE;
            recHit_meanDrDphi /= totE;
            recHit_meanDetaDphi /= totE;
        }
        
        else
        {
            recHit_meanDrSq = 0;
            recHit_meanDetaSq = 0;
            recHit_meanDphiSq = 0;
            
            recHit_meanDrDeta = 0;
            recHit_meanDrDphi = 0;
            recHit_meanDetaDphi = 0;
            
            printf("Warning in Common::getMultiClusterPCAinfo(...): Encountered multicluster with zero energy. \n");
        }
        
        int dimension = 3;
        
        // Covariance matrix
        TMatrixD mat_multiClus_rEtaPhiCov(dimension, dimension);
        
        mat_multiClus_rEtaPhiCov(0, 0) = recHit_meanDrSq;
        mat_multiClus_rEtaPhiCov(1, 1) = recHit_meanDetaSq;
        mat_multiClus_rEtaPhiCov(2, 2) = recHit_meanDphiSq;
        
        mat_multiClus_rEtaPhiCov(0, 1) = mat_multiClus_rEtaPhiCov(1, 0) = recHit_meanDrDeta;
        mat_multiClus_rEtaPhiCov(0, 2) = mat_multiClus_rEtaPhiCov(2, 0) = recHit_meanDrDphi;
        mat_multiClus_rEtaPhiCov(1, 2) = mat_multiClus_rEtaPhiCov(2, 1) = recHit_meanDetaDphi;
        
        
        // Get eigen values and vectors
        TVectorD v_multiClus_rEtaPhiCov_eigVal(dimension);
        TMatrixD mat_multiClus_rEtaPhiCov_eigVec(dimension, dimension);
        
        if(totE > 0 && multiCluster->energy() > 0)
        {
            try
            {
                mat_multiClus_rEtaPhiCov_eigVec = mat_multiClus_rEtaPhiCov.EigenVectors(v_multiClus_rEtaPhiCov_eigVal);
            }
            
            catch(...)
            {
                printf("Error in Common::getMultiClusterPCAinfo(...): Cannot get eigen values and vectors. \n");
                
                printf(
                    "Multicluster: "
                    "E %0.2e, "
                    "x %0.2e, y %0.2e, z %0.2e \n",
                    multiCluster->energy(),
                    multiCluster_3mom.x(), multiCluster_3mom.y(), multiCluster_3mom.z()
                );
                
                printf("recHit_meanDrSq %0.2f \n", recHit_meanDrSq);
                printf("recHit_meanDetaSq %0.2f \n", recHit_meanDetaSq);
                printf("recHit_meanDphiSq %0.2f \n", recHit_meanDphiSq);
                printf("recHit_meanDrDeta %0.2f \n", recHit_meanDrDeta);
                printf("recHit_meanDrDphi %0.2f \n", recHit_meanDrDphi);
                printf("recHit_meanDetaDphi %0.2f \n", recHit_meanDetaDphi);
                
                //printf("Total energy: %0.2f \n", totE);
                
                mat_multiClus_rEtaPhiCov.Print();
                
                fflush(stdout);
                fflush(stderr);
            }
        }
        
        if(debug)
        {
            printf("In Common::getMultiClusterPCAinfo(...): \n");
            
            printf(
                "Multicluster: "
                "E %0.2e, "
                "x %0.2e, y %0.2e, z %0.2e \n",
                multiCluster->energy(),
                multiCluster_3mom.x(), multiCluster_3mom.y(), multiCluster_3mom.z()
            );
            
            printf("Covariance matrix: \n");
            mat_multiClus_rEtaPhiCov.Print();
            
            printf("Eigen values: \n");
            v_multiClus_rEtaPhiCov_eigVal.Print();
            
            printf("Eigen vectors: \n");
            mat_multiClus_rEtaPhiCov_eigVec.Print();
            
            fflush(stdout);
            fflush(stderr);
        }
        
        auto info = std::make_tuple(
            mat_multiClus_rEtaPhiCov,
            mat_multiClus_rEtaPhiCov_eigVec,
            v_multiClus_rEtaPhiCov_eigVal
        );
        
        fflush(stdout);
        fflush(stderr);
        
        return info;
    }
}


# endif
