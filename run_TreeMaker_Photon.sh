#!/bin/bash


cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
    print \
    sourceFile=\
sourceFiles/DoublePhoton_FlatPt-1To100_Phase2HLTTDRWinter20RECOMiniAOD-PU200_110X_mcRun4_realistic_v3-v1_MINIAODSIM/DoublePhoton_FlatPt-1To100_Phase2HLTTDRWinter20RECOMiniAOD-PU200_110X_mcRun4_realistic_v3-v1_MINIAODSIM.txt \
    genEleFilter=0 \
    genPhoFilter=1 \
    isGunSample=1 \
    debugFile=0 \
    maxEvents=50 \
