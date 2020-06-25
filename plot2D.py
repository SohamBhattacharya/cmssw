import os
import numpy

import ROOT

import Common

import CMS_lumi
import tdrstyle


ROOT.gSystem.Load("EDAnalyzers/TreeMaker/interface/CustomRootDict_cc.so")


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


 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ZEE (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_isoDR0p3_pfCand_PV_dtSigni : slimmedEle_isoDR0p3_pfCand_PV_dz"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4 && slimmedEle_isoDR0p3_pfCand_charge"
pltQty_temp.nBinX = 1010
pltQty_temp.createXmin = -10
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1020
pltQty_temp.createYmin = -10
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 20
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "dz [cm]"
pltQty_temp.yTitle = "#sigma_{t}"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{ZEE iso-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ETratio-wtd_ZEE (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_isoDR0p3_pfCand_PV_dtSigni : slimmedEle_isoDR0p3_pfCand_PV_dz"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4"
pltQty_temp.weightStr = "slimmedEle_isoDR0p3_pfCand_ET / slimmedEle_ET[slimmedEle_isoDR0p3_pfCand_eleIdx]"
#pltQty_temp.weightStr = "slimmedEle_isoDR0p3_pfCand_ET"
pltQty_temp.normalize = False
pltQty_temp.binAvg = True
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 0
pltQty_temp.yMax = 5
pltQty_temp.zMin = 0.01
pltQty_temp.zMax = 0.1
pltQty_temp.logZ = True
pltQty_temp.plotStyle = "colz text89 E"
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "dz [cm]"
pltQty_temp.yTitle = "#sigma_{t}"
pltQty_temp.zTitle = "E^{iso-PF}_{T} / E^{ele}_{T}"
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{ZEE iso-PF cand.}"
pltQty_temp.extraTextX = 1
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ETratio-wtd_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_isoDR0p3_pfCand_PV_dtSigni : slimmedEle_isoDR0p3_pfCand_PV_dz"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 5
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "dz [cm]"
pltQty_temp.yTitle = "#sigma_{t}"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{QCD iso-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ETratio-wtd_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_isoDR0p3_pfCand_PV_dtSigni : slimmedEle_isoDR0p3_pfCand_PV_dz"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15"
pltQty_temp.weightStr = "slimmedEle_isoDR0p3_pfCand_ET / slimmedEle_ET[slimmedEle_isoDR0p3_pfCand_eleIdx]"
#pltQty_temp.weightStr = "slimmedEle_isoDR0p3_pfCand_ET"
pltQty_temp.normalize = False
pltQty_temp.binAvg = True
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 0
pltQty_temp.yMax = 5
pltQty_temp.zMin = 0.01
pltQty_temp.zMax = 0.1
pltQty_temp.logZ = True
pltQty_temp.plotStyle = "colz text89 E"
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "dz [cm]"
pltQty_temp.yTitle = "#sigma_{t}"
pltQty_temp.zTitle = "E^{iso-PF}_{T} / E^{ele}_{T}"
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{QCD iso-PF cand.}"
pltQty_temp.extraTextX = 1
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigni_vs_pfCand-PV-dz_ETratio-wtd_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_sig_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_ZEE (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all : slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_sig_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_sig_pfCand_eleIdx] < 0.4"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 20
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{ZEE sig-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_sig_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_sig_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all : slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_sig_pfCand_eleIdx] > 15"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 20
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{QCD sig-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_sig_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_ZEE (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3 : slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 20
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{ZEE iso-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3 : slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 100.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 5
pltQty_temp.yMin = 0
pltQty_temp.yMax = 20
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{T}-weighted #LTdz#GT [cm]"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{QCD iso-PF cand.}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 19
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_pfCand-PV-dtSigniMean_vs_pfCand-PV-dzMean_ETwtd_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_dzLt0p5_pfCand-PV-dtSigniMean_ETwtd_vs_sumETratio_charged_ZEE (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5 : slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15 && slimmedEle_genEl_minDeltaR[slimmedEle_isoDR0p3_pfCand_eleIdx] < 0.4"
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 50.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 3
pltQty_temp.yMin = 0
pltQty_temp.yMax = 10
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I^{ch}_{0.3}"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{ZEE iso-PF cand. (dz<0.5cm)}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 4
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_dzLt0p5_pfCand-PV-dtSigniMean_ETwtd_vs_sumETratio_charged_ZEE_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



 ########## slimmedEle_isoDR0p3_dzLt0p5_pfCand-PV-dtSigniMean_ETwtd_vs_sumETratio_charged_QCD (PU 200) ########## 
pltQty_temp = plotQuantity()
pltQty_temp.inFileName = "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
pltQty_temp.plotStr = "slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5 : slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5"
pltQty_temp.cutStr = "slimmedEle_pT[slimmedEle_isoDR0p3_pfCand_eleIdx] > 15"
pltQty_temp.nBinX = 500
pltQty_temp.createXmin = 0.0
pltQty_temp.createXmax = 50.0
pltQty_temp.nBinY = 1000
pltQty_temp.createYmin = 0.0
pltQty_temp.createYmax = 500.0
pltQty_temp.xMin = 0
pltQty_temp.xMax = 3
pltQty_temp.yMin = 0
pltQty_temp.yMax = 10
pltQty_temp.zMin = 1e-4
pltQty_temp.zMax = 1e-1
pltQty_temp.logZ = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "I^{ch}_{0.3}"
pltQty_temp.yTitle = "E_{T}-weighted #LT#sigma_{t}#GT"
pltQty_temp.zTitle = "a.u."
pltQty_temp.extraText = "#splitline{Phase-II EB (PU 200)}{QCD iso-PF cand. (dz<0.5cm)}"
pltQty_temp.extraTextX = 0.5
pltQty_temp.extraTextY = 4
pltQty_temp.outFileName = "slimmedEle_isoDR0p3_dzLt0p5_pfCand-PV-dtSigniMean_ETwtd_vs_sumETratio_charged_QCD_PU200"
pltQty_temp.outDir = "plots/EB"
l_plotQuantity.append(pltQty_temp)



for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    outDir = "%s" %(plotQuantity.outDir)
    os.system("mkdir -p %s" %(outDir))
    
    
    inFile = ROOT.TFile.Open(plotQuantity.inFileName, "READ")
    
    tree = inFile.Get("treeMaker/tree")
    
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
    
    tree.Draw(plotStr, weightStr)
    
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
    
    
    inFile.Close()
