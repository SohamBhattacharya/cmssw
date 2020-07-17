import os

import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras
#process = cms.Process("RECO", eras.Run2_2017)
#process = cms.Process("RECO", eras.Run2_2018)

#process = cms.Process("Demo", eras.phase2_hgcal)
#process = cms.Process("Demo", eras.Phase2C8_timing_layer_bar)
process = cms.Process("Demo", eras.Phase2C9)

#process = cms.Process("RECO", eras.Phase2C8_timing_layer_bar)

process.load("FWCore.MessageService.MessageLogger_cfi")
MessageLogger = cms.Service("MessageLogger")


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
##process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
##process.load('SimGeneral.MixingModule.mixNoPU_cfi')
##process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
##process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
#process.GlobalTag.globaltag = "94X_mc2017_realistic_v10"
#process.GlobalTag.globaltag = "100X_upgrade2018_realistic_v10"

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, "auto:phase2_realistic", "")
process.GlobalTag = GlobalTag(process.GlobalTag, "auto:phase2_realistic_T15", "")
#process.GlobalTag = GlobalTag(process.GlobalTag, "94X_mc2017_realistic_v10")
#process.GlobalTag = GlobalTag(process.GlobalTag, "94X_mc2017_realistic_v11")
#process.GlobalTag = GlobalTag(process.GlobalTag, "112X_mcRun3_2021_realistic_v2")


#process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')

#process.load('Configuration.Geometry.GeometryExtended2023D41_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49_cff')


############################## Parse arguments ##############################

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing("analysis")


options.parseArguments()


sourceFileNames = cms.untracked.vstring([
    #"root://eoscms.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/SingleElectron_PT2to200/GEN-SIM-DIGI-RAW/PU200_110X_mcRun4_realistic_v3_ext2-v2/40000/D560AB5E-1069-614C-9FE8-13FD64D005BC.root",
    
    "root://cms-xrd-global.cern.ch//store/mc/Phase2HLTTDRWinter20DIGI/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8/GEN-SIM-DIGI-RAW/NoPU_110X_mcRun4_realistic_v3-v2/20000/0E64E0EE-3128-3242-B738-45A24C6CF855.root",
])


process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    fileNames = sourceFileNames,
    
    # Run1:Event1 to Run2:Event2
    #eventsToProcess = cms.untracked.VEventRange("1:78722-1:78722"),
    
    #duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
)


# Test HLT-TDR EventContent
#from HLTrigger.Configuration.Tools.hltTDREventContent import dropInputProducts
#dropInputProducts(process.source)


# Aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
customise_aging_1000(process)


process.reco_seq = cms.Sequence(
    process.RawToDigi *
    process.L1Reco *
    process.reconstruction
)


outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands


from MyModules.Test.ecalDrivenGsfElectronsFromTICL_cff import ecalDrivenGsfElectronsFromTICL_customizeProcess
process = ecalDrivenGsfElectronsFromTICL_customizeProcess(process, onReco = False, outputCommands = outputCommands)
process.TICLele_seq = cms.Sequence(process.ecalDrivenGsfElectronsFromTICL_step)


###### PixelCPE issue
process.TrackProducer.TTRHBuilder = "WithTrackAngle"
process.PixelCPEGenericESProducer.UseErrorsFromTemplates = False
process.PixelCPEGenericESProducer.LoadTemplatesFromDB = False
process.PixelCPEGenericESProducer.TruncatePixelCharge = False
process.PixelCPEGenericESProducer.IrradiationBiasCorrection = False
process.PixelCPEGenericESProducer.DoCosmics = False
process.PixelCPEGenericESProducer.Upgrade = cms.bool(True) 
######


process.p = cms.Path(
    process.reco_seq *
    process.TICLele_seq
)


# Output definition
process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        #dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string("output.root"),

    outputCommands = outputCommands,
    #outputCommands = process.RECOSIMEventContent.outputCommands,
    #outputCommands = process.AODSIMEventContent.outputCommands,

    splitLevel = cms.untracked.int32(0),

    compressionAlgorithm = cms.untracked.string("LZMA"),
)


process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)


process.schedule = cms.Schedule(
    process.p,
    process.endjob_step,
    process.FEVTDEBUGHLToutput_step,
)

from RecoHGCal.TICL.iterativeTICL_cff import iterTICLTask
process.schedule.associate(iterTICLTask)


print "\n"
print "*"*50
print "process.schedule:", process.schedule
print "*"*50
#print "process.schedule.__dict__:", process.schedule.__dict__
#print "*"*50
print "\n"


# Debug
#process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string("debug.root")
#)
#
#process.output_step = cms.EndPath(process.out)
#process.schedule.extend([process.output_step])


#from FWCore.ParameterSet.Utilities import convertToUnscheduled
#process = convertToUnscheduled(process)


# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion
