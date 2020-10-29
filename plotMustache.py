import numpy
import os
import time

import ROOT

import CMS_lumi
import tdrstyle

import Common
import Details


ROOT.gROOT.ProcessLine(".L EDAnalyzers/TreeMaker/interface/CustomRootDict.cc+")


#def getMustacheParabolae(maxEta, maxPhi, ClustE, ClusEta, ClusPhi) :
def getMustacheParabolae(maxEta, ClustE) :
    
    p00 = -0.107537
    p01 = 0.590969
    p02 = -0.076494
    p10 = -0.0268843
    p11 = 0.147742
    p12 = -0.0191235

    w00 = -0.00571429
    w01 = -0.002
    w10 = 0.0135714
    w11 = 0.001

    sineta0 = numpy.sin(maxEta)
    eta0xsineta0 = maxEta * sineta0

    #2 parabolas (upper and lower)
    #of the form: y = a*x*x + b

    #b comes from a fit to the width
    #and has a slight dependence on E on the upper edge
    # this only works because of fine tuning :-D
    sqrt_log10_clustE = numpy.sqrt(numpy.log10(ClustE) + 1.1)
    # we need to have this in two steps, so that we don't improperly shift
    # the lower bound!
    b_upper = w10 * eta0xsineta0 + w11 / sqrt_log10_clustE
    b_lower = w00 * eta0xsineta0 + w01 / sqrt_log10_clustE
    midpoint = 0.5 * (b_upper + b_lower)
    b_upper -= midpoint
    b_lower -= midpoint

    #the curvature comes from a parabolic
    #fit for many slices in eta given a
    #slice -0.1 < log10(Et) < 0.1
    curv_up = eta0xsineta0 * (p00 * eta0xsineta0 + p01) + p02
    curv_low = eta0xsineta0 * (p10 * eta0xsineta0 + p11) + p12

    #solving for the curviness given the width of this particular point
    a_upper = (1.0 / (4 * curv_up)) - abs(b_upper)
    a_lower = (1.0 / (4 * curv_low)) - abs(b_lower)

    #dphi = TVector2::Phi_mpi_pi(ClusPhi - maxPhi)
    #dphi2 = dphi * dphi
    ## minimum offset is half a crystal width in either direction
    ## because science.
    #const float upper_cut = (std::max((1. / (4. * a_upper)), 0.0) * dphi2 + std::max(b_upper, 0.0087f)) + 0.0087
    #const float lower_cut = (std::max((1. / (4. * a_lower)), 0.0) * dphi2 + std::min(b_lower, -0.0087f))
    #
    ##if(deta < upper_cut && deta > lower_cut) inMust=true
    #
    #const float deta = (1 - 2 * (maxEta < 0)) * (ClusEta - maxEta)  # sign flip deta
    #return (deta < upper_cut && deta > lower_cut)
    
    #parabolaStr_upr = "%f * %f*x*x + %f" %(a_upper, b_upper)
    #parabolaStr_lwr = "%f * %f*x*x + %f" %(a_lower, b_lower)
    
    print "a_upper = %+0.4f" %(a_upper)
    print "a_lower = %+0.4f" %(a_lower)
    
    print "b_upper = %+0.4f" %(b_upper)
    print "b_lower = %+0.4f" %(b_lower)
    
    print ""
    
    #a_upper *= 0.6
    ##a_lower *= 0.4
    #
    #b_upper *= 0.3
    #b_lower *= 0.3
    
    parabolaStr_upr = "(max((1. / (4. * %f)), 0.0) * x*x + max(%f, +0.0087)) + 0.0087" %(a_upper, b_upper)
    parabolaStr_lwr = "(max((1. / (4. * %f)), 0.0) * x*x + min(%f, -0.0087))        " %(a_lower, b_lower)
    
    #parabolaStr_upr = "(max((1. / (4. * %f)), 0.0) * x*x + max(%f, +0.001))" %(a_upper, b_upper)
    #parabolaStr_lwr = "(max((1. / (4. * %f)), 0.0) * x*x + min(%f, -0.001))" %(a_lower, b_lower)
    
    f1_parabola_upr = ROOT.TF1("f1_parabola_upr", parabolaStr_upr, -10.0, +10.0)
    f1_parabola_lwr = ROOT.TF1("f1_parabola_lwr", parabolaStr_lwr, -10.0, +10.0)
    
    return [f1_parabola_upr, f1_parabola_lwr]


l_varName = [
    "gsfEleFromTICL_E",
    "gsfEleFromTICL_pT",
    "gsfEleFromTICL_eta",
    
    "gsfEleFromTICL_R2p8",
    
    "gsfEleFromTICL_superClus_nClus",
    
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
plotStr_x = "gsfEleFromTICL_superClusSeed_TICLclus_dPhi"
plotStr_y = "gsfEleFromTICL_superClusSeed_TICLclus_dEta"

cutStr = "1"
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


extraTextX = -0.2
extraTextY = 0.8
extraText = ""

#extraText = "R2.8 < 0.9"
#extraText = "R2.8 > 0.95"


#plotDir = "plots/mustache"
#plotDir = "plots/mustache_newTICL"
#plotDir = "plots/mustache_test"
plotDir = "plots/mustache_with-TICLfragmentationFix"
#plotDir = "plots/mustache_11_0_0_pre11"

os.system("mkdir -p %s" %(plotDir))


outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dEta_vs_dPhi"
#outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dEta_vs_dPhi_low-R2p8"
#outFileName = "gsfEleFromTICL_superClusSeed_TICLclus_dEta_vs_dPhi_high-R2p8"

nEvent = tree.GetEntries()


h2_temp = ROOT.TH2F(
    "h2_temp", "h2_temp",
    #400, -1.0, 1.0,
    #400, -1.0, 1.0,
    500, -0.5, 0.5,
    500, -0.5, 0.5,
)
h2_temp.Sumw2()


for iEvent in range(0, nEvent) :
    
    tree.GetEntry(iEvent)
    
    d_varInfo = {}
    
    for iVar in range(0, len(l_varName)) :
        
        varName = l_varName[iVar]
        varData = getattr(tree, varName)
        
        d_varInfo[varName] = varData
    
    plotData_x = getattr(tree, plotStr_x)
    plotData_y = getattr(tree, plotStr_y)
    
    nObj_mod = min(nObj, plotData_x.size())
    #print nObj_mod
    
    for iObj in range(0, nObj_mod) :
        
        nElement = plotData_x.at(iObj).size()
        #print nElement
        
        for iElement in range(0, nElement) :
            
            cutStr_mod = cutStr
            
            for iVar in range(0, len(l_varName)) :
                
                varName = l_varName[iVar]
                
                varData = d_varInfo[varName]
                
                type_str = str(type(varData))
                
                if(len(Common.findAllInStr(type_str, "vector")) == 1) :
                    
                    varVal = varData.at(iObj)
                    
                    cutStr_mod = cutStr_mod.replace(varName, str(float(varVal)))
                
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
            
            h2_temp.Fill(x, y)
            

#h2_temp.Draw("colz")
#time.sleep(100000)


tdrstyle.setTDRStyle()

canvas = ROOT.TCanvas("canvas", "canvas")

canvas.SetCanvasSize(800, 600)
canvas.SetLeftMargin(0.8 * canvas.GetLeftMargin())
canvas.SetRightMargin(10 * canvas.GetRightMargin())#0.19)

legend = ROOT.TLegend(0.3, 0.15, 0.75, 0.475)
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

h2_temp.GetXaxis().SetTitle("#Delta#phi")
h2_temp.GetXaxis().CenterTitle()

h2_temp.GetYaxis().SetTitle("#Delta#eta")
h2_temp.GetYaxis().SetTitleOffset(0.95)
h2_temp.GetYaxis().CenterTitle()

h2_temp.GetZaxis().SetTitle("a.u.")
h2_temp.GetZaxis().SetTitleOffset(1.1)
h2_temp.GetZaxis().CenterTitle()
#
#h2_temp.GetXaxis().CenterLabels(plotQuantity.centerLabelsX)
#h2_temp.GetYaxis().CenterLabels(plotQuantity.centerLabelsY)
#
h2_temp.GetXaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("X") * 0.9)
h2_temp.GetYaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Y") * 0.9)
h2_temp.GetZaxis().SetLabelSize(ROOT.gStyle.GetLabelSize("Z") * 0.9)

h2_temp.GetXaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("X") * 1.2)
h2_temp.GetYaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Y") * 1.2)
h2_temp.GetZaxis().SetTitleSize(ROOT.gStyle.GetTitleSize("Z") * 1.1)

h2_temp.GetXaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("X") * 0.85)
h2_temp.GetYaxis().SetTitleOffset(ROOT.gStyle.GetTitleOffset("Y") * 0.65)

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


l_mustache_param = [
    {
        "seedEta": 1.8,
        "clusE": 1.0,
    },
    
    {
        "seedEta": 2.5,
        "clusE": 1.0,
    },
]


l_mustache = []


for iMustache in range(0, len(l_mustache_param)) :
    
    l_parabola = getMustacheParabolae(
        maxEta = l_mustache_param[iMustache]["seedEta"],
        ClustE = l_mustache_param[iMustache]["clusE"],
    )
    
    l_mustache.append(l_parabola)
    
    color = iMustache+1
    
    l_parabola[0].SetMarkerSize(0)
    l_parabola[1].SetMarkerSize(0)
    
    l_parabola[0].SetLineColor(color)
    l_parabola[1].SetLineColor(color)
    
    l_parabola[0].SetTitle("#eta_{seed}=%0.1f, E_{clus}=%0.1f GeV" %(l_mustache_param[iMustache]["seedEta"], l_mustache_param[iMustache]["clusE"]))
    
    l_parabola[0].Draw("same")
    l_parabola[1].Draw("same")
    
    
    legend.AddEntry(l_parabola[0], l_parabola[0].GetTitle(), "l")


latex = ROOT.TLatex()
#latex.SetTextFont(62);
latex.SetTextSize(0.045);
latex.SetTextAlign(13);

latex.DrawLatex(extraTextX, extraTextY, extraText)


legend.Draw()


CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")


canvas.SaveAs("%s/%s.pdf" %(plotDir, outFileName))
canvas.SaveAs("%s/%s.png" %(plotDir, outFileName))
