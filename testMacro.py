import ROOT


ROOT.gROOT.ProcessLine(".L EDAnalyzers/TreeMaker/interface/CustomRootDict.cc+");

inputFile = ROOT.TFile.Open("ntupleTree_modTICLele.root");

tree = inputFile.Get("treeMaker/tree");

#tree->SetBranchAddress("gsfEleFromTICL_superClusSeed_TICLclus_dEta", &vv_gsfEleFromTICL_superClusSeed_TICLclus$

nEvent = tree.GetEntries();

#for iEvent in range(0, nEvent) :
#for iEvent in range(0, 10) :
#    
#    tree.GetEntry(iEvent);
#    
#    gsfEleFromTICL_E = getattr(tree, "gsfEleFromTICL_E")
#    l_gsfEleFromTICL_superClusSeed_TICLclus_dEta = getattr(tree, "gsfEleFromTICL_superClusSeed_TICLclus_dEta")
#    l_gsfEleFromTICL_superClusSeed_TICLclus_dPhi = getattr(tree, "gsfEleFromTICL_superClusSeed_TICLclus_dPhi")
#    
#    print type(gsfEleFromTICL_E)
#    print type(l_gsfEleFromTICL_superClusSeed_TICLclus_dEta)
#    
#    nEle = len(l_gsfEleFromTICL_superClusSeed_TICLclus_dEta)
#    
#    print "[%d] %d" %(iEvent+1, nEle);
#    
#    print gsfEleFromTICL_E, gsfEleFromTICL_E.size()
#    
#    if (nEle) :
#        
#        gsfEleFromTICL_superClusSeed_TICLclus_dEta = l_gsfEleFromTICL_superClusSeed_TICLclus_dEta[0]
#        gsfEleFromTICL_superClusSeed_TICLclus_dPhi = l_gsfEleFromTICL_superClusSeed_TICLclus_dPhi[0]
#        
#        #print gsfEleFromTICL_superClusSeed_TICLclus_dEta.size()
#        
#        l1 = []
#        l2 = []
#        
#        for i in range(0, gsfEleFromTICL_superClusSeed_TICLclus_dEta.size()) :
#            
#            dEta = gsfEleFromTICL_superClusSeed_TICLclus_dEta.at(i)
#            dPhi = gsfEleFromTICL_superClusSeed_TICLclus_dPhi.at(i)
#            
#            l1.append("(%0.2e, %0.2e)" %(dEta, dPhi))
#            l2.append(int(abs(dEta) < 1e-3 and abs(dPhi) < 1e-3))
#        
#        print l1
#        print l2
#        print sum(l2)
#    
#    print "\n"
#    

outFile = ROOT.TFile.Open("plots/mustache/mustache.root", "RECREATE")

h3_dEta_dPhi_dZ = ROOT.TH3F(
    "h3_dEta_dPhi_dZ",
    "h3_dEta_dPhi_dZ",
    200, -50.0, +50.0,
    100, -1.0 , +1.0 ,
    100, -1.0 , +1.0 ,
)

tree.Draw("gsfEleFromTICL_superClusSeed_TICLclus_dEta:gsfEleFromTICL_superClusSeed_TICLclus_dPhi:gsfEleFromTICL_superClusSeed_TICLclus_dZ >> h3_dEta_dPhi_dZ")

h3_dEta_dPhi_dZ.GetXaxis().SetTitle("#Deltaz")
h3_dEta_dPhi_dZ.GetXaxis().SetTitleOffset(1.7)
h3_dEta_dPhi_dZ.GetXaxis().CenterTitle(True)

h3_dEta_dPhi_dZ.GetYaxis().SetTitle("#Delta#phi")
h3_dEta_dPhi_dZ.GetYaxis().SetTitleOffset(1.7)
h3_dEta_dPhi_dZ.GetYaxis().CenterTitle(True)

h3_dEta_dPhi_dZ.GetZaxis().SetTitle("#Delta#eta")
h3_dEta_dPhi_dZ.GetZaxis().SetTitleOffset(1.2)
h3_dEta_dPhi_dZ.GetZaxis().CenterTitle(True)

outFile.cd()
h3_dEta_dPhi_dZ.Write()
