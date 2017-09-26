import FWCore.ParameterSet.Config as cms
from  PhysicsTools.NanoAOD.common_cff import *



##################### User floats producers, selectors ##########################

mergedGenParticles = cms.EDProducer("MergedGenParticleProducer",
    inputPruned = cms.InputTag("prunedGenParticles"),
    inputPacked = cms.InputTag("packedGenParticles"),
)

genParticles2HepMC = cms.EDProducer("GenParticles2HepMCConverter",
    genParticles = cms.InputTag("mergedGenParticles"),
    genEventInfo = cms.InputTag("generator"),
    signalParticlePdgIds = cms.vint32(),
)

particleLevel = cms.EDProducer("ParticleLevelProducer",
    src = cms.InputTag("genParticles2HepMC:unsmeared"),
    
    usePromptFinalStates = cms.bool(True), # for leptons, photons, neutrinos
    excludePromptLeptonsFromJetClustering = cms.bool(True),
    excludeNeutrinosFromJetClustering = cms.bool(True),
    
    particleMinPt  = cms.double(0.),
    particleMaxEta = cms.double(5.), # HF range. Maximum 6.0 on MiniAOD
    
    lepConeSize = cms.double(0.1), # for photon dressing
    lepMinPt    = cms.double(15.),
    lepMaxEta   = cms.double(2.5),
    
    jetConeSize = cms.double(0.4),
    jetMinPt    = cms.double(20.),
    jetMaxEta   = cms.double(2.4),
    
    fatJetConeSize = cms.double(0.8),
    fatJetMinPt    = cms.double(200.),
    fatJetMaxEta   = cms.double(2.4),
)



##################### Tables for final output and docs ##########################
rivetLeptonTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("particleLevel:leptons"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("RivetDressedLepton"),
    doc = cms.string("Dressed leptons from Rivet-based ParticleLevelProducer"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table
    variables = cms.PSet(
        P4Vars,
        pdgId = Var("pdgId", int, doc="PDG id"), 
    )
)

rivetJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("particleLevel:jets"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("RivetJet"),
    doc = cms.string("AK4 jets from Rivet-based ParticleLevelProducer"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table
    variables = cms.PSet(
        P4Vars,
        pdgId = Var("pdgId", int, doc="PDG id"), 
    )
)

rivetFatJetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("particleLevel:fatjets"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("RivetFatJet"),
    doc = cms.string("AK8 jets from Rivet-based ParticleLevelProducer"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table
    variables = cms.PSet(
        P4Vars,
        pdgId = Var("pdgId", int, doc="PDG id"), 
    )
)

rivetTagTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("particleLevel:tags"),
    cut = cms.string(""), #we should not filter after pruning
    name= cms.string("RivetTag"),
    doc = cms.string("Tag particles from Rivet-based ParticleLevelProducer, momenta scaled down by 10e-20"),
    singleton = cms.bool(False), # the number of entries is variable
    extension = cms.bool(False), # this is the main table
    variables = cms.PSet(
        P4Vars,
        pdgId = Var("pdgId", int, doc="PDG id"), 
    )
)

rivetMetTable = cms.EDProducer("SimpleCandidateFlatTableProducer",
    src = cms.InputTag("particleLevel:mets"),
    name = cms.string("RivetMET"),
    doc = cms.string("MET from Rivet-based ParticleLevelProducer"),
    singleton = cms.bool(True),  # there's always exactly one MET per event
    extension = cms.bool(False), # this is the main table
    variables = cms.PSet(
       pt  = Var("pt",  float, precision=10),
       phi = Var("phi", float, precision=10),
    ),
)

particleLevelSequence = cms.Sequence(mergedGenParticles + genParticles2HepMC + particleLevel)
particleLevelTables = cms.Sequence(rivetLeptonTable + rivetJetTable + rivetFatJetTable + rivetTagTable + rivetMetTable)

