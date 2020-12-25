import os


outDir = "sourceFiles"

prefix = "root://cms-xrd-global.cern.ch//store"
toReplace = "/store"


l_sampleName = [
    "/DoublePhoton_FlatPt-1To100/Phase2HLTTDRWinter20RECOMiniAOD-PU200_110X_mcRun4_realistic_v3-v1/MINIAODSIM",
]


for iSample in range(0, len(l_sampleName)) :
    
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
    
    with open(outFile, "r") as f :
        
        fileContent = f.read()
    
    fileContent = fileContent.replace(toReplace, prefix)
    
    with open(outFile, "w") as f :
        
        f.write(fileContent)
