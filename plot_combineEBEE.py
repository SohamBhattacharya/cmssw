import numpy
import os
import time

import ROOT

import CMS_lumi
import tdrstyle

import Common


outDir = "plots/combined_EBEE/electrons"
os.system("mkdir -p %s" %(outDir))


fileName_EB = "plots/from_Soumya/electron_response.root"
histName_EB = "eta_res_update"


fileName_EE = "plots/response_resolution_TMVA/HGCalEE/gsfEleFromTICL-corrE_by_genEl-E_vs_genEl-eta.root"
histName_EE = "h1_mu"


outFileName = "recoEl-E_by_genEl-E_vs_genEl-eta"


file_EB = ROOT.TFile(fileName_EB)
hist_EB = file_EB.Get(histName_EB)

file_EE = ROOT.TFile(fileName_EE)
hist_EE = file_EE.Get(histName_EE)


hist_EB.Rebin(5)


hist_comb = ROOT.TH1F("hist_comb", "hist_comb", 60, 0.0, 3.0)


nBin = hist_comb.GetNbinsX()


for iBin in range(1, nBin+1) :
    
    
    binCenter = hist_comb.GetXaxis().GetBinCenter(iBin)
    
    binVal = 0
    binErr = 0
    
    if (binCenter < 1.5) :
        
        binNum = hist_EB.GetXaxis().FindBin(binCenter)
        
        binVal = hist_EB.GetBinContent(binNum)
        binErr = hist_EB.GetBinError(binNum)
    
    else :
        
        binNum = hist_EE.GetXaxis().FindBin(binCenter)
        
        binVal = hist_EE.GetBinContent(binNum)
        binErr = hist_EE.GetBinError(binNum)
    
    
    hist_comb.SetBinContent(iBin, binVal)
    hist_comb.SetBinError(iBin, binErr)


histDetail = Common.HistogramDetails()
histDetail.hist = hist_comb.Clone()
histDetail.lineWidth = 4
histDetail.lineColor = 4
#histDetail.markerSize = 0
histDetail.drawOption = "E1"
histDetail.addToLegend = False

l_extraText = [
    ([0.5, 0.9, "Phase-II, PU 200"])
]

outFileName = "%s/%s" %(outDir, outFileName)

Common.plot1D(
    list_histDetails = [histDetail],
    stackDrawOption = "nostack",
    title = "",
    xTitle = "#||{#eta_{gen-ele}}",
    yTitle = "<E_{reco} / E_{gen}>",
    xMin = 0, xMax = 3,
    yMin = 0.8, yMax = 1.2,
    #yMin = 0.7, yMax = 1.1,
    yTitleSizeScale = 0.7,
    yTitleOffset = 1.8,
    yLabelSizeScale = 0.9,
    #logX = False, logY = True,
    gridX = True, gridY = True,
    #nDivisionsX = plotQuantity.nDivisionsX,
    #nDivisionsY = plotQuantity.nDivisionsY,
    drawLegend = False,
    legendHeightScale = 0.5,
    #legendNcol = plotQuantity.legendNcol,
    #legendHeightScale = plotQuantity.legendHeightScale,
    #legendWidthScale = plotQuantity.legendWidthScale,
    transparentLegend = False,
    legendTextSize = -1,
    legendBorderSize = 0,
    legendPos = "LR",
    l_extraText = l_extraText,
    #legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
    CMSextraText = "Simulation Preliminary",
    fixAlphanumericBinLabels = False,
    outFileName = outFileName,
    outFileName_suffix = "",
)
