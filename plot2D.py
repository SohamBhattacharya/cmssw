import os
import numpy

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
    
    inFileName = ""
    
    nBinX = 0
    createXmin = 0
    createXmax = 0
    
    nBinY = 0
    createYmin = 0
    createYmax = 0
    
    normalize = True
    binAvg = False
    
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
    zLabelSizeScale = 1.0
    
    centerLabelsX = False
    centerLabelsY = False
    centerLabelsZ = False
    
    xTitle = ""
    yTitle = ""
    zTitle = ""
    
    xTitleSizeScale = 1.0
    yTitleSizeScale = 1.0
    zTitleSizeScale = 1.0
    
    xTitleOffsetscale = 1.0
    yTitleOffsetscale = 1.0
    zTitleOffsetscale = 1.0
    
    extraText = ""
    extraTextX = ""
    extraTextY = ""
    
    plotStyle = "colz"
    
    #legendTitle = "Phase-II EB"
    #legendPos = "UR"
    #legendTextSize = 0.03
    #legendWidthScale = 1
    
    outFileName = ""
    outDir = ""


tdrstyle.setTDRStyle()


l_plotQuantity = []


# ########## gsfEleFromTICL_sigmaEtaEta_vs_eta_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2etaEta) : fabs(gsfEleFromTICL_eta)"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 800
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 4
#pltQty_temp.nBinY = 400
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.2
#pltQty_temp.xMin = 1.4
#pltQty_temp.xMax = 3.1
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.05
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#||{#eta}"
#pltQty_temp.yTitle = "#sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.5
#pltQty_temp.extraTextY = 0.045
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaEtaEta_vs_eta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)
#
#
#
## ########## jet_sigmaEtaEta_vs_eta_PU200 (PU 200) ########## 
##pltQty_temp = plotQuantity()
##pltQty_temp.inFileName = "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt"
##pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2etaEta) : fabs(gsfEleFromTICL_eta)"
##pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4"
##pltQty_temp.nBinX = 800
##pltQty_temp.createXmin = 0
##pltQty_temp.createXmax = 4
##pltQty_temp.nBinY = 400
##pltQty_temp.createYmin = 0
##pltQty_temp.createYmax = 0.2
##pltQty_temp.xMin = 1.4
##pltQty_temp.xMax = 3.1
##pltQty_temp.yMin = 0.0
##pltQty_temp.yMax = 0.05
##pltQty_temp.zMin = 1e-5
##pltQty_temp.zMax = 1e-2
##pltQty_temp.logZ = True
##pltQty_temp.nDivisionsY = [5, 5, 0]
##pltQty_temp.yLabelSizeScale = 0.9
##pltQty_temp.xTitle = "#||{#eta}"
##pltQty_temp.yTitle = "#sigma_{#eta#eta}"
##pltQty_temp.zTitle = "a.u."
##pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Misid. electrons}"
##pltQty_temp.extraTextX = 1.5
##pltQty_temp.extraTextY = 0.045
##pltQty_temp.outFileName = "jet_sigmaEtaEta_vs_eta_PU200"
##pltQty_temp.outDir = "plots/vars_ID"
##l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## gsfEleFromTICL_sigmaPhiPhi_vs_eta_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2phiPhi) : fabs(gsfEleFromTICL_eta)"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 800
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 4
#pltQty_temp.nBinY = 400
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.2
#pltQty_temp.xMin = 1.4
#pltQty_temp.xMax = 3.1
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.05
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#||{#eta}"
#pltQty_temp.yTitle = "#sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.5
#pltQty_temp.extraTextY = 0.045
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaPhiPhi_vs_eta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)
#
#
#
## ########## jet_sigmaPhiPhi_vs_eta_PU200 (PU 200) ########## 
##pltQty_temp = plotQuantity()
##pltQty_temp.inFileName = "sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt"
##pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2phiPhi) : fabs(gsfEleFromTICL_eta)"
##pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4"
##pltQty_temp.nBinX = 800
##pltQty_temp.createXmin = 0
##pltQty_temp.createXmax = 4
##pltQty_temp.nBinY = 400
##pltQty_temp.createYmin = 0
##pltQty_temp.createYmax = 0.2
##pltQty_temp.xMin = 1.4
##pltQty_temp.xMax = 3.1
##pltQty_temp.yMin = 0.0
##pltQty_temp.yMax = 0.05
##pltQty_temp.zMin = 1e-5
##pltQty_temp.zMax = 1e-2
##pltQty_temp.logZ = True
##pltQty_temp.nDivisionsY = [5, 5, 0]
##pltQty_temp.yLabelSizeScale = 0.9
##pltQty_temp.xTitle = "#||{#eta}"
##pltQty_temp.yTitle = "#sigma_{#phi#phi}"
##pltQty_temp.zTitle = "a.u."
##pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Misid. electrons}"
##pltQty_temp.extraTextX = 1.5
##pltQty_temp.extraTextY = 0.045
##pltQty_temp.outFileName = "jet_sigmaPhiPhi_vs_eta_PU200"
##pltQty_temp.outDir = "plots/vars_ID"
##l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## gsfEleFromTICL_sigmaEtaEta_vs_E_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2etaEta) : gsfEleFromTICL_E"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 400
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2000
#pltQty_temp.nBinY = 400
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.2
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 1000
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.05
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [5, 5, 0]
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "E [GeV]"
#pltQty_temp.yTitle = "#sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.5
#pltQty_temp.extraTextY = 0.045
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaEtaEta_vs_E_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)
#
#
#
# ########## gsfEleFromTICL_sigmaPhiPhi_vs_E_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_superClus_sigma2phiPhi) : gsfEleFromTICL_E"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 400
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2000
#pltQty_temp.nBinY = 400
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.2
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 1000
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.05
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [5, 5, 0]
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "E [GeV]"
#pltQty_temp.yTitle = "#sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.5
#pltQty_temp.extraTextY = 0.045
#pltQty_temp.outFileName = "gsfEleFromTICL_sigmaPhiPhi_vs_E_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_E_vs_eta_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "gsfEleFromTICL_E : abs(gsfEleFromTICL_eta)"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 800
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 4
#pltQty_temp.nBinY = 400
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 2000
#pltQty_temp.xMin = 1.4
#pltQty_temp.xMax = 3.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 1000
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#||{#eta}"
#pltQty_temp.yTitle = "E [GeV]"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 900
#pltQty_temp.outFileName = "gsfEleFromTICL_E_vs_eta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



#l_cylR = ["2.0", "2.8", "3.5"]
#
#for iR, cylR in enumerate(l_cylR) :
#    
#    cylR_mod = cylR.replace(".", "p")
#    
#    ########## gsfEleFromTICL_sigmaUU_cylR2p8_vs_eta_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2uu_cylR%s) : fabs(gsfEleFromTICL_eta)" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 800
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 4
#    pltQty_temp.nBinY = 500
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 2
#    pltQty_temp.xMin = 1.4
#    pltQty_temp.xMax = 3.1
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 2
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "#||{#eta}"
#    pltQty_temp.yTitle = "#sigma_{uu} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 1.5
#    pltQty_temp.extraTextY = 1.75
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaUU_cylR%s_vs_eta_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_sigmaVV_cylR%s_vs_eta_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2vv_cylR%s) : fabs(gsfEleFromTICL_eta)" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 800
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 4
#    pltQty_temp.nBinY = 500
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 2
#    pltQty_temp.xMin = 1.4
#    pltQty_temp.xMax = 3.1
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 2
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "#||{#eta}"
#    pltQty_temp.yTitle = "#sigma_{vv} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 1.5
#    pltQty_temp.extraTextY = 1.75
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaVV_cylR%s_vs_eta_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_sigmaWW_cylR%s_vs_eta_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2ww_cylR%s) : fabs(gsfEleFromTICL_eta)" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 800
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 4
#    pltQty_temp.nBinY = 1000
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 50
#    pltQty_temp.xMin = 1.4
#    pltQty_temp.xMax = 3.1
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 10
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "#||{#eta}"
#    pltQty_temp.yTitle = "#sigma_{ww} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 1.5
#    pltQty_temp.extraTextY = 2.0
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaWW_cylR%s_vs_eta_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_sigmaUU_cylR%s_vs_E_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2uu_cylR%s) : gsfEleFromTICL_E" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 400
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 2000
#    pltQty_temp.nBinY = 500
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 2
#    pltQty_temp.xMin = 0
#    pltQty_temp.xMax = 1000
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 2
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsX = [5, 5, 0]
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "E [GeV]"
#    pltQty_temp.yTitle = "#sigma_{uu} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 100
#    pltQty_temp.extraTextY = 1.75
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaUU_cylR%s_vs_E_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_sigmaVV_cylR%s_vs_E_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2vv_cylR%s) : gsfEleFromTICL_E" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 400
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 2000
#    pltQty_temp.nBinY = 500
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 2
#    pltQty_temp.xMin = 0
#    pltQty_temp.xMax = 1000
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 2
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsX = [5, 5, 0]
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "E [GeV]"
#    pltQty_temp.yTitle = "#sigma_{vv} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 100
#    pltQty_temp.extraTextY = 1.75
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaVV_cylR%s_vs_E_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_sigmaWW_cylR%s_vs_E_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "sqrt(gsfEleFromTICL_sigma2ww_cylR%s) : gsfEleFromTICL_E" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 400
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 2000
#    pltQty_temp.nBinY = 1000
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 50
#    pltQty_temp.xMin = 0
#    pltQty_temp.xMax = 1000
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 10
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsX = [5, 5, 0]
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "E [GeV]"
#    pltQty_temp.yTitle = "#sigma_{ww} (R=%scm)" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 100
#    pltQty_temp.extraTextY = 2.0
#    pltQty_temp.outFileName = "gsfEleFromTICL_sigmaWW_cylR%s_vs_E_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    ########## gsfEleFromTICL_Rvar_cylR%s_vs_eta_PU200 (PU 200) ########## 
#    pltQty_temp = plotQuantity()
#    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    pltQty_temp.plotStr = "gsfEleFromTICL_Rvar_cylR%s : fabs(gsfEleFromTICL_eta)" %(cylR_mod)
#    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    pltQty_temp.nBinX = 800
#    pltQty_temp.createXmin = 0
#    pltQty_temp.createXmax = 4
#    pltQty_temp.nBinY = 200
#    pltQty_temp.createYmin = 0
#    pltQty_temp.createYmax = 2
#    pltQty_temp.xMin = 1.4
#    pltQty_temp.xMax = 3.1
#    pltQty_temp.yMin = 0.0
#    pltQty_temp.yMax = 1.0
#    pltQty_temp.zMin = 1e-5
#    pltQty_temp.zMax = 1e-2
#    pltQty_temp.logZ = True
#    pltQty_temp.nDivisionsY = [5, 5, 0]
#    pltQty_temp.yLabelSizeScale = 0.9
#    pltQty_temp.xTitle = "#||{#eta}"
#    pltQty_temp.yTitle = "R_{%s}" %(cylR)
#    pltQty_temp.zTitle = "a.u."
#    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    pltQty_temp.extraTextX = 2.1
#    pltQty_temp.extraTextY = 0.5
#    pltQty_temp.outFileName = "gsfEleFromTICL_Rvar_cylR%s_vs_eta_PU200" %(cylR_mod)
#    pltQty_temp.outDir = "plots/vars_ID"
#    l_plotQuantity.append(pltQty_temp)
#    
#    
#    
#    # ########## gsfEleFromTICL_R2p8_vs_eta_PU200 (PU 200) ########## 
#    #pltQty_temp = plotQuantity()
#    #pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#    #pltQty_temp.plotStr = "gsfEleFromTICL_R2p8 : fabs(gsfEleFromTICL_eta)"
#    #pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#    #pltQty_temp.nBinX = 800
#    #pltQty_temp.createXmin = 0
#    #pltQty_temp.createXmax = 4
#    #pltQty_temp.nBinY = 200
#    #pltQty_temp.createYmin = 0
#    #pltQty_temp.createYmax = 2
#    #pltQty_temp.xMin = 1.4
#    #pltQty_temp.xMax = 3.1
#    #pltQty_temp.yMin = 0.5
#    #pltQty_temp.yMax = 1.0
#    #pltQty_temp.zMin = 1e-5
#    #pltQty_temp.zMax = 1e-2
#    #pltQty_temp.logZ = True
#    #pltQty_temp.nDivisionsY = [5, 5, 0]
#    #pltQty_temp.yLabelSizeScale = 0.9
#    #pltQty_temp.xTitle = "#||{#eta}"
#    #pltQty_temp.yTitle = "R_{2.8}"
#    #pltQty_temp.zTitle = "a.u."
#    #pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#    #pltQty_temp.extraTextX = 2.1
#    #pltQty_temp.extraTextY = 0.7
#    #pltQty_temp.outFileName = "gsfEleFromTICL_R2p8_vs_eta_PU200"
#    #pltQty_temp.outDir = "plots/vars_ID"
#    #l_plotQuantity.append(pltQty_temp)



l_coneR = ["0.15", "0.2", "0.3"]

for iR, coneR in enumerate(l_coneR) :
    
    coneR_mod = coneR.replace(".", "p")
    
    ########## gsfEleFromTICL_HoverE_vs_pT_PU200 (PU 200) ########## 
    pltQty_temp = plotQuantity()
    pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
    pltQty_temp.plotStr = "gsfEleFromTICL_HoverE_dR%s : gsfEleFromTICL_pT" %(coneR_mod)
    pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
    pltQty_temp.nBinX = 30
    pltQty_temp.createXmin = 0
    pltQty_temp.createXmax = 300
    pltQty_temp.nBinY = 1000
    pltQty_temp.createYmin = 0
    pltQty_temp.createYmax = 50
    pltQty_temp.xMin = 0
    pltQty_temp.xMax = 250
    pltQty_temp.yMin = 0.0
    pltQty_temp.yMax = 2.5
    pltQty_temp.zMin = 1e-5
    pltQty_temp.zMax = 1e-2
    pltQty_temp.logZ = True
    pltQty_temp.nDivisionsX = [5, 5, 0]
    pltQty_temp.nDivisionsY = [5, 5, 0]
    pltQty_temp.yLabelSizeScale = 0.9
    pltQty_temp.xTitle = "p_{T} [GeV]"
    pltQty_temp.yTitle = "H/E (dR_{cone}=%s)" %(coneR)
    pltQty_temp.zTitle = "a.u."
    pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
    pltQty_temp.extraTextX = 20
    pltQty_temp.extraTextY = 2
    pltQty_temp.outFileName = "gsfEleFromTICL_HoverE_dR%s_vs_pT_PU200" %(coneR_mod)
    pltQty_temp.outDir = "plots/vars_ID"
    l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_iso_sumETratio_dR0p3_vs_eta_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "gsfEleFromTICL_iso_sumETratio_dR0p3 : fabs(gsfEleFromTICL_eta)"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 800
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 4
#pltQty_temp.nBinY = 500
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 50
#pltQty_temp.xMin = 1.4
#pltQty_temp.xMax = 3.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 5
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#||{#eta}"
#pltQty_temp.yTitle = "I_{0.3}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 2.1
#pltQty_temp.extraTextY = 4.5
#pltQty_temp.outFileName = "gsfEleFromTICL_iso_sumETratio_dR0p3_vs_eta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



# ########## gsfEleFromTICL_E_vs_eta_PU200 (PU 200) ########## 
#pltQty_temp = plotQuantity()
#pltQty_temp.inFileName = "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt"
#pltQty_temp.plotStr = "gsfEleFromTICL_E : fabs(gsfEleFromTICL_eta)"
#pltQty_temp.cutStr = "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4"
#pltQty_temp.nBinX = 800
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 4
#pltQty_temp.nBinY = 200
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 2000
#pltQty_temp.xMin = 1.4
#pltQty_temp.xMax = 3.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 1000
#pltQty_temp.zMin = 1e-5
#pltQty_temp.zMax = 1e-2
#pltQty_temp.logZ = True
##pltQty_temp.nDivisionsY = [5, 5, 0]
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "#||{#eta}"
#pltQty_temp.yTitle = "E [GeV]"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "#splitline{Phase-II HGCal (PU 200)}{Electrons}"
#pltQty_temp.extraTextX = 1.5
#pltQty_temp.extraTextY = 950
#pltQty_temp.outFileName = "gsfEleFromTICL_E_vs_eta_PU200"
#pltQty_temp.outDir = "plots/vars_ID"
#l_plotQuantity.append(pltQty_temp)



m_inputTree = {}


for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    outDir = "%s" %(plotQuantity.outDir)
    os.system("mkdir -p %s" %(outDir))
    
    
    #inFile = ROOT.TFile.Open(plotQuantity.inFileName, "READ")
    #
    #tree = inFile.Get("treeMaker/tree")
    
    tree = None
    
    if (plotQuantity.inFileName not in m_inputTree) :
        
        l_inFileName_iSample = []
        
        if (".root" in plotQuantity.inFileName) :
            
            l_inFileName_iSample = sigFiles.split(":")
        
        else :
            
            l_inFileName_iSample = numpy.loadtxt(plotQuantity.inFileName, delimiter = "someNonExistantString", dtype = str, ndmin = 1)
        
        
        treeName = "treeMaker/tree"
        tree = ROOT.TChain("tree")
        
        Common.openTChain(
            listFileName = plotQuantity.inFileName,
            chain = tree,
            treeName = treeName,
            nFileMax = -1,
            debug = True,
        )
        
        m_inputTree[plotQuantity.inFileName] = tree
    
    else :
        
        tree = m_inputTree[plotQuantity.inFileName]
    
    
    h2_temp = ROOT.TH2F(
        "h2_temp", "h2_temp",
        plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax,
        plotQuantity.nBinY, plotQuantity.createYmin, plotQuantity.createYmax,
    )
    h2_temp.Sumw2()
    
    h2_temp_count = h2_temp.Clone()
    h2_temp_count.SetName("h2_temp_count")
    h2_temp_count.SetTitle("h2_temp_count")
    
    plotStr = "%s >> %s" %(plotQuantity.plotStr, h2_temp.GetName())
    plotStr_count = "%s >> %s" %(plotQuantity.plotStr, h2_temp_count.GetName())
    weightStr = "%s * (%s)" %(plotQuantity.weightStr, plotQuantity.cutStr)
    
    print plotStr
    print weightStr
    
    tree.Draw(plotStr, weightStr, "goff")
    
    if (plotQuantity.binAvg) :
        
        tree.Draw(plotStr_count, plotQuantity.cutStr)
        
        h2_temp.Divide(h2_temp_count)
    
    if (plotQuantity.normalize) :
        
        h2_temp.Scale(1.0 / h2_temp.Integral())
    
    
    outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
    
    histDetail_temp = Common.HistogramDetails()
    histDetail_temp.hist = h2_temp.Clone()
    histDetail_temp.xMin = plotQuantity.xMin
    histDetail_temp.xMax = plotQuantity.xMax
    histDetail_temp.yMin = plotQuantity.yMin
    histDetail_temp.yMax = plotQuantity.yMax
    histDetail_temp.zMin = plotQuantity.zMin
    histDetail_temp.zMax = plotQuantity.zMax
    histDetail_temp.xTitle = plotQuantity.xTitle
    histDetail_temp.yTitle = plotQuantity.yTitle
    histDetail_temp.zTitle = plotQuantity.zTitle
    histDetail_temp.xTitleSizeScale = plotQuantity.xTitleSizeScale
    histDetail_temp.yTitleSizeScale = plotQuantity.yTitleSizeScale
    histDetail_temp.zTitleSizeScale = plotQuantity.zTitleSizeScale
    histDetail_temp.xTitleOffsetScale = 1.0
    histDetail_temp.yTitleOffsetScale = 0.85
    histDetail_temp.zTitleOffsetScale = 1.1
    histDetail_temp.xLabelSizeScale = plotQuantity.xLabelSizeScale
    histDetail_temp.yLabelSizeScale = plotQuantity.yLabelSizeScale
    histDetail_temp.zLabelSizeScale = plotQuantity.zLabelSizeScale
    histDetail_temp.nDivisionsX = plotQuantity.nDivisionsX
    histDetail_temp.nDivisionsY = plotQuantity.nDivisionsY
    histDetail_temp.drawOption = plotQuantity.plotStyle
    histDetail_temp.logZ = plotQuantity.logZ
    histDetail_temp.gridX = True
    histDetail_temp.gridY = True
    histDetail_temp.outFileName = outFileName
    
    
    ROOT.gStyle.SetPaintTextFormat("0.2g")
    
    
    Common.plot2D(
        histDetails = histDetail_temp,
        palette = ROOT.kVisibleSpectrum,
        l_extraText = [[plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText]],
        CMSextraText = "Simulation Preliminary",
    )
    
    
    #inFile.Close()
