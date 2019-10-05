# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: MyPackages/GeneratorFragments/python/Py8PtGun_electron_cfi.py --conditions auto:phase2_realistic -n 10 --era Phase2C8_timing_layer_bar --eventcontent FEVTDEBUGHLT -s GEN,SIM,DIGI:pdigi_valid,L1,L1TrackTrigger,DIGI2RAW,HLT:@fake2 --datatier GEN-SIM-DIGI-RAW --beamspot HLLHC --geometry Extended2023D41 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT',eras.Phase2C8_timing_layer_bar)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
#process.load('Configuration.Geometry.GeometryExtended2023D41Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41Reco_cff')
#process.load('Configuration.Geometry.GeometryExtended2023D41_cff')
process.load('Configuration.Geometry.GeometryExtended2026D41_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedHLLHC_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.L1TrackTrigger_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake2_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


############################## Parse arguments ##############################
import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing("analysis")

#options.maxEvents = 0
options.outputFile = ""


options.register("randSeed",
    1, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.int, # string, int, or float
    "Random number seed" # Description"
)

options.register("minPt",
    -1, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.float, # string, int, or float
    "Minimum pT" # Description"
)

options.register("maxPt",
    -1, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.float, # string, int, or float
    "Maximum pT" # Description"
)

options.register("minEta",
    0.0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.float, # string, int, or float
    "Minimum eta" # Description"
)

options.register("maxEta",
    3.0, # Default value
    VarParsing.VarParsing.multiplicity.singleton, # singleton or list
    VarParsing.VarParsing.varType.float, # string, int, or float
    "Maximum eta" # Description"
)


options.parseArguments()


#if (options.maxEvents <= 0) :
#    
#    print "Error: Enter a valid maxEvents."
#    exit(1)

if (options.minPt < 0) :
    
    print "Error: Enter a valid minPt."
    exit(1)

if (options.maxPt < 0) :

    print "Error: Enter a valid maxPt."
    exit(1)

if (options.minPt >= options.maxPt) :
    
    print "Error: minPt MUST be LESS than maxPt."
    exit(1)

if (options.minEta < 0 or options.maxEta < 0) :
    
    print "Error: minEta and maxEta MUST be positive."
    exit(1)

if (options.minEta >= options.maxEta) :

    print "Error: minEta MUST be LESS than maxEta."
    exit(1)

process.RandomNumberGeneratorService.generator.initialSeed = options.randSeed


#minPt_str = "%d" %(options.minPt) if (int(options.minPt)-options.minPt == 0) else str(options.minPt)
#maxPt_str = "%d" %(options.maxPt) if (int(options.maxPt)-options.maxPt == 0) else str(options.maxPt)

# Remove extra auto-generated string from filename
outFileName = options.outputFile.replace("_numEvent%d" %(options.maxEvents), "")

if (not len(outFileName) or outFileName == ".root") :

    #outFileName = "temp_pT-%s-%s_GEN-SIM-DIGI-RAW.root" %(minPt_str, maxPt_str)
    outFileName = "output.root"

print "Output file: %s" %(outFileName)


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('MyPackages/GeneratorFragments/python/Py8PtGun_electron_cfi.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.FEVTDEBUGHLToutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-DIGI-RAW'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string(outFileName),
    outputCommands = process.FEVTDEBUGHLTEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersValid)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:phase2_realistic', '')

process.generator = cms.EDFilter("Pythia8PtGun",
    PGunParameters = cms.PSet(
        AddAntiParticle = cms.bool(True),
        MaxEta = cms.double(options.maxEta),
        MaxPhi = cms.double(3.14159265359),
        MaxPt = cms.double(options.maxPt),
        MinEta = cms.double(options.minEta),
        MinPhi = cms.double(-3.14159265359),
        MinPt = cms.double(options.minPt),
        ParticleID = cms.vint32(11)
    ),
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring()
    ),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.digitisation_step = cms.Path(process.pdigi_valid)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.L1TrackTrigger_step = cms.Path(process.L1TrackTrigger)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.FEVTDEBUGHLToutput_step = cms.EndPath(process.FEVTDEBUGHLToutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.digitisation_step,process.L1simulation_step,process.L1TrackTrigger_step,process.digi2raw_step)
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.FEVTDEBUGHLToutput_step])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.generator)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
