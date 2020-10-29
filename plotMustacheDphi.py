import numpy
import os
import time

import ROOT

import CMS_lumi
import tdrstyle

import Common
import Details


ROOT.gROOT.ProcessLine(".L EDAnalyzers/TreeMaker/interface/CustomRootDict.cc+")


def getDphiExponential(seedEta) :
    
    yoffsetEB = 7.151e-02
    scaleEB = 5.656e-01
    xoffsetEB = 2.931e-01
    widthEB = 2.976e-01
    
    yoffsetEE_0 = 5.058e-02
    scaleEE_0 = 7.131e-01
    xoffsetEE_0 = 1.668e-02
    widthEE_0 = 4.114e-01
    
    yoffsetEE_1 = -9.913e-02
    scaleEE_1 = 4.404e+01
    xoffsetEE_1 = -5.326e+00
    widthEE_1 = 1.184e+00
    
    yoffsetEE_2 = -6.346e-01
    scaleEE_2 = 1.317e+01
    xoffsetEE_2 = -7.037e+00
    widthEE_2 = 2.836e+00
    
    absSeedEta = abs(seedEta)
    etaBin = ((int)(absSeedEta >= 1.479) + (int)(absSeedEta >= 1.75) + (int)(absSeedEta >= 2.0))
    #logClustEt = numpy.log10(ClustET)
    #const double clusDphi = std::abs(TVector2::Phi_mpi_pi(seedPhi - ClusPhi))
    
    yoffset = 0
    scale = 0
    xoffset = 0
    width = 0
    saturation = 0
    cutoff = 0
    maxdphi = 0
    
    if (etaBin == 0) :  # EB
        
        yoffset = yoffsetEB
        scale = scaleEB
        xoffset = xoffsetEB
        width = 1.0 / widthEB
        saturation = 0.14
        cutoff = 0.60
    
    elif (etaBin == 1) :  # 1.479 -> 1.75
        
        yoffset = yoffsetEE_0
        scale = scaleEE_0
        xoffset = xoffsetEE_0
        width = 1.0 / widthEE_0
        saturation = 0.14
        cutoff = 0.55
    
    elif (etaBin == 2) :  # 1.75 -> 2.0
        
        yoffset = yoffsetEE_1
        scale = scaleEE_1
        xoffset = xoffsetEE_1
        width = 1.0 / widthEE_1
        saturation = 0.12
        cutoff = 0.45
    
    elif (etaBin == 3) :  # 2.0 and up
        
        yoffset = yoffsetEE_2
        scale = scaleEE_2
        xoffset = xoffsetEE_2
        width = 1.0 / widthEE_2
        saturation = 0.12
        cutoff = 0.30
    
    else :
        
        print "Invalid eta bin."
        exit(1)
    
    #width *= 1.02
    
    #saturation = 0.01
    
    #maxdphi = yoffset + scale / (1 + std::exp((logClustEt - xoffset) * width))
    #maxdphi = std::min(maxdphi, cutoff)
    #maxdphi = std::max(maxdphi, saturation)
    
    maxdphi_str = "max(min(%f + %f / (1 + exp((x - %f) * %f)), %f), %f)" %(yoffset, scale, xoffset, width, cutoff, saturation)
    
    #return clusDphi < maxdphi
    
    f1_maxdphi = ROOT.TF1("f1_maxdphi", maxdphi_str, -10.0, 100.0)
    
    return f1_maxdphi


l_varName = [
    "gsfEleFromTICL_E",
    "gsfEleFromTICL_pT",
    "gsfEleFromTICL_eta",
    
    "gsfEleFromTICL_R2p8",
    
    "gsfEleFromTICL_superClus_nClus",
    
    "gsfEleFromTICL_superClusSeed_eta",
    "gsfEleFromTICL_superClusSeed_ET",
    "gsfEleFromTICL_superClusSeed_E",
    
    "gsfEleFromTICL_superClus_TICLclus_ET",
    "gsfEleFromTICL_superClus_TICLclus_E",
    
    "gsfEleFromTICL_superClusSeed_TICLclus_dEta",
    "gsfEleFromTICL_superClusSeed_TICLclus_dPhi",
]


#inputFile = ROOT.TFile.Open("ntupleTree_modTICLele.root")
#inputFile = ROOT.TFile.Open("ntupleTree_rerunTICL_modTICLeleWithRerunTICL_with-TICLFragmentationFix.root")
inputFile = ROOT.TFile.Open("/media/soham/E/HGCal_ele-reco/data_felice/ntupleTree_rerunTICL_modTICLeleWithRerunTICL_with-TICLFragmentationFix.root")
#inputFile = ROOT.TFile.Open("ntupleTree_rerunTICL_modTICLeleWithRerunTICL_11_0_0_pre11.root")

tree = inputFile.Get("treeMaker/tree")


nObj = 2
objName_x = "gsfEleFromTICL_superClus_TICLclus_ET"
objName_y = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi"

plotStr_x = "numpy.log10(gsfEleFromTICL_superClus_TICLclus_ET)"
plotStr_y = "abs(gsfEleFromTICL_superClusSeed_TICLclus_dPhi)"

cutStr = "1"
#cutStr = "gsfEleFromTICL_superClus_TICLclus_ET"
#cutStr = "gsfEleFromTICL_pT < 20"
#cutStr = "gsfEleFromTICL_R2p8 < 0.8 and gsfEleFromTICL_pT < 20"
#cutStr = "gsfEleFromTICL_R2p8 < 0.9"
#cutStr = "gsfEleFromTICL_R2p8 > 0.95"
#cutStr = "gsfEleFromTICL_superClus_TICLclus_ET > 0.5"
#cutStr = "abs(gsfEleFromTICL_superClusSeed_TICLclus_dEta) > 1e-3 and abs(gsfEleFromTICL_superClusSeed_TICLclus_dPhi) > 1e-3"
#cutStr = "abs(gsfEleFromTICL_eta) > 2"
#cutStr = "gsfEleFromTICL_superClus_TICLclus_ET/gsfEleFromTICL_pT > 0.2"
#cutStr = "gsfEleFromTICL_superClusSeed_E/gsfEleFromTICL_E < 0.8"
#cutStr = "gsfEleFromTICL_superClus_TICLclus_E/gsfEleFromTICL_superClusSeed_E > 0.1"
#cutStr = "gsfEleFromTICL_superClus_TICLclus_E/gsfEleFromTICL_superClusSeed_E > 0.03"


#etaStr = "-numpy.log(numpy.tan(0.5*numpy.arcsin(gsfEleFromTICL_superClusSeed_ET/gsfEleFromTICL_superClusSeed_E)))"
#etaStr = "gsfEleFromTICL_superClusSeed_eta"

#l_param_idx = 0
#cutStr = "1.479 < abs(gsfEleFromTICL_superClusSeed_eta) < 1.75"
##cutStr = "1.479 < abs(%s) < 1.75" %(etaStr)
#outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi_vs_ET_eta-1p479-1p75"

#l_param_idx = 1
#cutStr = "1.75 < abs(gsfEleFromTICL_superClusSeed_eta) < 2.0"
##cutStr = "1.75 < abs(%s) < 2.0" %(etaStr)
#outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi_vs_ET_eta-1p75-2p0"

l_param_idx = 2
cutStr = "2.0 < abs(gsfEleFromTICL_superClusSeed_eta)"
#cutStr = "2.0 < abs(%s)" %(etaStr)
outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi_vs_ET_eta-gt2p0"


extraTextX = -0.2
extraTextY = +0.8
extraText = ""

#extraText = "R2.8 < 0.9"
#extraText = "R2.8 > 0.95"


plotDir = "plots/mustache-dPhi_with-TICLfragmentationFix"

os.system("mkdir -p %s" %(plotDir))


#outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi_vs_ET"

nEvent = tree.GetEntries()


h2_temp = ROOT.TH2F(
    "h2_temp", "h2_temp",
    200, -1.0, 3.0,
    200, 0.0, 1.0,
)
h2_temp.Sumw2()


for iEvent in range(0, nEvent) :
    
    tree.GetEntry(iEvent)
    
    d_varInfo = {}
    
    for iVar in range(0, len(l_varName)) :
        
        varName = l_varName[iVar]
        varData = getattr(tree, varName)
        
        d_varInfo[varName] = varData
    
    plotData_x = getattr(tree, objName_x)
    plotData_y = getattr(tree, objName_y)
    
    nObj_mod = min(nObj, plotData_x.size())
    #print nObj_mod
    
    for iObj in range(0, nObj_mod) :
        
        nElement = plotData_x.at(iObj).size()
        #print nElement
        
        for iElement in range(0, nElement) :
            
            plotStr_x_mod = plotStr_x
            plotStr_y_mod = plotStr_y
            
            cutStr_mod = cutStr
            
            for iVar in range(0, len(l_varName)) :
                
                varName = l_varName[iVar]
                
                varData = d_varInfo[varName]
                
                type_str = str(type(varData))
                
                if(len(Common.findAllInStr(type_str, "vector")) == 1) :
                    
                    varVal = varData.at(iObj)
                    
                    cutStr_mod = cutStr_mod.replace(varName, str(float(varVal)))
                    
                    plotStr_x_mod = plotStr_x_mod.replace(varName, str(float(varVal)))
                    plotStr_y_mod = plotStr_y_mod.replace(varName, str(float(varVal)))
                
                elif(len(Common.findAllInStr(type_str, "vector")) == 2) :
                    
                    varVal = varData.at(iObj).at(iElement)
                    
                    cutStr_mod = cutStr_mod.replace(varName, str(float(varVal)))
                
                else :
                    
                    print "Error: Unknown type"
                    exit(1)
            
            if (not eval(cutStr_mod)) :
                
                #print "xxx"
                continue
            
            x = plotData_x.at(iObj).at(iElement)
            y = plotData_y.at(iObj).at(iElement)
            
            x = eval(plotStr_x_mod.replace(objName_x, str(x)))
            y = eval(plotStr_y_mod.replace(objName_y, str(y)))
            
            weight = eval(cutStr_mod)
            
            h2_temp.Fill(x, y, weight)
            


envelopePercent = 99
gr_envelope = ROOT.TGraph(h2_temp.GetNbinsX())


for iBinX in range(1, h2_temp.GetNbinsX()+1) :
    
    iBinX_integral = h2_temp.Integral(iBinX, iBinX, 1, h2_temp.GetNbinsY()+1)
    
    #envelope_binY = h2_temp.GetYaxis().FindBin(envelopeFraction * iBinX_integral)
    envelope_binY = 0
    
    sum_temp = 0
    
    for iBinY in range(1, h2_temp.GetNbinsY()) :
        
        binContent = h2_temp.GetBinContent(iBinX, iBinY)
        
        sum_temp += binContent
        
        if (sum_temp >= float(envelopePercent)/100.0*iBinX_integral) :
            
            envelope_binY = iBinY
            break
    
    
    #envelope_x = h2_temp.GetXaxis().GetBinUpEdge(iBinX)
    envelope_x = h2_temp.GetXaxis().GetBinCenter(iBinX)
    envelope_y = h2_temp.GetYaxis().GetBinCenter(envelope_binY)
    
    gr_envelope.SetPoint(iBinX-1, envelope_x, envelope_y)
    
    #print iBinX-1, envelope_x, envelope_y, iBinX_integral
    
    #for iBinY in range(1, h2_temp.GetNbinsY()) :
    #    
    #    binContent = h2_temp.GetBinContent(iBinX, iBinY)
    #    
    #    if (iBinX_integral) :
    #        
    #        binContent /= float(iBinX_integral)
    #    
    #    h2_temp.SetBinContent(iBinX, iBinY, binContent)


#fitFuncStr = "max(min([0] + [1] / (1 + exp((x - [2]) * [3])), [4]), [5])"
fitFuncStr = "[0] + [1] / (1 + exp((x - [2]) * [3]))"

fitFuncLatex = "#{}{[0]} + #frac{#{}{[1]}}{1 + exp[#{}{[3]}(x - #{}{[2]})]}"

fitFuncLatex_mod = fitFuncLatex

fitLwr = -0.3
fitUpr = +1.5

f1_fitFunc = ROOT.TF1("f1_fitFunc", fitFuncStr, fitLwr, fitUpr)

f1_fitFunc.SetParName(0, "yoffset"   )
f1_fitFunc.SetParName(1, "scale"     )
f1_fitFunc.SetParName(2, "xoffset"   )
f1_fitFunc.SetParName(3, "width"     )
#f1_fitFunc.SetParName(4, "cutoff"    )
#f1_fitFunc.SetParName(5, "saturation")

statusStr = ""
NDF = 0
chiSqPerNDF = 10
fitIter = 0

while ((statusStr not in ["CONVERGED", "OK", "SUCCESSFUL"] or chiSqPerNDF > 1) and fitIter < 5) :
    
    fitResult = gr_envelope.Fit(f1_fitFunc, "RBSEM", "", fitLwr, fitUpr)
    
    statusStr = ROOT.gMinuit.fCstatu
    statusStr = statusStr.strip()
    
    chiSq = f1_fitFunc.GetChisquare()
    NDF = f1_fitFunc.GetNDF()
    
    if (NDF) :
        
        chiSqPerNDF = chiSq / NDF
    
    print "Chi^2:", chiSq
    print "NDF:", NDF
    print "Chi^2 / NDF:", chiSqPerNDF
    
    yoffset    = f1_fitFunc.GetParameter("yoffset"   )
    scale      = f1_fitFunc.GetParameter("scale"     )
    xoffset    = f1_fitFunc.GetParameter("xoffset"   )
    width      = f1_fitFunc.GetParameter("width"     )
    #cutoff     = f1_fitFunc.GetParameter("cutoff"    )
    #saturation = f1_fitFunc.GetParameter("saturation")
    
    #stochTermErr = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("stoch"))
    #noiseTermErr = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("noise"))
    #constTermErr = f1_fitFunc.GetParError(f1_fitFunc.GetParNumber("const"))
    
    
    for iPar in range(0, f1_fitFunc.GetNpar()) :
        
        fitFuncLatex_mod = fitFuncLatex_mod.replace("[%d]" %(iPar), "%0.4g" %(f1_fitFunc.GetParameter(iPar)))
    
    
    fitIter += 1

#fitFuncLatex_mod = fitFuncLatex_mod.replace("- -", "+")


gr_envelope.SetMarkerStyle(24)
gr_envelope.SetMarkerSize(1)
gr_envelope.SetMarkerColor(6)
gr_envelope.SetLineColor(6)
gr_envelope.SetLineWidth(2)
gr_envelope.GetListOfFunctions().FindObject("f1_fitFunc").SetLineColor(6)
gr_envelope.GetListOfFunctions().FindObject("f1_fitFunc").SetLineWidth(2)


#h2_temp.Draw("colz")
#time.sleep(100000)



########## Plot ##########


tdrstyle.setTDRStyle()

ROOT.gStyle.SetOptFit(0)

canvas = ROOT.TCanvas("canvas", "canvas")

canvas.SetCanvasSize(800, 600)
canvas.SetLeftMargin(0.8 * canvas.GetLeftMargin())
canvas.SetRightMargin(10 * canvas.GetRightMargin())#0.19)

legend = ROOT.TLegend(0.3, 0.55, 0.75, 0.95)
#legend.SetTextSize(legendTextSize)
legend.SetFillStyle(0)
legend.SetBorderSize(0)

h2_temp.Scale(1.0 / h2_temp.Integral())

#tree.Draw(plotStr, weightStr, plotQuantity.plotStyle)
#
#if (plotQuantity.normalize) :
#    
#    h2_temp.Scale(1.0 / h2_temp.Integral())
#
#h2_temp.Scale(plotQuantity.scale)
##print h2_temp.Integral()

h2_temp.Draw("colz")

#h2_temp.GetXaxis().SetRangeUser(plotQuantity.xMin, plotQuantity.xMax)
#h2_temp.GetYaxis().SetRangeUser(-0.5, 0.3)

h2_temp.GetXaxis().SetTitle("log_{10}(E^{clus}_{T})")
h2_temp.GetXaxis().CenterTitle()

h2_temp.GetYaxis().SetTitle("#||{#Delta#phi_{clus-seed}}")
h2_temp.GetYaxis().SetTitleOffset(0.95)
h2_temp.GetYaxis().CenterTitle()

h2_temp.GetZaxis().SetTitle("a.u.")
#h2_temp.GetZaxis().SetTitle("E^{iX, iY}_{T} / E^{iX}_{T}")
h2_temp.GetZaxis().SetTitleOffset(1.1)
h2_temp.GetZaxis().CenterTitle()
#
#h2_temp.GetXaxis().CenterLabels(plotQuantity.centerLabelsX)
#h2_temp.GetYaxis().CenterLabels(plotQuantity.centerLabelsY)
#
h2_temp.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * 0.9)
h2_temp.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * 0.9)
h2_temp.GetZaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Z") * 0.9)

h2_temp.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * 1.1)
h2_temp.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * 1.2)
h2_temp.GetZaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Z") * 1.1)

h2_temp.GetXaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("X") * 0.85)
h2_temp.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Y") * 0.65)


h2_temp.GetYaxis().SetRangeUser(0.0, 0.8)


#if (abs(sum(plotQuantity.nDivisionsX)) > 0) :
#    
#    h2_temp.GetXaxis().SetNdivisions(plotQuantity.nDivisionsX[0], plotQuantity.nDivisionsX[1], plotQuantity.nDivisionsX[2])
#
#if (abs(sum(plotQuantity.nDivisionsY)) > 0) :
#    
#    h2_temp.GetYaxis().SetNdivisions(plotQuantity.nDivisionsY[0], plotQuantity.nDivisionsY[1], plotQuantity.nDivisionsY[2])
#
#canvas.SetLogx(plotQuantity.logX)
#canvas.SetLogy(plotQuantity.logY)
#canvas.SetLogz(plotQuantity.logZ)
#
#if (len(plotQuantity.extraText)) :
#    
#    latex = ROOT.TLatex()
#    #latex.SetTextFont(62);
#    latex.SetTextSize(0.045);
#    latex.SetTextAlign(13);
#    
#    latex.DrawLatex(plotQuantity.extraTextX, plotQuantity.extraTextY, plotQuantity.extraText)


l_param = [
    {
        "seedEta": 1.6,
        "label": "#scale[1.5]{1.479 < #||{eta_{seed}} < 1.75}",
        },
    
    {
        "seedEta": 1.9,
        "label": "#scale[1.5]{1.75 < #||{eta_{seed}} < 2.0}",
    },
    
    {
        "seedEta": 2.1,
        "label": "#scale[1.5]{#||{eta_{seed}} > 2.0}",
    },
]


l_param = [l_param[l_param_idx]]


l_curve = []


for iCurve in range(0, len(l_param)) :
    
    curve = getDphiExponential(
        seedEta = l_param[iCurve]["seedEta"],
    )
    
    l_curve.append(curve)
    
    color = iCurve+1
    
    curve.SetMarkerSize(0)
    
    curve.SetLineColor(color)
    curve.SetLineWidth(2)
    
    curve.SetTitle(l_param[iCurve]["label"])
    
    curve.Draw("same")
    
    
    legend.AddEntry(curve, curve.GetTitle(), "l")


gr_envelope.Draw("P same")

gr_envelope_label = "#splitline{#scale[1.5]{%s%% envelope and fit}}{%s}" %(str(envelopePercent), fitFuncLatex_mod)
legend.AddEntry(gr_envelope, gr_envelope_label, "pl")


latex = ROOT.TLatex()
#latex.SetTextFont(62);
latex.SetTextSize(0.045);
latex.SetTextAlign(13);

latex.DrawLatex(extraTextX, extraTextY, extraText)


legend.Draw()


CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")


canvas.SaveAs("%s/%s.pdf" %(plotDir, outFileName))
canvas.SaveAs("%s/%s.png" %(plotDir, outFileName))
