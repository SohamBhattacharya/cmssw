#!/bin/bash


#cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
#    sourceFile=\
#sourceFiles/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    genEleFilter=1 \
#    genPartonFilter=0 \
#    isGunSample=1 \
#    modTICLele=1 \
#    modTICLeleWithRerunTICL=1 \
#    rerunTICL=1 \
#    onRaw=0 \
#    maxEvents=100 \
##    storeSimHit=1 \
##    storeRecHit=1 \



cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
    sourceFile=\
sourceFiles/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2_GEN-SIM-modRECO/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2_GEN-SIM-modRECO.txt \
    genEleFilter=1 \
    genPartonFilter=0 \
    isGunSample=1 \
    modTICLele=1 \
    modTICLeleWithRerunTICL=1 \
    rerunTICL=1 \
    onRaw=0 \
    debugFile=0 \
    maxEvents=2000 \



#cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
#    sourceFile=\
#sourceFiles/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-NoPU_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    genEleFilter=1 \
#    genPartonFilter=0 \
#    isGunSample=1 \
#    onRaw=1 \
#    maxEvents=1000 \



#cmsRun EDAnalyzers/TreeMaker/python/ConfFile_cfg.py \
#    sourceFile=\
#sourceFiles/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-DIGI-RAW/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-DIGI-RAW.txt \
#    genEleFilter=1 \
#    genPartonFilter=0 \
#    isGunSample=1 \
#    modTICLele=0 \
#    modTICLeleWithRerunTICL=0 \
#    rerunTICL=0 \
#    onRaw=1 \
#    debugFile=0 \
#    maxEvents=10 \
