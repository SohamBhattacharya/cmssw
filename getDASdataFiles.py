import os


outDir = "sourceFiles"

prefix = "root://cms-xrd-global.cern.ch//store"
toReplace = "/store"


l_sampleName = [
    
    "/RelValElectronGunPt2To100/CMSSW_10_6_0_pre4-106X_upgrade2023_realistic_v2_2023D41noPU-v1/GEN-SIM-RECO",
    "/RelValElectronGunPt2To100/CMSSW_10_6_0-106X_upgrade2023_realistic_v2_2023D41noPU-v1/GEN-SIM-RECO",
    "/RelValElectronGunPt2To100/CMSSW_10_6_0_patch2-106X_upgrade2023_realistic_v3_2023D41noPU-v1/GEN-SIM-RECO",
    
    "/RelValElectronGunPt2To100/CMSSW_10_6_0_pre4-PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/GEN-SIM-RECO",
    "/RelValElectronGunPt2To100/CMSSW_10_6_0-PU25ns_106X_upgrade2023_realistic_v2_2023D41PU200-v1/GEN-SIM-RECO",
    "/RelValElectronGunPt2To100/CMSSW_10_6_0_patch2-PU25ns_106X_upgrade2023_realistic_v3_2023D41PU200-v1/GEN-SIM-RECO",
]


for iSample in range(0, len(l_sampleName)) :
    
    print "\n"
    print "*"*50
    
    sampleName = l_sampleName[iSample]
    
    sampleName_mod = sampleName[1:].replace("/", "_")
    
    outDir_mod = "%s/%s" %(outDir, sampleName_mod)
    
    command = "mkdir -p %s" %(outDir_mod)
    print "Command:", command
    print ""
    os.system(command)
    
    outFile = "%s/%s.txt" %(outDir_mod, sampleName_mod)
    
    command = "dasgoclient -query=\"file dataset=%s\" > %s" %(sampleName, outFile)
    print "Command:", command
    print ""
    os.system(command)
    
    fileContent = ""
    
    print "Replacing \"%s\" with \"%s\" in file." %(toReplace, prefix)
    print ""
    
    print "Number of lines:"
    os.system("wc -l %s" %(outFile))
    print ""
    
    with open(outFile, "r") as f :
        
        fileContent = f.read()
    
    fileContent = fileContent.replace(toReplace, prefix)
    
    with open(outFile, "w") as f :
        
        f.write(fileContent)
