import os


outfileName = "statements.txt"

toReplace = "$$$"

l_str = [
    "multiClus_HGCalEEP_clus1_dX",
    "multiClus_HGCalEEP_clus1_dY",
    "multiClus_HGCalEEP_clus1_dZ",
    
    "multiClus_HGCalEEP_clus1_dEta",
    "multiClus_HGCalEEP_clus1_dPhi",
    "multiClus_HGCalEEP_clus1_dR",
    
    "multiClus_HGCalEEM_clus1_dX",
    "multiClus_HGCalEEM_clus1_dY",
    "multiClus_HGCalEEM_clus1_dZ",
    
    "multiClus_HGCalEEM_clus1_dEta",
    "multiClus_HGCalEEM_clus1_dPhi",
    "multiClus_HGCalEEM_clus1_dR",
]


templateStr = (
    "sprintf(name, \"%s\");\n"
    "tree->Branch(name, &v_%s);"
)
linegaps = 1


#templateStr = (
#    "treeOutput->v_%s.push_back();"
#)
#linegaps = 0



with open(outfileName, "w") as f :
    
    for iEntry in range(0, len(l_str)) :
        
        #temp_str = templateStr %(l_str[iEntry])
        temp_str = templateStr
        temp_str = temp_str.replace("%s", l_str[iEntry])
        
        print temp_str + "\n" * linegaps
        
        temp_str += "\n"
        temp_str += "\n" * linegaps
        
        f.write(temp_str)
        

