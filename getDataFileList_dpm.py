import os


crabDirPath = "crabJobs"


dictionary = {
    "SingleElectronFlatPtGun_pT-0-200": {
        "sampleName": "/SingleElectronFlatPtGun_pT-0-200/sobhatta-crab_SingleElectronFlatPtGun_pT-0-200_GEN-SIM-RECO-ffc2278112c688bef3890fc698a39794/USER",
        "crabDirName": "SingleElectronFlatPtGun_pT-0-200_GEN-SIM-RECO"
    }
}

outDir = "sourceFiles"

scriptName = "getDataFileList_dpm.sh"
scriptName_mod = "getDataFileList_dpm_mod.sh"


for key in dictionary :
    
    sampleName = dictionary[key]["sampleName"]
    sampleName_mod = sampleName[1:].replace("/", "_")
    print "Getting file list:", sampleName
    
    #jobName = sampleName[1: sampleName.find("/", 1)]
    #print "Job name:", jobName
    
    crabDir = "%s/crab_%s" %(crabDirPath, dictionary[key]["crabDirName"])
    print "Crab directory:", crabDir
    
    outDir_mod = "%s/%s" %(outDir, sampleName_mod)
    os.system("mkdir -p %s" %(outDir_mod))
    
    outFile = "%s/%s.txt" %(outDir_mod, sampleName_mod)
    print "Output:", outFile
    
    command = "mkdir -p " + outDir
    print command
    os.system(command)
    
    command = "crab getoutput --xrootd " + crabDir + " | sort -V > " + outFile
    print command
    os.system(command)
    
    os.system("echo \"Number of files: `wc -l %s`\"" %(outFile))
    
    print "\n"
