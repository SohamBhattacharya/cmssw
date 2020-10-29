import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle


inFile = ROOT.TFile.Open("ntupleTree.root")
#inFile = ROOT.TFile.Open("ntupleTree_rajdeep.root")

tree = inFile.Get("treeMaker/tree")

HGCalEE_nLayer = 32

zsideStr = "M"
hitTypeStr = "rec"

h1_hitTotalE_vs_HGCalEElayer = ROOT.TH1F(
    "h1_hit_totalE-mean_vs_HGCalEElayer",
    "h1_hit_totalE-mean_vs_HGCalEElayer", 
    HGCalEE_nLayer, 0.0, float(HGCalEE_nLayer)
)

for iLayer in range(0, HGCalEE_nLayer) :
    
    branchName = "%sHit_HGCalEE%slayer%d_totE" %(hitTypeStr, zsideStr, iLayer+1)
    histName = "h1_%s" %(branchName)
    
    plotStr = "%s >> %s" %(branchName, histName)
    
    cutStr = ""
    #cutStr = "genEl_n > 0 && genEl_pT[0] > 14.5 && genEl_pT[0] < 200"
    
    h1_temp = ROOT.TH1F(histName, histName, int(1e4), 0.0, 10.0)
    h1_temp.Sumw2()
    
    tree.Draw(plotStr)
    
    mean = h1_temp.GetMean()
    sigma = h1_temp.GetStdDev()
    
    h1_hitTotalE_vs_HGCalEElayer.SetBinContent(iLayer+1, mean)
    h1_hitTotalE_vs_HGCalEElayer.SetBinError(iLayer+1, sigma)
    
    h1_hitTotalE_vs_HGCalEElayer.GetXaxis().SetBinLabel(iLayer+1, str(iLayer+1))

h1_hitTotalE_vs_HGCalEElayer.SetLineWidth(4)
h1_hitTotalE_vs_HGCalEElayer.SetLineColor(4)

h1_hitTotalE_vs_HGCalEElayer.SetMarkerStyle(10)
h1_hitTotalE_vs_HGCalEElayer.SetMarkerColor(4)

h1_hitTotalE_vs_HGCalEElayer.GetXaxis().SetTitle("HGCal EE%s layer" %(zsideStr))
h1_hitTotalE_vs_HGCalEElayer.GetXaxis().CenterTitle(True)
h1_hitTotalE_vs_HGCalEElayer.GetXaxis().CenterLabels(True)
h1_hitTotalE_vs_HGCalEElayer.GetXaxis().SetNdivisions(HGCalEE_nLayer, 1, 1)
h1_hitTotalE_vs_HGCalEElayer.GetXaxis().LabelsOption("v")

h1_hitTotalE_vs_HGCalEElayer.GetYaxis().SetTitle("#mu#[]{E^{tot}_{%s-hit}} [GeV]" %(hitTypeStr))
h1_hitTotalE_vs_HGCalEElayer.GetYaxis().SetTitleOffset(2.25)
h1_hitTotalE_vs_HGCalEElayer.GetYaxis().CenterTitle(True)

tdrstyle.setTDRStyle()

canvas = ROOT.TCanvas("canvas", "canvas")

h1_hitTotalE_vs_HGCalEElayer.Draw("E1")

CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")

canvas.SaveAs("plots/%sHit_totalE-mean_vs_HGCalEE%slayer.pdf" %(hitTypeStr, zsideStr))
