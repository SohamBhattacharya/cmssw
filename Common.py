import array
import matplotlib
import matplotlib.pyplot
import numpy
import os
import time


import ROOT
from ROOT import TAxis
from ROOT import TCanvas
from ROOT import TF1
from ROOT import TFile
from ROOT import TGraph
from ROOT import TH1F
from ROOT import TH2F
from ROOT import THStack
from ROOT import TLatex
from ROOT import TLegend
from ROOT import TMVA
from ROOT import TStyle

import CMS_lumi
import tdrstyle

initVal = -9999

numberFormat_int = ".0f"
numberFormat_float = ".3f"

someNonExistantString = "someNonExistantString"


class VarInfo :
    
    name = ""
    
    l_discName = []
    
    xMin = 0
    xMax = 0
    nBin = 0
    
    yMin = 0
    yMax = 0
    
    title = ""
    
    xTitle = ""
    yTitle = ""
    
    logY = False
    
    legendPos = "UR"
    
    outFileName = ""
    
    
    def __init__(
        self,
        name = "",
        l_discName = [],
        xMin = 0,
        xMax = 0,
        nBin = 0,
        yMin = 0,
        yMax = 0,
        title = "",
        xTitle = "",
        yTitle = "",
        logY = False,
        legendPos = "UR",
        outFileName = ""
    ) :
        
        self.name = name
        
        self.l_discName = l_discName
        
        self.xMin = xMin
        self.xMax = xMax
        self.nBin = nBin
        
        self.yMin = yMin
        self.yMax = yMax
        
        self.title = title
        
        self.xTitle = xTitle
        self.yTitle = yTitle
        
        self.logY = logY
        
        self.legendPos = legendPos
        
        self.outFileName = outFileName



def getFormulaStr(
    func,
    formulaStr = "",
    precision_val = 4,
    precision_err = 4,
    relativeError = False
    ) :
    
    if (formulaStr == "") :
        
        formulaStr = str(func.GetExpFormula())
    
    print formulaStr
    
    nPar = func.GetNpar()
    
    for iPar in range(0, nPar) :
        
        parName = func.GetParName(iPar)
        parValue = func.GetParameter(iPar)
        parError = func.GetParError(iPar)
        
        relErrorStr = ""
        
        if (relativeError) :
            
            parError = abs(parError / parValue * 100.0)
            
            relErrorStr = "%"
        
        # Note: %+d prints the sign explicitly
        
        # If there is a plus sign, consider that
        strToReplace = "+[%s]" %(parName)
        newStr = "%+0.*f [%0.*f%s]" %(precision_val, parValue, precision_err, parError, relErrorStr)
        formulaStr = formulaStr.replace(strToReplace, newStr)
        
        # If there is a minus sign, consider that
        strToReplace = "-[%s]" %(parName)
        newStr = "%+0.*f [%0.*f%s]" %(precision_val, parValue, precision_err, parError, relErrorStr)
        formulaStr = formulaStr.replace(strToReplace, newStr)
        
        # If there is no sign before the parameter
        strToReplace = "[%s]" %(parName)
        newStr = "%0.*f [%0.*f%s]" %(precision_val, parValue, precision_err, parError, relErrorStr)
        formulaStr = formulaStr.replace(strToReplace, newStr)
    
    return formulaStr


class HistogramDetails :
    
    rootFileName = ""
    rootFile = 0
    
    treeName = ""
    
    histName = ""
    histTitle = ""
    histLabel = ""
    
    lineColor = 4
    lineStyle = 1
    lineWidth = 1
    
    markerStyle = 20
    markerColor = 4
    markerSize = -1
    
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
    drawFunctions = True
    
    addToLegend = True
    
    outFileName = ""
    outFileName_suffix = ""
    
    
    def __init__(
        self,
        rootFileName = "",
        treeName = "",
        histName = "",
        hist = 0,
        ) :
        
        self.rootFileName = rootFileName
        
        self.treeName = treeName
        
        self.histName = histName
        
        self.hist = hist
    
    
    #def getHistFromTree(
    #    plotStr = "",
    #    cutStr = ""
    #    ) :
    #    
    #    self.rootFile = TFile(self.rootFileName)
    #    
    #    tree = self.rootFile.Get(treeName)
    #    
    #    plotStr = "%s >> %s" %(hist)
    #    
    #    tree.Draw()
    
    
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
    
    
    def normalize(self, byBinWidth = False, byBinArea = False) :
        
        integral = self.hist.Integral()
        
        self.hist.Scale(1.0 / integral)
        
        if (byBinWidth) :
            
            for iBinX in range(0, self.hist.GetNbinsX()) :
                
                binWidth = self.hist.GetXaxis().GetBinWidth(iBinX+1)
                binContent = self.hist.GetBinContent(iBinX+1)
                binError = self.hist.GetBinError(iBinX+1)
                
                #print binWidth, binContent
                
                scale = 1.0 / binWidth
                
                self.hist.SetBinContent(iBinX+1, binContent*scale)
                self.hist.SetBinError(iBinX+1, binError*scale)
        
        if (byBinArea) :
            
            for iBinX in range(0, self.hist.GetNbinsX()) :
                
                for iBinY in range(0, self.hist.GetNbinsY()) :
                    
                    binArea = self.hist.GetXaxis().GetBinArea(iBinX+1)*self.hist.GetYaxis().GetBinArea(iBinY+1)
                    binContent = self.hist.GetBinContent(iBinX+1, iBixY+1)
                    binError = self.hist.GetBinError(iBinX+1, iBinY+1)
                    
                    #print binArea, binContent
                    
                    scale = 1.0 / binArea
                    
                    self.hist.SetBinContent(iBinX+1, iBinY+1, binContent*scale)
                    self.hist.SetBinError(iBinX+1, iBinY+1, binError*scale)


def plot1D(list_histDetails,
    stackDrawOption = "nostack",
    title = "",
    xTitle = "", yTitle = "",
    xMin = initVal, xMax = initVal,
    yMin = initVal, yMax = initVal,
    logX = False, logY = False,
    gridX = False, gridY = False,
    nDivisionsX = [0, 0, 0], nDivisionsY = [0, 0, 0],
    xTitleSizeScale = 1.0, yTitleSizeScale = 1.0,
    xTitleOffset = 1.0, yTitleOffset = 1.0,
    xLabelSizeScale = 1.0, yLabelSizeScale = 1.0,
    centerLabelsX = False, centerLabelsY = False,
    drawLegend = True,
    legendDrawOption = "",
    legendNcol = 1,
    legendWidthScale = 1,
    legendHeightScale = 1,
    transparentLegend = False,
    legendTextSize = -1,
    legendBorderSize = 1,
    legendPos = "UR",
    legendTitle = "",
    l_extraText = [], #[[x, y, text], ...]
    CMSextraText = "",
    sampleText = "",
    fixAlphanumericBinLabels = False,
    outFileName = "outFile",
    outFileName_suffix = "",
    ) :
    
    tdrstyle.setTDRStyle()
    
    ROOT.gStyle.SetOptStat(0)
    ROOT.gStyle.SetOptFit(0)
    
    canvas = TCanvas("canvas", "canvas")
    
    canvas.cd(1).SetRightMargin(0.05)
    
    legend = 0
    
    legendHeight = legendHeightScale * 0.375
    legendWidth = legendWidthScale * 0.425
    
    if(legendPos == "UR") :
        
        legend = TLegend(0.925-legendWidth, 0.925-legendHeight, 0.925, 0.925)
    
    elif(legendPos == "LR") :
        
        legend = TLegend(0.925-legendWidth, 0.15, 0.925, 0.15+legendHeight)
    
    elif(legendPos == "UL") :
        
        legend = TLegend(0.185, 0.925-legendHeight, 0.15+legendWidth, 0.925)
    
    else :
        
        print "Wrong legend position option:", legendPos
        exit(1)
    
    legend.SetNColumns(legendNcol)
    
    if (legendTextSize > 0) :
        
        legend.SetTextSize(legendTextSize)
    
    if (transparentLegend) :
        
        legend.SetFillStyle(0)
    
    if (legendBorderSize >= 0) :
        
        legend.SetBorderSize(legendBorderSize)
    
    
    ROOT.SetOwnership(legend, 0)
    
    if (len(legendTitle)) :
        
        legend.SetHeader(legendTitle)
        legendHeader = legend.GetListOfPrimitives().First()
        legendHeader.SetTextAlign(23)
        
        # For whatever reason, SetHeader("Header", "C") does not accept the second argument in python
        # So, center the header this way
        # EVEN THIS DOESN'T WORK! Gives a seg-fault when calling the plot1D(...) function for the second time
        #legend.GetListOfPrimitives().First().SetTextAlign(22)
    
    #legend.SetLegendBorderMode(0)
    
    stack = THStack()
    
    if (fixAlphanumericBinLabels) :
        
        h1_temp = TH1F("temp", "temp", list_histDetails[0].hist.GetXaxis().GetNbins(), list_histDetails[0].hist.GetXaxis().GetXmin(), list_histDetails[0].hist.GetXaxis().GetXmax())
        stack.Add(h1_temp)
    
    for iHist in range(0, len(list_histDetails)) :
        
        list_histDetails[iHist].hist.SetLineColor(list_histDetails[iHist].lineColor)
        list_histDetails[iHist].hist.SetLineStyle(list_histDetails[iHist].lineStyle)
        list_histDetails[iHist].hist.SetLineWidth(list_histDetails[iHist].lineWidth)
        
        list_histDetails[iHist].hist.SetMarkerStyle(list_histDetails[iHist].markerStyle)
        list_histDetails[iHist].hist.SetMarkerColor(list_histDetails[iHist].markerColor)
        
        if (list_histDetails[iHist].markerSize >= 0) :
            
            list_histDetails[iHist].hist.SetMarkerSize(list_histDetails[iHist].markerSize)
        
        if (list_histDetails[iHist].drawOption == "hist") :
            
            list_histDetails[iHist].hist.SetMarkerSize(0)
        
        stack.Add(list_histDetails[iHist].hist, list_histDetails[iHist].drawOption)
        
        if (list_histDetails[iHist].addToLegend) :
            
            if (len(legendDrawOption)) :
                
                legend.AddEntry(list_histDetails[iHist].hist, list_histDetails[iHist].histLabel, legendDrawOption)
            
            else :
                
                legend.AddEntry(list_histDetails[iHist].hist, list_histDetails[iHist].histLabel)
    
    stack.Draw(stackDrawOption)
    
    # Draw the associated (fit) functions
    for iHist in range(0, len(list_histDetails)) :
        
        if (list_histDetails[iHist].drawFunctions) :
            
            funcList = list_histDetails[iHist].hist.GetListOfFunctions()
            
            if (not funcList.GetSize()) :
                
                continue
            
            for iFunc in range(0, funcList.GetEntries()) :
                
                f1_temp = funcList.At(iFunc)
                
                # For some reason the list also contains the stat box at times
                if (type(f1_temp) is ROOT.TF1) :
                    
                    f1_temp.GetHistogram().SetStats(0)
                    f1_temp.Draw("L same")
    
    if (drawLegend) :
        
        legend.Draw()
    
    if (fixAlphanumericBinLabels) :
        
        for iBin in range(0, stack.GetXaxis().GetNbins()) :
            
            stack.GetXaxis().SetBinLabel(iBin, list_histDetails[0].hist.GetXaxis().GetBinLabel(iBin))
        
        #stack.GetXaxis().SetLabelSize(0.025)
        stack.GetXaxis().LabelsOption("v")
    
    stack.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * xLabelSizeScale)
    stack.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * yLabelSizeScale)
    
    stack.GetXaxis().SetTitle(xTitle)
    stack.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * xTitleSizeScale)
    
    if (xTitleOffset != 1) :
        
        stack.GetXaxis().SetTitleOffset(xTitleOffset)
    
    stack.GetYaxis().SetTitle(yTitle)
    stack.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * yTitleSizeScale)
    #stack.GetYaxis().SetTitleOffset(1 + 3*(1-yTitleSizeScale))
    
    if (yTitleOffset != 1) :
        
        stack.GetYaxis().SetTitleOffset(yTitleOffset)
    
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
        
    else :
        
        stack.GetXaxis().SetNdivisions(5, 5, 0)
    
    if (abs(sum(nDivisionsY)) > 0) :
        
        stack.GetYaxis().SetNdivisions(nDivisionsY[0], nDivisionsY[1], nDivisionsY[2])
    
    #else :
    #    
    #    stack.GetYaxis().SetNdivisions(5, 5, 0)
    
    # Bin label position
    if (centerLabelsX) :
        
        stack.GetXaxis().CenterLabels()
    
    if (centerLabelsY) :
        
        stack.GetYaxis().CenterLabels()
    
    # CMS label
    CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = CMSextraText)
    
    canvas.SetLogx(logX)
    canvas.SetLogy(logY)
    
    canvas.SetGridx(gridX)
    canvas.SetGridy(gridY)
    
    
    # Extra text
    for iText in range(0, len(l_extraText)) :
        
        textX = l_extraText[iText][0]
        textY = l_extraText[iText][1]
        text = l_extraText[iText][2]
        
        if (len(text)) :
            
            latex = ROOT.TLatex()
            #latex.SetTextFont(62);
            latex.SetTextSize(0.045);
            latex.SetTextAlign(13);
            
            latex.DrawLatex(textX, textY, text)
    
    
    #canvas.SetRightMargin(0.13)
    
    outFileName = outFileName + ("_"*(outFileName_suffix != "")) + outFileName_suffix + ".pdf"
    print "Output:", outFileName
    
    canvas.SaveAs(outFileName)
    canvas.SaveAs(outFileName.replace(".pdf", ".png"))
    
    print "\n"


def plot2D(histDetails) :
    
    canvas = TCanvas("canvas", "canvas")
    canvas.SetCanvasSize(800, 600)
    
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


def findAllInStr(mainStr, findStr, offset = 0) :
    
    strLen = len(findStr)
    
    l_pos = []
    
    pos = mainStr.find(findStr)
    #print pos
    
    if (pos >= 0) :
        
        l_pos = [pos+offset]
        
        l_pos.extend(
            findAllInStr(mainStr[pos+strLen:], findStr, pos+strLen+offset)
        )
    
    return l_pos


def getIterStr(baseStr, iIter) :
    
    baseStr_mod = baseStr
    
    l_replaceStr_start = findAllInStr(baseStr, "{{")
    l_replaceStr_end = findAllInStr(baseStr, "}}")
    
    if (len(l_replaceStr_start) != len(l_replaceStr_end)) :
        
        print "Error in Common.iterateAndDraw(...): \"{{/}}\" not matched properly in weight string."
        exit(1)
    
    l_replaceStr_start = [ele+2 for ele in l_replaceStr_start]
    
    #print iIter, baseStr_mod
    #print iIter, l_replaceStr_start
    #print iIter, l_replaceStr_end
    
    for iReplace in range(0, len(l_replaceStr_start)) :
        
        replaceStr = baseStr[l_replaceStr_start[iReplace]: l_replaceStr_end[iReplace]]
        
        baseStr_replace = "{{%s}}" %(replaceStr)
        baseStr_replaceWith = "%s[%d]" %(replaceStr, iIter)
        
        print baseStr_replace, baseStr_replaceWith
        
        baseStr_mod = baseStr_mod.replace(baseStr_replace, baseStr_replaceWith)
    
    
    return baseStr_mod


def iterateAndDraw(tree, plotStr, weightStr, histName) :
    
    print "%s Entering iterateAndDraw(...) %s" %("*"*10, "*"*10)
    
    
    #histName = hist.GetName()
    
    # If the string has {{iterVarName[nIter]}}
    # Then have to iterate over iterVarName[0], ... iterVarName[nIter-1]
    iterVarName = plotStr[plotStr.find("{{")+2: plotStr.find("}}")]
    nIter = int(iterVarName[iterVarName.find("[")+1: iterVarName.find("]")])
    iterVarName = iterVarName[0: iterVarName.find("[")]
    
    #print iterVarName
    
    for iIter in range(0, nIter) :
        
        iterVarStr = "%s[%d]" %(iterVarName, iIter)
        
        plotStr_mod = plotStr
        weightStr_mod = weightStr
        
        
        # Replace in plotStr
        plotStr_replace = "{{%s[%d]}}" %(iterVarName, nIter)
        plotStr_mod = plotStr_mod.replace(plotStr_replace, iterVarStr)
        plotStr_mod = getIterStr(plotStr_mod, iIter)
        
        
        # Replace in weightStr
        weightStr_mod = getIterStr(weightStr_mod, iIter)
        
        #l_replaceStr_start = findAllInStr(weightStr, "{{")
        #l_replaceStr_end = findAllInStr(weightStr, "}}")
        #
        #if (len(l_replaceStr_start) != len(l_replaceStr_end)) :
        #    
        #    print "Error in Common.iterateAndDraw(...): \"{{/}}\" not matched properly in weight string."
        #    exit(1)
        #
        #l_replaceStr_start = [ele+2 for ele in l_replaceStr_start]
        #
        ##print iIter, weightStr_mod
        ##print iIter, l_replaceStr_start
        ##print iIter, l_replaceStr_end
        #
        #for iReplace in range(0, len(l_replaceStr_start)) :
        #    
        #    replaceStr = weightStr[l_replaceStr_start[iReplace]: l_replaceStr_end[iReplace]]
        #    
        #    weightStr_replace = "{{%s}}" %(replaceStr)
        #    weightStr_replaceWith = "%s[%d]" %(replaceStr, iIter)
        #    
        #    print weightStr_replace, weightStr_replaceWith
        #    
        #    weightStr_mod = weightStr_mod.replace(weightStr_replace, weightStr_replaceWith)
        #    
        #    #print weightStr
        #    #print weightStr_mod
        #
        
        # From the 2nd iterattion onward, prepend "+" to the histName in order to add to the existing histogram
        plotStr_mod = "%s >> %s%s" %(plotStr_mod, "+"*(iIter > 0), histName)
        
        #print "%d: %s" %(iIter, plotStr_mod)
        #print "%d: %s" %(iIter, weightStr_mod)
        
        print plotStr_mod
        print weightStr_mod
        print "Drawn entries", tree.Draw(plotStr_mod, weightStr_mod, "hist")
    
    
    print "%s Exiting iterateAndDraw(...) %s" %("*" * 10, "*" * 10)


def TGraphToTH1(graph) :
    
    hist = graph.GetHistogram().Clone()
    hist.SetDirectory(0)
    
    nPoint = graph.GetN()
    
    for iPoint in range(0, nPoint) :
        
        pointValX = ROOT.Double(0)
        pointValY = ROOT.Double(0)
        
        graph.GetPoint(iPoint, pointValX, pointValY)
        
        pointErrX = graph.GetErrorX(iPoint)
        pointErrY = graph.GetErrorY(iPoint)
        
        binNum = hist.FindBin(pointValX)
        
        hist.SetBinContent(binNum, pointValY)
        hist.SetBinError(binNum, pointErrY)
    
    return hist


def openTChain(listFileName, chain, nFileMax = -1) :
    
    l_fileName = numpy.loadtxt(listFileName, dtype = str, delimiter = someNonExistantString)
    
    nFile = 0
    
    for iFile, fileName in enumerate(l_fileName) :
        
        fileName_mod = fileName
        
        if(fileName_mod.find("/eos/cms") == 0) :
            
            fileName_mod = "root://eoscms.cern.ch/%s" %(fileName_mod)
        
        
        print "Checking file: %s" %(fileName_mod)
        inFile = ROOT.TFile.Open(fileName_mod)
        
        if(inFile and not inFile.IsZombie()) :
            
            print "Adding to chain..."
            
            chain.Add(fileName_mod)
            
            inFile.Close()
            
            nFile += 1
        
        
        if(nFileMax > 0 and nFile >= nFileMax) :
            
            break
        
    
