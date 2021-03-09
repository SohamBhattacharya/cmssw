import FWCore.ParameterSet.Config as cms



def customize_eleEBID(process, processName = "") :
    
    process.electronMVAIDProducerEB = cms.EDProducer(
        "ElectronMVAIDProducerEB",
        
        instanceName = cms.string(""),
        
        effAreaFile = cms.string("MyTools/EDProducers/data/EffectiveArea_electrons_barrel_PhaseII.txt"),
        
        electrons = cms.InputTag("slimmedElectrons"),
        beamSpot = cms.InputTag("offlineBeamSpot"),
        conversions = cms.InputTag("allConversions"),
        vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        
        recHitsEB = cms.InputTag("reducedEgamma", "reducedEBRecHits"),
        recHitsEE = cms.InputTag("reducedEgamma", "reducedEERecHits"),
        recHitsES = cms.InputTag("reducedEgamma", "reducedESRecHits"),
        
        minPt = cms.double(0.0),
        
        debug = cms.bool(True),
    )
    
    process.eleEBID_seq = cms.Sequence(
        process.electronMVAIDProducerEB
    )
    
    return process


def customize_phoEBID(process, processName = "") :
    
    process.photonMVAIDProducerEB = cms.EDProducer(
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
    
    process.phoEBID_seq = cms.Sequence(
        process.photonMVAIDProducerEB
    )
    
    return process
