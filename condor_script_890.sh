#!/bin/sh

DIR=/afs/cern.ch/work/s/sobhatta/private/HGCal_ele-reco/production/CMSSW_11_1_0_pre3/src

echo "Working directory: "$DIR
cd $DIR
echo "Moved to working directory."

export SCRAM_ARCH=slc7_amd64_gcc820
export CPATH=$CPATH:$DIR
export ROOT_INCLUDE_PATH=$ROOT_INCLUDE_PATH:$DIR

# Proxy path must be common to all nodes
# Default path is /tmp/, but thatis not common for all nodes
export X509_USER_PROXY=/afs/cern.ch/user/s/sobhatta/proxies/x509up_u84631

source /cvmfs/cms.cern.ch/cmsset_default.sh

eval cmsenv

#echo "Creating voms-proxy..."
#eval vpxy
echo "Proxy info:"
voms-proxy-info -all
echo ""

cmsRun MyModules/Test/python/reco_test_RAW2DIGI_L1Reco_RECO_RECOSIM_withTICL_mod.py \
	 print \
	 sourceFile=condorJobs/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-RECO/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-DIGI-RAW_890.txt \
	 outputDir=./ \
	 outFileNumber=890 \

