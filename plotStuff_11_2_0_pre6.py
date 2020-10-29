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


pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "TDR-ele",
    "TICL-ele (current release)",
    "TICL-ele (HGCal seeded)",
    "TICL-ele (2020-10-14, 9b855f6)",
]
pltQty_temp.l_lineColor = [
    1,
    2,
    4,
    6,
]
pltQty_temp.l_lineStyle = [
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "gsfEleFromMultiClus_n",
    "gsfEleFromTICL_n",
    "gsfEleFromTICL_n",
    "gsfEleFromTICL_n",
]
pltQty_temp.l_cutStr = [
    "1",
    "1",
    "1",
    "1",
]
pltQty_temp.nBinX = 10000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 100
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 50
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "n_{ele}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "E2"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.legendPos = "UR"
pltQty_temp.outFileName = "gsfEle_n"
pltQty_temp.outDir = "plots/validation_11_2_0_pre6"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "TDR-ele",
    "TICL-ele (current release)",
    "TICL-ele (HGCal seeded)",
    "TICL-ele (2020-10-14, 9b855f6)",
]
pltQty_temp.l_lineColor = [
    1,
    2,
    4,
    6,
]
pltQty_temp.l_lineStyle = [
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "gsfEleFromMultiClus_E / gsfEleFromMultiClus_matchedGenEl_E",
    "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E",
    "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E",
    "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E",
]
pltQty_temp.l_cutStr = [
    "gsfEleFromMultiClus_pT > 15 && gsfEleFromMultiClus_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 3
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{reco} / E_{gen}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.legendPos = "UR"
pltQty_temp.outFileName = "gsfEle-E_by_genEle-E_PU200"
pltQty_temp.outDir = "plots/validation_11_2_0_pre6"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM.txt",
    "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "TICL-ele (current release)",
    "TICL-ele (HGCal seeded)",
    "TICL-ele (2020-10-14, 9b855f6)",
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
    "gsfEleFromTICL_superClus_nClus",
    "gsfEleFromTICL_superClus_nClus",
    "gsfEleFromTICL_superClus_nClus",
]
pltQty_temp.l_cutStr = [
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
    "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4",
]
pltQty_temp.nBinX = 10000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 100
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 10
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "n_{clus} in SC"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "E2"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.legendPos = "LL"
pltQty_temp.outFileName = "gsfEle_superClus-nClus"
pltQty_temp.outDir = "plots/validation_11_2_0_pre6"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.l_inFileName = [
    "sourceFiles/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
    "sourceFiles/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_11_2_0_pre7.txt",
    "sourceFiles/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_multiClustersFromTrackstersEM.txt",
    "sourceFiles/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6/TreeMaker_SinglePhoton_PT2to200_Phase2HLTTDRSummer20ReRECOMiniAOD-PU200_111X_mcRun4_realistic_T15_v1_ext2-v1_FEVT_felicepantaleo_EMTrackSeeded_11_2_0_pre6_2020-10-14_1_9b855f6.txt",
]
pltQty_temp.l_treeName = [
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
    "treeMaker/tree",
]
pltQty_temp.l_label = [
    "TDR-pho",
    "TICL-pho (current release)",
    "TICL-pho (HGCal seeded)",
    "TICL-pho (2020-10-14, 9b855f6)",
]
pltQty_temp.l_lineColor = [
    1,
    2,
    4,
    6,
]
pltQty_temp.l_lineStyle = [
    1,
    1,
    1,
    1,
]
pltQty_temp.l_plotStr = [
    "phoFromMultiClus_E / phoFromMultiClus_matchedGenPh_E",
    "phoFromTICL_E / phoFromTICL_matchedGenPh_E",
    "phoFromTICL_E / phoFromTICL_matchedGenPh_E",
    "phoFromTICL_E / phoFromTICL_matchedGenPh_E",
]
pltQty_temp.l_cutStr = [
    "phoFromMultiClus_pT > 15 && phoFromMultiClus_genPh_minDeltaR < 0.4",
    "phoFromTICL_pT > 15 && phoFromTICL_genPh_minDeltaR < 0.4",
    "phoFromTICL_pT > 15 && phoFromTICL_genPh_minDeltaR < 0.4",
    "phoFromTICL_pT > 15 && phoFromTICL_genPh_minDeltaR < 0.4",
]
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0.0
pltQty_temp.xMax = 2
pltQty_temp.yMin = 1e-4
pltQty_temp.yMax = 3
pltQty_temp.logY = True
pltQty_temp.yLabelSizeScale = 0.9
pltQty_temp.xTitle = "E_{reco} / E_{gen}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.plotStyle = "hist"
pltQty_temp.legendTitle = "Phase-II HGCal (PU 200)"
pltQty_temp.legendPos = "UL"
pltQty_temp.outFileName = "pho-E_by_genPho-E_PU200"
pltQty_temp.outDir = "plots/validation_11_2_0_pre6"
l_plotQuantity.append(pltQty_temp)



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
        histDetail_temp.markerColor = l_lineColor[iSample]
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
