import FWCore.ParameterSet.Config as cms

from RecoEcal.EgammaClusterProducers.hybridSuperClusters_cfi import cleanedHybridSuperClusters
from RecoEcal.EgammaClusterProducers.multi5x5BasicClusters_cfi import multi5x5BasicClustersCleaned

from RecoEgamma.EgammaIsolationAlgos.electronTrackIsolations_cfi import trkIsol03CfgV1,trkIsol04CfgV1,trkIsol03CfgV2,trkIsol04CfgV2

from RecoEgamma.EgammaElectronProducers.gsfElectronProducer_cfi import gsfElectronProducer

#==============================================================================
# Producer of transient ecal driven gsf electrons
#==============================================================================

ecalDrivenGsfElectrons = gsfElectronProducer.clone(

    # Ecal rec hits configuration
    recHitFlagsToBeExcludedBarrel = cleanedHybridSuperClusters.RecHitFlagToBeExcluded,
    recHitFlagsToBeExcludedEndcaps = multi5x5BasicClustersCleaned.RecHitFlagToBeExcluded,
    recHitSeverityToBeExcludedBarrel = cleanedHybridSuperClusters.RecHitSeverityToBeExcluded,
    recHitSeverityToBeExcludedEndcaps = cleanedHybridSuperClusters.RecHitSeverityToBeExcluded,

    # Isolation algos configuration
    trkIsol03Cfg = trkIsol03CfgV1,
    trkIsol04Cfg = trkIsol04CfgV1,
    trkIsolHEEP03Cfg = trkIsol03CfgV2,
    trkIsolHEEP04Cfg = trkIsol04CfgV2,
)

from Configuration.Eras.Modifier_pp_on_AA_2018_cff import pp_on_AA_2018
pp_on_AA_2018.toModify(ecalDrivenGsfElectrons.preselection, minSCEtBarrel = 15.0)
pp_on_AA_2018.toModify(ecalDrivenGsfElectrons.preselection, minSCEtEndcaps = 15.0)

ecalDrivenGsfElectronsFromMultiCl = ecalDrivenGsfElectrons.clone(
  gsfElectronCoresTag = "ecalDrivenGsfElectronCoresFromMultiCl",
)


from Configuration.Eras.Modifier_phase2_hgcal_cff import phase2_hgcal

phase2_hgcal.toModify(
    ecalDrivenGsfElectronsFromMultiCl,
    
    useGsfPfRecTracks = cms.bool(False),
    ambClustersOverlapStrategy = cms.uint32(0),
    applyAmbResolution = cms.bool(True),
    applyPreselection = cms.bool(False),
    ignoreNotPreselected = cms.bool(False),
)
