import FWCore.ParameterSet.Config as cms

from RecoParticleFlow.PFClusterProducer.particleFlowRecHitHGC_cfi import *
from RecoParticleFlow.PFClusterProducer.particleFlowClusterHGC_cfi import *
from RecoEcal.EgammaClusterProducers.particleFlowSuperClusteringSequence_cff import *
from RecoEgamma.EgammaElectronProducers.ecalDrivenElectronSeeds_cfi import *
from RecoParticleFlow.PFTracking.mergedElectronSeeds_cfi import *
from TrackingTools.GsfTracking.CkfElectronCandidateMaker_cff import *
from TrackingTools.GsfTracking.GsfElectronGsfFit_cff import *
from RecoEgamma.EgammaElectronProducers.gsfElectronCores_cfi import *
from RecoEgamma.EgammaElectronProducers.gsfElectrons_cfi import *


particleFlowClusterHGCalFromTICL         = particleFlowClusterHGCalFromMultiCl.clone()
particleFlowSuperClusterHGCalFromTICL    = particleFlowSuperClusterHGCalFromMultiCl.clone()
ecalDrivenElectronSeedsFromTICL          = ecalDrivenElectronSeedsFromMultiCl.clone()
electronMergedSeedsFromTICL              = electronMergedSeedsFromMultiCl.clone()
electronCkfTrackCandidatesFromTICL       = electronCkfTrackCandidatesFromMultiCl.clone()
electronGsfTracksFromTICL                = electronGsfTracksFromMultiCl.clone()
ecalDrivenGsfElectronCoresFromTICL       = ecalDrivenGsfElectronCoresFromMultiCl.clone()
ecalDrivenGsfElectronsFromTICL           = ecalDrivenGsfElectronsFromMultiCl.clone()


particleFlowClusterHGCalFromTICL.initialClusteringStep.clusterSrc = cms.InputTag("MultiClustersFromTracksters", "MultiClustersFromTracksterByCA", "RECO")
particleFlowSuperClusterHGCalFromTICL.PFClusters = cms.InputTag("particleFlowClusterHGCalFromTICL")
particleFlowSuperClusterHGCalFromTICL.use_preshower = cms.bool(False)
ecalDrivenElectronSeedsFromTICL.endcapSuperClusters = "particleFlowSuperClusterHGCalFromTICL"
electronMergedSeedsFromTICL.EcalBasedSeeds = "ecalDrivenElectronSeedsFromTICL"
electronCkfTrackCandidatesFromTICL.src = "electronMergedSeedsFromTICL"
electronGsfTracksFromTICL.src = "electronCkfTrackCandidatesFromTICL"
ecalDrivenGsfElectronCoresFromTICL.gsfTracks = "electronGsfTracksFromTICL"
ecalDrivenGsfElectronsFromTICL.gsfElectronCoresTag = "ecalDrivenGsfElectronCoresFromTICL"

ecalDrivenGsfElectronsFromTICL_step = cms.Path(
    particleFlowClusterHGCalFromTICL *
    particleFlowSuperClusterHGCalFromTICL *
    ecalDrivenElectronSeedsFromTICL *
    electronMergedSeedsFromTICL *
    electronCkfTrackCandidatesFromTICL *
    electronGsfTracksFromTICL *
    ecalDrivenGsfElectronCoresFromTICL *
    ecalDrivenGsfElectronsFromTICL
)

