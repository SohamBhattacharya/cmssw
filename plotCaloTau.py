import numpy

import ROOT
from ROOT import TAxis
from ROOT import TCanvas
from ROOT import TFile
from ROOT import TH1F
from ROOT import TH2F
from ROOT import THStack
from ROOT import TLegend
from ROOT import TStyle


initVal = -9999

numberFormat_int = ".0f"
numberFormat_float = ".3f"


ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetPaintTextFormat(numberFormat_float)
ROOT.gStyle.SetTitleH(0.035)


l_discriminatorName = [
    "none",
    "againstElectron",
    "againstMuon",
    "byECALIsolation",
    "byIsolation",
    "byTrackIsolation",
    "byLeadingTrackPtCut",
]

l_varName_discName = [
    ["leadTrackHCAL3x3hitsEtSum", ["none"]],
    ["leadTrackHCAL3x3hitsEtSum_by_sigTrack1pT", ["none"]],
    ["leadTrackHCAL3x3hitsEtSum_by_sigTrackHT", ["none"]],
    
    ["maximumHCALhitEt", ["none"]],
    ["maximumHCALhitEt_by_sigTrack1pT", ["none"]],
    ["maximumHCALhitEt_by_sigTrackHT", ["none"]],
    
    ["isolationECALhitsEtSum", ["none"]],
    ["isolationECALhitsEtSum_by_sigTrack1pT", ["none"]],
    ["isolationECALhitsEtSum_by_sigTrackHT", ["none"]],
    
    ["isolationTracksPtSum", ["none"]],
    ["isolationTracksPtSum_by_sigTrack1pT", ["none"]],
    ["isolationTracksPtSum_by_sigTrackHT", ["none"]],
    
    ["m", ["none"]],
    ["signalTracksInvariantMass", ["none"]],
    ["TracksInvariantMass", ["none"]],
    
    ["sigTrack1_deltaR", ["none", "byLeadingTrackPtCut"]],
    ["isoTrack1_deltaR", ["none", "byLeadingTrackPtCut"]],
    
    ["sigTrack_n", ["none"]],
    ["isoTrack_n", ["none"]],
]

l_var_xMax = [
    [800],
    [5],
    [5],
    
    [600],
    [5],
    [5],
    
    [100],
    [5],
    [5],
    
    [100],
    [5],
    [5],
    
    [10],
    [10],
    [10],
    
    [0.4, 0.4],
    [0.9, 0.9],
    
    [20],
    [20],
]

l_varLabel = [
    "#tau^{calo}_{h} leadTrackHCAL3x3hitsEtSum",
    "#tau^{calo}_{h} leadTrackHCAL3x3hitsEtSum / p^{sig-trk_{1}}_{T}",
    "#tau^{calo}_{h} leadTrackHCAL3x3hitsEtSum / H^{sig-trk}_{T}",
    
    "#tau^{calo}_{h} maximumHCALhitEt",
    "#tau^{calo}_{h} maximumHCALhitEt / p^{sig-trk_{1}}_{T}",
    "#tau^{calo}_{h} maximumHCALhitEt / H^{sig-trk}_{T}",
    
    "#tau^{calo}_{h} isolationECALhitsEtSum",
    "#tau^{calo}_{h} isolationECALhitsEtSum / p^{sig-trk_{1}}_{T}",
    "#tau^{calo}_{h} isolationECALhitsEtSum / H^{sig-trk}_{T}",
    
    "#tau^{calo}_{h} isolationTracksPtSum",
    "#tau^{calo}_{h} isolationTracksPtSum / p^{sig-trk_{1}}_{T}",
    "#tau^{calo}_{h} isolationTracksPtSum / H^{sig-trk}_{T}",
    
    "#tau^{calo}_{h} m",
    "#tau^{calo}_{h} signalTracksInvariantMass",
    "#tau^{calo}_{h} TracksInvariantMass",
    
    "#DeltaR(#tau^{calo}_{h}, sig-trk_{1})",
    "#DeltaR(#tau^{calo}_{h}, iso-trk_{1})",
    
    "n_{sig-trk}",
    "n_{iso-trk}",
]

color_genMatched = 8
color_genNotMatched = 2


#inputFile_RelValZpTT_1500_13 = "CaloTauAnalysis.root"
inputFile_RelValZpTT_1500_13 = "output/RelValZpTT_1500_13_CMSSW_10_1_0_pre1-PU25ns_100X_upgrade2018_realistic_v10-v1_GEN-SIM-RECO/CaloTauAnalysis.root"
inputFile_RelValQCD_FlatPt_15_3000HS_13 = "output/RelValQCD_FlatPt_15_3000HS_13_CMSSW_10_1_0_pre2-PU25ns_100X_upgrade2018_realistic_v11-v1_GEN-SIM-RECO/CaloTauAnalysis.root"


class HistogramDetails :
    
    rootFileName = ""
    rootFile = 0
    
    histName = ""
    histTitle = ""
    histLabel = ""
    
    lineColor = 4
    lineStyle = 1
    lineWidth = 1
    
    hist = 0
    
    xTitle = ""
    yTitle = ""
    
    xMin = initVal
    xMax = initVal
    
    yMin = initVal
    yMax = initVal
    
    zMin = initVal
    zMax = initVal
    
    logX = False
    logY = False
    logZ = False
    
    gridX = False
    gridY = False
    
    nDivisionsX = [0, 0, 0]
    nDivisionsY = [0, 0, 0]
    
    centerLabelsX = False
    centerLabelsY = False
    
    drawOption = "hist"
    
    outFileName = ""
    outFileName_suffix = ""
    
    
    def getHist(self, projection = "", startBin = 0, endBin = -1, findStartBin = False, findEndBin = False, suffix = "") :
        
        print "File:", self.rootFileName
        print "Name:", self.histName
        
        self.rootFile = TFile(self.rootFileName)
        
        axis = 0
        
        if (projection == "X") :
            
            hist_temp = self.rootFile.Get(self.histName).Clone()
            axis = hist_temp.GetYaxis()
        
        elif (projection == "Y") :
            
            hist_temp = self.rootFile.Get(self.histName).Clone()
            axis = hist_temp.GetXaxis()
        
        if (projection != "" and findStartBin) :
            
            startBin = axis.FindBin(startBin)
        
        if (projection != "" and findEndBin) :
            
            endBin = axis.FindBin(endBin)
        
        # Get histogram
        if (projection == "") :
            
            self.hist = self.rootFile.Get(self.histName).Clone()
            self.hist.Sumw2()
        
        elif (projection == "X") :
            
            print "Projection X"
            self.hist = self.rootFile.Get(self.histName).Clone().ProjectionX(self.histName + "_px" + suffix, startBin, endBin)
            self.hist.Sumw2()
        
        elif (projection == "Y") :
            
            print "Projection Y"
            self.hist = self.rootFile.Get(self.histName).Clone().ProjectionY(self.histName + "_py" + suffix, startBin, endBin)
            self.hist.Sumw2()
        
        else :
            
            print "Wrong projection option to HistogramDetails.getHist(...)"
            exit(1)
    
    
    def normalize(self, byBinWidth = False) :
        
        integral = self.hist.Integral()
        
        self.hist.Scale(1.0 / integral)
        
        if (byBinWidth) :
            
            for iBin in range(0, self.hist.GetNbinsX()) :
                
                binWidth = self.hist.GetXaxis().GetBinWidth(iBin+1)
                binContent = self.hist.GetBinContent(iBin+1)
                binError = self.hist.GetBinError(iBin+1)
                
                #print binWidth, binContent
                
                scale = 1.0 / binWidth
                
                self.hist.SetBinContent(iBin+1, binContent*scale)
                self.hist.SetBinError(iBin+1, binError*scale)


def plot1D(list_histDetails,
    stackDrawOption = "nostack",
    title = "",
    xTitle = "", yTitle = "",
    xMin = initVal, xMax = initVal,
    yMin = initVal, yMax = initVal,
    logX = False, logY = False,
    gridX = False, gridY = False,
    nDivisionsX = [0, 0, 0], nDivisionsY = [0, 0, 0],
    centerLabelsX = False, centerLabelsY = False,
    drawLegend = True,
    legendTextSize = -1,
    legendPos = "UR",
    fixAlphanumericBinLabels = False,
    outFileName = "outFile",
    outFileName_suffix = "",
    ) :
    
    canvas = TCanvas("canvas", "canvas")
    canvas.SetCanvasSize(800, 600)
    
    legend = 0
    
    if(legendPos == "UR") :
        
        legend = TLegend(0.6, 0.6, 0.895, 0.895)
    
    elif(legendPos == "LR") :
        
        legend = TLegend(0.6, 0.105, 0.895, 0.40)
    
    else :
        
        print "Wrong legend position option:", legendPos
        exit(1)
    
    if (legendTextSize > 0) :
        
        legend.SetTextSize(legendTextSize)
    
    stack = THStack()
    
    if (fixAlphanumericBinLabels) :
        
        h1_temp = TH1F("temp", "temp", list_histDetails[0].hist.GetXaxis().GetNbins(), list_histDetails[0].hist.GetXaxis().GetXmin(), list_histDetails[0].hist.GetXaxis().GetXmax())
        stack.Add(h1_temp)
    
    for iHist in range(0, len(list_histDetails)) :
        
        list_histDetails[iHist].hist.SetLineColor(list_histDetails[iHist].lineColor)
        list_histDetails[iHist].hist.SetLineStyle(list_histDetails[iHist].lineStyle)
        list_histDetails[iHist].hist.SetLineWidth(list_histDetails[iHist].lineWidth)
        
        stack.Add(list_histDetails[iHist].hist, list_histDetails[iHist].drawOption)
        legend.AddEntry(list_histDetails[iHist].hist, list_histDetails[iHist].histLabel)
    
    stack.Draw(stackDrawOption)
    
    if (drawLegend) :
        
        legend.Draw()
    
    if (fixAlphanumericBinLabels) :
        
        for iBin in range(0, stack.GetXaxis().GetNbins()) :
            
            stack.GetXaxis().SetBinLabel(iBin, list_histDetails[0].hist.GetXaxis().GetBinLabel(iBin))
        
        stack.GetXaxis().SetLabelSize(0.025)
        stack.GetXaxis().LabelsOption("v")
    
    stack.GetXaxis().SetTitle(xTitle)
    stack.GetXaxis().SetTitleOffset(1.2)
    
    stack.GetYaxis().SetTitle(yTitle)
    stack.GetYaxis().SetTitleOffset(1.3)
    
    stack.SetTitle(title)
    
    # X range
    if (xMin != initVal and xMax != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            xMin,
            xMax
        )
    
    elif (xMin != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            xMin,
            stack.GetXaxis().GetXmax()
        )
    
    elif (xMax != initVal) :
        
        stack.GetXaxis().SetRangeUser(
            stack.GetXaxis().GetXmin(),
            xMax
        )
    
    # Y range
    if (yMin != initVal) :
        
        stack.SetMinimum(yMin)
    
    if (yMax != initVal) :
        
        stack.SetMaximum(yMax)
    
    stack.GetXaxis().CenterTitle(True)
    stack.GetYaxis().CenterTitle(True)
    
    #ROOT.TGaxis.SetMaxDigits(3)
    #stack.GetXaxis().SetMaxDigits(3)
    
    # Axis divisions
    if (abs(sum(nDivisionsX)) > 0) :
        
        stack.GetXaxis().SetNdivisions(nDivisionsX[0], nDivisionsX[1], nDivisionsX[2])
    
    if (abs(sum(nDivisionsY)) > 0) :
        
        stack.GetYaxis().SetNdivisions(nDivisionsY[0], nDivisionsY[1], nDivisionsY[2])
    
    # Bin label position
    if (centerLabelsX) :
        
        stack.GetXaxis().CenterLabels()
    
    if (centerLabelsY) :
        
        stack.GetYaxis().CenterLabels()
    
    canvas.SetLogx(logX)
    canvas.SetLogy(logY)
    
    canvas.SetGridx(gridX)
    canvas.SetGridy(gridY)
    
    #canvas.SetRightMargin(0.13)
    
    outFileName = outFileName + ("_"*(outFileName_suffix != "")) + outFileName_suffix + ".pdf"
    print "Output:", outFileName
    
    canvas.SaveAs(outFileName)
    
    print "\n"


def plot2D(histDetails) :
    
    canvas = TCanvas("canvas", "canvas")
    canvas.SetCanvasSize(800, 800)
    
    # X range
    if (histDetails.xMin != initVal and histDetails.xMax != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.xMin,
            histDetails.xMax
        )
    
    elif (histDetails.xMin != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.xMin,
            histDetails.hist.GetXaxis().GetXmax()
        )
    
    elif (histDetails.xMax != initVal) :
        
        histDetails.hist.GetXaxis().SetRangeUser(
            histDetails.hist.GetXaxis().GetXmin(),
            histDetails.xMax
        )
    
    # Y range
    if (histDetails.yMin != initVal and histDetails.yMax != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.yMin,
            histDetails.yMax
        )
    
    elif (histDetails.yMin != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.yMin,
            histDetails.hist.GetYaxis().GetXmax()
        )
    
    elif (histDetails.yMax != initVal) :
        
        histDetails.hist.GetYaxis().SetRangeUser(
            histDetails.hist.GetYaxis().GetXmin(),
            histDetails.yMax
        )
    
    # Z range
    if (histDetails.zMin != initVal) :
        
        histDetails.hist.SetMinimum(histDetails.zMin)
    
    if (histDetails.zMax != initVal) :
        
        histDetails.hist.SetMaximum(histDetails.zMax)
    
    # Axis divisions
    if (abs(sum(histDetails.nDivisionsX)) > 0) :
        
        histDetails.hist.GetXaxis().SetNdivisions(histDetails.nDivisionsX[0], histDetails.nDivisionsX[1], histDetails.nDivisionsX[2])
    
    if (abs(sum(histDetails.nDivisionsY)) > 0) :
        
        histDetails.hist.GetYaxis().SetNdivisions(histDetails.nDivisionsY[0], histDetails.nDivisionsY[1], histDetails.nDivisionsY[2])
    
    # Bin label position
    if (histDetails.centerLabelsX) :
        
        histDetails.hist.GetXaxis().CenterLabels()
    
    if (histDetails.centerLabelsY) :
        
        histDetails.hist.GetYaxis().CenterLabels()
    
    histDetails.hist.GetXaxis().SetTitle(histDetails.xTitle)
    histDetails.hist.GetXaxis().SetTitleOffset(1.2)
    
    histDetails.hist.GetYaxis().SetTitle(histDetails.yTitle)
    histDetails.hist.GetYaxis().SetTitleOffset(1.15)
    
    histDetails.hist.GetXaxis().CenterTitle(True)
    histDetails.hist.GetYaxis().CenterTitle(True)
    
    #histDetails.hist.SetStats(0)
    histDetails.hist.SetTitle(histDetails.histTitle)
    
    #ROOT.TGaxis.SetMaxDigits(3)
    
    canvas.SetLogx(histDetails.logX)
    canvas.SetLogy(histDetails.logY)
    canvas.SetLogz(histDetails.logZ)
    
    canvas.SetGridx(histDetails.gridX)
    canvas.SetGridy(histDetails.gridY)
    
    canvas.SetRightMargin(0.13)
    
    histDetails.hist.Draw(histDetails.drawOption)
    
    outFileName = histDetails.outFileName + ("_"*(histDetails.outFileName_suffix != "")) + histDetails.outFileName_suffix + ".pdf"
    print "Output:", outFileName
    
    canvas.SaveAs(outFileName)
    
    print "\n"


####################################################################################################
h1_tauh_pT_gen = HistogramDetails()
h1_tauh_pT_gen.rootFileName = inputFile_RelValZpTT_1500_13
h1_tauh_pT_gen.histName = "caloTauAnalysis/tauh_pT_gen"
h1_tauh_pT_gen.drawOption = "hist E"
h1_tauh_pT_gen.lineWidth = 2
h1_tauh_pT_gen.lineColor = 4
h1_tauh_pT_gen.getHist()
h1_tauh_pT_gen.normalize(byBinWidth = True)

plot1D(
    [h1_tauh_pT_gen],
    title = "#tau^{gen}_{h} p_{T}",
    xTitle = "p_{T} [GeV]", yTitle = "a.u.",
    xMin = 0,
    xMax = 1000,
    #yMax = 4,
    logY = True,
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/tauh_pT_gen",
)


####################################################################################################
h1_tauh_eta_gen = HistogramDetails()
h1_tauh_eta_gen.rootFileName = inputFile_RelValZpTT_1500_13
h1_tauh_eta_gen.histName = "caloTauAnalysis/tauh_eta_gen"
h1_tauh_eta_gen.drawOption = "hist E"
h1_tauh_eta_gen.lineWidth = 2
h1_tauh_eta_gen.lineColor = 4
h1_tauh_eta_gen.getHist()
h1_tauh_eta_gen.normalize()

plot1D(
    [h1_tauh_eta_gen],
    title = "#tau^{gen}_{h} #eta",
    xTitle = "#eta", yTitle = "a.u.",
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/tauh_eta_gen",
)


####################################################################################################
h1_tauh_m_gen = HistogramDetails()
h1_tauh_m_gen.rootFileName = inputFile_RelValZpTT_1500_13
h1_tauh_m_gen.histName = "caloTauAnalysis/tauh_m_gen"
h1_tauh_m_gen.drawOption = "hist E"
h1_tauh_m_gen.lineWidth = 2
h1_tauh_m_gen.lineColor = 4
h1_tauh_m_gen.getHist()
h1_tauh_m_gen.normalize()

plot1D(
    [h1_tauh_m_gen],
    title = "#tau^{gen}_{h} m",
    xTitle = "m [GeV]", yTitle = "a.u.",
    xMax = 3,
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/tauh_m_gen",
)


####################################################################################################
h1_tauh_decayMode_gen = HistogramDetails()
h1_tauh_decayMode_gen.rootFileName = inputFile_RelValZpTT_1500_13
h1_tauh_decayMode_gen.histName = "caloTauAnalysis/tauh_decayMode_gen"
h1_tauh_decayMode_gen.drawOption = "hist E"
h1_tauh_decayMode_gen.lineWidth = 2
h1_tauh_decayMode_gen.lineColor = 4
h1_tauh_decayMode_gen.drawOption = "hist E text"
h1_tauh_decayMode_gen.getHist()
h1_tauh_decayMode_gen.normalize()

plot1D(
    [h1_tauh_decayMode_gen],
    title = "#tau^{gen}_{h} DM [5*(n_{h^{#pm}}-1) + n_{#pi^{0}}]",
    xTitle = "Decay mode", yTitle = "a.u.",
    xMax = 15,
    gridX = True,
    gridY = True,
    nDivisionsX = [15, 1, 1],
    centerLabelsX = True,
    drawLegend = False,
    outFileName = "plots/tauh_decayMode_gen",
)


####################################################################################################
h2_tauh_decayMode_vs_m_gen = HistogramDetails()
h2_tauh_decayMode_vs_m_gen.rootFileName = inputFile_RelValZpTT_1500_13
h2_tauh_decayMode_vs_m_gen.histName = "caloTauAnalysis/tauh_decayMode_vs_m_gen"
h2_tauh_decayMode_vs_m_gen.histTitle = "#tau^{gen}_{h} DM [5*(n_{h^{#pm}}-1) + n_{#pi^{0}}] vs. m"
h2_tauh_decayMode_vs_m_gen.outFileName = "plots/tauh_decayMode_vs_m_gen"
h2_tauh_decayMode_vs_m_gen.drawOption = "colz"
h2_tauh_decayMode_vs_m_gen.xMin = 0
h2_tauh_decayMode_vs_m_gen.xMax = 3
h2_tauh_decayMode_vs_m_gen.yMax = 15
h2_tauh_decayMode_vs_m_gen.xTitle = "m [GeV]"
h2_tauh_decayMode_vs_m_gen.yTitle = "Decay mode"
h2_tauh_decayMode_vs_m_gen.gridX = True
h2_tauh_decayMode_vs_m_gen.gridY = True
h2_tauh_decayMode_vs_m_gen.nDivisionsY = [15, 1, 1]
h2_tauh_decayMode_vs_m_gen.centerLabelsY = True
h2_tauh_decayMode_vs_m_gen.getHist()
plot2D(h2_tauh_decayMode_vs_m_gen)


####################################################################################################
h1_caloTau_pT_reco = HistogramDetails()
h1_caloTau_pT_reco.rootFileName = inputFile_RelValZpTT_1500_13
h1_caloTau_pT_reco.histName = "caloTauAnalysis/caloTau_pT_reco"
h1_caloTau_pT_reco.drawOption = "hist E"
h1_caloTau_pT_reco.lineWidth = 2
h1_caloTau_pT_reco.lineColor = 4
h1_caloTau_pT_reco.getHist()
h1_caloTau_pT_reco.normalize(byBinWidth = True)

plot1D(
    [h1_caloTau_pT_reco],
    title = "#tau^{calo}_{h} p_{T}",
    xTitle = "p_{T} [GeV]", yTitle = "a.u.",
    xMin = 0,
    xMax = 1000,
    #yMax = 4,
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/caloTau_pT_reco",
)


####################################################################################################
h1_caloTau_eta_reco = HistogramDetails()
h1_caloTau_eta_reco.rootFileName = inputFile_RelValZpTT_1500_13
h1_caloTau_eta_reco.histName = "caloTauAnalysis/caloTau_eta_reco"
h1_caloTau_eta_reco.drawOption = "hist E"
h1_caloTau_eta_reco.lineWidth = 2
h1_caloTau_eta_reco.lineColor = 4
h1_caloTau_eta_reco.getHist()
h1_caloTau_eta_reco.normalize()

plot1D(
    [h1_caloTau_eta_reco],
    title = "#tau^{calo}_{h} #eta",
    xTitle = "#eta", yTitle = "a.u.",
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/caloTau_eta_reco",
)


####################################################################################################
h1_caloTau_m_reco = HistogramDetails()
h1_caloTau_m_reco.rootFileName = inputFile_RelValZpTT_1500_13
h1_caloTau_m_reco.histName = "caloTauAnalysis/caloTau_m_reco"
h1_caloTau_m_reco.drawOption = "hist E"
h1_caloTau_m_reco.lineWidth = 2
h1_caloTau_m_reco.lineColor = 4
h1_caloTau_m_reco.getHist()
h1_caloTau_m_reco.normalize()

plot1D(
    [h1_caloTau_m_reco],
    title = "#tau^{calo}_{h} m",
    xTitle = "m [GeV]", yTitle = "a.u.",
    xMax = 10,
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/caloTau_m_reco",
)


####################################################################################################
h1_caloTau_nearestGenTauh_deltaR_reco = HistogramDetails()
h1_caloTau_nearestGenTauh_deltaR_reco.rootFileName = inputFile_RelValZpTT_1500_13
h1_caloTau_nearestGenTauh_deltaR_reco.histName = "caloTauAnalysis/caloTau_nearestGenTauh_deltaR_reco"
h1_caloTau_nearestGenTauh_deltaR_reco.drawOption = "hist"
h1_caloTau_nearestGenTauh_deltaR_reco.lineWidth = 2
h1_caloTau_nearestGenTauh_deltaR_reco.lineColor = 4
h1_caloTau_nearestGenTauh_deltaR_reco.getHist()
h1_caloTau_nearestGenTauh_deltaR_reco.normalize()

plot1D(
    [h1_caloTau_nearestGenTauh_deltaR_reco],
    title = "#DeltaR between #tau^{calo}_{h} and its nearest #tau^{gen}_{h}",
    xTitle = "#DeltaR(#tau^{calo}_{h}, #tau^{gen}_{h})", yTitle = "a.u.",
    xMax = 3,
    gridX = True,
    gridY = True,
    logY = True,
    drawLegend = False,
    outFileName = "plots/caloTau_nearestGenTauh_deltaR_reco",
)


####################################################################################################
h1_ak4PFjet_pT_reco = HistogramDetails()
h1_ak4PFjet_pT_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h1_ak4PFjet_pT_reco.histName = "caloTauAnalysis/ak4PFjet_pT_reco"
h1_ak4PFjet_pT_reco.drawOption = "hist E"
h1_ak4PFjet_pT_reco.lineWidth = 2
h1_ak4PFjet_pT_reco.lineColor = 4
h1_ak4PFjet_pT_reco.getHist()
h1_ak4PFjet_pT_reco.normalize(byBinWidth = True)

plot1D(
    [h1_ak4PFjet_pT_reco],
    title = "AK4PF-jet p_{T}",
    xTitle = "p_{T} [GeV]", yTitle = "a.u.",
    xMin = 0,
    xMax = 1000,
    #yMax = 4,
    logY = True,
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/ak4PFjet_pT_reco",
)


####################################################################################################
h1_ak4PFjet_eta_reco = HistogramDetails()
h1_ak4PFjet_eta_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h1_ak4PFjet_eta_reco.histName = "caloTauAnalysis/ak4PFjet_eta_reco"
h1_ak4PFjet_eta_reco.drawOption = "hist E"
h1_ak4PFjet_eta_reco.lineWidth = 2
h1_ak4PFjet_eta_reco.lineColor = 4
h1_ak4PFjet_eta_reco.getHist()
h1_ak4PFjet_eta_reco.normalize()

plot1D(
    [h1_ak4PFjet_eta_reco],
    title = "AK4PF-jet #eta",
    xTitle = "#eta", yTitle = "a.u.",
    gridX = True,
    gridY = True,
    drawLegend = False,
    outFileName = "plots/ak4PFjet_eta_reco",
)


####################################################################################################
h1_caloTau_nearestAK4PFjet_deltaR_reco = HistogramDetails()
h1_caloTau_nearestAK4PFjet_deltaR_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h1_caloTau_nearestAK4PFjet_deltaR_reco.histName = "caloTauAnalysis/caloTau_nearestAK4PFjet_deltaR_reco"
h1_caloTau_nearestAK4PFjet_deltaR_reco.drawOption = "hist"
h1_caloTau_nearestAK4PFjet_deltaR_reco.lineWidth = 2
h1_caloTau_nearestAK4PFjet_deltaR_reco.lineColor = 4
h1_caloTau_nearestAK4PFjet_deltaR_reco.getHist()
h1_caloTau_nearestAK4PFjet_deltaR_reco.normalize()

plot1D(
    [h1_caloTau_nearestAK4PFjet_deltaR_reco],
    title = "#DeltaR between #tau^{calo}_{h} and its nearest AK4PF-jet",
    xTitle = "#DeltaR(#tau^{calo}_{h}, AK4PF-jet)", yTitle = "a.u.",
    xMax = 3,
    gridX = True,
    gridY = True,
    logY = True,
    drawLegend = False,
    outFileName = "plots/caloTau_nearestAK4PFjet_deltaR_reco",
)


####################################################################################################

h1_tauh_pT_gen = HistogramDetails()
h1_tauh_pT_gen.rootFileName = inputFile_RelValZpTT_1500_13
h1_tauh_pT_gen.histName = "caloTauAnalysis/tauh_pT_gen"
h1_tauh_pT_gen.getHist()


####################################################################################################
h1_genTauh_nPV = HistogramDetails()
h1_genTauh_nPV.rootFileName = inputFile_RelValZpTT_1500_13
h1_genTauh_nPV.histName = "caloTauAnalysis/genTauh_pT_vs_nPV"
h1_genTauh_nPV.getHist(projection = "X")
h1_genTauh_nPV.hist.RebinX(5)


####################################################################################################
h2_genTauh_pT_vs_nPV = HistogramDetails()
h2_genTauh_pT_vs_nPV.rootFileName = inputFile_RelValZpTT_1500_13
h2_genTauh_pT_vs_nPV.histName = "caloTauAnalysis/genTauh_pT_vs_nPV"
h2_genTauh_pT_vs_nPV.getHist()
h2_genTauh_pT_vs_nPV.hist.RebinX(5)


####################################################################################################
h1_ak4PFjet_pT_gen = HistogramDetails()
h1_ak4PFjet_pT_gen.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h1_ak4PFjet_pT_gen.histName = "caloTauAnalysis/ak4PFjet_pT_reco"
h1_ak4PFjet_pT_gen.getHist()


####################################################################################################
h1_ak4PFjet_nPV = HistogramDetails()
h1_ak4PFjet_nPV.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h1_ak4PFjet_nPV.histName = "caloTauAnalysis/ak4PFjet_pT_vs_nPV"
h1_ak4PFjet_nPV.getHist(projection = "X")
h1_ak4PFjet_nPV.hist.RebinX(5)


####################################################################################################
h2_ak4PFjet_pT_vs_nPV = HistogramDetails()
h2_ak4PFjet_pT_vs_nPV.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
h2_ak4PFjet_pT_vs_nPV.histName = "caloTauAnalysis/ak4PFjet_pT_vs_nPV"
h2_ak4PFjet_pT_vs_nPV.getHist()
h2_ak4PFjet_pT_vs_nPV.hist.RebinX(5)


for iDisc in range(0, len(l_discriminatorName)) :
    
    ####################################################################################################
    h1_caloTau_genMatched_pT_reco = HistogramDetails()
    h1_caloTau_genMatched_pT_reco.rootFileName = inputFile_RelValZpTT_1500_13
    h1_caloTau_genMatched_pT_reco.histName = "caloTauAnalysis/caloTau_genMatched_%s_pT_reco" %(l_discriminatorName[iDisc])
    h1_caloTau_genMatched_pT_reco.drawOption = "hist E"
    h1_caloTau_genMatched_pT_reco.lineWidth = 2
    h1_caloTau_genMatched_pT_reco.lineColor = 4
    h1_caloTau_genMatched_pT_reco.getHist()
    
    h1_caloTau_genMatched_pT_reco.hist.Divide(h1_tauh_pT_gen.hist)
    
    plot1D(
        [h1_caloTau_genMatched_pT_reco],
        title = "#tau^{calo}_{h} \"%s\" efficiency vs. p^{#tau^{gen}_{h}}_{T}" %(l_discriminatorName[iDisc]),
        xTitle = "p^{#tau^{gen}_{h}}_{T} [GeV]", yTitle = "efficiency",
        xMin = 0,
        xMax = 1000,
        yMax = 1.2,
        gridX = True,
        gridY = True,
        drawLegend = False,
        outFileName = "plots/caloTau_genMatched_%s_efficiency_pT" %(l_discriminatorName[iDisc]),
    )
    
    
    ####################################################################################################
    h1_caloTau_genMatched_nPV_reco = HistogramDetails()
    h1_caloTau_genMatched_nPV_reco.rootFileName = inputFile_RelValZpTT_1500_13
    h1_caloTau_genMatched_nPV_reco.histName = "caloTauAnalysis/caloTau_genMatched_%s_pT_vs_nPV_reco" %(l_discriminatorName[iDisc])
    h1_caloTau_genMatched_nPV_reco.drawOption = "hist E"
    h1_caloTau_genMatched_nPV_reco.lineWidth = 2
    h1_caloTau_genMatched_nPV_reco.lineColor = 4
    h1_caloTau_genMatched_nPV_reco.getHist(projection = "X")
    h1_caloTau_genMatched_nPV_reco.hist.RebinX(5)
    
    h1_caloTau_genMatched_nPV_reco.hist.Divide(h1_genTauh_nPV.hist)
    
    plot1D(
        [h1_caloTau_genMatched_nPV_reco],
        title = "#tau^{calo}_{h} \"%s\" efficiency vs. #PV" %(l_discriminatorName[iDisc]),
        xTitle = "#PV", yTitle = "efficiency",
        xMin = 0,
        xMax = 100,
        yMax = 1.2,
        gridX = True,
        gridY = True,
        drawLegend = False,
        outFileName = "plots/caloTau_genMatched_%s_efficiency_nPV" %(l_discriminatorName[iDisc]),
    )
    
    
    ####################################################################################################
    h2_caloTau_genMatched_pT_vs_nPV_reco = HistogramDetails()
    h2_caloTau_genMatched_pT_vs_nPV_reco.rootFileName = inputFile_RelValZpTT_1500_13
    h2_caloTau_genMatched_pT_vs_nPV_reco.histName = "caloTauAnalysis/caloTau_genMatched_%s_pT_vs_nPV_reco" %(l_discriminatorName[iDisc])
    h2_caloTau_genMatched_pT_vs_nPV_reco.histTitle = "#tau^{calo}_{h} \"%s\" efficiency vs. and p^{#tau^{gen}_{h}}_{T} and #PV" %(l_discriminatorName[iDisc])
    h2_caloTau_genMatched_pT_vs_nPV_reco.outFileName = "plots/caloTau_genMatched_%s_efficiency_pT_vs_nPV" %(l_discriminatorName[iDisc])
    h2_caloTau_genMatched_pT_vs_nPV_reco.drawOption = "colz"
    h2_caloTau_genMatched_pT_vs_nPV_reco.xMax = 100
    h2_caloTau_genMatched_pT_vs_nPV_reco.yMax = 1000
    h2_caloTau_genMatched_pT_vs_nPV_reco.xTitle = "#PV"
    h2_caloTau_genMatched_pT_vs_nPV_reco.yTitle = "p^{#tau^{gen}_{h}}_{T} [GeV]"
    h2_caloTau_genMatched_pT_vs_nPV_reco.gridX = True
    h2_caloTau_genMatched_pT_vs_nPV_reco.gridY = True
    #h2_caloTau_genMatched_pT_vs_nPV_reco.nDivisionsY = [15, 1, 1]
    #h2_caloTau_genMatched_pT_vs_nPV_reco.centerLabelsX = True
    h2_caloTau_genMatched_pT_vs_nPV_reco.getHist()
    h2_caloTau_genMatched_pT_vs_nPV_reco.hist.RebinX(5)
    
    h2_caloTau_genMatched_pT_vs_nPV_reco.hist.Divide(h2_genTauh_pT_vs_nPV.hist)
    
    plot2D(h2_caloTau_genMatched_pT_vs_nPV_reco)
    
    
    ####################################################################################################
    h1_caloTau_genMatched_pTresolution_reco = HistogramDetails()
    h1_caloTau_genMatched_pTresolution_reco.rootFileName = inputFile_RelValZpTT_1500_13
    h1_caloTau_genMatched_pTresolution_reco.histName = "caloTauAnalysis/caloTau_genMatched_%s_pTresolution_reco" %(l_discriminatorName[iDisc])
    h1_caloTau_genMatched_pTresolution_reco.drawOption = "hist E"
    h1_caloTau_genMatched_pTresolution_reco.lineWidth = 2
    h1_caloTau_genMatched_pTresolution_reco.lineColor = 4
    h1_caloTau_genMatched_pTresolution_reco.getHist()
    h1_caloTau_genMatched_pTresolution_reco.normalize()
    
    plot1D(
        [h1_caloTau_genMatched_pTresolution_reco],
        title = "#tau^{calo}_{h} \"%s\" p_{T} resolution [#mu = %0.4f, #sigma = %0.4f]"
            %(l_discriminatorName[iDisc], h1_caloTau_genMatched_pTresolution_reco.hist.GetMean(), h1_caloTau_genMatched_pTresolution_reco.hist.GetStdDev()),
        xTitle = "p^{#tau^{calo}_{h}}_{T} / p^{#tau^{gen}_{h}}_{T}", yTitle = "a.u.",
        xMin = 0,
        xMax = 5,
        yMax = 1,
        gridX = True,
        gridY = True,
        logY = True,
        drawLegend = False,
        outFileName = "plots/caloTau_genMatched_%s_pTresolution_reco" %(l_discriminatorName[iDisc]),
    )
    
    
    ####################################################################################################
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco = HistogramDetails()
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.histName = "caloTauAnalysis/caloTau_genNotMatched_ak4PFjetMatched_%s_pT_reco" %(l_discriminatorName[iDisc])
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.drawOption = "hist E"
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.lineWidth = 2
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.lineColor = 4
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.getHist()
    
    h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco.hist.Divide(h1_ak4PFjet_pT_gen.hist)
    
    plot1D(
        [h1_caloTau_genNotMatched_ak4PFjetMatched_pT_reco],
        title = "AK4PF-jet#rightarrow#tau^{calo}_{h} \"%s\" fake-rate vs. p^{AK4PF-jet}_{T}" %(l_discriminatorName[iDisc]),
        xTitle = "p^{AK4PF-jet}_{T} [GeV]", yTitle = "fake-rate",
        xMin = 0,
        xMax = 1000,
        yMax = 1.2,
        logY = True,
        gridX = True,
        gridY = True,
        drawLegend = False,
        outFileName = "plots/caloTau_genNotMatched_ak4PFjetMatched_%s_efficiency_pT" %(l_discriminatorName[iDisc]),
    )
    
    
    ####################################################################################################
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco = HistogramDetails()
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.histName = "caloTauAnalysis/caloTau_genNotMatched_ak4PFjetMatched_%s_pT_vs_nPV_reco" %(l_discriminatorName[iDisc])
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.drawOption = "hist E"
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.lineWidth = 2
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.lineColor = 4
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.getHist(projection = "X")
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.hist.RebinX(5)
    
    h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco.hist.Divide(h1_ak4PFjet_nPV.hist)
    
    plot1D(
        [h1_caloTau_genNotMatched_ak4PFjetMatched_nPV_reco],
        title = "AK4PF-jet#rightarrow#tau^{calo}_{h} \"%s\" fake-rate vs. #PV" %(l_discriminatorName[iDisc]),
        xTitle = "#PV", yTitle = "fake-rate",
        xMin = 0,
        xMax = 100,
        yMax = 1.2,
        logY = True,
        gridX = True,
        gridY = True,
        drawLegend = False,
        outFileName = "plots/caloTau_genNotMatched_ak4PFjetMatched_%s_efficiency_nPV" %(l_discriminatorName[iDisc]),
    )
    
    
    ####################################################################################################
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco = HistogramDetails()
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.rootFileName = inputFile_RelValQCD_FlatPt_15_3000HS_13
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.histName = "caloTauAnalysis/caloTau_genNotMatched_ak4PFjetMatched_%s_pT_vs_nPV_reco" %(l_discriminatorName[iDisc])
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.histTitle = "AK4PF-jet#rightarrow#tau^{calo}_{h} \"%s\" fake-rate vs. and p^{AK4PF-jet}_{T} and #PV" %(l_discriminatorName[iDisc])
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.outFileName = "plots/caloTau_genNotMatched_ak4PFjetMatched_%s_efficiency_pT_vs_nPV" %(l_discriminatorName[iDisc])
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.drawOption = "colz"
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.xMax = 100
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.yMax = 1000
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.xTitle = "#PV"
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.yTitle = "p^{AK4PF-jet}_{T} [GeV]"
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.gridX = True
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.gridY = True
    #h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.nDivisionsY = [15, 1, 1]
    #h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.centerLabelsX = True
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.getHist()
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.hist.RebinX(5)
    
    h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco.hist.Divide(h2_ak4PFjet_pT_vs_nPV.hist)
    
    plot2D(h2_caloTau_genNotMatched_ak4PFjetMatched_pT_vs_nPV_reco)


for iVar in range(0, len(l_varName_discName)) :
    
    varName = l_varName_discName[iVar][0]
    l_discName = l_varName_discName[iVar][1]
    
    for iDisc in range(0, len(l_discName)) :
        
        ####################################################################################################
        h1_caloTau_genMatched_var_reco = HistogramDetails()
        h1_caloTau_genMatched_var_reco.rootFileName = inputFile_RelValZpTT_1500_13
        h1_caloTau_genMatched_var_reco.histName = "caloTauAnalysis/caloTau_genMatched_%s_%s_reco" %(l_discName[iDisc], varName)
        h1_caloTau_genMatched_var_reco.histLabel = "gen matched"
        h1_caloTau_genMatched_var_reco.drawOption = "hist"
        h1_caloTau_genMatched_var_reco.lineWidth = 2
        h1_caloTau_genMatched_var_reco.lineColor = color_genMatched
        h1_caloTau_genMatched_var_reco.getHist()
        h1_caloTau_genMatched_var_reco.normalize()
        
        h1_caloTau_genNotMatched_var_reco = HistogramDetails()
        h1_caloTau_genNotMatched_var_reco.rootFileName = inputFile_RelValZpTT_1500_13
        h1_caloTau_genNotMatched_var_reco.histName = "caloTauAnalysis/caloTau_genNotMatched_%s_%s_reco" %(l_discName[iDisc], varName)
        h1_caloTau_genNotMatched_var_reco.histLabel = "gen not matched"
        h1_caloTau_genNotMatched_var_reco.drawOption = "hist"
        h1_caloTau_genNotMatched_var_reco.lineWidth = 2
        h1_caloTau_genNotMatched_var_reco.lineColor = color_genNotMatched
        h1_caloTau_genNotMatched_var_reco.getHist()
        h1_caloTau_genNotMatched_var_reco.normalize()
        
        plot1D(
            [h1_caloTau_genMatched_var_reco, h1_caloTau_genNotMatched_var_reco],
            title = "%s [%s]" %(l_varLabel[iVar], l_discName[iDisc]),
            xTitle = "%s" %(l_varLabel[iVar]), yTitle = "a.u.",
            xMax = l_var_xMax[iVar][iDisc],
            gridX = True,
            gridY = True,
            yMax = 1,
            logY = True,
            #drawLegend = False,
            outFileName = "plots/caloTau_%s_%s_reco" %(l_discName[iDisc], varName),
        )
