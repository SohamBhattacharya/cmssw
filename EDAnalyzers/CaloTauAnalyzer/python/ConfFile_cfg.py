import os

import FWCore.ParameterSet.Config as cms

#from Configuration.StandardSequences.Eras import eras
#process = cms.Process("RECO", eras.Run2_2018)

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
MessageLogger = cms.Service("MessageLogger")

process.load("Configuration.Geometry.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("RecoJets.JetAssociationProducers.ak4JTA_cff")
#process.load("RecoJets.JetAssociationProducers.ic5JetTracksAssociatorAtVertex_cfi")
#process.load("RecoJets.JetProducers.ic5CaloJets_cfi")
process.load("RecoJets.JetProducers.ak4CaloJets_cfi")
process.load("RecoTauTag.Configuration.RecoCaloTauTag_cff")
process.load("RecoTracker.TrackProducer.CTFFinalFitWithMaterial_cfi")
process.load("RecoTracker.TransientTrackingRecHit.TransientTrackingRecHitBuilder_cfi")
process.load("RecoVertex.PrimaryVertexProducer.OfflinePrimaryVertices_cfi")
process.load("TrackingTools.TrackFitters.KFTrajectoryFitter_cfi")
process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")


#from RecoJets.JetAssociationProducers.ak4JTA_cff import *
#from RecoJets.JetProducers.ak4CaloJets_cfi import *


#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
#process.GlobalTag.globaltag = "100X_upgrade2018_realistic_v10"

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:run2_mc")

maxEvents = -1
#maxEvents = 1000
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(maxEvents))


#sourceFileNames = cms.untracked.vstring([
#    "",
#    "",
#])


#sourceFile = "sourceFiles/RelValZpTT_1500_13_CMSSW_10_0_2-100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO/RelValZpTT_1500_13_CMSSW_10_0_2-100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO.txt"
#sourceFile = "sourceFiles/RelValZpTT_1500_13_CMSSW_10_0_2-100X_upgrade2018_realistic_v10-v1_GEN-SIM-DIGI-RAW/RelValZpTT_1500_13_CMSSW_10_0_2-100X_upgrade2018_realistic_v10-v1_GEN-SIM-DIGI-RAW.txt"

#sourceFile = "sourceFiles/RelValZpTT_1500_13_CMSSW_10_0_2-PU25ns_100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO/RelValZpTT_1500_13_CMSSW_10_0_2-PU25ns_100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO.txt"

sourceFile = "sourceFiles/RelValZpTT_1500_13_CMSSW_10_1_0_pre1-PU25ns_100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO/RelValZpTT_1500_13_CMSSW_10_1_0_pre1-PU25ns_100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO.txt"
#sourceFile = "sourceFiles/RelValQCD_FlatPt_15_3000HS_13_CMSSW_10_1_0_pre2-PU25ns_100X_upgrade2018_realistic_v11-v1_GEN-SIM-RECO/RelValQCD_FlatPt_15_3000HS_13_CMSSW_10_1_0_pre2-PU25ns_100X_upgrade2018_realistic_v11-v1_GEN-SIM-RECO.txt"

#sourceFile = "sourceFiles/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_AODSIM/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_RunIISummer16DR80Premix-PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1_AODSIM.txt"
#sourceFile = "sourceFiles/SingleNeutrino_RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_GEN-SIM-RECO/SingleNeutrino_RunIISummer16DR80-FlatPU0to75TuneCP0_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v2_GEN-SIM-RECO.txt"


outDir = sourceFile[sourceFile.rfind("/")+1: sourceFile.rfind(".txt")]
outDir = "output/%s" %(outDir)
os.system("mkdir -p %s" %(outDir))

outFile = "%s/CaloTauAnalysis.root" %(outDir)
print "Output file:", outFile

fNames = []

with open(sourceFile) as f:
    
    fNames = f.readlines()

sourceFileNames = cms.untracked.vstring(fNames)

process.source = cms.Source("PoolSource",
    fileNames = sourceFileNames
)

process.caloTauAnalysis = cms.EDAnalyzer(
    "CaloTauAnalyzer",
    
    ############################## GEN ##############################
    label_genParticle = cms.untracked.InputTag("genParticles"),
    
    
    ############################## GEN ##############################
    label_primaryVertex = cms.untracked.InputTag("offlinePrimaryVertices"),
    label_pileUp = cms.untracked.InputTag("slimmedAddPileupInfo"),
    #label_pileUp = cms.untracked.InputTag("addPileupInfo"),
    
    label_caloTau = cms.untracked.InputTag("caloRecoTauProducer"),
    label_caloTauTagInfo = cms.untracked.InputTag("caloRecoTauTagInfoProducer"),
    
    label_caloRecoTauDiscriminationAgainstElectron = cms.untracked.InputTag("caloRecoTauDiscriminationAgainstElectron"),
    label_caloRecoTauDiscriminationAgainstMuon = cms.untracked.InputTag("caloRecoTauDiscriminationAgainstMuon"),
    label_caloRecoTauDiscriminationByECALIsolation = cms.untracked.InputTag("caloRecoTauDiscriminationByECALIsolation"),
    label_caloRecoTauDiscriminationByIsolation = cms.untracked.InputTag("caloRecoTauDiscriminationByIsolation"),
    label_caloRecoTauDiscriminationByLeadingTrackFinding = cms.untracked.InputTag("caloRecoTauDiscriminationByLeadingTrackFinding"),
    label_caloRecoTauDiscriminationByLeadingTrackPtCut = cms.untracked.InputTag("caloRecoTauDiscriminationByLeadingTrackPtCut"),
    label_caloRecoTauDiscriminationByTrackIsolation = cms.untracked.InputTag("caloRecoTauDiscriminationByTrackIsolation"),
    
    label_ak4PFJet = cms.untracked.InputTag("ak4PFJets"),
)


process.ak5CaloJets = process.ak4CaloJets.clone(
    rParam = 0.5
)

process.ak5JetTracksAssociatorAtVertex = process.ak4JetTracksAssociatorAtVertex.clone(
    coneSize = cms.double(0.5),
    jets = cms.InputTag("ak5CaloJets")
)

# Trace modules
#process.Tracer = cms.Service("Tracer")


process.p = cms.Path(
    #iterativeCone5CaloJets *
    #process.ic5JetTracksAssociatorAtVertex *
    
    #process.offlinePrimaryVertices *
    
    #process.ak4CaloJets *
    #process.ak4JetTracksAssociatorAtVertex *
    
    #process.ctfWithMaterialTracks *
    
    process.ak5CaloJets *
    process.ak5JetTracksAssociatorAtVertex *
    
    process.tautagging *
    process.caloTauAnalysis
)


# Output
process.TFileService = cms.Service("TFileService", fileName = cms.string(outFile))

process.schedule = cms.Schedule(process.p)

# Debug
#process.out = cms.OutputModule("PoolOutputModule", 
#    fileName = cms.untracked.string("debug.root")
#)
#
#process.output_step = cms.EndPath(process.out)
#process.schedule.extend([process.output_step])
