import os
import numpy
import time

import ROOT

import Common

import CMS_lumi
import tdrstyle


#ROOT.gSystem.Load("EDAnalyzers/TreeMaker/interface/CustomRootDict_cc.so")

ROOT.gROOT.SetBatch(1)



class plotQuantity :
    
    isMultiLayer = False
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
    l_inFileName = []
    l_treeName = []
    l_label = []
    l_lineColor = []
    l_lineStyle = []
    
    l_plotStr = []
    l_cutStr = []
    
    nBinX = 0
    createXmin = 0
    createXmax = 0
    
    nBinY = 0
    createYmin = 0
    createYmax = 0
    
    normalize = True
    
    scale = 1.0
    
    xMin = 0
    xMax = 0
    
    yMin = 0
    yMax = 0
    
    zMin = 0
    zMax = 0
    
    logX = False
    logY = False
    logZ = False
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    xLabelSizeScale = 1.0
    yLabelSizeScale = 1.0
    
    centerLabelsX = False
    centerLabelsY = False
    
    xTitle = ""
    yTitle = ""
    zTitle = ""
    
    xTitleSizeScale = 1.0
    yTitleSizeScale = 1.0
    
    extraText = ""
    extraTextX = ""
    extraTextY = ""
    
    plotStyle = "hist"
    
    legendTitle = "Phase-II EB"
    legendPos = "UR"
    legendTextSize = 0.03
    legendWidthScale = 1
    
    outFileName = ""
    outDir = ""


tdrstyle.setTDRStyle()


l_plotQuantity = []



# ########## gsfEleFromTICL_iso_sumETratio_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Ele (dR<0.3)",
#    "Ele (dR<0.3, E_{T}>1GeV)",
#    "Ele (dR<0.4)",
#    "Ele (dR<0.4, E_{T}>1GeV)",
#    "Jet (dR<0.3)",
#    "Jet (dR<0.3, E_{T}>1GeV)",
#    "Jet (dR<0.4)",
#    "Jet (dR<0.4, E_{T}>1GeV)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#    6,
#    6,
#    8,
#    8,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    7,
#    1,
#    7,
#    1,
#    7,
#    1,
#    7,
#]
#pltQty_temp.l_plotStr = [
#    "gsfEleFromTICL_iso_sumETratio_dR0p3",
#    "gsfEleFromTICL_iso_sumETratio_dR0p3_clusET1_trkDz0p15_trkPt1",
#    "gsfEleFromTICL_iso_sumETratio_dR0p4",
#    "gsfEleFromTICL_iso_sumETratio_dR0p4_clusET1_trkDz0p15_trkPt1",
#    "gsfEleFromTICL_iso_sumETratio_dR0p3",
#    "gsfEleFromTICL_iso_sumETratio_dR0p3_clusET1_trkDz0p15_trkPt1",
#    "gsfEleFromTICL_iso_sumETratio_dR0p4",
#    "gsfEleFromTICL_iso_sumETratio_dR0p4_clusET1_trkDz0p15_trkPt1",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 1e-3
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I^{clus}_{dR}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_iso_sumETratio_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_iso_trackSumPtRatio_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Ele (dR<0.3)",
#    "Ele (dR<0.3, p_{T}>1GeV, dz<0.15cm)",
#    "Ele (dR<0.4)",
#    "Ele (dR<0.4, p_{T}>1GeV, dz<0.15cm)",
#    "Jet (dR<0.3)",
#    "Jet (dR<0.3, p_{T}>1GeV, dz<0.15cm)",
#    "Jet (dR<0.4)",
#    "Jet (dR<0.4, p_{T}>1GeV, dz<0.15cm)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#    6,
#    6,
#    8,
#    8,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    7,
#    1,
#    7,
#    1,
#    7,
#    1,
#    7,
#]
#pltQty_temp.l_plotStr = [
#    "gsfEleFromTICL_iso_trackSumPt_dR0p3/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p3_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p4/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p4_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p3/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p3_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p4/gsfEleFromTICL_pT",
#    "gsfEleFromTICL_iso_trackSumPt_dR0p4_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 1e-3
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I^{trk}_{dR}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_iso_trackSumPtRatio_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_HoverE_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Ele (dR_{cone}<0.15)",
#    "Ele (dR_{cone}<0.2) ",
#    "Ele (dR_{cone}<0.3) ",
#    "Jet (dR_{cone}<0.15)",
#    "Jet (dR_{cone}<0.2) ",
#    "Jet (dR_{cone}<0.3) ",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    2,
#    4,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    3,
#    7,
#    1,
#    3,
#    7,
#]
#pltQty_temp.l_plotStr = [
#    "gsfEleFromTICL_HoverE_dR0p15",
#    "gsfEleFromTICL_HoverE_dR0p2",
#    "gsfEleFromTICL_HoverE_dR0p3",
#    "gsfEleFromTICL_HoverE_dR0p15",
#    "gsfEleFromTICL_HoverE_dR0p2",
#    "gsfEleFromTICL_HoverE_dR0p3",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 4
#pltQty_temp.yMin = 1e-3
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "H/E"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_HoverE_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## gsfEleFromTICL_Rvar_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Ele (R_{2.0})",
#    "Ele (R_{2.8})",
#    "Ele (R_{3.5})",
#    "Jet (R_{2.0})",
#    "Jet (R_{2.8})",
#    "Jet (R_{3.5})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    2,
#    4,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    3,
#    7,
#    1,
#    3,
#    7,
#]
#pltQty_temp.l_plotStr = [
#    "gsfEleFromTICL_Rvar_cylR2p0",
#    "gsfEleFromTICL_Rvar_cylR2p8",
#    "gsfEleFromTICL_Rvar_cylR3p5",
#    "gsfEleFromTICL_Rvar_cylR2p0",
#    "gsfEleFromTICL_Rvar_cylR2p8",
#    "gsfEleFromTICL_Rvar_cylR3p5",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 200
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 1.2
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "R_{d}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.legendPos = "UL"
#pltQty_temp.outFileName = "gsfEleFromTICL_Rvar_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_sigmaEtaEta_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Electron",
#    "Jet",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "sqrt(gsfEleFromTICL_superClus_sigma2etaEta)",
#    "sqrt(gsfEleFromTICL_superClus_sigma2etaEta)",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 200
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.05
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#sigma_{#eta#eta}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaEtaEta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## gsfEleFromTICL_sigmaPhiPhi_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Electron",
#    "Jet",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "sqrt(gsfEleFromTICL_superClus_sigma2phiPhi)",
#    "sqrt(gsfEleFromTICL_superClus_sigma2phiPhi)",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 200
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.05
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#sigma_{#phi#phi}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaPhiPhi_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_sigmaRR_ZEE_QCD (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
#    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
#]
#pltQty_temp.l_treeName = [
#    "treeMaker/tree",
#    "treeMaker/tree",
#]
#pltQty_temp.l_label = [
#    "Electron",
#    "Jet",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "sqrt(gsfEleFromTICL_superClus_sigma2rr)",
#    "sqrt(gsfEleFromTICL_superClus_sigma2rr)",
#]
#pltQty_temp.l_cutStr = [
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
#    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
#]
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 20
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#sigma_{rr} [cm]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaRR_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



 ########## gsfEleFromTICL_sigmaUU_ZEE_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "Ele (R_{cyl}=2.0cm)",
    "Ele (R_{cyl}=2.8cm)",
    "Ele (R_{cyl}=3.5cm)",
    "Jet (R_{cyl}=2.0cm)",
    "Jet (R_{cyl}=2.8cm)",
    "Jet (R_{cyl}=3.5cm)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    2,
    4,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    1,
    3,
    7,
    1,
    3,
    7,
]
pltQty_temp.l_plotStr = [
    "sqrt(gsfEleFromTICL_sigma2uu_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2uu_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2uu_cylR3p5)",
    "sqrt(gsfEleFromTICL_sigma2uu_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2uu_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2uu_cylR3p5)",
]
pltQty_temp.l_cutStr = [
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
]
pltQty_temp.nBinX = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 2
pltQty_temp.xMin = 0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{uu}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.outFileName = "gsfEleFromTICL_sigmaUU_PU200"
pltQty_temp.outDir = "plots/vars_ID"
l_plotQuantity.append(pltQty_temp)



 ########## gsfEleFromTICL_sigmaVV_ZEE_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "Ele (R_{cyl}=2.0cm)",
    "Ele (R_{cyl}=2.8cm)",
    "Ele (R_{cyl}=3.5cm)",
    "Jet (R_{cyl}=2.0cm)",
    "Jet (R_{cyl}=2.8cm)",
    "Jet (R_{cyl}=3.5cm)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    2,
    4,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    1,
    3,
    7,
    1,
    3,
    7,
]
pltQty_temp.l_plotStr = [
    "sqrt(gsfEleFromTICL_sigma2vv_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2vv_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2vv_cylR3p5)",
    "sqrt(gsfEleFromTICL_sigma2vv_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2vv_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2vv_cylR3p5)",
]
pltQty_temp.l_cutStr = [
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
]
pltQty_temp.nBinX = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 2
pltQty_temp.xMin = 0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{vv}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.outFileName = "gsfEleFromTICL_sigmaVV_PU200"
pltQty_temp.outDir = "plots/vars_ID"
l_plotQuantity.append(pltQty_temp)



 ########## gsfEleFromTICL_sigmaWW_ZEE_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
    "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "Ele (R_{cyl}=2.0cm)",
    "Ele (R_{cyl}=2.8cm)",
    "Ele (R_{cyl}=3.5cm)",
    "Jet (R_{cyl}=2.0cm)",
    "Jet (R_{cyl}=2.8cm)",
    "Jet (R_{cyl}=3.5cm)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    2,
    4,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    1,
    3,
    7,
    1,
    3,
    7,
]
pltQty_temp.l_plotStr = [
    "sqrt(gsfEleFromTICL_sigma2ww_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2ww_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2ww_cylR3p5)",
    "sqrt(gsfEleFromTICL_sigma2ww_cylR2p0)",
    "sqrt(gsfEleFromTICL_sigma2ww_cylR2p8)",
    "sqrt(gsfEleFromTICL_sigma2ww_cylR3p5)",
]
pltQty_temp.l_cutStr = [
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4",
]
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0
pltQty_temp.xMax = 15
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{ww}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.outFileName = "gsfEleFromTICL_sigmaWW_PU200"
pltQty_temp.outDir = "plots/vars_ID"
l_plotQuantity.append(pltQty_temp)



# ########## classifier_TMVA_BDT (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/TMVA.root",
#    "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/TMVA.root",
#    "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/TMVA.root",
#    "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/TMVA.root",
#]
#pltQty_temp.l_treeName = [
#    "dataset/TrainTree",
#    "dataset/TestTree",
#    "dataset/TrainTree",
#    "dataset/TestTree",
#]
#pltQty_temp.l_label = [
#    "Sig.: electron (train)",
#    "Sig.: electron (test)",
#    "Bkg.: jet (train)",
#    "Bkg.: jet (test)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    1,
#    7,
#    1,
#    7,
#]
#pltQty_temp.l_plotStr = [
#    "BDT",
#    "BDT",
#    "BDT",
#    "BDT",
#]
#pltQty_temp.l_cutStr = [
#    "classID == 0",
#    "classID == 0",
#    "classID == 1",
#    "classID == 1",
#]
#pltQty_temp.nBinX = 200
#pltQty_temp.createXmin = -1
#pltQty_temp.createXmax = +1
#pltQty_temp.xMin = -0.6
#pltQty_temp.xMax = +0.4
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.1
##pltQty_temp.logY = True
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TMVA BDT classifier"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
#pltQty_temp.legendPos = "UL"
#pltQty_temp.outFileName = "classifier_TMVA_BDT_PU200"
#pltQty_temp.outDir = "plots/ID_TMVA/vars"
#l_plotQuantity.append(pltQty_temp)




m_inputTree = {}


for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    outDir = "%s" %(plotQuantity.outDir)
    os.system("mkdir -p %s" %(outDir))
    
    l_inFile = []
    l_tree = []
    
    l_inFileName = plotQuantity.l_inFileName
    
    l_label = plotQuantity.l_label
    l_lineColor = plotQuantity.l_lineColor
    l_lineStyle = plotQuantity.l_lineStyle
    
    for iSample in range(0, len(l_inFileName)) :
        
        #inFile = ROOT.TFile.Open(l_inFileName[iSample], "READ")
        #
        #tree = inFile.Get("treeMaker/tree")
        #
        ##tree.Print()
        #
        #l_inFile.append(inFile)
        #l_tree.append(tree)
        
        #if (l_inFileName[iSample] not in m_inputTree) :
        #    
        #    l_inFileName_iSample = []
        #    
        #    if (".root" in l_inFileName[iSample]) :
        #        
        #        l_inFileName_iSample = sigFiles.split(":")
        #    
        #    else :
        #        
        #        l_inFileName_iSample = numpy.loadtxt(l_inFileName[iSample], delimiter = "someNonExistantString", dtype = str, ndmin = 1)
        #    
        #    
        #    tree = ROOT.TChain("treeMaker/tree")
        #    
        #    Common.openTChain(
        #        l_inFileName[iSample],
        #        tree,
        #        #nFileMax = 1
        #    )
        #    
        #    
        #    
        #    l_tree.append(tree)
        #    
        #    
        #    m_inputTree[l_inFileName[iSample]] = tree
        
        l_treeName = plotQuantity.l_treeName[iSample].split(":")
        
        tree = None
        
        key = "%s_%s" %(l_inFileName[iSample], plotQuantity.l_treeName[iSample])
        
        if (key not in m_inputTree) :
            
            tree = ROOT.TChain("tree")
            
            if (".root" in l_inFileName[iSample]) :
                
                l_inFileName_tmp = l_inFileName[iSample].split(":")
            
            else :
                
                l_inFileName_tmp = numpy.loadtxt(l_inFileName[iSample], delimiter = "someNonExistantString", dtype = str, ndmin = 1)
            
            for iTree, treeName in enumerate(l_treeName) :
                
                #for iFile in range(0, len(l_inFileName_tmp)) :
                #    
                #    tree.AddFile(l_inFileName_tmp[iFile], -1, treeName)
                
                Common.openTChain(
                    listFileName = l_inFileName_tmp,
                    chain = tree,
                    treeName = treeName,
                    #nFileMax = 100,
                    debug = True,
                )
            
            m_inputTree[key] = tree
        
        #else :
        #    
        #    tree = m_inputTree[key]
        #
        #l_tree.append(tree)
    
    
    l_histDetail = []
    
    
    for iSample in range(0, len(l_inFileName)) :
        
        key = "%s_%s" %(l_inFileName[iSample], plotQuantity.l_treeName[iSample])
        
        #tree = l_tree[iSample]
        tree = m_inputTree[key]
        
        plotStr = plotQuantity.l_plotStr[iSample]
        cutStr = plotQuantity.l_cutStr[iSample]
        weightStr = plotQuantity.weightStr
        
        h1_temp = ROOT.TH1F("h1_temp_%s" %(iSample+1), l_label[iSample], plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax)
        h1_temp.Sumw2()
        
        plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
        weightStr = "%s * (%s)" %(weightStr, cutStr)
        
        print plotStr
        print weightStr
        
        tree.Draw(plotStr, weightStr, "goff")
        
        if (plotQuantity.normalize and h1_temp.Integral()) :
            
            h1_temp.Scale(1.0 / h1_temp.Integral())
    
    
        histDetail_temp = Common.HistogramDetails()
        histDetail_temp.hist = h1_temp.Clone()
        histDetail_temp.hist.SetFillStyle(0)
        histDetail_temp.lineWidth = 4
        histDetail_temp.lineColor = l_lineColor[iSample]
        histDetail_temp.lineStyle = l_lineStyle[iSample]
        histDetail_temp.markerColor = 0
        #histDetail_temp.addToLegend = False
        histDetail_temp.histLabel = l_label[iSample]# + " %0.2g" %(h1_temp.GetBinContent(1))
        histDetail_temp.drawOption = plotQuantity.plotStyle
        
        l_histDetail.append(histDetail_temp)
        
    
    outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
    
    Common.plot1D(
        list_histDetails = l_histDetail,
        stackDrawOption = "nostack",
        title = "",
        xTitle = plotQuantity.xTitle,
        yTitle = plotQuantity.yTitle,
        xTitleSizeScale = plotQuantity.xTitleSizeScale,
        yTitleSizeScale = plotQuantity.yTitleSizeScale,
        xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
        yMin = plotQuantity.yMin, yMax = plotQuantity.yMax,
        logX = plotQuantity.logX, logY = plotQuantity.logY,
        gridX = True, gridY = True,
        nDivisionsX = plotQuantity.nDivisionsX,
        nDivisionsY = plotQuantity.nDivisionsY,
        xLabelSizeScale = plotQuantity.xLabelSizeScale,
        yLabelSizeScale = plotQuantity.yLabelSizeScale,
        centerLabelsX = plotQuantity.centerLabelsX,
        centerLabelsY = plotQuantity.centerLabelsY,
        drawLegend = True,
        #legendHeightScale = 0.3,
        transparentLegend = True,
        legendTextSize = plotQuantity.legendTextSize,
        legendBorderSize = 0,
        legendPos = plotQuantity.legendPos,
        legendTitle = "#scale[1.45]{%s}" %(plotQuantity.legendTitle),
        legendWidthScale = plotQuantity.legendWidthScale,
        l_extraText = [[plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText]],
        CMSextraText = "Simulation Preliminary",
        fixAlphanumericBinLabels = False,
        outFileName = outFileName,
        outFileName_suffix = "",
    )
    
    
    #for f in l_inFile :
    #    
    #    f.Close()
    
    
    #time.sleep(2)
