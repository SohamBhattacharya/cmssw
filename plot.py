import os
import numpy
import time

import ROOT

import Common

import CMS_lumi
import tdrstyle


ROOT.gSystem.Load("EDAnalyzers/TreeMaker/interface/CustomRootDict_cc.so")

ROOT.gROOT.SetBatch(1)


class plotQuantity :
    
    isMultiLayer = False
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
    l_inFileName = []
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



# ########## slimmedEle_isoDR0p3_sumETratio (PU 0) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE (PU 0)",
#    "ZEE (PU 0) (cleaned I_{0.3})",
#    "QCD (PU 0)",
#    "QCD (PU 0) (cleaned I_{0.3})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_isoDR0p3_sumETratio",
#    "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma",
#    "slimmedEle_isoDR0p3_sumETratio",
#    "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 7
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I_{0.3}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_isoDR0p3_sumETratio_ZEE_QCD_PU0"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## slimmedEle_isoDR0p3_sumETratio (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE (PU 200)",
#    "ZEE (PU 200) (cleaned I_{0.3})",
#    "QCD (PU 200)",
#    "QCD (PU 200) (cleaned I_{0.3})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_isoDR0p3_sumETratio",
#    "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma",
#    "slimmedEle_isoDR0p3_sumETratio",
#    "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 7
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I_{0.3}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_isoDR0p3_sumETratio_ZEE_QCD_PU200"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)


 ########## slimmedEle_iso_sumETratio_dR0p3_dzLt0p5 (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE",
    "ZEE (dz<0.5cm)",
    "ZEE (dz<0.5cm, #sigma_{t}<3)",
    "QCD",
    "QCD (dz<0.5cm)",
    "QCD (dz<0.5cm, #sigma_{t}<3)",
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
    7,
    9,
    1,
    7,
    9,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_sumETratio_dR0p3",
    "slimmedEle_iso_sumETratio_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt3",
    "slimmedEle_iso_sumETratio_dR0p3",
    "slimmedEle_iso_sumETratio_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 4
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I_{0.3}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 200)"
pltQty_temp.outFileName = "slimmedEle_iso_sumETratio_dR0p3_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5 (PU 0) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE",
    "ZEE (dz<0.5cm)",
    "ZEE (#sigma_{t}<3)",
    "ZEE (dz<0.5cm, #sigma_{t}<3)",
    "QCD",
    "QCD (dz<0.5cm)",
    "QCD (#sigma_{t}<3)",
    "QCD (dz<0.5cm, #sigma_{t}<3)",
]
pltQty_temp.l_lineColor = [
    2,
    4,
    8,
    6,
    2,
    4,
    8,
    6,
]
pltQty_temp.l_lineStyle = [
    7,
    7,
    7,
    7,
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_sumETratio_charged_dR0p3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I^{ch}_{0.3}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 0)"
#pltQty_temp.legendWidthScale = 0.85
pltQty_temp.outFileName = "slimmedEle_iso_sumETratio_charged_dR0p3_ZEE_QCD_PU0"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5 (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE",
    "ZEE (dz<0.5cm)",
    "ZEE (#sigma_{t}<3)",
    "ZEE (dz<0.5cm, #sigma_{t}<3)",
    "QCD",
    "QCD (dz<0.5cm)",
    "QCD (#sigma_{t}<3)",
    "QCD (dz<0.5cm, #sigma_{t}<3)",
]
pltQty_temp.l_lineColor = [
    2,
    4,
    8,
    6,
    2,
    4,
    8,
    6,
]
pltQty_temp.l_lineStyle = [
    7,
    7,
    7,
    7,
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_sumETratio_charged_dR0p3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I^{ch}_{0.3}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 200)"
#pltQty_temp.legendWidthScale = 0.85
pltQty_temp.outFileName = "slimmedEle_iso_sumETratio_charged_dR0p3_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_ZEE_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE (dz<0.5cm)",
    "ZEE (dz<0.5cm, #sigma_{t}<2)",
    "ZEE (dz<0.5cm, #sigma_{t}<3)",
    "ZEE (dz<0.5cm, #sigma_{t}<4)",
    "QCD (dz<0.5cm)",
    "QCD (dz<0.5cm, #sigma_{t}<2)",
    "QCD (dz<0.5cm, #sigma_{t}<3)",
    "QCD (dz<0.5cm, #sigma_{t}<4)",
]
pltQty_temp.l_lineColor = [
    2,
    4,
    8,
    6,
    2,
    4,
    8,
    6,
]
pltQty_temp.l_lineStyle = [
    7,
    7,
    7,
    7,
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3",
    "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I^{ch}_{0.3}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 200)"
#pltQty_temp.legendWidthScale = 0.85
pltQty_temp.outFileName = "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



# ########## slimmedEle_isoDR0p3_sumETratio_neutral ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE (PU 200)",
#    "ZEE (PU 200) (cleaned I_{0.3})",
#    "QCD (PU 200)",
#    "QCD (PU 200) (cleaned I_{0.3})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_isoDR0p3_sumETratio_neutral",
#    "slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma",
#    "slimmedEle_isoDR0p3_sumETratio_neutral",
#    "slimmedEle_isoDR0p3_sumETratio_neutral_cleanedDT3sigma",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 7
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I^{neutral}_{0.3}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_isoDR0p3_sumETratio_neutral_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## slimmedEle_isoDR0p3_sumETratio_ecal ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE (PU 200)",
#    "ZEE (PU 200) (cleaned I_{0.3})",
#    "QCD (PU 200)",
#    "QCD (PU 200) (cleaned I_{0.3})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_isoDR0p3_sumETratio_ecal",
#    "slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma",
#    "slimmedEle_isoDR0p3_sumETratio_ecal",
#    "slimmedEle_isoDR0p3_sumETratio_ecal_cleanedDT3sigma",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I^{ECAL}_{0.3}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_isoDR0p3_sumETratio_ecal_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## slimmedEle_isoDR0p3_sumETratio_hcal ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    
#    #"output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    #"output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    #"output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    #"output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE (PU 200)",
#    "ZEE (PU 200) (cleaned I_{0.3})",
#    "QCD (PU 200)",
#    "QCD (PU 200) (cleaned I_{0.3})",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_isoDR0p3_sumETratio_hcal",
#    "slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma",
#    "slimmedEle_isoDR0p3_sumETratio_hcal",
#    "slimmedEle_isoDR0p3_sumETratio_hcal_cleanedDT3sigma",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "I^{HCAL}_{0.3}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_isoDR0p3_sumETratio_hcal_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)



# ########## PV_tErr_ZEE ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE events (PU 0)",
#    "ZEE events (PU 200)",
#    "QCD events (PU 0)",
#    "QCD events (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "1000 * PV_tErr",
#    "1000 * PV_tErr",
#    "1000 * PV_tErr",
#    "1000 * PV_tErr",
#]
#pltQty_temp.l_cutStr = [
#    "1",
#    "1",
#    "1",
#    "1",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 50
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#deltat_{PV} [ps]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "PV_tErr_ZEE"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)
#
#
# ########## slimmedEle_pfCand_tErr_ZEE ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE sig-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE sig-PF cand. (PU 200)",
#    "ZEE iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "1000 * slimmedEle_sig_pfCand_tErr",
#    "1000 * slimmedEle_isoDR0p3_pfCand_tErr",
#    "1000 * slimmedEle_sig_pfCand_tErr",
#    "1000 * slimmedEle_isoDR0p3_pfCand_tErr",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 50
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#deltat_{PF} [ps]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_pfCand_tErr_ZEE"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)



# ########## slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_ZEE_QCD ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 200)",
#    "QCD iso-PF cand. (PU 0)",
#    "QCD iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 30
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#LT#sigma_{t}#GT"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)


# ########## slimmedEle_iso_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_ZEE_QCD ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 200)",
#    "QCD iso-PF cand. (PU 0)",
#    "QCD iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 30
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_iso_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)


 ########## slimmedEle_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_ZEE_QCD_PU200 ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand. (PU 200)",
    "ZEE iso-PF cand. (PU 200)",
    "QCD sig-PF cand. (PU 200)",
    "QCD iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
    "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 100
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0
pltQty_temp.xMax = 30
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



# ########## slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_ZEE_QCD ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 200)",
#    "QCD iso-PF cand. (PU 0)",
#    "QCD iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 30
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#LT#sigma_{t}#GT (dz < 0.5 cm)"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)



# ########## slimmedEle_iso_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_dzLt0p5_ZEE_QCD ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 200)",
#    "QCD iso-PF cand. (PU 0)",
#    "QCD iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
#    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 50
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 30
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "E_{T}-weighted #LT#sigma_{t}#GT (dz < 0.5 cm)"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "slimmedEle_iso_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_dzLt0p5_ZEE_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_dzLt0p5_ZEE_QCD_PU200 ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand. (PU 200)",
    "#splitline{ZEE iso-PF cand. (PU 200)}{(dz<0.5cm)}",
    "QCD sig-PF cand. (PU 200)",
    "#splitline{QCD iso-PF cand. (PU 200)}{(dz<0.5cm)}",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
    "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 100
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 50
pltQty_temp.xMin = 0
pltQty_temp.xMax = 30
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigniMean_ET-wtd_dR0p3_dzLt0p5_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_ZEE_QCD ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE lead. iso-PF cand. (PU 0)",
    "ZEE lead. iso-PF cand. (PU 200)",
    "QCD lead. iso-PF cand. (PU 0)",
    "QCD lead. iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 1020
pltQty_temp.createXmin = -10
pltQty_temp.createXmax = 500
pltQty_temp.xMin = -10
pltQty_temp.xMax = 30
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendWidthScale = 1.2
pltQty_temp.outFileName = "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_ZEE_QCD"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_ZEE_QCD ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE lead. iso-PF cand. (PU 0)",
    "ZEE lead. iso-PF cand. (PU 200)",
    "QCD lead. iso-PF cand. (PU 0)",
    "QCD lead. iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5",
    "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 1020
pltQty_temp.createXmin = -10
pltQty_temp.createXmax = 500
pltQty_temp.xMin = -10
pltQty_temp.xMax = 30
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t} (dz < 0.5 cm)"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendWidthScale = 1.2
pltQty_temp.outFileName = "slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_ZEE_QCD"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_pfCand_PV_dtSigni_ZEE ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand. (PU 0)",
    "ZEE iso-PF cand. (PU 0)",
    "ZEE sig-PF cand. (PU 200)",
    "ZEE iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 500
pltQty_temp.xMin = 0
pltQty_temp.xMax = 15
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigni_ZEE"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_pfCand_PV_dtSigni_ZEE_PU200 ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand.",
    "ZEE iso-PF cand.",
    "ZEE iso-PF cand. (dz<0.5cm)",
]
pltQty_temp.l_lineColor = [
    2,
    4,
    6,
]
pltQty_temp.l_lineStyle = [
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4 && slimmedEle_isoDR0p3_pfCand_PV_dz < 0.5",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 500
pltQty_temp.xMin = 0
pltQty_temp.xMax = 15
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 200)"
pltQty_temp.legendWidthScale = 1.1
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigni_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_pfCand_PV_dtSigni_QCD ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "QCD sig-PF cand. (PU 0)",
    "QCD iso-PF cand. (PU 0)",
    "QCD sig-PF cand. (PU 200)",
    "QCD iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 500
pltQty_temp.xMin = 0
pltQty_temp.xMax = 15
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigni_QCD"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)


 ########## slimmedEle_pfCand_PV_dtSigni_QCD_PU200 ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "QCD sig-PF cand.",
    "QCD iso-PF cand.",
    "QCD iso-PF cand. (dz<0.5cm)",
]
pltQty_temp.l_lineColor = [
    2,
    4,
    6,
]
pltQty_temp.l_lineStyle = [
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
    "slimmedEle_isoDR0p3_pfCand_PV_dtSigni",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15",
    "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && fabs(slimmedEle_isoDR0p3_pfCand_PV_dz) < 0.5",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 500
pltQty_temp.xMin = 0
pltQty_temp.xMax = 15
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#sigma_{t}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II EB (PU 200)"
pltQty_temp.legendWidthScale = 1.1
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dtSigni_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)


# ########## slimmedEle_pfCand_PV_dz_ZEE ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "ZEE sig-PF cand. (PU 0)",
#    "ZEE iso-PF cand. (PU 0)",
#    "ZEE sig-PF cand. (PU 200)",
#    "ZEE iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_sig_pfCand_PV_dz",
#    "slimmedEle_isoDR0p3_pfCand_PV_dz",
#    "slimmedEle_sig_pfCand_PV_dz",
#    "slimmedEle_isoDR0p3_pfCand_PV_dz",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
#]
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "dz [cm]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II EB"
#pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dz_ZEE"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## slimmedEle_pfCand_PV_dz_QCD ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.l_inFileName = [
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
#]
#pltQty_temp.l_label = [
#    "QCD sig-PF cand. (PU 0)",
#    "QCD iso-PF cand. (PU 0)",
#    "QCD sig-PF cand. (PU 200)",
#    "QCD iso-PF cand. (PU 200)",
#]
#pltQty_temp.l_lineColor = [
#    2,
#    2,
#    4,
#    4,
#]
#pltQty_temp.l_lineStyle = [
#    7,
#    1,
#    7,
#    1,
#]
#pltQty_temp.l_plotStr = [
#    "slimmedEle_sig_pfCand_PV_dz",
#    "slimmedEle_isoDR0p3_pfCand_PV_dz",
#    "slimmedEle_sig_pfCand_PV_dz",
#    "slimmedEle_isoDR0p3_pfCand_PV_dz",
#]
#pltQty_temp.l_cutStr = [
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#    "slimmedEle_pT > 15",
#]
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 1e-4
#pltQty_temp.yMax = 3
#pltQty_temp.logY = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "dz [cm]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.legendTitle = "Phase-II EB"
#pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dz_QCD"
#pltQty_temp.outDir = "plots/EB"
#l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_ZEE_QCD ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE iso-PF cand. (PU 0)",
    "ZEE iso-PF cand. (PU 200)",
    "QCD iso-PF cand. (PU 0)",
    "QCD iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_ZEE_QCD"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)


 ########## slimmedEle_sig_pfCand_PV_dzMean_ETwtd_ZEE_QCD ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-110X_mcRun4_realistic_v3_2026D49noPU-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand. (PU 0)",
    "ZEE sig-PF cand. (PU 200)",
    "QCD sig-PF cand. (PU 0)",
    "QCD sig-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_ZEE_QCD"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_pfCand_PV_dzMean_ETwtd_ZEE_QCD_PU200 ########## 
pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
    "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root",
]
pltQty_temp.l_label = [
    "ZEE sig-PF cand. (PU 200)",
    "ZEE iso-PF cand. (PU 200)",
    "QCD sig-PF cand. (PU 200)",
    "QCD iso-PF cand. (PU 200)",
]
pltQty_temp.l_lineColor = [
    2,
    2,
    4,
    4,
]
pltQty_temp.l_lineStyle = [
    7,
    1,
    7,
    1,
]
pltQty_temp.l_plotStr = [
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
    "slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all",
    "slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3",
]
pltQty_temp.l_cutStr = [
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15 && slimmedEle_genEl_minDeltaR < 0.4",
    "slimmedEle_pT > 15",
    "slimmedEle_pT > 15",
]
pltQty_temp.nBinX = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.outFileName = "slimmedEle_pfCand_PV_dzMean_ETwtd_ZEE_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



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
        
        inFile = ROOT.TFile.Open(l_inFileName[iSample], "READ")
        
        tree = inFile.Get("treeMaker/tree")
        
        #tree.Print()
        
        l_inFile.append(inFile)
        l_tree.append(tree)
    
    
    l_histDetail = []
    
    
    for iSample in range(0, len(l_inFileName)) :
        
        tree = l_tree[iSample]
        
        plotStr = plotQuantity.l_plotStr[iSample]
        cutStr = plotQuantity.l_cutStr[iSample]
        weightStr = plotQuantity.weightStr
        
        h1_temp = ROOT.TH1F("h1_temp_%s" %(iSample+1), l_label[iSample], plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax)
        h1_temp.Sumw2()
        
        plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
        weightStr = "%s * (%s)" %(weightStr, cutStr)
        
        print plotStr
        print weightStr
        
        tree.Draw(plotStr, weightStr)
        
        if (plotQuantity.normalize) :
            
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
        legendTitle = "#scale[1.7]{%s}" %(plotQuantity.legendTitle),
        legendWidthScale = plotQuantity.legendWidthScale,
        l_extraText = [[plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText]],
        CMSextraText = "Simulation Preliminary",
        fixAlphanumericBinLabels = False,
        outFileName = outFileName,
        outFileName_suffix = "",
    )
    
    
    for f in l_inFile :
        
        f.Close()
    
    
    #time.sleep(2)
