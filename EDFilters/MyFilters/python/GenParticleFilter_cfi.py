import FWCore.ParameterSet.Config as cms


GenParticleFilter = cms.EDFilter(
    "GenParticleFilter",
    
    label_generator = cms.untracked.InputTag("generator"),
    label_genParticle = cms.untracked.InputTag("genParticles"),
    
    atLeastN = cms.int32(1),
    pdgId = cms.int32(0),
    
    minEta = cms.double(0.0),
    maxEta = cms.double(9999.0),
    
    isGunSample = cms.bool(False),
    
    debug = cms.bool(False),
)
