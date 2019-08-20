# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco --filein file:Py8PtGun_cfi_py_GEN_SIM_DIGI_L1_L1TrackTrigger_DIGI2RAW_HLT.root --conditions auto:phase2_realistic -n 10 --era Phase2C8_timing_layer_bar --eventcontent FEVTDEBUGHLT --runUnscheduled -s RAW2DIGI,L1Reco,RECO,RECOSIM --datatier GEN-SIM-RECO --geometry Extended2023D41 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Phase2C8_timing_layer_bar)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.RecoSim_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


############################## Parse arguments ##############################
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing("analysis")

options.outputFile = "output_GEN-SIM-RECO.root"

options.register("sourceFile",
    "", # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.string, # string, int, or float
    "File containing list of input files" # Description
)

options.register("isCRAB",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "CRAB run or not" # Description
)

options.register("debugFile",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Create debug file" # Description
)

options.parseArguments()

if (options.isCRAB) :
    
    options.debugFile = 0

fNames = []


if (not options.isCRAB) :
    
    #sourceFile = "sourceFiles/RelValElectronGunPt2To100_CMSSW_10_6_0_pre4-106X_upgrade2023_realistic_v2_2023D41noPU-v1_GEN-SIM-DIGI-RAW/RelValElectronGunPt2To100_CMSSW_10_6_0_pre4-106X_upgrade2023_realistic_v2_2023D41noPU-v1_GEN-SIM-DIGI-RAW.txt"
    sourceFile = "sourceFiles/SingleElectronFlatPtGun_pT-15_eta-1p5-3p0_sobhatta-crab_SingleElectronFlatPtGun_pT-15_eta-1p5-3p0_GEN-SIM-DIGI-RAW-284165e958c955242461cd9651f5a03c_USER/SingleElectronFlatPtGun_pT-15_eta-1p5-3p0_sobhatta-crab_SingleElectronFlatPtGun_pT-15_eta-1p5-3p0_GEN-SIM-DIGI-RAW-284165e958c955242461cd9651f5a03c_USER_mod.txt"
    
    if (len(options.sourceFile)) :
    
        sourceFile = options.sourceFile
    
    with open(sourceFile) as f:
        
        fNames = f.readlines()
    
    
    if (not(len(options.inputFiles))) :
        
        options.inputFiles = fNames
        #print "Error: Enter a valid inputFiles."
        #exit(1)
    
    #if (not len(options.outputFile)) :
    #    
    #    #print "Error: Enter a valid outputFile."
    #    #exit(1)
    
    
    for iFile in range(0, len(options.inputFiles)) :
        
        fileName = options.inputFiles[iFile]
        
        if (fileName.find("file:") < 0 and fileName.find("root:") < 0) :
            
            options.inputFiles[iFile] = "file:%s" %(fileName)


#print options.maxEvents
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)


# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles),
    secondaryFileNames = cms.untracked.vstring()
)


process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('reco nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RECO'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(options.outputFile),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    #outputCommands = cms.untracked.vstring("keep *"),
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.recosim_step = cms.Path(process.recosim)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)


# Import TICL
#from ticl_iterations import TICL_iterations
from RecoHGCal.TICL.ticl_iterations import TICL_iterations_withReco

# Attach a sequence to process: process.TICL
#process = TICL_iterations(process)
#process = TICL_iterations_withReco(process)


#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *_ecalDrivenGsfElectrons*_*_*"])
#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *_*FromTICL*_*_*"])

#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *_*particleFlowRecHitHGC*_*_*"])
#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *_*mixedTripletStepSeeds*_*_*"])


#process.FEVTDEBUGHLTEventContent.outputCommands = cms.untracked.vstring("keep *")

#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *"])

#process.FEVTDEBUGHLTEventContent.outputCommands.extend(["keep *_*_*_*"])


process.FEVTDEBUGHLTEventContent.outputCommands.extend([
    "keep *_*particleFlowRecHitHGC*_*_*",
    "keep *_hgcalDigis_*_*",
    "keep *_particleFlowClusterECAL_*_*",
    "keep *_siPhase2Clusters_*_*",
    "keep *_siStripDigis_*_*",
    "keep *_siPixelClusters_*_*",
    "keep *_siPixelClustersCache_*_*", 
    "keep *_siPixelClusterShapeCache_*_*",
    "keep *_siPixelRecHits*_*_*",
    "keep *_trackerDrivenElectronSeeds_*_*",
    "keep *_pfTrackElec_*_*",
    
    "keep *_ecalDrivenGsfElectrons*_*_*",
    "keep *_*FromTICL*_*_*",
])


process.load("MyModules.Test.ecalDrivenGsfElectronsFromTICL_cff")

# Schedule definition
process.schedule = cms.Schedule(
    process.raw2digi_step,
    process.L1Reco_step,
    process.reconstruction_step,
    process.recosim_step,
    #process.TICL,
    process.ecalDrivenGsfElectronsFromTICL_step,
    process.endjob_step,
    process.FEVTDEBUGHLToutput_step
)

TICL_iterations_withReco(process)

# Debug
if (options.debugFile) :
    
    process.out = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string("debug.root")
    )
    
    process.output_step = cms.EndPath(process.out)
    process.schedule.extend([process.output_step])

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

#do not add changes to your config after this point (unless you know what you are doing)
from FWCore.ParameterSet.Utilities import convertToUnscheduled
process=convertToUnscheduled(process)


# Customisation from command line

#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion

