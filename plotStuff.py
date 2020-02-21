import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle

import Common
import Details


class plotQuantity :
    
    isMultiLayer = False
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
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
    
    outFileName = ""
    outDir = ""


tdrstyle.setTDRStyle()

ROOT.gStyle.SetPaintTextFormat("0.1f")

#inFile = ROOT.TFile.Open("ntupleTree.root")
#inFile = ROOT.TFile.Open("ntupleTree_modTICLele.root")
inFile = ROOT.TFile.Open("ntupleTree_rerunTICL_modTICLeleWithRerunTICL_with-TICLFragmentationFix.root")

#inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits_withRecToSimAssoc.root")
#inFile = ROOT.TFile.Open("/media/soham/E/HGCal_ele-reco/data_mySample/ntupleTree.root")

#inFile = ROOT.TFile.Open("/media/soham/E/HGCal_ele-reco/data_mySample/ntupleTree_Expo3D.root")

tree = inFile.Get("treeMaker/tree")


##################################################
##### 1D plots ###################################
##################################################
l_plotQuantity = []


# unclustered recHits
l_unclusRecHtLayer = [1, 2, 3, 6, 7, 8, 15, 26, 27]
#l_unclusRecHtLayer = [3]

for iLayer in range(0, len(l_unclusRecHtLayer)) :
    
    layer = l_unclusRecHtLayer[iLayer]
    
    
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && !recHit_isMultiClusMatched && recHit_matchedHGCALlayerClusIndex >= 0 && recHit_layer == %d) / "
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && !recHit_isMultiClusMatched && recHit_layer == %d)" %(layer, layer)
    #)
    #pltQty_temp.cutStr = (
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && !recHit_isMultiClusMatched && recHit_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = 100
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 1.1
    #pltQty_temp.yMin = 1e-3
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.5]{#frac{# rec-hit (w. sim-hit, not in multi-clus, in 2D-clus)}{# rec-hit (w. sim-hit, not in multi-clus)}}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.1
    #pltQty_temp.extraTextY = 0.7
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "unclusRecHit_3Dclus-efficiency_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    #
    #
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && recHit_matchedHGCALlayerClusIndex >= 0 && recHit_layer == %d) / "
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && recHit_layer == %d)" %(layer, layer)
    #)
    #pltQty_temp.cutStr = (
    #    "Sum$(recHit_matchedSimHitIndex >= 0 && recHit_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = 100
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 1.1
    #pltQty_temp.yMin = 1e-3
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.5]{#frac{# rec-hit (w. sim-hit, in 2D-clus)}{# rec-hit (w. sim-hit)}}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.1
    #pltQty_temp.extraTextY = 0.7
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "recHit_2Dclus-efficiency_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    
    
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "recHit_E*(recHit_matchedSimHitIndex >= 0 && recHit_matchedHGCALlayerClusIndex < 0 && recHit_layer == %d)" %(layer)
    #)
    #pltQty_temp.cutStr = (
    #    "(recHit_matchedSimHitIndex >= 0 && recHit_matchedHGCALlayerClusIndex < 0 && recHit_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = int(1e5)
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 1e2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 0.05
    #pltQty_temp.yMin = 1e-5
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.8]{E_{rec-hit} (not in 2D-clus, w. sim-hit) [GeV]}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.03
    #pltQty_temp.extraTextY = 0.1
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "recHit-notIn2Dclus-withSimHit-E_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    #
    #
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "recHit_E*(recHit_matchedSimHitIndex < 0 && recHit_matchedHGCALlayerClusIndex < 0 && recHit_layer == %d)" %(layer)
    #)
    #pltQty_temp.cutStr = (
    #    "(recHit_matchedSimHitIndex < 0 && recHit_matchedHGCALlayerClusIndex < 0 && recHit_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = int(1e5)
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 1e2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 0.05
    #pltQty_temp.yMin = 1e-5
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.8]{E_{rec-hit} (not in 2D-clus, w/o. sim-hit) [GeV]}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.03
    #pltQty_temp.extraTextY = 0.1
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "recHit-notIn2Dclus-withoutSimHit-E_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    
    
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "Sum$(HGCALlayerClus_sigRecHit_Efraction > 0.9 && HGCALlayerClus_layer == %d && HGCALlayerClus_isInMultiClus) / "
    #    "Sum$(HGCALlayerClus_sigRecHit_Efraction > 0.9 && HGCALlayerClus_layer == %d)" %(layer, layer)
    #)
    #pltQty_temp.cutStr = (
    #    "Sum$(HGCALlayerClus_sigRecHit_Efraction > 0.9 && HGCALlayerClus_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = 100
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 1.1
    #pltQty_temp.yMin = 1e-3
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.xLabelSizeScale = 0.8
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.5]{#frac{# 2D-clus (f_{sig} > 0.9, in multi-clus)}{# 2D-clus (f_{sig} > 0.9)}}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.1
    #pltQty_temp.extraTextY = 0.7
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "2Dclus-fSigGeq0p9_3Dclus-efficiency_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    
    
     #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "HGCALlayerClus_E*(!HGCALlayerClus_isInMultiClus && HGCALlayerClus_sigRecHit_Efraction > 0.9 && HGCALlayerClus_layer == %d)" %(layer)
    #)
    #pltQty_temp.cutStr = (
    #    "(!HGCALlayerClus_isInMultiClus && HGCALlayerClus_sigRecHit_Efraction > 0.9 && HGCALlayerClus_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = int(2 * 1e4)
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 1e2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 0.3
    #pltQty_temp.yMin = 1e-4
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.8]{E_{2D-clus} (not in multi-clus, f_{sig} > 0.9) [GeV]}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.2
    #pltQty_temp.extraTextY = 0.6
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "2Dclus-notInMultiCLus-fSigGeq0p9-E_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)
    #
    #
    # #####
    #pltQty_temp = plotQuantity()
    #pltQty_temp.isMultiLayer = False
    #pltQty_temp.plotStr = (
    #    "HGCALlayerClus_E*(!HGCALlayerClus_isInMultiClus && HGCALlayerClus_layer == %d)" %(layer)
    #)
    #pltQty_temp.cutStr = (
    #    "(!HGCALlayerClus_isInMultiClus && HGCALlayerClus_layer == %d) > 0" %(layer)
    #)
    #pltQty_temp.nBinX = int(2 * 1e4)
    #pltQty_temp.createXmin = 0
    #pltQty_temp.createXmax = 1e2
    #pltQty_temp.xMin = 0
    #pltQty_temp.xMax = 0.3
    #pltQty_temp.yMin = 1e-4
    #pltQty_temp.yMax = 1
    #pltQty_temp.logY = True
    #pltQty_temp.yLabelSizeScale = 0.9
    #pltQty_temp.xTitle = "#scale[0.8]{E_{2D-clus} (not in multi-clus) [GeV]}"
    #pltQty_temp.yTitle = "a.u."
    #pltQty_temp.extraText = "Layer %d" %(layer)
    #pltQty_temp.extraTextX = 0.2
    #pltQty_temp.extraTextY = 0.6
    #pltQty_temp.plotStyle = "hist"
    #pltQty_temp.outFileName = "2Dclus-notInMultiCLus-E_layer%d" %(layer)
    #pltQty_temp.outDir = "plots/misc"
    #l_plotQuantity.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.plotStr = "gsfEleFromMultiClus_n"
#pltQty_temp.cutStr = "1"
#pltQty_temp.nBinX = 10
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 5
#pltQty_temp.nDivisionsX = [5, 1, 1]
#pltQty_temp.centerLabelsX = True
#pltQty_temp.xTitle = "n_{TDR-e}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "tdrEl_n"
#pltQty_temp.outDir = "plots/misc"
#l_plotQuantity.append(pltQty_temp)


# ########## multicluster sigmaEtaEta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEP_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEM_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity.append(pltQty_temp)
#
#
# ########## multicluster sigmaPhiPhi
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEP_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEM_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity.append(pltQty_temp)
#
#
# ########## multicluster sigma-uu
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag1[multiClus_HGCalEEP_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 20
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 20
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.2
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{uu}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 13
#pltQty_temp.extraTextY = 0.18
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaUU"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag1[multiClus_HGCalEEM_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 20
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 20
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.2
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{uu}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 13
#pltQty_temp.extraTextY = 0.18
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaUU"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity.append(pltQty_temp)
#
#
# ########## multicluster sigma-vv
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag2[multiClus_HGCalEEP_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{vv}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaVV"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag2[multiClus_HGCalEEM_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{vv}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaVV"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity.append(pltQty_temp)
#
#
# ########## multicluster sigma-ww
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag3[multiClus_HGCalEEP_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{ww}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaWW"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag3[multiClus_HGCalEEM_EsortedIndex[0]])"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.1
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{ww}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 0.04
#pltQty_temp.extraTextY = 0.09
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "multiClus1-sigmaWW"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R7"
##pltQty_temp.cutStr = "fabs(gsfEleFromTICL_eta) > 1.7"
#pltQty_temp.nBinX = 400
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2
#pltQty_temp.xMin = 0.5
#pltQty_temp.xMax = 1.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.2
#pltQty_temp.logY = False
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele R7"
#pltQty_temp.yTitle = "a.u."
##pltQty_temp.extraText = "Layer %d" %(layer)
##pltQty_temp.extraTextX = 0.1
##pltQty_temp.extraTextY = 0.7
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "TICL-ele_R7"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R19"
##pltQty_temp.cutStr = "fabs(gsfEleFromTICL_eta) > 1.7"
#pltQty_temp.nBinX = 400
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2
#pltQty_temp.xMin = 0.5
#pltQty_temp.xMax = 1.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.2
#pltQty_temp.logY = False
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele R19"
#pltQty_temp.yTitle = "a.u."
##pltQty_temp.extraText = "Layer %d" %(layer)
##pltQty_temp.extraTextX = 0.1
##pltQty_temp.extraTextY = 0.7
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "TICL-ele_R19"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R2p8"
##pltQty_temp.cutStr = "fabs(gsfEleFromTICL_eta) > 1.7"
#pltQty_temp.nBinX = 400
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 2
#pltQty_temp.xMin = 0.5
#pltQty_temp.xMax = 1.1
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.2
#pltQty_temp.logY = False
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele R2.8"
#pltQty_temp.yTitle = "a.u."
##pltQty_temp.extraText = "Layer %d" %(layer)
##pltQty_temp.extraTextX = 0.1
##pltQty_temp.extraTextY = 0.7
#pltQty_temp.plotStyle = "hist"
#pltQty_temp.outFileName = "TICL-ele_R2p8"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity.append(pltQty_temp)



##################################################
##### 2D plots ###################################
##################################################
l_plotQuantity2D = []


# ########## multicluster-cluster size vs. multiplicity
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_nHit:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z > 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 15
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.nDivisionsY = [15, 1, 1]
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "Cluster size #(){n_{hit}}"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 14
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-nHit_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_nHit:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z < 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 15
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.nDivisionsY = [15, 1, 1]
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "Cluster size #(){n_{hit}}"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 14
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-nHit_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster-cluster layer vs. multiplicity
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_layer:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z > 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 1
#pltQty_temp.yMax = 29
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.nDivisionsY = [29, 1, 1]
#pltQty_temp.yLabelSizeScale = 0.8
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "Cluster layer"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 27
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-layer_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_layer:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z < 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 1
#pltQty_temp.yMax = 29
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.nDivisionsY = [29, 1, 1]
#pltQty_temp.yLabelSizeScale = 0.8
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "Cluster layer"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 27
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-layer_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster-cluster E vs. multiplicity
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_E:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z > 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 2000
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 1
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.centerLabelsX = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "E_{cluster} [GeV]"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 0.9
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-E_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_E:multiClus_uniqueClus_multiplicity"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z < 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 2000
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 100
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 10
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 1
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [10, 1, 1]
#pltQty_temp.centerLabelsX = True
#pltQty_temp.xTitle = "Cluster multiplicity in TICL-multiclusters"
#pltQty_temp.yTitle = "E_{cluster} [GeV]"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 7
#pltQty_temp.extraTextY = 0.9
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-E_vs_multiClus-clus-multiplicity"
#pltQty_temp.outDir = "plots/misc/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster-cluster size vs. layer
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_nHit:multiClus_uniqueClus_layer"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z > 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 200
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 200
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1
#pltQty_temp.xMax = 29
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 21
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [29, 1, 1]
#pltQty_temp.nDivisionsY = [21, 1, 1]
#pltQty_temp.xLabelSizeScale = 0.5
#pltQty_temp.yLabelSizeScale = 0.7
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster layer"
#pltQty_temp.yTitle = "Cluster size #(){n_{hit}}"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 21
#pltQty_temp.extraTextY = 19
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-nHit_vs_multiClus-clus-layer"
#pltQty_temp.outDir = "plots/misc/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "multiClus_uniqueClus_nHit:multiClus_uniqueClus_layer"
#pltQty_temp.cutStr = "multiClus_uniqueClus_z < 0"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 100
#pltQty_temp.nBinY = 200
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 200
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1
#pltQty_temp.xMax = 29
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 21
#pltQty_temp.logZ = True
#pltQty_temp.nDivisionsX = [29, 1, 1]
#pltQty_temp.nDivisionsY = [21, 1, 1]
#pltQty_temp.xLabelSizeScale = 0.5
#pltQty_temp.yLabelSizeScale = 0.7
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = "Cluster layer"
#pltQty_temp.yTitle = "Cluster size #(){n_{hit}}"
#pltQty_temp.zTitle = "% of clusters"
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 21
#pltQty_temp.extraTextY = 19
#pltQty_temp.plotStyle = "colz text45"
#pltQty_temp.outFileName = "multiClus-clus-nHit_vs_multiClus-clus-layer"
#pltQty_temp.outDir = "plots/misc/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)


# ########## multicluster sigma-rr vs. eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2rr[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 20
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{rr}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 18
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaRR_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2rr[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 20
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{rr}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 18
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaRR_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigmaEtaEta vs eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigmaEtaEta vs E
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_E[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 150
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 E [GeV]"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 115
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-E"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_E[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 150
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 E [GeV]"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 115
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-E"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigmaPhiPhi vs. eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigmaPhiPhi vs E
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_E[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 150
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 E [GeV]"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 115
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi_vs_multiClus1-E"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_E[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 150
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 E [GeV]"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 115
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaPhiPhi_vs_multiClus1-E"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigmaEtaEta vs. sigmaPhiPhi
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEP_EsortedIndex[0]]):sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 0.01
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-sigmaPhiPhi"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2etaEta[multiClus_HGCalEEM_EsortedIndex[0]]):sqrt(multiClus_sigma2phiPhi[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 0.0
#pltQty_temp.createXmax = 0.1
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.07
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 #sigma_{#phi#phi}"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{#eta#eta}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 0.01
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaEtaEta_vs_multiClus1-sigmaPhiPhi"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigma-uu vs. eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag1[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 20
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{uu}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 18
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaUU_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag1[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 20
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{uu}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 18
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaUU_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigma-vv vs. eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag2[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{vv}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaVV_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag2[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{vv}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaVV_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)
#
#
# ########## multicluster sigma-ww vs. eta
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag3[multiClus_HGCalEEP_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEP_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEP_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0.0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{ww}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#plus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaWW_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEP"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "sqrt(multiClus_sigma2diag3[multiClus_HGCalEEM_EsortedIndex[0]]):fabs(multiClus_eta[multiClus_HGCalEEM_EsortedIndex[0]])"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 100
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 0.1
##pltQty_temp.normalize = False
#pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 0.07
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "multi-clus1 |#eta|"
#pltQty_temp.yTitle = "multi-clus1 #sigma_{ww}"
#pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = "HGCal EE#minus"
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "multiClus1-sigmaWW_vs_multiClus1-eta"
#pltQty_temp.outDir = "plots/showerShape/HGCalEEM"
#l_plotQuantity2D.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R7:fabs(gsfEleFromTICL_eta)"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 50
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 1
##pltQty_temp.normalize = False
##pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 1.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele |#eta|"
#pltQty_temp.yTitle = "R7"
#pltQty_temp.zTitle = "a.u."
##pltQty_temp.extraText = ""
##pltQty_temp.extraTextX = 1.6
##pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "TICL-ele_R7_vs_eta"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R19:fabs(gsfEleFromTICL_eta)"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 50
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 1
##pltQty_temp.normalize = False
##pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 1.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele |#eta|"
#pltQty_temp.yTitle = "R19"
#pltQty_temp.zTitle = "a.u."
##pltQty_temp.extraText = ""
##pltQty_temp.extraTextX = 1.6
##pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "TICL-ele_R19_vs_eta"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity2D.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "gsfEleFromTICL_R2p8:fabs(gsfEleFromTICL_eta)"
##pltQty_temp.cutStr = ""
##pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
#pltQty_temp.nBinX = 50
#pltQty_temp.createXmin = 1.5
#pltQty_temp.createXmax = 3.0
#pltQty_temp.nBinY = 100
#pltQty_temp.createYmin = 0
#pltQty_temp.createYmax = 1
##pltQty_temp.normalize = False
##pltQty_temp.scale = 100
#pltQty_temp.xMin = 1.5
#pltQty_temp.xMax = 3.0
#pltQty_temp.yMin = 0.0
#pltQty_temp.yMax = 1.0
#pltQty_temp.yLabelSizeScale = 0.9
#pltQty_temp.xTitle = "TICL-ele |#eta|"
#pltQty_temp.yTitle = "R2.8"
#pltQty_temp.zTitle = "a.u."
##pltQty_temp.extraText = ""
##pltQty_temp.extraTextX = 1.6
##pltQty_temp.extraTextY = 0.065
#pltQty_temp.plotStyle = "colz"
#pltQty_temp.outFileName = "TICL-ele_R2p8_vs_eta"
#pltQty_temp.outDir = "plots/showerShape/"
#l_plotQuantity2D.append(pltQty_temp)


pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.plotStr = "multiClus_mc1_dEta:multiClus_mc1_dPhi"
#pltQty_temp.cutStr = "genEl_pT[0] < 30"
#pltQty_temp.weightStr = "multiClus_ET[multiClus_HGCalEEM_EsortedIndex[0]]"
pltQty_temp.nBinX = 2000
pltQty_temp.createXmin = -5.0
pltQty_temp.createXmax = +5.0
pltQty_temp.nBinY = 2000
pltQty_temp.createYmin = -5.0
pltQty_temp.createYmax = +5.0
#pltQty_temp.normalize = False
#pltQty_temp.scale = 100
pltQty_temp.xMin = -0.5
pltQty_temp.xMax = +0.5
pltQty_temp.yMin = -0.5
pltQty_temp.yMax = +0.5
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "#Delta#phi"
pltQty_temp.yTitle = "#Delta#eta"
pltQty_temp.zTitle = "a.u."
#pltQty_temp.extraText = ""
#pltQty_temp.extraTextX = 1.6
#pltQty_temp.extraTextY = 0.065
pltQty_temp.plotStyle = "colz"
pltQty_temp.outFileName = "multiClus_mc1_dEta_vs_dPhi"
pltQty_temp.outDir = "plots/mustache_with-TICLfragmentationFix/"
l_plotQuantity2D.append(pltQty_temp)




for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    outDir = "%s" %(plotQuantity.outDir)
    os.system("mkdir -p %s" %(outDir))
    
    l_histDetail = []
    
    plotStr = plotQuantity.plotStr
    cutStr = plotQuantity.cutStr
    weightStr = plotQuantity.weightStr
    
    #for key in d_strReplace :
    #    
    #    print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
    #    
    #    plotStr = plotStr.replace(key, d_strReplace[key])
    #    cutStr = cutStr.replace(key, d_strReplace[key])
    
    
    h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax)
    h1_temp.Sumw2()
    
    plotStr = "%s >> h1_temp" %(plotStr)
    weightStr = "%s * (%s)" %(weightStr, cutStr)
    
    print plotStr
    print weightStr
    
    tree.Draw(plotStr, weightStr)
    
    if (plotQuantity.normalize) :
        
        h1_temp.Scale(1.0 / h1_temp.Integral())
    
    histDetail_temp = Common.HistogramDetails()
    histDetail_temp.hist = h1_temp.Clone()
    histDetail_temp.lineWidth = 4
    histDetail_temp.lineColor = 4
    #histDetail_temp.addToLegend = False
    #histDetail_temp.histLabel = "#mu=%0.1e" %(histDetail_temp.hist.GetMean())
    
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
        #gridX = False, gridY = False,
        nDivisionsX = plotQuantity.nDivisionsX,
        nDivisionsY = plotQuantity.nDivisionsY,
        xLabelSizeScale = plotQuantity.xLabelSizeScale,
        yLabelSizeScale = plotQuantity.yLabelSizeScale,
        centerLabelsX = plotQuantity.centerLabelsX,
        centerLabelsY = plotQuantity.centerLabelsY,
        drawLegend = False,
        #legendHeightScale = 0.3,
        #transparentLegend = True,
        #legendTextSize = -1,
        #legendBorderSize = 0,
        #legendPos = "UR",
        #legendTitle = "#scale[1.1]{HGCal EE%s}" %(zsizeSignLatex),
        l_extraText = [[plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText]],
        CMSextraText = "Simulation Preliminary",
        fixAlphanumericBinLabels = False,
        outFileName = outFileName,
        outFileName_suffix = "",
    )


for iQty in range(0, len(l_plotQuantity2D)) :
    
    plotQuantity = l_plotQuantity2D[iQty]
    
    plotStr = plotQuantity.plotStr
    cutStr = plotQuantity.cutStr
    weightStr = plotQuantity.weightStr
    
    plotDir = plotQuantity.outDir
    outFileName = plotQuantity.outFileName
    
    os.system("mkdir -p %s" %(plotDir))
    
    
    h2_temp = ROOT.TH2F(
        "h2_temp", "h2_temp",
        plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax,
        plotQuantity.nBinY, plotQuantity.createYmin, plotQuantity.createYmax
    )
    h2_temp.Sumw2()
    
    plotStr = "%s >> h2_temp" %(plotStr)
    weightStr = "%s * (%s)" %(weightStr, cutStr)
    
    print plotStr
    print weightStr
    
    
    canvas = ROOT.TCanvas("canvas", "canvas")
    
    canvas.SetCanvasSize(800, 600)
    canvas.SetLeftMargin(0.8 * canvas.GetLeftMargin())
    canvas.SetRightMargin(10 * canvas.GetRightMargin())#0.19)
    
    tree.Draw(plotStr, weightStr, plotQuantity.plotStyle)
    
    if (plotQuantity.normalize) :
        
        h2_temp.Scale(1.0 / h2_temp.Integral())
    
    h2_temp.Scale(plotQuantity.scale)
    #print h2_temp.Integral()
    
    h2_temp.GetXaxis().SetRangeUser(plotQuantity.xMin, plotQuantity.xMax)
    h2_temp.GetYaxis().SetRangeUser(plotQuantity.yMin, plotQuantity.yMax)
    
    h2_temp.GetXaxis().SetTitle(plotQuantity.xTitle)
    h2_temp.GetXaxis().CenterTitle()
    
    h2_temp.GetYaxis().SetTitle(plotQuantity.yTitle)
    h2_temp.GetYaxis().SetTitleOffset(0.95)
    h2_temp.GetYaxis().CenterTitle()
    
    h2_temp.GetZaxis().SetTitle(plotQuantity.zTitle)
    h2_temp.GetZaxis().SetTitleOffset(1.2)
    h2_temp.GetZaxis().CenterTitle()
    
    h2_temp.GetXaxis().CenterLabels(plotQuantity.centerLabelsX)
    h2_temp.GetYaxis().CenterLabels(plotQuantity.centerLabelsY)
    
    h2_temp.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * plotQuantity.xLabelSizeScale)
    h2_temp.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * plotQuantity.yLabelSizeScale)
    
    h2_temp.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * plotQuantity.xTitleSizeScale)
    h2_temp.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * plotQuantity.yTitleSizeScale)
    
    h2_temp.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Y") * 0.8)#plotQuantity.yTitleSizeScale)
    
    if (abs(sum(plotQuantity.nDivisionsX)) > 0) :
        
        h2_temp.GetXaxis().SetNdivisions(plotQuantity.nDivisionsX[0], plotQuantity.nDivisionsX[1], plotQuantity.nDivisionsX[2])
    
    if (abs(sum(plotQuantity.nDivisionsY)) > 0) :
        
        h2_temp.GetYaxis().SetNdivisions(plotQuantity.nDivisionsY[0], plotQuantity.nDivisionsY[1], plotQuantity.nDivisionsY[2])
    
    canvas.SetLogx(plotQuantity.logX)
    canvas.SetLogy(plotQuantity.logY)
    canvas.SetLogz(plotQuantity.logZ)
    
    if (len(plotQuantity.extraText)) :
        
        latex = ROOT.TLatex()
        #latex.SetTextFont(62);
        latex.SetTextSize(0.045);
        latex.SetTextAlign(13);
        
        latex.DrawLatex(plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText)
    
    
    CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")
    
    
    canvas.SaveAs("%s/%s.pdf" %(plotDir, outFileName))
    canvas.SaveAs("%s/%s.png" %(plotDir, outFileName))
