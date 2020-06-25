#!/usr/bin/env python


import os


def cmdFailedStatement(cmdReturn) :
    
    if (cmdReturn) :
        
        print "Failed. Exiting..."
        exit(1)


def runCmd(cmdStr) :
    
    print "Running: %s" %(cmdStr)
    
    cmdReturn = os.system(cmdStr)
    cmdFailedStatement(cmdReturn)
    
    print "\n"


# Compile
cmdStr = "scram b -j8 USER_CXXFLAGS=\"-fopenmp\""
runCmd(cmdStr)


# ZEE noPU
cmdStr = (
    "nohup cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py "
    "sourceFile=sourceFiles/RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM.txt "
    "outputDir=output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM "
    "> logs/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM.log &"
)
runCmd(cmdStr)


# ZEE PU200
cmdStr = (
    "nohup cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py "
    "sourceFile=sourceFiles/RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt "
    "outputDir=output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM "
    "> logs/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.log &"
)
runCmd(cmdStr)


# QCD noPU
cmdStr = (
    "nohup cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py "
    "genEleFilter=0 "
    "sourceFile=sourceFiles/RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM.txt "
    "outputDir=output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM "
    "> logs/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM.log &"
)
runCmd(cmdStr)


# QCD 200PU
cmdStr = (
    "nohup cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py "
    "genEleFilter=0 "
    "sourceFile=sourceFiles/RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt "
    "outputDir=output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM "
    "> logs/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.log &"
)
runCmd(cmdStr)
