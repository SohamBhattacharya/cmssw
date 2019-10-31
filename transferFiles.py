import argparse
import getpass
import os


# Argument parser
parser = argparse.ArgumentParser()

# List of directories
parser.add_argument(
    "--dest",
    help = "Destination",
    #nargs = "1",
    type = str,
    required = True,
)


#parser.add_argument(
#    "--pwd",
#    help = "Password",
#    #nargs = "1",
#    type = str,
#    required = True,
#)

parser.add_argument(
    "--rsyncFlags",
    help = "rsync flags",
    #nargs = "*",
    type = str,
    default = "",
    required = False,
)


# Parse arguments
args = parser.parse_args()

#DEST = "/afs/cern.ch/work/s/sobhatta/private/HGCal_ele-reco/analysis/CMSSW_11_0_0_pre9/src"
DEST = args.dest

PWD = getpass.getpass("Password: ")

#RSYNC_EXTRAFLAGS = ""
RSYNC_EXTRAFLAGS = args.rsyncFlags


l_file = [
    #"RecoParticleFlow/PFClusterProducer/plugins/Cluster3DPCACalculator.cc",
    "RecoParticleFlow/PFClusterProducer/plugins/PFClusterFromHGCalMultiCluster.cc",
    #"RecoParticleFlow/PFClusterProducer/plugins/PFClusterProducer.cc",
    
    "RecoEgamma/EgammaElectronAlgos/interface/GsfElectronAlgo.h",
    "RecoEgamma/EgammaElectronAlgos/src/GsfElectronAlgo.cc",
    #"RecoEgamma/EgammaElectronAlgos/src/ElectronSeedGenerator.cc",
    
    "RecoEgamma/EgammaElectronProducers/plugins/GsfElectronEcalDrivenProducer.h",
    "RecoEgamma/EgammaElectronProducers/plugins/GsfElectronEcalDrivenProducer.cc",
    "RecoEgamma/EgammaElectronProducers/plugins/GsfElectronBaseProducer.h",
    "RecoEgamma/EgammaElectronProducers/plugins/GsfElectronBaseProducer.cc",
    "RecoEgamma/EgammaElectronProducers/python/gsfElectrons_cfi.py",
    #"RecoEgamma/EgammaElectronProducers/plugins/ElectronSeedProducer.cc",
    
    "RecoEcal/EgammaClusterAlgos/src/PFECALSuperClusterAlgo.cc",
    
    "RecoEcal/EgammaClusterProducers/src/PFECALSuperClusterProducer.cc",
]


for iFile in range(0, len(l_file)) :
    
    fileName =  l_file[iFile]
    fileDir = fileName[0: fileName.rfind("/")]
    
    #cmdStr = "rsync -asP -e ssh %s %s sobhatta@lxplus.cern.ch:%s/%s/" %(RSYNC_EXTRAFLAGS, fileName, DEST, fileDir)
    cmdStr = "rsync -asP -e ssh %s %s %s/%s/" %(RSYNC_EXTRAFLAGS, fileName, DEST, fileDir)
    
    print cmdStr
    
    cmdStr = "sshpass -p \"%s\" %s" %(PWD, cmdStr)
    
    os.system(cmdStr)
    
    print "\n"
