#!/bin/bash

cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
    sourceFile=\
sourceFiles/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1_FEVT/TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1-v1_FEVT.txt \
    genEleFilter=0 \
    genPartonFilter=0 \
    isGunSample=0 \
    onRaw=1 \
    debugFile=0 \
    maxEvents=100 \
