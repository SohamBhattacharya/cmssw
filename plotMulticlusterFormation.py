import numpy
import os
import time

import ROOT

import CMS_lumi
import tdrstyle

import Details


tdrstyle.setTDRStyle()

ROOT.gStyle.SetOptStat(1001110)
ROOT.gStyle.SetPalette(ROOT.kRainBow)


class PlotQuantity :
    
    xBranchName = ""
    yBranchName = ""
    zBranchName = ""
    
    xStr = ""
    yStr = ""
    zStr = ""
    
    xTitle = ""
    yTitle = ""
    zTitle = ""
    
    xMin_rangeDelta = 0
    xMax_rangeDelta = 0
    
    yMin_rangeDelta = 0
    yMax_rangeDelta = 0
    
    zMin_rangeDelta = 0
    zMax_rangeDelta = 0


#inFile = ROOT.TFile.Open("ntupleTree_withSimRecHits_withRecToSimAssoc.root")
inFile = ROOT.TFile.Open("ntupleTree_Expo.root")

tree = inFile.Get("treeMaker/tree")

#plotDir = "plots/multiCluster-formation"
#plotDir = "plots/multiCluster-formation_pi0"
plotDir = "plots/multiCluster-formation_ZprimeToEE"

HGCalEE_nLayer = 28

l_eventNumber = [
    100,
    500,
    700,
    900,
]


l_zsideVal = [+1, -1]

l_color = [2, 4, 6, 8]

#l_zlayer_pos = []
#
#for iLayer in range(0, HGCalEE_nLayer) :
#    
#    h1_zLayer_pos = ROOT.TH1F("h1_zLayer_pos", "h1_zLayer_pos", 5000, 0, 500)
#    
#    tree.Draw("recHit_z >> h1_zLayer_pos", "recHit_layer == %d && recHit_z > 0" %(iLayer+1))
#    
#    zlayer_pos = h1_zLayer_pos.GetMean()
#    
#    l_zlayer_pos.append(zlayer_pos)
#
#print l_zlayer_pos

l_plotQuantity = []


pltQty_temp = PlotQuantity()
pltQty_temp.xBranchName = "multiClus_clus_z"
pltQty_temp.yBranchName = "multiClus_clus_eta"
pltQty_temp.xStr = "z"
pltQty_temp.yStr = "eta"
pltQty_temp.xTitle = "z_{clus} [cm]"
pltQty_temp.yTitle = "#eta_{clus}"
pltQty_temp.xMin_rangeDelta = -5
pltQty_temp.xMax_rangeDelta = +5
pltQty_temp.yMin_rangeDelta = -0.01
pltQty_temp.yMax_rangeDelta = +0.01
l_plotQuantity.append(pltQty_temp)


pltQty_temp = PlotQuantity()
pltQty_temp.xBranchName = "multiClus_clus_z"
pltQty_temp.yBranchName = "multiClus_clus_phi"
pltQty_temp.xStr = "z"
pltQty_temp.yStr = "phi"
pltQty_temp.xTitle = "z_{clus} [cm]"
pltQty_temp.yTitle = "#phi_{clus}"
pltQty_temp.xMin_rangeDelta = -5
pltQty_temp.xMax_rangeDelta = +5
pltQty_temp.yMin_rangeDelta = -0.01
pltQty_temp.yMax_rangeDelta = +0.01
l_plotQuantity.append(pltQty_temp)



##### 3D #####

l_plotQuantity3D = []


pltQty_temp = PlotQuantity()
pltQty_temp.xBranchName = "multiClus_clus_z"
pltQty_temp.yBranchName = "multiClus_clus_phi"
pltQty_temp.zBranchName = "multiClus_clus_eta"
pltQty_temp.xStr = "z"
pltQty_temp.yStr = "phi"
pltQty_temp.zStr = "eta"
pltQty_temp.xTitle = "z_{clus} [cm]"
pltQty_temp.yTitle = "#phi_{clus}"
pltQty_temp.zTitle = "#eta_{clus}"
pltQty_temp.xMin_rangeDelta = -5
pltQty_temp.xMax_rangeDelta = +5
pltQty_temp.yMin_rangeDelta = -0.01
pltQty_temp.yMax_rangeDelta = +0.01
pltQty_temp.zMin_rangeDelta = -0.01
pltQty_temp.zMax_rangeDelta = +0.01
l_plotQuantity3D.append(pltQty_temp)


for iQty in range(0, len(l_plotQuantity)) :
    
    plotQuantity = l_plotQuantity[iQty]
    
    for iEvent in range(0, len(l_eventNumber)) :
        
        eventNumber = l_eventNumber[iEvent]
        
        if (eventNumber >= tree.GetEntries()) :
            
            print "Error: Event number must be in the range [0, %d]" %( tree.GetEntries()-1)
            exit(1)
        
        tree.GetEntry(eventNumber)
        
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
            
            plotDir_mod = "%s/event-%d/HGCalEE%s" %(plotDir, eventNumber, zsideStr)
            os.system("mkdir -p %s" %(plotDir_mod))
            
            canvas = ROOT.TCanvas("canvas", "canvas")
            canvas.SetCanvasSize(800, 600)
            canvas.SetLeftMargin(1.1 * canvas.GetLeftMargin())
            canvas.SetRightMargin(2 * canvas.GetRightMargin())#0.19)
            
            legend = legend = ROOT.TLegend(0.7, 0.75, 0.925, 0.925)
            #legend.SetFillStyle(0)
            legend.SetBorderSize(1)
            
            legend.SetHeader("HGCalEE%s" %(zsideSignLatex))
            legendHeader = legend.GetListOfPrimitives().First()
            legendHeader.SetTextAlign(23)
            
            multiGraph = ROOT.TMultiGraph("multiGraph", "multiGraph")
            
            #clusterIndex = 0
            nMultiCluster = tree.multiClus_clus_n.size()
            
            minX = +9999
            maxX = -9999
            
            minY = +9999
            maxY = -9999
            
            graphCounter = 0
            
            multiClus_sortedIndex = range(0, nMultiCluster)
            multiClus_sortedIndex.sort(key = lambda idx: tree.multiClus_E.at(idx), reverse = True)
            print multiClus_sortedIndex
            
            for iMultiCluster in range(0, nMultiCluster) :
                
                multiClusIndex = multiClus_sortedIndex[iMultiCluster]
                
                if (graphCounter > 1) :
                    
                    break
                
                #print int(numpy.sign(tree.multiClus_z.at(multiClusIndex))), zsideVal
                
                nCluster = int(tree.multiClus_clus_n.at(multiClusIndex))
                
                if (int(numpy.sign(tree.multiClus_z.at(multiClusIndex))) != zsideVal) :
                    
                    #clusterIndex += nCluster
                    
                    continue
                
                print "nCluster %d" %(nCluster)
                
                l_value_x = []
                l_value_y = []
                
                for iCluster in range(0, nCluster) :
                    
                    clusterIndex = int(tree.multiClus_clus_startIndex.at(multiClusIndex)) + iCluster
                    
                    #print "Multi-cluster %d/%d: cluster %d/%d" %(multiClusIndex+1, nMultiCluster, iCluster+1, nCluster)
                    
                    l_value_x.append(getattr(tree, plotQuantity.xBranchName).at(clusterIndex))
                    l_value_y.append(getattr(tree, plotQuantity.yBranchName).at(clusterIndex))
                    
                    # Update global cluster index
                    #clusterIndex += 1
                
                #print l_cluster_z
                
                minX = min(minX, min(l_value_x))
                maxX = max(maxX, max(l_value_x))
                
                minY = min(minY, min(l_value_y))
                maxY = max(maxY, max(l_value_y))
                
                # Sort by z
                #l_sortedIndex = range(0, len(l_value_x))
                #l_sortedIndex.sort(key = lambda idx: l_cluster_z[idx])
                #
                #l_value_x = [l_value_x[idx] for idx in l_sortedIndex]
                #l_value_y = [l_value_y[idx] for idx in l_sortedIndex]
                #l_cluster_z = [l_cluster_z[idx] for idx in l_sortedIndex]
                
                gr_cluster = ROOT.TGraph(len(l_value_x), numpy.array(l_value_x), numpy.array(l_value_y))
                
                color = l_color[graphCounter]
                
                if (color >= 19) :
                    
                    color = 19 + multiClusIndex + 1
                
                gr_cluster.SetMarkerColorAlpha(color, 0.5)
                gr_cluster.SetMarkerSize(1)
                gr_cluster.SetMarkerStyle(20)
                gr_cluster.SetLineColorAlpha(color, 0.5)
                gr_cluster.SetLineWidth(3)
                
                multiGraph.Add(gr_cluster, "P")
                legend.AddEntry(gr_cluster, "multi-clus%d" %(graphCounter+1), "P")
                
                
                # Increment the number of graphs
                graphCounter += 1
            
            
            multiGraph.Draw("A")
            
            multiGraph.GetXaxis().SetTitle(plotQuantity.xTitle)
            multiGraph.GetXaxis().CenterTitle()
            
            multiGraph.GetYaxis().SetTitle(plotQuantity.yTitle)
            multiGraph.GetYaxis().SetTitleOffset(1.5)
            multiGraph.GetYaxis().CenterTitle()
            
            minX = min(Details.d_HGCalEE_layerZ[zsideStr])
            maxX = max(Details.d_HGCalEE_layerZ[zsideStr])
            
            multiGraph.GetXaxis().SetRangeUser(minX+plotQuantity.xMin_rangeDelta, maxX+plotQuantity.xMax_rangeDelta)
            multiGraph.GetYaxis().SetRangeUser(minY+plotQuantity.yMin_rangeDelta, maxY+plotQuantity.yMax_rangeDelta)
            
            
            l_xGrid = []
            
            for iLayer in range(0, len(Details.d_HGCalEE_layerZ[zsideStr])) :
            #for iLayer in range(0, HGCalEE_nLayer) :
                
                layerZ = Details.l_HGCalEE_layerZ[iLayer]
                
                l_xGrid_x = numpy.array([layerZ, layerZ], dtype = float)
                l_xGrid_y = numpy.array([multiGraph.GetYaxis().GetXmin(), multiGraph.GetYaxis().GetXmax()])
                
                gr_temp = ROOT.TGraph(
                    2,
                    l_xGrid_x,
                    l_xGrid_y,
                )
                
                # Gets deleted otherwise
                l_xGrid.append(gr_temp)
                
                gr_temp.SetLineColor(1)
                gr_temp.SetLineStyle(3)
                gr_temp.SetLineWidth(1)
                
                gr_temp.Draw("same L")
            
            #canvas.SetGridx()
            canvas.SetGridy()
            
            legend.Draw()
            
            CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")
            
            outFileName = "multiClus-clus_%s_vs_%s.pdf" %(plotQuantity.yStr, plotQuantity.xStr)
            
            canvas.SaveAs("%s/%s" %(plotDir_mod, outFileName))



for iQty in range(0, len(l_plotQuantity3D)) :
    
    plotQuantity = l_plotQuantity3D[iQty]
    
    for iEvent in range(0, len(l_eventNumber)) :
        
        eventNumber = l_eventNumber[iEvent]
        
        if (eventNumber >= tree.GetEntries()) :
            
            print "Error: Event number must be in the range [0, %d]" %( tree.GetEntries()-1)
            exit(1)
        
        tree.GetEntry(eventNumber)
        
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
            
            plotDir_mod = "%s/event-%d/HGCalEE%s" %(plotDir, eventNumber, zsideStr)
            os.system("mkdir -p %s" %(plotDir_mod))
            
            canvas = ROOT.TCanvas("canvas", "canvas")
            canvas.SetCanvasSize(800, 600)
            canvas.SetLeftMargin(1.1 * canvas.GetLeftMargin())
            canvas.SetRightMargin(5 * canvas.GetRightMargin())
            
            legend = legend = ROOT.TLegend(0.75, 0.75, 0.975, 0.925)
            #legend.SetFillStyle(0)
            legend.SetBorderSize(1)
            
            legend.SetHeader("HGCalEE%s" %(zsideSignLatex))
            legendHeader = legend.GetListOfPrimitives().First()
            legendHeader.SetTextAlign(23)
            
            l_graph2D = []
            
            #clusterIndex = 0
            nMultiCluster = tree.multiClus_clus_n.size()
            
            minX = +9999
            maxX = -9999
            
            minY = +9999
            maxY = -9999
            
            minZ = +9999
            maxZ = -9999
            
            graphCounter = 0
            
            multiClus_sortedIndex = range(0, nMultiCluster)
            multiClus_sortedIndex.sort(key = lambda idx: tree.multiClus_E.at(idx), reverse = True)
            print multiClus_sortedIndex
            
            for iMultiCluster in range(0, nMultiCluster) :
                
                multiClusIndex = multiClus_sortedIndex[iMultiCluster]
                
                if (graphCounter > 1) :
                    
                    break
                
                #print int(numpy.sign(tree.multiClus_z.at(multiClusIndex))), zsideVal
                
                nCluster = int(tree.multiClus_clus_n.at(multiClusIndex))
                
                if (int(numpy.sign(tree.multiClus_z.at(multiClusIndex))) != zsideVal) :
                    
                    #clusterIndex += nCluster
                    
                    continue
                
                print "nCluster %d" %(nCluster)
                
                l_value_x = []
                l_value_y = []
                l_value_z = []
                
                l_temp_x = []
                l_temp_y = []
                l_temp_z = []
                
                for iCluster in range(0, nCluster) :
                    
                    clusterIndex = int(tree.multiClus_clus_startIndex.at(multiClusIndex)) + iCluster
                    
                    #print "Multi-cluster %d/%d: cluster %d/%d" %(multiClusIndex+1, nMultiCluster, iCluster+1, nCluster)
                    
                    l_value_x.append(getattr(tree, plotQuantity.xBranchName).at(clusterIndex))
                    l_value_y.append(getattr(tree, plotQuantity.yBranchName).at(clusterIndex))
                    l_value_z.append(getattr(tree, plotQuantity.zBranchName).at(clusterIndex))
                    
                    # Update global cluster index
                    #clusterIndex += 1
                
                #print l_cluster_z
                
                minX = min(minX, min(l_value_x))
                maxX = max(maxX, max(l_value_x))
                
                minY = min(minY, min(l_value_y))
                maxY = max(maxY, max(l_value_y))
                
                minZ = min(minZ, min(l_value_z))
                maxZ = max(maxZ, max(l_value_z))
                
                # Sort by z
                #l_sortedIndex = range(0, len(l_value_x))
                #l_sortedIndex.sort(key = lambda idx: l_cluster_z[idx])
                #
                #l_value_x = [l_value_x[idx] for idx in l_sortedIndex]
                #l_value_y = [l_value_y[idx] for idx in l_sortedIndex]
                #l_cluster_z = [l_cluster_z[idx] for idx in l_sortedIndex]
                
                gr_cluster = ROOT.TGraph(len(l_value_x), numpy.array(l_value_x), numpy.array(l_value_y))
                
                color = l_color[graphCounter]
                
                if (color >= 19) :
                    
                    color = 19 + multiClusIndex + 1
                
                gr2_cluster = ROOT.TGraph2D(len(l_value_x), numpy.array(l_value_x), numpy.array(l_value_y), numpy.array(l_value_z))
                gr2_cluster.SetMarkerColorAlpha(color, 0.5)
                gr2_cluster.SetMarkerSize(1)
                gr2_cluster.SetMarkerStyle(20)
                gr2_cluster.SetLineColorAlpha(color, 0.5)
                gr2_cluster.SetLineWidth(3)
                gr2_cluster.GetXaxis().SetTitle()
                gr2_cluster.GetYaxis().SetTitle("phi")
                gr2_cluster.GetZaxis().SetTitle("eta")
                
                l_graph2D.append(gr2_cluster)
                legend.AddEntry(gr2_cluster, "multi-clus%d" %(graphCounter+1), "P")
                
                
                # Increment the number of graphs
                graphCounter += 1
            
            
            #h3_temp = ROOT.TH3F("h3_temp", "h3_temp",
            #    100, minX+plotQuantity.xMin_rangeDelta, maxX+plotQuantity.xMax_rangeDelta,
            #    100, minY+plotQuantity.yMin_rangeDelta, maxY+plotQuantity.yMax_rangeDelta,
            #    100, minZ+plotQuantity.zMin_rangeDelta, maxZ+plotQuantity.zMax_rangeDelta,
            #)
            #
            #h3_temp.Draw()
            
            for iGraph2D in range(0, len(l_graph2D)) :
                
                l_graph2D[iGraph2D].Draw("P %s" %("same" * (iGraph2D > 0)))
                
                l_graph2D[iGraph2D].GetXaxis().SetTitle(plotQuantity.xTitle)
                l_graph2D[iGraph2D].GetXaxis().SetTitleOffset(1.5)
                l_graph2D[iGraph2D].GetXaxis().CenterTitle()
                
                l_graph2D[iGraph2D].GetYaxis().SetTitle(plotQuantity.yTitle)
                l_graph2D[iGraph2D].GetYaxis().SetTitleOffset(1.7)
                l_graph2D[iGraph2D].GetYaxis().CenterTitle()
                
                l_graph2D[iGraph2D].GetZaxis().SetTitle(plotQuantity.zTitle)
                l_graph2D[iGraph2D].GetZaxis().SetTitleOffset(1.5)
                l_graph2D[iGraph2D].GetZaxis().CenterTitle()
                
                minX = min(Details.d_HGCalEE_layerZ[zsideStr])
                maxX = max(Details.d_HGCalEE_layerZ[zsideStr])
                
                l_graph2D[iGraph2D].GetXaxis().SetRangeUser(minX+plotQuantity.xMin_rangeDelta, maxX+plotQuantity.xMax_rangeDelta)
                l_graph2D[iGraph2D].GetYaxis().SetRangeUser(minY+plotQuantity.yMin_rangeDelta, maxY+plotQuantity.yMax_rangeDelta)
                l_graph2D[iGraph2D].GetZaxis().SetRangeUser(minZ+plotQuantity.zMin_rangeDelta, maxZ+plotQuantity.zMax_rangeDelta)
                
                canvas.Modified()
                canvas.Update()
            
            
            l_xGrid = []
            
            #for iLayer in range(0, len(Details.l_HGCalEE_layerZ)) :
            #    
            #    layerZ = Details.l_HGCalEE_layerZ[iLayer]
            #    
            #    l_xGrid_x = numpy.array([layerZ, layerZ], dtype = float)
            #    l_xGrid_y = numpy.array([multiGraph.GetYaxis().GetXmin(), multiGraph.GetYaxis().GetXmax()])
            #    l_xGrid_y = numpy.array([multiGraph.GetYaxis().GetXmin(), multiGraph.GetYaxis().GetXmax()])
            #    
            #    gr_temp = ROOT.TGraph(
            #        2,
            #        l_xGrid_x,
            #        l_xGrid_y,
            #    )
            #    
            #    # Gets deleted otherwise
            #    l_xGrid.append(gr_temp)
            #    
            #    gr_temp.SetLineColor(1)
            #    gr_temp.SetLineStyle(3)
            #    gr_temp.SetLineWidth(1)
            #    
            #    gr_temp.Draw("same L")
            
            legend.Draw()
            
            canvas.SetGridx()
            canvas.SetGridy()
            #canvas.SetGridz()
            
            if (zsideVal < 0) :
                
                #canvas.SetTheta(-canvas.GetTheta())
                canvas.SetPhi(-canvas.GetPhi())
            
            print canvas.GetTheta(), canvas.GetPhi()
            
            #time.sleep(10000)
            
            CMS_lumi.CMS_lumi(pad = canvas, iPeriod = 0, iPosX = 0, CMSextraText = "Simulation Preliminary", lumiText = "")
            
            outFileName = "multiClus-clus_%s_vs_%s_vs_%s.pdf" %(plotQuantity.zStr, plotQuantity.yStr, plotQuantity.xStr)
            
            canvas.SaveAs("%s/%s" %(plotDir_mod, outFileName))
