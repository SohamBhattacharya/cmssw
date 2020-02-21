import numpy
import os
import time

import ROOT

import CMS_lumi
import tdrstyle

import Common


class plotQuantity :
    
    isMultiLayer = False
    l_zsideVal = []
    
    isEtaBinned = False
    l_etaBinStr = []
    l_etaBinStr_muSigma = []
    etaObjStr = ""
    etaObjLatex = ""
    etaUnitStr = ""
    
    plotStr = ""
    cutStr = "1"
    weightStr = "1"
    
    nBin = 0
    nBinFit = 0
    l_nBinFit = []
    createXmin = 0
    createXmax = 0
    
    normalize = True
    
    fit = False
    fitResponse = False
    
    fitResolution = False
    fitResolution_draw = True
    resolutionFit_extraTerm = "0"
    resolutionFit_range = []
    
    resolutionFit_plotStr = ""
    resolutionFit_cutStr = "1"
    
    xMin = 0
    xMax = 0
    
    yMin = 0
    yMax = 0
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    xTitle = ""
    yTitle = ""
    
    
    mu_xMin = 0
    mu_xMax = 0
    
    mu_yMin = 0
    mu_yMax = 0
    
    sigma_xMin = 0
    sigma_xMax = 0
    
    sigma_yMin = 0
    sigma_yMax = 0
    
    resolutionFit_yMin = 0
    resolutionFit_yMax = 0
    
    resolutionFit_xTitle = ""
    resolutionFit_yTitle = ""
    
    legendNcol = 1
    legendHeightScale = 1
    legendWidthScale = 1
    
    d_fitInfo = {}
    
    outFileName = ""
    outDir = ""


d_fitInfo_crystalBall = {
    
}


saveToRootFile = True


#ROOT.gROOT.ProcessLine(".L EDAnalyzers/TreeMaker/interface/CustomRootDict.cc+");

inFileName = "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/regression/TMVA/TMVAReg.root"

#inFile = ROOT.TFile.Open(inFileName)
#tree = inFile.Get("dataset/TestTree")

tree = ROOT.TChain("chain")
tree.AddFile(inFileName, -1, "dataset/TrainTree")
tree.AddFile(inFileName, -1, "dataset/TestTree")


HGCalEE_nLayer = 28


hitTypeStr = "rec"
l_zsideVal = [+1, -1, 0]
l_zsideValComb = [0]
l_layer = [1, 2, 7, 8, 26, 27, 28]


l_etaBinStr = ["%0.1f" %(val) for val in numpy.arange(1.4, 3+0.3, 0.3)]
l_etaBinStr_muSigma = ["%f" %(val) for val in numpy.arange(1.4, 3+0.05, 0.05)]


l_EbinStr = ["%d" %(val) for val in range(30, 700+30, 30)]
l_EbinStr_muSigma = ["%d" %(val) for val in range(5, 700+5, 5)]


l_PUbinStr = ["%d" %(val) for val in range(150, 250+10, 10)]
l_PUbinStr_muSigma = ["%d" %(val) for val in range(150, 250+5, 5)]


l_nBinFit = []

for iBin in range(0, len(l_EbinStr_muSigma)) :
    
    binVal = float(l_EbinStr_muSigma[iBin])
    
    nBin = 0
    
    if (binVal < 30) :
        
        nBin = 2000
    
    elif (binVal < 500) :
        
        nBin = 1000
    
    else :
        
        nBin = 500
    
    l_nBinFit.append(nBin)


d_strReplace = {
    "@zsideCondStr@": "",
}


l_plotQuantity = []



 ########## versus genEl-E ##########

pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_EbinStr
pltQty_temp.l_etaBinStr_muSigma = l_EbinStr_muSigma
pltQty_temp.etaObjStr = "gsfEleFromTICL_matchedGenEl_E"
pltQty_temp.etaObjLatex = "E_{gen-ele}"
pltQty_temp.etaUnitStr = "GeV"
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = False
#pltQty_temp.resolutionFit_plotStr = "genEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.resolutionFit_range = [40, 140]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.8
plotQuantity.mu_yMax = 1.1
pltQty_temp.xTitle = "E_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
#pltQty_temp.resolutionFit_yMin = 0
#pltQty_temp.resolutionFit_yMax = 10
#pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
#pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{tot}_{rec-hit}} / #mu#[]{E^{tot}_{rec-hit}} [%] (rec-hit w. sim-hit)"
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-E_by_genEl-E_vs_genEl-E"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "LD / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_EbinStr
pltQty_temp.l_etaBinStr_muSigma = l_EbinStr_muSigma
pltQty_temp.etaObjStr = "gsfEleFromTICL_matchedGenEl_E"
pltQty_temp.etaObjLatex = "E_{gen-ele}"
pltQty_temp.etaUnitStr = "GeV"
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = True
pltQty_temp.resolutionFit_plotStr = "gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.resolutionFit_range = [40, l_EbinStr_muSigma[-1]]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.8
plotQuantity.mu_yMax = 1.1
pltQty_temp.xTitle = "E^{corr}_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.resolutionFit_yMin = 0
pltQty_temp.resolutionFit_yMax = 20
pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{corr}_{TICL-ele}} / #mu#[]{E^{corr}_{TICL-ele}} [%]"
pltQty_temp.fitResolution_draw = False
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-corrE_by_genEl-E_vs_genEl-E"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)


 ########## versus genEl-eta ##########

pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_etaBinStr
pltQty_temp.l_etaBinStr_muSigma = l_etaBinStr_muSigma
pltQty_temp.etaObjStr = "abs_gsfEleFromTICL_eta_"
pltQty_temp.etaObjLatex = "#||{#eta_{gen-ele}}"
pltQty_temp.etaUnitStr = ""
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = False
#pltQty_temp.resolutionFit_plotStr = "genEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.resolutionFit_range = [40, 140]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.8
plotQuantity.mu_yMax = 1.1
pltQty_temp.xTitle = "E_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
#pltQty_temp.resolutionFit_yMin = 0
#pltQty_temp.resolutionFit_yMax = 10
#pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
#pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{tot}_{rec-hit}} / #mu#[]{E^{tot}_{rec-hit}} [%] (rec-hit w. sim-hit)"
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-E_by_genEl-E_vs_genEl-eta"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "LD / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_etaBinStr
pltQty_temp.l_etaBinStr_muSigma = l_etaBinStr_muSigma
pltQty_temp.etaObjStr = "abs_gsfEleFromTICL_eta_"
pltQty_temp.etaObjLatex = "#||{#eta_{gen-ele}}"
pltQty_temp.etaUnitStr = ""
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = False
#pltQty_temp.resolutionFit_plotStr = "genEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.resolutionFit_range = [40, 140]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.8
plotQuantity.mu_yMax = 1.1
pltQty_temp.xTitle = "E^{corr}_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
#pltQty_temp.resolutionFit_yMin = 0
#pltQty_temp.resolutionFit_yMax = 10
#pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
#pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{tot}_{rec-hit}} / #mu#[]{E^{tot}_{rec-hit}} [%] (rec-hit w. sim-hit)"
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-corrE_by_genEl-E_vs_genEl-eta"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)


 ########## versus PU ##########

pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "gsfEleFromTICL_E / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_PUbinStr
pltQty_temp.l_etaBinStr_muSigma = l_PUbinStr_muSigma
pltQty_temp.etaObjStr = "pileup_n"
pltQty_temp.etaObjLatex = "N_{PU}"
pltQty_temp.etaUnitStr = ""
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = False
#pltQty_temp.resolutionFit_plotStr = "genEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.resolutionFit_range = [40, 140]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.85
plotQuantity.mu_yMax = 1.05
pltQty_temp.xTitle = "E_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
#pltQty_temp.resolutionFit_yMin = 0
#pltQty_temp.resolutionFit_yMax = 10
#pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
#pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{tot}_{rec-hit}} / #mu#[]{E^{tot}_{rec-hit}} [%] (rec-hit w. sim-hit)"
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-E_by_genEl-E_vs_PU"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)



pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.l_zsideVal = l_zsideValComb
pltQty_temp.plotStr = "LD / gsfEleFromTICL_matchedGenEl_E"
#pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = True
pltQty_temp.l_etaBinStr = l_PUbinStr
pltQty_temp.l_etaBinStr_muSigma = l_PUbinStr_muSigma
pltQty_temp.etaObjStr = "pileup_n"
pltQty_temp.etaObjLatex = "N_{PU}"
pltQty_temp.etaUnitStr = ""
pltQty_temp.nBin = 500
pltQty_temp.nBinFit = 1000
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 5
pltQty_temp.fit = True
pltQty_temp.fitResolution = False
#pltQty_temp.resolutionFit_plotStr = "genEl_E"
#pltQty_temp.resolutionFit_cutStr = "genEl_eta @zsideCondStr@"
#pltQty_temp.resolutionFit_range = [40, 140]
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 1.5
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
#plotQuantity.mu_xMin
#plotQuantity.mu_xMax
plotQuantity.mu_yMin = 0.85
plotQuantity.mu_yMax = 1.05
pltQty_temp.xTitle = "E^{corr}_{TICL-ele} / E_{gen-ele}"
pltQty_temp.yTitle = "a.u."
#pltQty_temp.resolutionFit_yMin = 0
#pltQty_temp.resolutionFit_yMax = 10
#pltQty_temp.resolutionFit_xTitle = "E_{gen-e} [GeV]"
#pltQty_temp.resolutionFit_yTitle = "#sigma#[]{E^{tot}_{rec-hit}} / #mu#[]{E^{tot}_{rec-hit}} [%] (rec-hit w. sim-hit)"
#pltQty_temp.legendHeightScale = 1.5
#pltQty_temp.legendWidthScale = 0.8
pltQty_temp.outFileName = "gsfEleFromTICL-corrE_by_genEl-E_vs_PU"
pltQty_temp.outDir = "plots/response_resolution_TMVA"
l_plotQuantity.append(pltQty_temp)



for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    etaUnitStr = ""
    
    if (len(plotQuantity.etaUnitStr)) :
        
        etaUnitStr = "[%s]" %(plotQuantity.etaUnitStr)
    
    l_zsideVal = plotQuantity.l_zsideVal
    
    for izside in range(0, len(l_zsideVal)) :
        
        zsideVal = l_zsideVal[izside]
        
        zsideStr = ""
        zsideSignLatex = ""
        
        if (zsideVal == +1) :
            
            zsideStr = "P"
            zsideSignLatex = "#plus"
            
            d_strReplace["@zsideCondStr@"] = "> 0"
        
        elif (zsideVal == -1) :
            
            zsideStr = "M"
            zsideSignLatex = "#minus"
            
            d_strReplace["@zsideCondStr@"] = "< 0"
        
        elif (zsideVal == 0) :
            
            zsideStr = ""
            zsideSignLatex = ""
            
            #d_strReplace["@zsideCondStr@"] = "< 0"
        
        
        outDir = "%s/HGCalEE%s" %(plotQuantity.outDir, zsideStr)
        os.system("mkdir -p %s" %(outDir))
        
        
        l_histDetail = []
        
        if (plotQuantity.isEtaBinned) :
            
            l_etaBin = [float(ele) for ele in plotQuantity.l_etaBinStr]
            
            for iEtaBin in range(0, len(plotQuantity.l_etaBinStr)-1) :
                
                etaBinLwrStr = plotQuantity.l_etaBinStr[iEtaBin]
                etaBinUprStr = plotQuantity.l_etaBinStr[iEtaBin+1]
                
                plotStr = plotQuantity.plotStr
                cutStr = plotQuantity.cutStr
                weightStr = plotQuantity.weightStr
                
                cutStr = "%s && (%s > %s && %s < %s)" %(cutStr, plotQuantity.etaObjStr, etaBinLwrStr, plotQuantity.etaObjStr, etaBinUprStr)
                
                h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
                h1_temp.Sumw2()
                
                # Combine cut and weight
                weightStr = "%s * (%s)" %(weightStr, cutStr)
                
                for key in d_strReplace :
                    
                    print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                    
                    plotStr = plotStr.replace(key, d_strReplace[key])
                    weightStr = weightStr.replace(key, d_strReplace[key])
                
                
                if ("{{" in plotStr) :
                    
                    Common.iterateAndDraw(tree, plotStr, weightStr, h1_temp.GetName())
                
                else :
                    
                    plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
                    
                    print iEtaBin, plotQuantity.etaObjStr, etaBinLwrStr, etaBinUprStr
                    print plotStr
                    print weightStr
                    
                    tree.Draw(plotStr, weightStr)
                
                # Continue if the histogram is empty
                if (not h1_temp.Integral()) :
                    
                    continue
                
                if (plotQuantity.normalize) :
                    
                    h1_temp.Scale(1.0 / h1_temp.Integral())
                
                color = iEtaBin+1
                
                if (color == 3) :
                    
                    color = ROOT.kGreen+2
                
                elif (color == 5) :
                    
                    color = ROOT.kOrange+7
                
                elif (color > 9) :
                    
                    color = 30 + iEtaBin
                
                mu = h1_temp.GetMean()
                muErr = h1_temp.GetMeanError()
                sigma = h1_temp.GetStdDev()
                
                maxBin = h1_temp.GetMaximumBin()
                maxPos = h1_temp.GetBinCenter(maxBin)
                
                
                # Fit
                if (plotQuantity.fit) :
                    
                    nSigmaLwr = 2
                    nSigmaUpr = 2
                    fitLwr = max(0, maxPos - nSigmaLwr*sigma)
                    fitUpr = maxPos + nSigmaUpr*sigma
                    
                    #f1_fitFunc = ROOT.TF1("CrystalBall", "crystalball(x)", fitLwr, fitUpr)
                    f1_fitFunc = ROOT.TF1("Gaussian", "gaus(x)", fitLwr, fitUpr)
                    f1_fitFunc.SetLineColor(color)
                    f1_fitFunc.SetLineWidth(2)
                    
                    f1_fitFunc.SetParameter("Mean", mu)
                    f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Mean"), fitLwr, fitUpr)
                    
                    f1_fitFunc.SetParameter("Sigma", sigma)
                    f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Sigma"), 0, 3*sigma)
                    
                    ##f1_fitFunc.SetParameter("Alpha", fitUpr/2.0)
                    #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Alpha"), 0, fitUpr)
                    #
                    #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("N"), 0, 100)
                    
                    fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                    
                    statusStr = ""
                    NDF = 0
                    chiSqPerNDF = 10
                    fitIter = 0
                    
                    while ((statusStr != "CONVERGED" or chiSqPerNDF > 1) and fitIter < 5) :
                        
                        fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                        
                        statusStr = ROOT.gMinuit.fCstatu
                        statusStr = statusStr.strip()
                        
                        chiSq = f1_fitFunc.GetChisquare()
                        NDF = f1_fitFunc.GetNDF()
                        
                        if (NDF) :
                            
                            chiSqPerNDF = chiSq / NDF
                        
                        print "Chi^2:", chiSq
                        print "NDF:", NDF
                        print "Chi^2 / NDF:", chiSqPerNDF
                        
                        fitIter += 1
                    
                    if (statusStr != "CONVERGED" and NDF) :
                        
                        print "\n"
                        print "#" * 50
                        print "Error: Fit failed."
                        print "#" * 50
                        exit(1)
                
                
                histDetail_temp = Common.HistogramDetails()
                histDetail_temp.hist = h1_temp.Clone()
                histDetail_temp.lineWidth = 4
                histDetail_temp.lineColor = color
                histDetail_temp.histLabel = "#splitline{%s < %s < %s %s}{(#mu, #sigma)=(%0.1e, %0.1e)}" %(
                    etaBinLwrStr, plotQuantity.etaObjLatex, etaBinUprStr, plotQuantity.etaUnitStr,
                    mu, sigma
                ) 
                
                l_histDetail.append(histDetail_temp)
            
            outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
            
            xTitle_unitStr = ""
            
            if (len(plotQuantity.etaUnitStr)) :
                
                xTitle_unitStr = "[%s]" %(plotQuantity.etaUnitStr)
            
            xTitle = "%s %s" %(plotQuantity.xTitle, xTitle_unitStr)
            
            Common.plot1D(
                list_histDetails = l_histDetail,
                stackDrawOption = "nostack",
                title = "",
                xTitle = xTitle,
                yTitle = plotQuantity.yTitle,
                xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
                yMin = plotQuantity.yMin, yMax = plotQuantity.yMax,
                logX = False, logY = True,
                gridX = True, gridY = True,
                nDivisionsX = plotQuantity.nDivisionsX,
                nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendDrawOption = "L",
                legendNcol = plotQuantity.legendNcol,
                legendHeightScale = plotQuantity.legendHeightScale,
                legendWidthScale = plotQuantity.legendWidthScale,
                transparentLegend = False,
                #legendTextSize = 0.017,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[2]{HGCal EE%s}" %(zsideSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
            
            
            # mu, sigma plots
            l_etaBin_muSigma = [float(ele) for ele in plotQuantity.l_etaBinStr_muSigma]
            
            print "*"*100, "\n", l_etaBin_muSigma, "\n", numpy.array(l_etaBin_muSigma)
            
            h1_mu = ROOT.TH1F("h1_mu", "h1_mu", len(l_etaBin_muSigma)-1, numpy.array(l_etaBin_muSigma))
            h1_mu.Sumw2()
            
            h1_fitMu = ROOT.TH1F("h1_fitMu", "h1_fitMu", len(l_etaBin_muSigma)-1, numpy.array(l_etaBin_muSigma))
            h1_fitMu.Sumw2()
            
            h1_fitSigma = ROOT.TH1F("h1_fitSigma", "h1_fitSigma", len(l_etaBin_muSigma)-1, numpy.array(l_etaBin_muSigma))
            h1_fitSigma.Sumw2()
            
            h1_fitSigmaByMu = ROOT.TH1F("h1_fitSigmaByMu", "h1_fitSigmaByMu", len(l_etaBin_muSigma)-1, numpy.array(l_etaBin_muSigma))
            h1_fitSigmaByMu.Sumw2()
            
            h1_relResolution = ROOT.TH1F("h1_relResolution", "h1_relResolution", len(l_etaBin_muSigma)-1, numpy.array(l_etaBin_muSigma))
            h1_relResolution.Sumw2()
            
            gr_relResolution = ROOT.TGraphErrors(len(plotQuantity.l_etaBinStr_muSigma)-1)
            gr_relResolution.SetNameTitle("gr_relResolution", "gr_relResolution")
            
            
            print "*"*100
            
            nBinFit = plotQuantity.nBinFit
            l_nBinFit = plotQuantity.l_nBinFit
            
            for iEtaBin in range(0, len(plotQuantity.l_etaBinStr_muSigma)-1) :
                
                etaBinLwrStr = plotQuantity.l_etaBinStr_muSigma[iEtaBin]
                etaBinUprStr = plotQuantity.l_etaBinStr_muSigma[iEtaBin+1]
                
                etaBinLwr = float(etaBinLwrStr)
                etaBinUpr = float(etaBinUprStr)
                
                plotStr = plotQuantity.plotStr
                cutStr = plotQuantity.cutStr
                weightStr = plotQuantity.weightStr
                
                if (len(l_nBinFit)) :
                    
                    nBinFit = l_nBinFit[iEtaBin]
                
                cutStr = "%s && (%s > %s && %s < %s)" %(cutStr, plotQuantity.etaObjStr, etaBinLwrStr, plotQuantity.etaObjStr, etaBinUprStr)
                
                h1_temp = ROOT.TH1F("h1_temp", "h1_temp", nBinFit, plotQuantity.createXmin, plotQuantity.createXmax)
                h1_temp.Sumw2()
                
                # Combine cut and weight
                weightStr = "%s * (%s)" %(weightStr, cutStr)
                
                for key in d_strReplace :
                    
                    print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                    
                    plotStr = plotStr.replace(key, d_strReplace[key])
                    weightStr = weightStr.replace(key, d_strReplace[key])
                
                
                if ("{{" in plotStr) :
                    
                    Common.iterateAndDraw(tree, plotStr, weightStr, h1_temp.GetName())
                
                else :
                    
                    plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
                    
                    print iEtaBin, plotQuantity.etaObjStr, etaBinLwrStr, etaBinUprStr
                    print plotStr
                    print weightStr
                    
                    tree.Draw(plotStr, weightStr)
                
                # Continue if the histogram is empty
                print "Integral: %e" %(h1_temp.Integral())
                
                if (not h1_temp.Integral() > 0) :
                    
                    continue
                
                if (plotQuantity.normalize) :
                    
                    h1_temp.Scale(1.0 / h1_temp.Integral())
                
                
                mu = h1_temp.GetMean()
                muErr = h1_temp.GetMeanError()
                sigma = h1_temp.GetStdDev()
                sigmaErr = h1_temp.GetStdDevError() # Note: This assumes a Normal ditribution
                
                maxBin = h1_temp.GetMaximumBin()
                maxPos = h1_temp.GetBinCenter(maxBin)
                
                
                h1_mu.SetBinContent(iEtaBin+1, mu)
                h1_mu.SetBinError(iEtaBin+1, muErr)
                
                
                #if (plotQuantity.fitResolution) :
                #    
                #    plotStr = plotQuantity.plotStr
                #    cutStr = plotQuantity.cutStr
                #    weightStr = plotQuantity.weightStr
                #    
                #    cutStr = "%s && (%s > %s && %s < %s)" %(cutStr, plotQuantity.etaObjStr, etaBinLwrStr, plotQuantity.etaObjStr, etaBinUprStr)
                #    
                #    h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
                #    h1_temp.Sumw2()
                #    
                #    # Combine cut and weight
                #    weightStr = "%s * (%s)" %(weightStr, cutStr)
                #    
                #    for key in d_strReplace :
                #        
                #        print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                #        
                #        plotStr = plotStr.replace(key, d_strReplace[key])
                #        weightStr = weightStr.replace(key, d_strReplace[key])
                #    
                #    
                #    if ("{{" in plotStr) :
                #        
                #        Common.iterateAndDraw(tree, plotStr, weightStr, h1_temp.GetName())
                #    
                #    else :
                #        
                #        plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
                #        
                #        print iEtaBin, plotQuantity.etaObjStr, etaBinLwrStr, etaBinUprStr
                #        print plotStr
                #        print weightStr
                #        
                #        tree.Draw(plotStr, weightStr)
                #    
                #    h1_relResolDenom = ROOT.TH1F("h1_relResolDenom", "h1_relResolDenom", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
                #    h1_relResolDenom.Sumw2()
                #    
                #    tree.Draw(
                #        "%s >> %s" %(plotQuantity.etaObjStr, h1_relResolDenom.GetName()),
                #        "%s" %(weightStr)
                #    )
                #    
                #    relResolDenom = h1_relResolDenom.GetMean()
                #    #relResolDenom = (etaBinLwr + etaBinUpr) / 2.0
                #    
                #    
                #    ########## Fill the relative resolution vs. E histogram ########## 
                #    if (relResolDenom > 0) :
                #        
                #        #relResol = sigma / relResolDenom * 100
                #        relResol = sigma / mu * 100
                #        
                #        #relResol_err = relResol * (sigmaErr/sigma)
                #        relResol_err = relResol * ((sigmaErr/sigma)**2 + (muErr/mu)**2)**0.5
                #        
                #        h1_relResolution.SetBinContent(iEtaBin+1, relResol)
                #        h1_relResolution.SetBinError(iEtaBin+1, relResol_err)
                
                
                
                #################################################
                # Use distribution values for relative resolution
                #################################################
                
                relResol_num = sigma
                relResol_numErr = sigmaErr
                
                relResol_den = mu
                relResol_denErr = muErr
                
                
                # Fit
                if (plotQuantity.fit) :
                    
                    #### TEST TEST TEST ####
                    #####maxPos = mu
                    
                    nSigmaLwr = 2
                    nSigmaUpr = 2
                    fitLwr = max(0, maxPos - nSigmaLwr*sigma)
                    fitUpr = maxPos + nSigmaUpr*sigma
                    
                    print "*"*50, maxPos, fitLwr, fitUpr
                    
                    #f1_fitFunc = ROOT.TF1("CrystalBall", "crystalball(x)", fitLwr, fitUpr)
                    f1_fitFunc = ROOT.TF1("Gaussian", "gaus(x)", fitLwr, fitUpr)
                    f1_fitFunc.SetLineColor(color)
                    f1_fitFunc.SetLineWidth(2)
                    
                    #f1_fitFunc.SetParameter("Constant", h1_temp.Integral())
                    
                    f1_fitFunc.SetParameter("Mean", mu)
                    f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Mean"), fitLwr, fitUpr)
                    
                    f1_fitFunc.SetParameter("Sigma", sigma)
                    f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Sigma"), 0, 3*sigma)
                    
                    ##f1_fitFunc.SetParameter("Alpha", fitUpr/2.0)
                    #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Alpha"), 0, fitUpr)
                    #
                    #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("N"), 0, 100)
                    
                    #print mu, sigma
                    
                    statusStr = ""
                    NDF = 0
                    chiSqPerNDF = 10
                    fitIter = 0
                    
                    while ((statusStr != "CONVERGED" or chiSqPerNDF > 1) and fitIter < 5) :
                        
                        fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                        
                        statusStr = ROOT.gMinuit.fCstatu
                        statusStr = statusStr.strip()
                        
                        chiSq = f1_fitFunc.GetChisquare()
                        NDF = f1_fitFunc.GetNDF()
                        
                        if (NDF) :
                            
                            chiSqPerNDF = chiSq / NDF
                        
                        print "Chi^2:", chiSq
                        print "NDF:", NDF
                        print "Chi^2 / NDF:", chiSqPerNDF
                        print "Hist entries:", h1_temp.GetEntries()
                        print "Hist bins:", h1_temp.GetNbinsX()
                        
                        fitIter += 1
                    
                    
                    #fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                    #
                    #statusStr = ROOT.gMinuit.fCstatu
                    #statusStr = statusStr.strip()
                    
                    if (statusStr != "CONVERGED" and NDF) :
                        
                        print "Error: Fit failed."
                        exit(1)
                    
                    fitMu = f1_fitFunc.GetParameter("Mean")
                    fitMu_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Mean"))
                    
                    fitSigma = f1_fitFunc.GetParameter("Sigma")
                    fitSigma_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Sigma"))
                    
                    h1_fitMu.SetBinContent(iEtaBin+1, fitMu)
                    h1_fitMu.SetBinError(iEtaBin+1, fitMu_err)
                    
                    h1_fitSigma.SetBinContent(iEtaBin+1, fitSigma)
                    h1_fitSigma.SetBinError(iEtaBin+1, fitSigma_err)
                    
                    fitSigmaByMu = 0
                    fitSigmaByMu_err = 0
                    
                    if (fitMu) :
                        
                        fitSigmaByMu = fitSigma / fitMu * 100
                    
                    if (fitMu and fitSigma) :
                        
                        fitSigmaByMu_err = fitSigmaByMu * ((fitMu_err/fitMu)**2 + (fitSigma_err/fitSigma)**2)**0.5
                    
                    h1_fitSigmaByMu.SetBinContent(iEtaBin+1, fitSigmaByMu)
                    h1_fitSigmaByMu.SetBinError(iEtaBin+1, fitSigmaByMu_err)
                    
                    
                    
                    ########################################
                    # Use fit values for relative resolution
                    ########################################
                    
                    relResol_num = fitSigma
                    relResol_numErr = fitSigma_err
                    
                    relResol_den = fitMu
                    relResol_denErr = fitMu_err
                
                
                ########## Fill the relative resolution vs. E histogram ########## 
                if (plotQuantity.fitResolution) :
                #if (1) :
                    
                    ##### TEST TEST TEST #####
                    
                    #if (etaBinLwr > 160 and etaBinUpr < 240) :
                    #    
                    #    continue
                    
                    ##### TEST TEST TEST #####
                    
                    
                    relResol = 0
                    relResol_err = 0
                    
                    if (relResol_den > 0) :
                        
                        relResol = relResol_num / relResol_den * 100
                    
                    if (relResol_num and relResol_den) :
                        
                        relResol_err = relResol * ((relResol_numErr/relResol_num)**2 + (relResol_denErr/relResol_den)**2)**0.5
                    
                    
                    relResBin = iEtaBin+1
                    #relResBin = h1_relResolution.FindBin(relResol_den)
                    
                    h1_relResolution.SetBinContent(relResBin, relResol)
                    h1_relResolution.SetBinError(relResBin, relResol_err)
                    
                    
                    gr_relResolution.SetPoint(iEtaBin, relResol_den, relResol)
                    gr_relResolution.SetPointError(iEtaBin, relResol_denErr, relResol_err)
            
            
            histDetail_mu = Common.HistogramDetails()
            histDetail_mu.hist = h1_mu.Clone()
            histDetail_mu.lineWidth = 4
            histDetail_mu.lineColor = 4
            histDetail_mu.drawOption = "PE1"
            histDetail_mu.addToLegend = False
            
            yTitle_unitStr = ""
            
            if (len(plotQuantity.etaUnitStr)) :
                
                yTitle_unitStr = "[%s]" %(plotQuantity.etaUnitStr)
            
            yTitle = "#mu#[]{%s} %s" %(plotQuantity.xTitle, yTitle_unitStr)
            
            outFileName = "%s/%s_mu" %(outDir, plotQuantity.outFileName)
            
            Common.plot1D(
                list_histDetails = [histDetail_mu],
                stackDrawOption = "nostack",
                title = "",
                xTitle = "%s %s" %(plotQuantity.etaObjLatex, etaUnitStr),
                yTitle = yTitle,
                xMin = plotQuantity.mu_xMin, xMax = plotQuantity.mu_xMax,
                yMin = plotQuantity.mu_yMin, yMax = plotQuantity.mu_yMax,
                #yMin = 0.7, yMax = 1.1,
                yTitleSizeScale = 0.7,
                yTitleOffset = 1.8,
                yLabelSizeScale = 0.9,
                #logX = False, logY = True,
                gridX = True, gridY = True,
                #nDivisionsX = plotQuantity.nDivisionsX,
                #nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = 0.5,
                #legendNcol = plotQuantity.legendNcol,
                #legendHeightScale = plotQuantity.legendHeightScale,
                #legendWidthScale = plotQuantity.legendWidthScale,
                transparentLegend = False,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "LR",
                legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
            
            
            yTitle = "#mu_{fit}#[]{%s} %s" %(plotQuantity.xTitle, yTitle_unitStr)
            
            # Fit mu
            if (plotQuantity.fit) :
                
                histDetail_fitMu = Common.HistogramDetails()
                histDetail_fitMu.hist = h1_fitMu.Clone()
                histDetail_fitMu.lineWidth = 4
                histDetail_fitMu.lineColor = 4
                histDetail_fitMu.drawOption = "PE1"
                histDetail_fitMu.addToLegend = False
                
                outFileName = "%s/%s_fitMu" %(outDir, plotQuantity.outFileName)
                
                Common.plot1D(
                    list_histDetails = [histDetail_fitMu],
                    stackDrawOption = "nostack",
                    title = "",
                    xTitle = "%s %s" %(plotQuantity.etaObjLatex, etaUnitStr),
                    yTitle = yTitle,
                    xMin = plotQuantity.mu_xMin, xMax = plotQuantity.mu_xMax,
                    yMin = plotQuantity.mu_yMin, yMax = plotQuantity.mu_yMax,
                    yTitleSizeScale = 0.7,
                    yTitleOffset = 1.8,
                    yLabelSizeScale = 0.9,
                    #logX = False, logY = True,
                    gridX = True, gridY = True,
                    #nDivisionsX = plotQuantity.nDivisionsX,
                    #nDivisionsY = plotQuantity.nDivisionsY,
                    drawLegend = True,
                    legendHeightScale = 0.5,
                    #legendNcol = plotQuantity.legendNcol,
                    #legendHeightScale = plotQuantity.legendHeightScale,
                    #legendWidthScale = plotQuantity.legendWidthScale,
                    transparentLegend = False,
                    legendTextSize = -1,
                    legendBorderSize = 0,
                    legendPos = "LR",
                    legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
                    CMSextraText = "Simulation Preliminary",
                    fixAlphanumericBinLabels = False,
                    outFileName = outFileName,
                    outFileName_suffix = "",
                )
            
            
            # Fit sigma
            if (plotQuantity.fit) :
                
                histDetail_fitSigma = Common.HistogramDetails()
                histDetail_fitSigma.hist = h1_fitSigma.Clone()
                histDetail_fitSigma.lineWidth = 4
                histDetail_fitSigma.lineColor = 4
                histDetail_fitSigma.drawOption = "PE1"
                histDetail_fitSigma.addToLegend = False
                
                outFileName = "%s/%s_fitSigma" %(outDir, plotQuantity.outFileName)
                
                Common.plot1D(
                    list_histDetails = [histDetail_fitSigma],
                    stackDrawOption = "nostack",
                    title = "",
                    xTitle = "%s %s" %(plotQuantity.etaObjLatex, etaUnitStr),
                    yTitle = yTitle,
                    xMin = plotQuantity.sigma_xMin, xMax = plotQuantity.sigma_xMax,
                    yMin = plotQuantity.sigma_yMin, yMax = plotQuantity.sigma_yMax,
                    yTitleSizeScale = 0.7,
                    yTitleOffset = 1.8,
                    yLabelSizeScale = 0.9,
                    #logX = False, logY = True,
                    gridX = True, gridY = True,
                    #nDivisionsX = plotQuantity.nDivisionsX,
                    #nDivisionsY = plotQuantity.nDivisionsY,
                    drawLegend = True,
                    legendHeightScale = 0.5,
                    #legendNcol = plotQuantity.legendNcol,
                    #legendHeightScale = plotQuantity.legendHeightScale,
                    #legendWidthScale = plotQuantity.legendWidthScale,
                    transparentLegend = False,
                    legendTextSize = -1,
                    legendBorderSize = 0,
                    legendPos = "UL",
                    legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
                    CMSextraText = "Simulation Preliminary",
                    fixAlphanumericBinLabels = False,
                    outFileName = outFileName,
                    outFileName_suffix = "",
                )
            
            
            l_extraText = []
            
            # Fit resolution
            if (plotQuantity.fitResolution) :
                
                #resolutionFitFuncStr = "([0]^2/x + [1]^2/x^2 + [2]^2)^0.5"
                #resolutionFitFuncStr = "pow([0]*[0]/x + [1]*[1]/(x*x) + [2]*[2], 0.5)"
                resolutionFitFuncStr = "pow([0]*[0]/x + [1]*[1]/(x*x) + [2]*[2] + pow(%s, 2), 0.5)" %(plotQuantity.resolutionFit_extraTerm)
                #resolutionFitFuncStr = "(([0]/sqrt(x))^2 + ([1]/x)^2 + [2]^2)^0.5"
                #resolutionFitFuncStr = "([0]^2/x + [1]^2/x^2 + [2]^2)"
                #resolutionFitFuncStr = "([0]/x + [1]/x^2 + [2])^0.5"
                
                f1_resolutionFitFunc = 0
                
                if (len(plotQuantity.resolutionFit_range)) :
                    
                    resolutionFit_lwr = float(plotQuantity.resolutionFit_range[0])
                    resolutionFit_upr = float(plotQuantity.resolutionFit_range[1])
                    
                    f1_resolutionFitFunc = ROOT.TF1("resolutionFitFunc", resolutionFitFuncStr, resolutionFit_lwr, resolutionFit_upr)
                
                else :
                    
                    f1_resolutionFitFunc = ROOT.TF1("resolutionFitFunc", resolutionFitFuncStr)
                
                f1_resolutionFitFunc.SetParName(0, "stoch")
                f1_resolutionFitFunc.SetParName(1, "noise")
                f1_resolutionFitFunc.SetParName(2, "const")
                
                f1_resolutionFitFunc.SetParLimits(f1_resolutionFitFunc.GetParNumber("stoch"), 0.0, 200.0)
                f1_resolutionFitFunc.SetParLimits(f1_resolutionFitFunc.GetParNumber("noise"), 0.0, 1000.0)
                f1_resolutionFitFunc.SetParLimits(f1_resolutionFitFunc.GetParNumber("const"), 0.0, 200.0)
                
                #f1_resolutionFitFunc.SetParameter("stoch", h1_relResolution.GetBinContent(h1_relResolution.FindBin(resolutionFit_lwr)) * resolutionFit_lwr**0.5)
                f1_resolutionFitFunc.SetParameter("stoch", 25.0)
                
                #f1_resolutionFitFunc.SetParameter("noise", h1_relResolution.GetBinContent(h1_relResolution.FindBin(resolutionFit_lwr)) * resolutionFit_lwr)
                f1_resolutionFitFunc.SetParameter("noise", 0.0)
                
                #f1_resolutionFitFunc.SetParameter("const", h1_relResolution.GetBinContent(h1_relResolution.FindBin(resolutionFit_upr)))
                f1_resolutionFitFunc.SetParameter("const", 2.0)
                
                #fixNoise = True
                fixNoise = False
                fixedStr = "(fixed)"
                
                #f1_resolutionFitFunc.FixParameter(f1_resolutionFitFunc.GetParNumber("stoch"), h1_relResolution.GetBinContent(h1_relResolution.FindBin(resolutionFit_lwr)) * resolutionFit_lwr**0.5)
                
                if(fixNoise) :
                    
                    f1_resolutionFitFunc.FixParameter(f1_resolutionFitFunc.GetParNumber("noise"), 0.0)
                    #f1_resolutionFitFunc.FixParameter(f1_resolutionFitFunc.GetParNumber("noise"), 350.0)
                
                #f1_resolutionFitFunc.FixParameter(f1_resolutionFitFunc.GetParNumber("const"), h1_relResolution.GetBinContent(h1_relResolution.FindBin(resolutionFit_upr)))
                
                constTerm = 0
                stochTerm = 0
                noiseTerm = 0
                
                statusStr = ""
                NDF = 0
                chiSqPerNDF = 10
                fitIter = 0
                
                
                #################### Use the graph ####################
                
                #h1_relResolution = Common.TGraphToTH1(gr_relResolution)
                
                #######################################################
                
                
                while ((statusStr not in ["CONVERGED", "OK", "SUCCESSFUL"] or chiSqPerNDF > 1) and fitIter < 5) :
                    
                    #fitResult = h1_temp.Fit(f1_resolutionFitFunc, "RBS", "", fitLwr, fitUpr)
                    #fitResult = h1_fitSigma.Fit(f1_resolutionFitFunc, "RBS")
                    
                    fitResult = h1_relResolution.Fit(f1_resolutionFitFunc, "RBSEM", "", resolutionFit_lwr, resolutionFit_upr)
                    #fitResult = gr_relResolution.Fit(f1_resolutionFitFunc, "RBSEM", "", resolutionFit_lwr, resolutionFit_upr)
                    
                    statusStr = ROOT.gMinuit.fCstatu
                    statusStr = statusStr.strip()
                    
                    chiSq = f1_resolutionFitFunc.GetChisquare()
                    NDF = f1_resolutionFitFunc.GetNDF()
                    
                    if (NDF) :
                        
                        chiSqPerNDF = chiSq / NDF
                    
                    print "Chi^2:", chiSq
                    print "NDF:", NDF
                    print "Chi^2 / NDF:", chiSqPerNDF
                    
                    stochTerm = f1_resolutionFitFunc.GetParameter("stoch")
                    noiseTerm = f1_resolutionFitFunc.GetParameter("noise")
                    constTerm = f1_resolutionFitFunc.GetParameter("const")
                    
                    stochTermErr = f1_resolutionFitFunc.GetParError(f1_resolutionFitFunc.GetParNumber("stoch"))
                    noiseTermErr = f1_resolutionFitFunc.GetParError(f1_resolutionFitFunc.GetParNumber("noise"))
                    constTermErr = f1_resolutionFitFunc.GetParError(f1_resolutionFitFunc.GetParNumber("const"))
                    
                    print "stoch", stochTerm
                    print "noise", noiseTerm
                    print "const", constTerm
                    
                    fitIter += 1
                
                if (statusStr not in ["CONVERGED", "OK", "SUCCESSFUL"] and NDF) :
                    
                    print "Error: Fit failed."
                    exit(1)
                
                
                stochTermStr = "#frac{%0.1f#pm%0.1f}{#sqrt{E}}[%%]" %(stochTerm, stochTermErr)
                noiseTermStr = "#frac{%0.1f#pm%0.1f}{E}[%%] %s" %(noiseTerm, noiseTermErr, fixNoise*fixedStr)
                constTermStr = "%0.1f#pm%0.1f [%%]" %(constTerm, constTermErr)
                
                chiSqStr = "#[]{#frac{#chi^{2}}{NDF}=%0.2f}" %(chiSqPerNDF)
                
                #fitExpressionStr = "#scale[0.7]{%s #oplus %s #oplus %s}" %(stochTermStr, noiseTermStr, constTermStr)
                fitExpressionStr = "#scale[0.6]{%s #oplus %s #oplus %s   %s}" %(stochTermStr, noiseTermStr, constTermStr, chiSqStr)
                #fitExpressionStr = "#scale[0.7]{%s #oplus %s}" %(stochTermStr, constTermStr)
                
                if (plotQuantity.fitResolution_draw) :
                    
                    l_extraText.append([40, 1.5, fitExpressionStr])
                
                
                
                histDetail_fitSigma = Common.HistogramDetails()
                #histDetail_fitSigma.hist = h1_fitSigma.Clone()
                histDetail_fitSigma.hist = h1_relResolution.Clone()
                #histDetail_fitSigma.hist = Common.TGraphToTH1(gr_relResolution)
                histDetail_fitSigma.lineWidth = 4
                histDetail_fitSigma.lineColor = 4
                histDetail_fitSigma.drawOption = "PE1"
                histDetail_fitSigma.addToLegend = False
                
                outFileName = "%s/%s_relResolution" %(outDir, plotQuantity.outFileName)
                
                Common.plot1D(
                    list_histDetails = [histDetail_fitSigma],
                    stackDrawOption = "nostack",
                    title = "",
                    xTitle = plotQuantity.resolutionFit_xTitle,
                    yTitle = plotQuantity.resolutionFit_yTitle,
                    xMin = 0.0,
                    xMax = float(plotQuantity.l_etaBinStr_muSigma[-1]),
                    yMin = plotQuantity.resolutionFit_yMin,
                    yMax = plotQuantity.resolutionFit_yMax,
                    yTitleSizeScale = 0.7,
                    yTitleOffset = 1.8,
                    yLabelSizeScale = 0.9,
                    #logX = False, logY = True,
                    gridX = True, gridY = True,
                    #nDivisionsX = plotQuantity.nDivisionsX,
                    #nDivisionsY = plotQuantity.nDivisionsY,
                    drawLegend = True,
                    legendHeightScale = 0.5,
                    #legendNcol = plotQuantity.legendNcol,
                    #legendHeightScale = plotQuantity.legendHeightScale,
                    #legendWidthScale = plotQuantity.legendWidthScale,
                    transparentLegend = False,
                    legendTextSize = -1,
                    legendBorderSize = 0,
                    legendPos = "UR",
                    legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
                    l_extraText = l_extraText,
                    CMSextraText = "Simulation Preliminary",
                    fixAlphanumericBinLabels = False,
                    outFileName = outFileName,
                    outFileName_suffix = "",
                )
            
            
            # Fit sigma-by-mu
            histDetail_fitSigmaByMu = Common.HistogramDetails()
            histDetail_fitSigmaByMu.hist = h1_fitSigmaByMu.Clone()
            histDetail_fitSigmaByMu.lineWidth = 4
            histDetail_fitSigmaByMu.lineColor = 4
            histDetail_fitSigmaByMu.drawOption = "PE1"
            histDetail_fitSigmaByMu.addToLegend = False
            
            outFileName = "%s/%s_fitSigmaByMu" %(outDir, plotQuantity.outFileName)
            
            Common.plot1D(
                list_histDetails = [histDetail_fitSigmaByMu],
                stackDrawOption = "nostack",
                title = "",
                xTitle = "%s %s" %(plotQuantity.etaObjLatex, etaUnitStr),
                yTitle = "Fit #sigma/#mu [%]",
                #xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
                #yMin = h1_fitSigmaByMu.GetMinimum()-0.05, yMax = 1.1,
                yMin = 0.0, yMax = 20,
                yTitleSizeScale = 0.7,
                yTitleOffset = 1.8,
                yLabelSizeScale = 0.9,
                #logX = False, logY = True,
                gridX = True, gridY = True,
                #nDivisionsX = plotQuantity.nDivisionsX,
                #nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = 0.5,
                #legendNcol = plotQuantity.legendNcol,
                #legendHeightScale = plotQuantity.legendHeightScale,
                #legendWidthScale = plotQuantity.legendWidthScale,
                transparentLegend = False,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[1.5]{HGCal EE%s}" %(zsideSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
            
            
            if (saveToRootFile) :
                
                outRootFileName = "%s/%s.root" %(outDir, plotQuantity.outFileName)
                outRootFile = ROOT.TFile.Open(outRootFileName, "RECREATE")
                outRootFile.cd()
                
                h1_mu.Write()
                
                h1_fitMu.Write()
                h1_fitSigma.Write()
                h1_fitSigmaByMu.Write()
                
                h1_relResolution.Write()
                
                outRootFile.Close()
        
        
        else :
            
            #print "xxx"
            
            plotStr = plotQuantity.plotStr
            cutStr = plotQuantity.cutStr
            weightStr = plotQuantity.weightStr
            
            h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
            h1_temp.Sumw2()
            
            plotStr = "%s" %(plotStr)
            weightStr = "%s * (%s)" %(weightStr, cutStr)
            
            for key in d_strReplace :
                
                print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                
                plotStr = plotStr.replace(key, d_strReplace[key])
                weightStr = weightStr.replace(key, d_strReplace[key])
            
            if ("{{" in plotStr) :
                    
                    Common.iterateAndDraw(tree, plotStr, weightStr, h1_temp.GetName())
            
            else :
                
                plotStr = "%s >> %s" %(plotStr, h1_temp.GetName())
                
                print plotStr
                print weightStr
                
                tree.Draw(plotStr, weightStr)
            
            #print plotStr
            #print weightStr
            
            #tree.Draw(plotStr, weightStr)
            
            if (plotQuantity.normalize) :
                
                h1_temp.Scale(1.0 / h1_temp.Integral())
            
            
            color = 4
            
            mu = h1_temp.GetMean()
            muErr = h1_temp.GetMeanError()
            
            sigma = h1_temp.GetStdDev()
            sigmaErr = h1_temp.GetStdDevError()
            
            sigmaByMu = sigma / mu * 100.0
            
            sigmaByMu_err = sigmaByMu * ((muErr/mu)**2 + (sigmaErr/sigma)**2)**0.5
            
            maxBin = h1_temp.GetMaximumBin()
            maxPos = h1_temp.GetBinCenter(maxBin)
            
            histLabel = "#scale[0.7]{#splitline{#mu=%0.1e, #sigma=%0.1e}{#sigma/#mu[%%]=%0.2f#pm%0.2f}}" %(mu, sigma, sigmaByMu, sigmaByMu_err)
            
            
            # Fit
            if (plotQuantity.fit) :
                
                nSigmaLwr = 2
                nSigmaUpr = 2
                fitLwr = max(0, maxPos - nSigmaLwr*sigma)
                fitUpr = maxPos + nSigmaUpr*sigma
                
                print "*"*50, maxPos, fitLwr, fitUpr
                
                f1_fitFunc = ROOT.TF1("Gaussian", "gaus(x)", fitLwr, fitUpr)
                f1_fitFunc.SetLineColor(color)
                f1_fitFunc.SetLineWidth(2)
                
                f1_fitFunc.SetParameter("Mean", mu)
                f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Mean"), fitLwr, fitUpr)
                
                f1_fitFunc.SetParameter("Sigma", sigma)
                f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Sigma"), 0, 3*sigma)
                
                
                #f1_fitFunc = ROOT.TF1("CrystalBall", "crystalball(x)", fitLwr, fitUpr)
                #f1_fitFunc.SetLineColor(color)
                #f1_fitFunc.SetLineWidth(2)
                #
                #f1_fitFunc.SetParameter("Mean", mu)
                #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Mean"), fitLwr, fitUpr)
                #
                #f1_fitFunc.SetParameter("Sigma", sigma)
                #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Sigma"), 0, 10*sigma)
                #
                #f1_fitFunc.SetParameter("Alpha", fitUpr/2.0)
                #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Alpha"), 0, fitUpr)
                #
                #f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("N"), 0, 100)
                
                
                statusStr = ""
                NDF = 0
                chiSqPerNDF = 10
                fitIter = 0
                
                while ((statusStr != "CONVERGED" or chiSqPerNDF > 1) and fitIter < 5) :
                    
                    fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                    
                    statusStr = ROOT.gMinuit.fCstatu
                    statusStr = statusStr.strip()
                    
                    chiSq = f1_fitFunc.GetChisquare()
                    NDF = f1_fitFunc.GetNDF()
                    
                    if (NDF) :
                        
                        chiSqPerNDF = chiSq / NDF
                    
                    print "Chi^2:", chiSq
                    print "NDF:", NDF
                    print "Chi^2 / NDF:", chiSqPerNDF
                    
                    fitIter += 1
                
                
                #fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                #
                #statusStr = ROOT.gMinuit.fCstatu
                #statusStr = statusStr.strip()
                
                if (statusStr != "CONVERGED" and NDF) :
                    
                    print "Error: Fit failed."
                    exit(1)
                
                fitMu = f1_fitFunc.GetParameter("Mean")
                fitMu_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Mean"))
                
                fitSigma = f1_fitFunc.GetParameter("Sigma")
                fitSigma_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Sigma"))
                
                fitSigmaByMu = fitSigma / fitMu * 100
                fitSigmaByMu_err = fitSigmaByMu * ((fitMu_err/fitMu)**2 + (fitSigma_err/fitSigma)**2)**0.5
                
                histLabel = "#scale[0.7]{#splitline{#mu_{fit}=%0.1e, #sigma_{fit}=%0.1e}{#sigma_{fit}/#mu_{fit}[%%]=%0.2f#pm%0.2f}}" %(fitMu, fitSigma, fitSigmaByMu, fitSigmaByMu_err)
            
            histDetail_temp = Common.HistogramDetails()
            histDetail_temp.hist = h1_temp.Clone()
            histDetail_temp.lineWidth = 4
            histDetail_temp.lineColor = color
            #histDetail_temp.markerSize = 0
            histDetail_temp.markerStyle = 1
            #histDetail_temp.addToLegend = False
            histDetail_temp.drawOption = "hist"
            histDetail_temp.histLabel = histLabel
            
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
                gridX = True, gridY = True,
                nDivisionsX = plotQuantity.nDivisionsX,
                nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = 0.5,
                transparentLegend = False,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[1.1]{HGCal EE%s}" %(zsideSignLatex),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
