import numpy
import os

import ROOT

import CMS_lumi
import tdrstyle


tdrstyle.setTDRStyle()

ROOT.gStyle.SetOptStat(1001110)
ROOT.gStyle.SetPalette(ROOT.kRainBow)


inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits.root")

tree = inFile.Get("treeMaker/tree")

HGCalEE_nLayer = 28

l_eventNumber = [
    300,
    500,
    700,
]

hitTypeStr = "rec"
l_zsideVal = [+1, -1]


for iEvent in range(0, len(l_eventNumber)) :
    
    eventNumber = l_eventNumber[iEvent]
    
    if (eventNumber >= tree.GetEntries()) :
        
        print "Error: Event number must be in the range [0, %d]" %( tree.GetEntries()-1)
        exit(1)
    
    for izside in range(0, len(l_zsideVal)) :
        
        zsideVal = l_zsideVal[izside]
        
        zsideStr = ""
        zsideSignLatex = ""
        
        if (zsideVal == +1) :
            
            zsideStr = "P"
            zsideSignLatex = "#plus"
        
        elif (zsideVal == -1) :
            
            zsideStr = "M"
            zsideSignLatex = "#minus"
        
        #print zsideVal, zsideStr, zsideSignLatex
        
        plotDir = "plots/%sHit/event-%d/HGCalEE%s" %(hitTypeStr, eventNumber, zsideStr)
        os.system("mkdir -p %s" %(plotDir))
        
        
        #tree->Draw("recHit_E", "recHit_layer==27 && recHit_zside > 0", "", 1, 300)
        #tree->Draw("recHit_y:recHit_x >> h2_temp(200, -100, 100, 200, -100, 100)", "recHit_E * (recHit_layer==27 && recHit_zside > 0)", "colz", 1, 300)
        
        
        for iLayer in range(0, HGCalEE_nLayer) :
            
            h2_temp = ROOT.TH2F("h2_temp", "", 200, -100, 100, 200, -100, 100)
            
            plotStr = "recHit_y:recHit_x >> h2_temp"
            
            cutStr = "recHit_layer == %d && recHit_zside == %d" %(iLayer+1, zsideVal)
            weightStr = "recHit_E * (%s)" %(cutStr)
            
            
            h1_temp = ROOT.TH1F("h1_temp", "h1_temp", 1000, 0, 1000)
            tree.Draw("recHit_E >> h1_temp", cutStr, "", 1, eventNumber)
            
            E_mean = h1_temp.GetMean()
            
            h2_temp.GetXaxis().SetTitle("x_{%s-hit} [cm]" %(hitTypeStr))
            h2_temp.GetXaxis().CenterTitle()
            
            h2_temp.GetYaxis().SetTitle("y_{%s-hit} [cm]" %(hitTypeStr))
            h2_temp.GetYaxis().SetTitleOffset(0.95)
            h2_temp.GetYaxis().CenterTitle()
            
            h2_temp.GetZaxis().SetTitle("E_{%s-hit} [GeV]" %(hitTypeStr))
            h2_temp.GetZaxis().SetTitleOffset(1.2)
            h2_temp.GetZaxis().CenterTitle()
            
            #h2_temp.SetMaximum()
            
            ROOT.gStyle.SetStatY(0.93)
            ROOT.gStyle.SetStatX(0.785)
            ROOT.gStyle.SetStatW(0.2)
            #ROOT.gStyle.SetStatH(0.5)
            ROOT.gStyle.SetStatFont(62)
            ROOT.gStyle.SetStatFontSize(0.03)
            ROOT.gStyle.SetStatBorderSize(0)
            
            
            canvas = ROOT.TCanvas("canvas", "canvas")
            
            canvas.SetCanvasSize(800, 600)
            canvas.SetLeftMargin(0.8 * canvas.GetLeftMargin())
            canvas.SetRightMargin(10 * canvas.GetRightMargin())#0.19)
            
            tree.Draw(plotStr, weightStr, "colz", 1, eventNumber)
            
            #statBox = h2_temp.FindObject("stats")
            #print statBox.SetName("xxx")
            #print statBox.GetName()
            
            latex = ROOT.TLatex()
            #latex.SetTextFont(62);
            latex.SetTextSize(0.045);
            latex.SetTextAlign(13);
            
            latex.DrawLatex(-90, 90, "#splitline{HGCal EE%s, Layer %d}{#scale[0.8]{#mu#[]{E_{%s-hit}}=%0.1e GeV}}" %(zsideSignLatex, iLayer+1, hitTypeStr, E_mean))
            
            
            CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")
            
            outFileName = "%sHit_y-vs-x_HGCalEE%s_layer%d.pdf" %(hitTypeStr, zsideStr, iLayer+1)
            
            canvas.SaveAs("%s/%s" %(plotDir, outFileName))
