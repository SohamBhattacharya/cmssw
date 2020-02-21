import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle

import Common


class plotQuantity :
    
    isMultiLayer = False
    
    isEtaBinned = False
    l_etaBinStr = []
    l_etaBinStr_muSigma = []
    etaObjStr = ""
    etaObjLatex = ""
    
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
    
    logX = False
    logY = False
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    xTitle = ""
    yTitle = ""
    
    legendNcol = 1
    legendHeightScale = 1
    legendWidthScale = 1
    
    d_fitInfo = {}
    
    outFileName = ""
    outDir = ""


d_fitInfo_crystalBall = {
    
}


#tdrstyle.setTDRStyle()

#ROOT.gStyle.SetOptStat(1001110)
#ROOT.gStyle.SetPalette(ROOT.kRainBow)


d_inputInfo = {
    "Mean": {
        "fileName": "/media/soham/E/HGCal_ele-reco/SingleZprimeToEEflatPtGun_m-5_pT-35_eta-1p5-3p0_GEN-SIM-RECO/ntupleTree_Mean.root",
        "file": 0,
        "tree": 0,
    },
    
    "Expo": {
        "fileName": "/media/soham/E/HGCal_ele-reco/SingleZprimeToEEflatPtGun_m-5_pT-35_eta-1p5-3p0_GEN-SIM-RECO/ntupleTree_Expo.root",
        "file": 0,
        "tree": 0,
    },
    
    "Expo3D": {
        "fileName": "/media/soham/E/HGCal_ele-reco/SingleZprimeToEEflatPtGun_m-5_pT-35_eta-1p5-3p0_GEN-SIM-RECO/ntupleTree_Expo3Ddist.root",
        "file": 0,
        "tree": 0,
    },
    
    "Gaus": {
        "fileName": "/media/soham/E/HGCal_ele-reco/SingleZprimeToEEflatPtGun_m-5_pT-35_eta-1p5-3p0_GEN-SIM-RECO/ntupleTree_Gaus.root",
        "file": 0,
        "tree": 0,
    },
    
    "Gaus3D": {
        "fileName": "/media/soham/E/HGCal_ele-reco/SingleZprimeToEEflatPtGun_m-5_pT-35_eta-1p5-3p0_GEN-SIM-RECO/ntupleTree_Gaus3Ddist.root",
        "file": 0,
        "tree": 0,
    },
}

#l_sharingAlgoKey = ["Mean", "Expo", "Gaus"]
l_sharingAlgoKey = d_inputInfo.keys()

for iSharingAlgoKey in range(0, len(l_sharingAlgoKey)) :
    
    sharingAlgoKey = l_sharingAlgoKey[iSharingAlgoKey]
    
    fileName = d_inputInfo[sharingAlgoKey]["fileName"]
    
    d_inputInfo[sharingAlgoKey]["file"] = ROOT.TFile.Open(fileName)
    
    d_inputInfo[sharingAlgoKey]["tree"] = d_inputInfo[sharingAlgoKey]["file"].Get("treeMaker/tree")


HGCalEE_nLayer = 28

l_zsideVal = [+1, -1]

#l_etaBinStr = ["2.75", "3.0"]
#l_etaBinStr = ["1.5", "1.75", "2.0", "2.25", "2.5", "2.75", "3.0"]
l_etaBinStr = ["%0.1f" %(val) for val in numpy.arange(1.5, 3.3, 0.3)]
#l_etaBinStr = ["%0.1f" %(val) for val in numpy.arange(1.5, 3.1, 0.75)]

#l_etaBinStr_muSigma = ["2.75", "3.0"]
l_etaBinStr_muSigma = ["%0.1f" %(val) for val in numpy.arange(1.5, 3.1, 0.1)]


d_strReplace = {
    "@zsideCondStr@": "",
}


l_plotQuantity = []


pltQty_temp = plotQuantity()
pltQty_temp.isMultiLayer = False
pltQty_temp.plotStr = "genEl_multiClus_totE/genEl_E"
pltQty_temp.cutStr = "genEl_eta @zsideCondStr@"
pltQty_temp.isEtaBinned = False
pltQty_temp.l_etaBinStr = l_etaBinStr
pltQty_temp.l_etaBinStr_muSigma = l_etaBinStr_muSigma
pltQty_temp.etaObjStr = "fabs(genEl_eta)"
pltQty_temp.etaObjLatex = "gen-e"
pltQty_temp.nBin = 400
pltQty_temp.createXmin = 0
pltQty_temp.createXmax = 10
pltQty_temp.xMin = 0.5
pltQty_temp.xMax = 2.0
pltQty_temp.yMin = 1e-3
pltQty_temp.yMax = 1
pltQty_temp.logY = True
pltQty_temp.xTitle = "E^{tot}_{multi-clus} / E_{gen-e}"
pltQty_temp.yTitle = "a.u."
pltQty_temp.legendHeightScale = 0.75
pltQty_temp.legendWidthScale = 1.2
pltQty_temp.outFileName = "genEl-multiClus-totE_by_genEl-E"
pltQty_temp.outDir = "plots/compareSharing"
l_plotQuantity.append(pltQty_temp)



for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
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
        
        
        #outDir = "%s/HGCalEE%s" %(plotQuantity.outDir, zsideStr)
        #os.system("mkdir -p %s" %(outDir))
        
        
        l_histDetail = []
        
        for iSharingAlgoKey in range(0, len(l_sharingAlgoKey)) :
            
            sharingAlgoKey = l_sharingAlgoKey[iSharingAlgoKey]
            tree = d_inputInfo[sharingAlgoKey]["tree"]
            
            outDir = "%s/%s/HGCalEE%s" %(plotQuantity.outDir, sharingAlgoKey, zsideStr)
            os.system("mkdir -p %s" %(outDir))
            
            #print "xxx"
            
            plotStr = plotQuantity.plotStr
            cutStr = plotQuantity.cutStr
            weightStr = plotQuantity.weightStr
            
            h1_temp = ROOT.TH1F("h1_temp", "h1_temp", plotQuantity.nBin, plotQuantity.createXmin, plotQuantity.createXmax)
            h1_temp.Sumw2()
            
            plotStr = "%s >> h1_temp" %(plotStr)
            weightStr = "%s * (%s)" %(weightStr, cutStr)
            
            for key in d_strReplace :
                
                print "Replacing \"%s\" with \"%s\"" %(key, d_strReplace[key])
                
                plotStr = plotStr.replace(key, d_strReplace[key])
                weightStr = weightStr.replace(key, d_strReplace[key])
            
            print plotStr
            print weightStr
            
            tree.Draw(plotStr, weightStr)
            
            if (plotQuantity.normalize) :
                
                h1_temp.Scale(1.0 / h1_temp.Integral())
            
            
            mu = h1_temp.GetMean()
            muErr = h1_temp.GetMeanError()
            sigma = h1_temp.GetStdDev()
            
            maxBin = h1_temp.GetMaximumBin()
            maxPos = h1_temp.GetBinCenter(maxBin)
            
            
            # Fit
            nSigmaLwr = 2
            nSigmaUpr = 2
            fitLwr = max(0, maxPos - nSigmaLwr*sigma)
            fitUpr = maxPos + nSigmaUpr*sigma
            
            f1_fitFunc = ROOT.TF1("CrystalBall", "crystalball(x)", fitLwr, fitUpr)
            #f1_fitFunc = ROOT.TF1("Gaussian", "gaus(x)", fitLwr, fitUpr)
            f1_fitFunc.SetLineColor(4)
            f1_fitFunc.SetLineWidth(2)
            
            f1_fitFunc.SetParameter("Mean", mu)
            f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Mean"), fitLwr, fitUpr)
            
            f1_fitFunc.SetParameter("Sigma", sigma)
            f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Sigma"), 0, 10*sigma)
            
            f1_fitFunc.SetParameter("Alpha", fitUpr/2.0)
            f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("Alpha"), 0, fitUpr)
            
            f1_fitFunc.SetParLimits(f1_fitFunc.GetParNumber("N"), 0, 100)
            
            statusStr = ""
            
            chiSqPerNDF = 10
            
            fitIter = 0
            
            while ((statusStr != "CONVERGED" or chiSqPerNDF > 3) and fitIter < 5) :
                
                fitResult = h1_temp.Fit(f1_fitFunc, "RBS", "", fitLwr, fitUpr)
                
                statusStr = ROOT.gMinuit.fCstatu
                statusStr = statusStr.strip()
                
                chiSq = f1_fitFunc.GetChisquare()
                NDF = f1_fitFunc.GetNDF()
                chiSqPerNDF = chiSq / NDF
                
                print "Chi^2:", chiSq
                print "NDF:", NDF
                print "Chi^2 / NDF:", chiSqPerNDF
                
                #if (statusStr != "CONVERGED") :
                #    
                #    print "\n"
                #    print "#" * 50
                #    print "Error: Fit failed."
                #    print "#" * 50
                #    exit(1)
                
                fitIter += 1
            
            fitMu = f1_fitFunc.GetParameter("Mean")
            fitMu_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Mean"))
            
            fitSigma = f1_fitFunc.GetParameter("Sigma")
            fitSigma_err = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("Sigma"))
            
            muBySigma = fitMu / fitSigma
            muBySigma_err = muBySigma * ((fitMu_err/fitMu)**2 + (fitSigma_err/fitSigma)**2)**0.5
            
            sigmaByMu = fitSigma / fitMu * 100
            sigmaByMu_err = sigmaByMu * ((fitMu_err/fitMu)**2 + (fitSigma_err/fitSigma)**2)**0.5
            
            
            histDetail_temp = Common.HistogramDetails()
            histDetail_temp.hist = h1_temp.Clone()
            histDetail_temp.lineWidth = 4
            histDetail_temp.lineColor = 4
            #histDetail_temp.markerSize = 0
            histDetail_temp.markerStyle = 1
            #histDetail_temp.addToLegend = False
            histDetail_temp.drawOption = "hist"
            histDetail_temp.histLabel = (
                "#splitline{"
                    "#splitline{Fit #mu = %0.1e#pm%0.1e}{Fit #sigma = %0.1e#pm%0.1e}"
                "}"
                "{"
                    "Fit #sigma/#mu [%%] = %0.1f#pm%0.1f"
                "}"
                %(
                    fitMu, fitMu_err,
                    fitSigma, fitSigma_err,
                    sigmaByMu, sigmaByMu_err,
                )
            )
            
            l_histDetail.append(histDetail_temp)
            
            outFileName = "%s/%s" %(outDir, plotQuantity.outFileName)
            
            Common.plot1D(
                list_histDetails = [histDetail_temp],
                stackDrawOption = "nostack",
                title = "",
                xTitle = plotQuantity.xTitle,
                yTitle = plotQuantity.yTitle,
                xMin = plotQuantity.xMin, xMax = plotQuantity.xMax,
                yMin = plotQuantity.yMin, yMax = plotQuantity.yMax,
                logX = plotQuantity.logX, logY = plotQuantity.logY,
                gridX = False, gridY = False,
                nDivisionsX = plotQuantity.nDivisionsX,
                nDivisionsY = plotQuantity.nDivisionsY,
                drawLegend = True,
                legendHeightScale = plotQuantity.legendHeightScale,
                legendWidthScale = plotQuantity.legendWidthScale,
                transparentLegend = True,
                legendTextSize = -1,
                legendBorderSize = 0,
                legendPos = "UR",
                legendTitle = "#scale[1.5]{#splitline{HGCal EE%s}{(%s sharing)}}" %(zsideSignLatex, sharingAlgoKey),
                CMSextraText = "Simulation Preliminary",
                fixAlphanumericBinLabels = False,
                outFileName = outFileName,
                outFileName_suffix = "",
            )
