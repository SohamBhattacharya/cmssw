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


#process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49Reco_cff')

#process.load('Configuration.Geometry.GeometryExtended2023D41_cff')
#process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load('Configuration.Geometry.GeometryExtended2026D49_cff')


############################## Parse arguments ##############################

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing("analysis")


options.register("sourceFile",
    "", # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.string, # string, int, or float
    "File containing list of input files" # Description
)

options.register("outputDir",
    "", # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.string, # string, int, or float
    "Output directory" # Description
)

options.register("outFileNumber",
    -1, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "File number (will be added to the filename if >= 0)" # Description
)

options.register("eventRange",
    "", # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.string, # string, int, or float
    "Syntax: Run1:Event1-Run2:Event2 (includes both)" # Description
)

options.register("debugFile",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Create debug file" # Description
)

options.register("eleGenMatchDR",
    99999, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.float, # string, int, or float
    "DeltaR to use for electron gen-matching (will store only the gen-matched ones)" # Description
)

options.register("genEleFilter",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Apply gen-electron filter" # Description
)

options.register("isGunSample",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Is it a particle gun sample" # Description
)

options.register("trace",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Trace modules" # Description
)

options.register("memoryCheck",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Check memory usage" # Description
)

options.register("depGraph",
    0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Produce dependency graph only" # Description
)

options.parseArguments()


#maxEvents = -1
#options.maxEvents = 15
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))


sourceFile = "sourceFiles/RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt"

if (len(options.sourceFile)) :
    
    sourceFile = options.sourceFile


fNames = []

if (len(options.inputFiles)) :
    
    fNames = options.inputFiles

else :
    
    with open(sourceFile) as f:
        
        fNames = f.readlines()


for iFile, fName in enumerate(fNames) :
    
    if (fName.find("/store") == 0) :
        
        fNames[iFile] = "root://cms-xrd-global.cern.ch/%s" %(fName)
    
    elif (
        "file:" not in fName and
        "root:" not in fName
    ) :
        
        fNames[iFile] = "file:%s" %(fName)


outFileSuffix = ""

outFile = "ntupleTree%s.root" %(outFileSuffix)

if (len(options.outputDir)) :
    
    os.system("mkdir -p %s" %(options.outputDir))
    
    outFile = "%s/%s" %(options.outputDir, outFile)


sourceFileNames = cms.untracked.vstring(fNames)
#print sourceFileNames

process.source = cms.Source("PoolSource",
    fileNames = sourceFileNames,
    
    # Run1:Event1 to Run2:Event2
    #eventsToProcess = cms.untracked.VEventRange("1:78722-1:78722"),
    
    #duplicateCheckMode = cms.untracked.string("noDuplicateCheck"),
)


if (len(options.eventRange)) :
    
    process.source.eventsToProcess = cms.untracked.VEventRange(options.eventRange)


#process.options = cms.untracked.PSet(
#    #SkipEvent = cms.untracked.vstring("ProductNotFound"),
#    
#    #printDependencies = cms.untracked.bool(True),
#)


if (options.depGraph) :
    
    process.DependencyGraph = cms.Service("DependencyGraph")
    process.source = cms.Source("EmptySource")
    process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(0))


process.treeMaker = cms.EDAnalyzer(
    "TreeMaker",
    
    ############################## My stuff ##############################
    debug = cms.bool(False),
    
    eleGenMatchDR = cms.double(options.eleGenMatchDR),
    isGunSample = cms.bool(bool(options.isGunSample)),
    
    ############################## GEN ##############################
    
    label_generator = cms.untracked.InputTag("generator"),
    label_genParticle = cms.untracked.InputTag("prunedGenParticles"),
    
    
    ############################## RECO ##############################
    
    label_primaryVertex = cms.untracked.InputTag("offlineSlimmedPrimaryVertices"),
    label_primaryVertex4D = cms.untracked.InputTag("offlineSlimmedPrimaryVertices4D"),
    
    label_pileup = cms.untracked.InputTag("slimmedAddPileupInfo"),
    label_rho = cms.untracked.InputTag("fixedGridRhoFastjetAll"),
    
    #label_slimmedEle = cms.untracked.InputTag("slimmedElectrons"),
    #label_slimmedEle = cms.untracked.InputTag("slimmedElectrons", processName = cms.InputTag.skipCurrentProcess()),
    #label_slimmedEle = cms.untracked.InputTag("slimmedElectronsWithUserData"),
    label_slimmedEle = cms.untracked.InputTag("updatedElectrons"),
    
    label_ElectronMVAEstimatorRun2Fall17IsoV2Values = cms.untracked.InputTag("electronMVAValueMapProducer", "ElectronMVAEstimatorRun2Fall17IsoV2Values"),
    label_ElectronMVAEstimatorRun2Fall17IsoV2RawValues = cms.untracked.InputTag("electronMVAValueMapProducer", "ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
    
    label_ElectronMVAEstimatorRun2Fall17NoIsoV2Values = cms.untracked.InputTag("electronMVAValueMapProducer", "ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
    label_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues = cms.untracked.InputTag("electronMVAValueMapProducer", "ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
    
    label_pfCandidate = cms.untracked.InputTag("packedPFCandidates"),
    
    ########## AK4 jet ##########
    
    #label_ak4PFjet = cms.untracked.InputTag("ak4PFJets"),
    
    
)


########## Filters ##########

from EDFilters.MyFilters.GenParticleFilter_cfi import *

process.GenParticleFilter_ele = GenParticleFilter.clone()
process.GenParticleFilter_ele.label_generator = cms.untracked.InputTag("generator")
process.GenParticleFilter_ele.label_genParticle = cms.untracked.InputTag("prunedGenParticles")
process.GenParticleFilter_ele.atLeastN = cms.int32(2)
process.GenParticleFilter_ele.pdgId = cms.int32(11)
process.GenParticleFilter_ele.minEta = cms.double(0)
process.GenParticleFilter_ele.maxEta = cms.double(1.479)
process.GenParticleFilter_ele.isGunSample = cms.bool(bool(options.isGunSample))
#process.GenParticleFilter_ele.debug = cms.bool(True)


process.filterSeq_ele = cms.Sequence()

if (options.genEleFilter) :
    
    process.filterSeq_ele = cms.Sequence(
        process.GenParticleFilter_ele
    )


# Output file name modification
if (outFile.find("/eos/cms") ==  0) :
    
    outFile = outFile.replace("/eos/cms", "root://eoscms.cern.ch//eos/cms")


# Output
process.TFileService = cms.Service(
    "TFileService",
    fileName = cms.string(outFile)
)


process.schedule = cms.Schedule()


# Aging
from SLHCUpgradeSimulations.Configuration.aging import customise_aging_1000
customise_aging_1000(process)


###### PixelCPE issue
process.TrackProducer.TTRHBuilder = "WithTrackAngle"
process.PixelCPEGenericESProducer.UseErrorsFromTemplates = False
process.PixelCPEGenericESProducer.LoadTemplatesFromDB = False
process.PixelCPEGenericESProducer.TruncatePixelCharge = False
process.PixelCPEGenericESProducer.IrradiationBiasCorrection = False
process.PixelCPEGenericESProducer.DoCosmics = False
process.PixelCPEGenericESProducer.Upgrade = cms.bool(True) 
######


##### Egamma MVA
from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
from EgammaUser.EgammaPostRecoTools.EgammaPostRecoTools import makeEgammaPATWithUserData

setupEgammaPostRecoSeq(process)
makeEgammaPATWithUserData(
    process,
    eleTag = cms.InputTag("slimmedElectrons"),
    phoTag = cms.InputTag("slimmedPhotons"),
)


process.p = cms.Path(
    process.filterSeq_ele *
    process.egammaPostRecoSeq *
    #process.egammaPostRecoPatUpdatorSeq *
    process.treeMaker
)

process.schedule.insert(0, process.p)

print "\n"
print "*"*50
print "process.schedule:", process.schedule
print "*"*50
#print "process.schedule.__dict__:", process.schedule.__dict__
#print "*"*50
print "\n"


# Tracer
if (options.trace) :
    
    process.Tracer = cms.Service("Tracer")


if (options.memoryCheck) :
    
    process.SimpleMemoryCheck = cms.Service(
        "SimpleMemoryCheck",
        moduleMemorySummary = cms.untracked.bool(True),
    )


# Debug
if (options.debugFile) :
    
    process.out = cms.OutputModule("PoolOutputModule",
        fileName = cms.untracked.string("debug.root")
    )
    
    process.output_step = cms.EndPath(process.out)
    process.schedule.extend([process.output_step])


from FWCore.ParameterSet.Utilities import convertToUnscheduled
process = convertToUnscheduled(process)


# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion
