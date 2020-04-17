cmsRun MyModules/Test/python/reco_test_RAW2DIGI_L1Reco_RECO_RECOSIM_withTICL_mod.py \
    sourceFile=sourceFiles/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-DIGI-RAW/SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-DIGI-RAW.txt \
    outputFile=output_modRECO.root \
    maxEvents=5 \
    keepList=\
*_*particleFlowRecHitHGC*_*_*,\
*_particleFlowClusterECAL_*_*,\
*_siPhase2Clusters_*_*,\
*_siStripDigis_*_*,\
*_siPixelClusters_*_*,\
*_siPixelClustersCache_*_*,\
*_siPixelClusterShapeCache_*_*,\
*_siPixelRecHits*_*_*,\
*_trackerDrivenElectronSeeds_*_*,\
*_pfTrackElec_*_*,\
*_tracksters*_*_*,\
*_ecalDrivenGsfElectrons*_*_*,\
*_*FromTICL*_*_*,\
\
*_generator_*_*,\
*_genParticles_*_*,\
*_addPileupInfo_*_*,\
*_fixedGridRhoFastjetAll_*_*,\
*_g4SimHits_*_*,\
*_HGCalRecHit_*_*,\
*_mix_MergedCaloTruth_*,\
*_*FromMultiCl_*_*,\
\
*_ecalRecHit_*_*,\
*_hbhereco_*_*,\
*_horeco_*_*,\
*_hfreco_*_*,\
*_towerMaker_*_*,\
*_*BeamSpot*_*_*,\
*_offlinePrimaryVertices_*_*,\
\
*_allConversions_*_*,\
*_particleFlowSuperClusterECAL_*_*,\
*_generalTracks_*_*,\
