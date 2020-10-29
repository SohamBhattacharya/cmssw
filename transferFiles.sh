#!/bin/bash

DEST="/afs/cern.ch/work/s/sobhatta/private/HGCal_ele-reco/CMSSW_11_0_0_pre9/src"

RSYNC_EXTRAFLAGS=""

rsync -asP $RSYNC_EXTRAFLAGS RecoParticleFlow/PFClusterProducer/plugins/PFClusterFromHGCalMultiCluster.cc \
    sobhatta@lxplus.cern.ch:$DEST/RecoParticleFlow/PFClusterProducer/plugins/
