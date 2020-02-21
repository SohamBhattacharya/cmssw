import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle


class plotQuantity :
    
    isMultiLayer = False
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
    d_layerwise_cutStr = {}
    
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
    
    centerLabelsX = False
    centerLabelsY = False
    
    xTitle = ""
    yTitle = ""
    zTitle = ""
    
    plotStyle = "hist"
    
    outFileName = ""
    outDir = ""


tdrstyle.setTDRStyle()

ROOT.gStyle.SetPaintTextFormat("0.1f")
ROOT.TGaxis.SetMaxDigits(2)
ROOT.TGaxis.SetExponentOffset(-0.14, -0.035, "Y")

HGCalEE_nLayer = 28

l_zsideVal = [+1, -1]

inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits_withRecToSimAssoc.root")
tree = inFile.Get("treeMaker/tree")


d_strReplace = {
    "@zsideCondStr@": "",
    "@layerCondStr@": "",
}


l_plotQuantity = []


#pltQty_temp = plotQuantity()
#pltQty_temp.plotStr = "Sum$(simHit_E * (simHit_z @zsideCondStr@ && simHit_layer @layerCondStr@))"
#pltQty_temp.cutStr = "1"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = HGCalEE_nLayer
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = ""
#pltQty_temp.yTitle = "#mu#[]{E^{tot}_{sim-hit}} [GeV]"
#pltQty_temp.plotStyle = "hist E1"
#pltQty_temp.outFileName = "simHit-totE_vs_layer"
#pltQty_temp.outDir = "plots/showerProfile-longitudinal"
#l_plotQuantity.append(pltQty_temp)
#
#
#pltQty_temp = plotQuantity()
#pltQty_temp.plotStr = "Sum$(recHit_E * (recHit_z @zsideCondStr@ && recHit_layer @layerCondStr@))"
#pltQty_temp.cutStr = "1"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = HGCalEE_nLayer
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = ""
#pltQty_temp.yTitle = "#mu#[]{E^{tot}_{rec-hit}} [GeV]"
#pltQty_temp.plotStyle = "hist E1"
#pltQty_temp.outFileName = "recHit-totE_vs_layer"
#pltQty_temp.outDir = "plots/showerProfile-longitudinal"
#l_plotQuantity.append(pltQty_temp)


pltQty_temp = plotQuantity()
pltQty_temp.plotStr = "Sum$(recHit_E * (recHit_z @zsideCondStr@ && recHit_layer @layerCondStr@))"
pltQty_temp.cutStr = "1"
pltQty_temp.d_layerwise_cutStr[28] = "recHit_E < 0.02"
pltQty_temp.nBinX = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 1000
pltQty_temp.xMin = 0
pltQty_temp.xMax = HGCalEE_nLayer
pltQty_temp.centerLabelsX = True
pltQty_temp.centerLabelsY = True
pltQty_temp.xTitle = ""
pltQty_temp.yTitle = "#mu#[]{E^{tot}_{rec-hit}} [GeV]"
pltQty_temp.plotStyle = "hist E1"
pltQty_temp.outFileName = "recHit-L28lt0p02-totE_vs_layer"
pltQty_temp.outDir = "plots/showerProfile-longitudinal"
l_plotQuantity.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.plotStr = "Sum$(recHit_E * (recHit_z @zsideCondStr@ && recHit_layer @layerCondStr@ && recHit_matchedSimHitIndex >= 0))"
#pltQty_temp.cutStr = "1"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = HGCalEE_nLayer
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = ""
#pltQty_temp.yTitle = "#mu#[]{E^{tot}_{rec-hit (with sim-hit)}} [GeV]"
#pltQty_temp.plotStyle = "hist E1"
#pltQty_temp.outFileName = "recHit-withSimHit-totE_vs_layer"
#pltQty_temp.outDir = "plots/showerProfile-longitudinal"
#l_plotQuantity.append(pltQty_temp)


#pltQty_temp = plotQuantity()
#pltQty_temp.plotStr = "Sum$(recHit_E * (recHit_isMultiClusMatched && recHit_z @zsideCondStr@ && recHit_layer @layerCondStr@))"
#pltQty_temp.cutStr = "1"
#pltQty_temp.nBinX = 1000
#pltQty_temp.createXmin = 0
#pltQty_temp.createXmax = 1000
#pltQty_temp.xMin = 0
#pltQty_temp.xMax = HGCalEE_nLayer
#pltQty_temp.centerLabelsX = True
#pltQty_temp.centerLabelsY = True
#pltQty_temp.xTitle = ""
#pltQty_temp.yTitle = "#mu#[]{E^{tot}_{rec-hit (in multi-cluster)}} [GeV]"
#pltQty_temp.plotStyle = "hist E1"
#pltQty_temp.outFileName = "recHit-inMultiClus-totE_vs_layer"
#pltQty_temp.outDir = "plots/showerProfile-longitudinal"
#l_plotQuantity.append(pltQty_temp)



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
        
        h1_outHist = ROOT.TH1F(
            "h1_outHist",
            "h1_outHist", 
            HGCalEE_nLayer, 0.0, float(HGCalEE_nLayer)
        )
        
        for iLayer in range(0, HGCalEE_nLayer) :
            
            plotStr = plotQuantity.plotStr
            cutStr = plotQuantity.cutStr
            weightStr = plotQuantity.weightStr
            
            d_strReplace["@layerCondStr@"] = (" == %d" %(iLayer+1))
            
            if (iLayer+1 in plotQuantity.d_layerwise_cutStr) :
                
                d_strReplace["@layerCondStr@"] = "%s && (%s)" %(d_strReplace["@layerCondStr@"], plotQuantity.d_layerwise_cutStr[iLayer+1])
            
            h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBinX, plotQuantity.createXmin, plotQuantity.createXmax)
            h1_temp.Sumw2()
            
            plotStr = "%s >> h1_temp" %(plotStr)
            weightStr = "%s * (%s)" %(weightStr, cutStr)
            
            for key in d_strReplace :
                
                print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                
                plotStr = plotStr.replace(key, d_strReplace[key])
                weightStr = weightStr.replace(key, d_strReplace[key])
            
            print  plotStr
            print  weightStr
            
            tree.Draw(plotStr, weightStr)
            
            mu = h1_temp.GetMean()
            #sigma = h1_temp.GetStdDev()
            sigma = h1_temp.GetMeanError()
            
            h1_outHist.SetBinContent(iLayer+1, mu)
            h1_outHist.SetBinError(iLayer+1, sigma)
            
            h1_outHist.GetXaxis().SetBinLabel(iLayer+1, str(iLayer+1))
        
        
        h1_outHist.SetLineWidth(4)
        h1_outHist.SetLineColor(4)
        
        h1_outHist.SetMarkerStyle(10)
        h1_outHist.SetMarkerColor(4)
        
        tdrstyle.setTDRStyle()
        
        canvas = ROOT.TCanvas("canvas", "canvas")
        
        h1_outHist.Draw("E1")
        
        h1_outHist.SetMinimum(0.0)
        
        #h1_outHist.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * plotQuantity.xLabelSizeScale)
        #h1_outHist.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * plotQuantity.yLabelSizeScale)
        
        h1_outHist.GetXaxis().SetTitle("HGCal EE%s layer" %(zsizeSignLatex))
        h1_outHist.GetXaxis().CenterTitle(True)
        h1_outHist.GetXaxis().CenterLabels(True)
        h1_outHist.GetXaxis().SetLabelFont(62)
        h1_outHist.GetXaxis().SetNdivisions(HGCalEE_nLayer, 1, 1)
        h1_outHist.GetXaxis().LabelsOption("v")
        #h1_outHist.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * plotQuantity.xTitleSizeScale)
        
        h1_outHist.GetYaxis().SetTitle(plotQuantity.yTitle)
        #h1_outHist.GetYaxis().SetTitleSize(0.03)
        h1_outHist.GetYaxis().SetTitleOffset(1.225)
        h1_outHist.GetYaxis().CenterTitle(True)
        #h1_outHist.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * plotQuantity.yTitleSizeScale)
        
        
        CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")
        
        canvas.SaveAs("%s/%s.pdf" %(outDir, plotQuantity.outFileName))
