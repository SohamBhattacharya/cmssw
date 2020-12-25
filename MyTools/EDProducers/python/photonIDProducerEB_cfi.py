import FWCore.ParameterSet.Config as cms


photonMVAIDProducerEB = cms.EDProducer(
    "PhotonMVAIDProducerEB",
    
    instanceName = cms.string(""),
    
    weightFile = cms.string("MyTools/EDProducers/data/PhotonID_MVA_barrel_Egamma_PhaseII_weight.xml"),
    
    photons = cms.InputTag("slimmedPhotons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    
    recHitsEB = cms.InputTag("reducedEgamma", "reducedEBRecHits"),
    recHitsEE = cms.InputTag("reducedEgamma", "reducedEERecHits"),
    recHitsES = cms.InputTag("reducedEgamma", "reducedESRecHits"),
    
    minPt = cms.double(0.0),
    
    debug = cms.bool(False),
)
