import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle

import Common


class plotQuantity :
    
    isMultiLayer = False
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
    nBin = 0
    createXmin = 0
    createXmax = 0
    
    normalize = True
    
    xMin = 0
    xMax = 0
    
    yMin = 0
    yMax = 0
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    xTitle = ""
    yTitle = ""
    
    outFileName = ""
    outDir = ""



tdrstyle.setTDRStyle()

ROOT.gStyle.SetOptStat(1001110)
ROOT.gStyle.SetPalette(ROOT.kRainBow)


inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits_withRecToSimAssoc.root")
#inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits_withRecToSimAssoc_mySample.root")

tree = inFile.Get("treeMaker/tree")

HGCalEE_nLayer = 28


hitTypeStr = "rec"
l_zsideVal = [+1, -1]
l_layer = [1, 2, 7, 8, 26, 27, 28]



d_strReplace = {
    "@zsideCondStr@": "",
}


l_plotQuantity = []


#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = True
#pltQty_temp.plotStr = "recHit_E"
#pltQty_temp.cutStr = "recHit_matchedSimHitIndex >= 0"
#pltQty_temp.nBin = 2000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.3
#pltQty_temp.yMin = 2e-3
#pltQty_temp.yMax = 0.3
#pltQty_temp.nDivisionsX = [10, 10, 1]
#pltQty_temp.xTitle = "E_{rec-hit (with valid sim-hit)} [GeV]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-simHitMatched-E"
#pltQty_temp.outDir = "plots/recHitLayerEnergy"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = True
#pltQty_temp.plotStr = "recHit_E"
#pltQty_temp.nBin = 2000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0.0
#pltQty_temp.xMax = 0.3
#pltQty_temp.yMin = 1e-5
#pltQty_temp.yMax = 1.0
#pltQty_temp.nDivisionsX = [10, 10, 1]
#pltQty_temp.xTitle = "E_{rec-hit} [GeV]"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-E"
#pltQty_temp.outDir = "plots/recHitLayerEnergy"
#l_plotQuantity.append(pltQty_temp)
#
#
###### multi-clus vs. rec-hit #####
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(multiClus_E*(multiClus_z @zsideCondStr@))/Sum$(recHit_E*(recHit_z @zsideCondStr@ && recHit_matchedSimHitIndex >= 0))"
#pltQty_temp.nBin = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.1
#pltQty_temp.xTitle = "E^{tot}_{multi-clus} / E^{tot}_{rec-hit (with valid sim-hit)}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "multiClus-totE_by_recHit-simHitMatched-totE"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(multiClus_E*(multiClus_z @zsideCondStr@))/Sum$(recHit_E*(recHit_z @zsideCondStr@))"
#pltQty_temp.nBin = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 2
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.3
#pltQty_temp.xTitle = "E^{tot}_{multi-clus} / E^{tot}_{rec-hit}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "multiClus-totE_by_recHit-totE"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(multiClus_E*(multiClus_z @zsideCondStr@))/Sum$(recHit_E*(recHit_isCaloParticleMatched && recHit_z @zsideCondStr@))"
#pltQty_temp.nBin = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.1
#pltQty_temp.xTitle = "E^{tot}_{multi-clus} / E^{tot}_{rec-hit (in calo-particle)}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "multiClus-totE_by_recHit-caloParticleMatched-totE"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
# ##### multi-clus vs. gen-el #####
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(multiClus_E*(multiClus_z @zsideCondStr@))/genEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.nBin = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.1
#pltQty_temp.xTitle = "E^{tot}_{multi-clus} / E_{gen-e}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "multiClus-totE_by_genEl-E"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
# ##### rec-hit vs. gen-el #####
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(recHit_E*(recHit_z @zsideCondStr@ && recHit_matchedSimHitIndex >= 0))/genEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.nBin = 500
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.3
#pltQty_temp.xTitle = "E^{tot}_{rec-hit (with valid sim-hit)} / E_{gen-e}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-simHitMatched-totE_by_genEl-E"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(recHit_E*(recHit_z @zsideCondStr@))/genEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.nBin = 100
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 5
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.15
#pltQty_temp.xTitle = "E^{tot}_{rec-hit} / E_{gen-e}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-totE_by_genEl-E"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(recHit_E*(recHit_isMultiClusMatched && recHit_z @zsideCondStr@))/genEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.nBin = 200
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 3
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.5
#pltQty_temp.xTitle = "E^{tot}_{rec-hit (in multi-clus)} / E_{gen-e}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-multiClusMatched-totE_by_genEl-E"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)


 ##### Rec-hits #####
#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(recHit_E*(recHit_z @zsideCondStr@ && recHit_isMultiClusMatched))/Sum$(recHit_E*(recHit_z @zsideCondStr@))"
#pltQty_temp.nBin = 250
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 2
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.2
#pltQty_temp.xTitle = "E^{tot}_{rec-hit (in multi-clus)} / E^{tot}_{rec-hit}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-multiClusterMatched-totE_by_recHit-totE"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.isMultiLayer = False
#pltQty_temp.plotStr = "Sum$(recHit_E*(recHit_z @zsideCondStr@ && recHit_matchedSimHitIndex >= 0))/Sum$(recHit_E*(recHit_z @zsideCondStr@))"
#pltQty_temp.nBin = 250
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 10
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = 2
#pltQty_temp.yMin = 0
#pltQty_temp.yMax = 0.2
#pltQty_temp.xTitle = "E^{tot}_{rec-hit (with valid sim-hit)} / E^{tot}_{rec-hit}"
#pltQty_temp.yTitle = "a.u."
#pltQty_temp.outFileName = "recHit-simHitMatched-totE_by_recHit-totE"
#pltQty_temp.outDir = "plots/response_resolution"
#l_plotQuantity.append(pltQty_temp)
#
#
# ##### TDR-el vs. gen-el #####
pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.plotStr = "gsfEleFromMultiClus_E/{{genEl_E[2]}}"
pltQty_temp.cutStr = "gsfEleFromMultiClus_eta @zsideCondStr@ && {{genEl_eta}} @zsideCondStr@"
pltQty_temp.nBin = 200
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0
pltQty_temp.xMax = 3
pltQty_temp.yMin = 0
pltQty_temp.yMax = 0.5
pltQty_temp.xTitle = "E_{TDR-e} / E_{gen-e}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.outFileName = "tdrEl-E_by_genEl-E"
pltQty_temp.outDir = "plots/response_resolution"
l_plotQuantity.append(pltQty_temp)



for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    for izside in range(0, len(l_zsideVal)) :
        
        zsideVal = l_zsideVal[izside]
        
        zsideStr = ""
        zsizeSignLatex = ""
        
        if (zsideVal == +1) :
            
            zsideStr = "P"
            zsizeSignLatex = "#plus"
            
            d_strReplace["@zsideCondStr@"] = "> 0"
        
        elif (zsideVal == -1) :
            
            zsideStr = "M"
            zsizeSignLatex = "#minus"
            
            d_strReplace["@zsideCondStr@"] = "< 0"
        
        
        outDir = "%s/HGCalEE%s" %(plotQuantity.outDir, zsideStr)
        os.system("mkdir -p %s" %(outDir))
        
        
        l_histDetail = []
        
        if (plotQuantity.isMultiLayer) :
            
            for iLayer in range(0, len(l_layer)) :
                
                layer = l_layer[iLayer]
                
                plotStr = plotQuantity.plotStr
                cutStr = plotQuantity.cutStr
                weightStr = plotQuantity.weightStr
                
                cutStr = "%s && recHit_zside == %d && recHit_layer == %d" %(cutStr, zsideVal, layer)
                
                h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
                h1_temp.Sumw2()
                
                plotStr = "%s >> h1_temp" %(plotStr)
                weightStr = "%s * (%s)" %(weightStr, cutStr)
                
                print iLayer
                print plotStr
                print weightStr
                
                tree.Draw(plotStr, weightStr)
                
                if (plotQuantity.normalize) :
                    
                    h1_temp.Scale(1.0 / h1_temp.Integral())
                
                color = iLayer+1
                
                if (color > 9) :
                    
                    color = 40 - iLayer
                
                histDetail_temp = Common.HistogramDetails()
                histDetail_temp.hist = h1_temp.Clone()
                histDetail_temp.lineWidth = 4
                histDetail_temp.lineColor = color
                histDetail_temp.histLabel = "Layer %d (#mu=%0.1e GeV)" %(layer, histDetail_temp.hist.GetMean()) 
                
                l_histDetail.append(histDetail_temp)
            
            outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
            
            Common.plot1D(
                list_histDetails = l_histDetail,
                stackDrawOption = "nostack",
                title = "",
                xTitle = plotQuantity.xTitle,
                yTitle = plotQuantity.yTitle,
                xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
                yMin = plotQuantity.yMin, yMax = plotQuantity.yMax,
                logX = False, logY = True,
                gridX = False, gridY = False,
                nDivisionsX = plotQuantity.nDivisionsX,
                nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = 1,
                transparentLegend = False,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsizeSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
        
        
        else :
            
            plotStr = plotQuantity.plotStr
            cutStr = plotQuantity.cutStr
            weightStr = plotQuantity.weightStr
            
            for key in d_strReplace :
                
                print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                
                plotStr = plotStr.replace(key, d_strReplace[key])
                cutStr = cutStr.replace(key, d_strReplace[key])
            
            
            h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
            h1_temp.Sumw2()
            
            
            weightStr = "%s * (%s)" %(weightStr, cutStr)
            
            
            if ("{{") :
                
                Common.iterateAndDraw(tree, plotStr, weightStr, h1_temp.GetName())
            
            else :
                
                plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
                
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
            histDetail_temp.histLabel = "#mu=%0.1e" %(histDetail_temp.hist.GetMean())
            
            l_histDetail.append(histDetail_temp)
            
            outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
            
            Common.plot1D(
                list_histDetails = l_histDetail,
                stackDrawOption = "nostack",
                title = "",
                xTitle = plotQuantity.xTitle,
                yTitle = plotQuantity.yTitle,
                xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
                yMin = plotQuantity.yMin, yMax = plotQuantity.yMax,
                logX = False, logY = False,
                gridX = False, gridY = False,
                nDivisionsX = plotQuantity.nDivisionsX,
                nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = 0.3,
                transparentLegend = True,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[1.1]{HGCal EE%s}" %(zsizeSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
