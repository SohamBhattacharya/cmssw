import os


outfileName = "statements.txt"

toReplace = "$$$"

l_str = [
    "slimmedEle_sig_pfCand1_deltaTsigni",
    "slimmedEle_sig_pfCand2_deltaTsigni",
    "slimmedEle_isoDR0p3_pfCand1_deltaTsigni",
    "slimmedEle_isoDR0p3_pfCand2_deltaTsigni",
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
        

