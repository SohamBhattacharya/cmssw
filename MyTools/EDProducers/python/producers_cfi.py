import FWCore.ParameterSet.Config as cms


HoverE = cms.EDProducer(
    "HGCalElectronHoverEProducer",
    
    instanceName = cms.string("HGCalElectronHoverEProducer"),
    
    electrons = cms.InputTag("ecalDrivenGsfElectronsFromMultiCl"),
    layerClusters = cms.InputTag("hgcalLayerClusters"),
    
    coneDR = cms.double(0.15),
    
    minClusE = cms.double(0.0),
    minClusET = cms.double(0.0),
    
    debug = cms.bool(False),
)


trackIso = cms.EDProducer(
    "HGCalElectronTrackIsoProducer",
    
    instanceName = cms.string("HGCalElectronTrackIsoProducer"),
    
    electrons = cms.InputTag("ecalDrivenGsfElectronsFromMultiCl"),
    tracks = cms.InputTag("generalTracks"),
    
    isoConeDR = cms.double(0.3),
    vetoConeDR = cms.double(0.01),
    vetoPhiStripDeta = cms.double(0.03),
    
    minTrackPt = cms.double(1.0),
    maxTrackEleDz = cms.double(0.15),
    
    debug = cms.bool(False),
)


Rvar = cms.EDProducer(
    "HGCalElectronRvarProducer",
    
    instanceName = cms.string("HGCalElectronRvarProducer"),
    
    electrons = cms.InputTag("ecalDrivenGsfElectronsFromMultiCl"),
    
    PFRecHits = cms.InputTag("particleFlowRecHitHGC"),
    HGCEERecHits = cms.untracked.InputTag("HGCalRecHit", "HGCEERecHits"),
    HGCHEFRecHits = cms.untracked.InputTag("HGCalRecHit", "HGCHEFRecHits"),
    HGCHEBRecHits = cms.untracked.InputTag("HGCalRecHit", "HGCHEBRecHits"),
    
    cylinderR = cms.double(2.8),
    nLayer = cms.int32(28),
    
    minHitE = cms.double(0.0),
    minHitET = cms.double(0.0),
    
    debug = cms.bool(False),
)


mapProducer = cms.EDProducer(
    "MapProducer",
    
    instanceName = cms.string("MapProducer"),
    
    collections = cms.VInputTag(),
    
    debug = cms.bool(False),
)
