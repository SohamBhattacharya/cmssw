#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --varROC \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p15)" \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p15_clusET1_trkDz0p15_trkPt1)" \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p3)" \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p3_clusET1_trkDz0p15_trkPt1)" \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p4)" \
#        "min(5.0, gsfEleFromTICL_iso_sumETratio_dR0p4_clusET1_trkDz0p15_trkPt1)" \
#    --cutSig \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --cutBkg \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#    --cutVars \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "I^{clus}_{0.15}" \
#        "I^{clus}_{0.15} (E_{T}>1GeV)" \
#        "I^{clus}_{0.3}" \
#        "I^{clus}_{0.3} (E_{T}>1GeV)" \
#        "I^{clus}_{0.4}" \
#        "I^{clus}_{0.4} (E_{T}>1GeV)" \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#        8 \
#        8 \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#        7 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 8e-3 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
#    --legendPos "UL" \
#    --outDir "plots/ROC_ID" \
#    --outFileName "gsfEleFromTICL_iso_sumETratio_PU200"



#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --varROC \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p15/gsfEleFromTICL_pT)" \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p15_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT)" \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p3/gsfEleFromTICL_pT)" \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p3_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT)" \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p4/gsfEleFromTICL_pT)" \
#        "min(5.0, gsfEleFromTICL_iso_trackSumPt_dR0p4_clusET1_trkDz0p15_trkPt1/gsfEleFromTICL_pT)" \
#    --cutSig \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --cutBkg \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#    --cutVars \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "I^{trk}_{0.15}" \
#        "I^{trk}_{0.15} (p_{T}>1GeV, dz<0.15cm)" \
#        "I^{trk}_{0.3}" \
#        "I^{trk}_{0.3} (p_{T}>1GeV, dz<0.15cm)" \
#        "I^{trk}_{0.4}" \
#        "I^{trk}_{0.4} (p_{T}>1GeV, dz<0.15cm)" \
#    --lineColorList \
#        2 \
#        2 \
#        4 \
#        4 \
#        8 \
#        8 \
#    --lineStyleList \
#        1 \
#        7 \
#        1 \
#        7 \
#        1 \
#        7 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 8e-3 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
#    --legendPos "LL" \
#    --outDir "plots/ROC_ID" \
#    --outFileName "gsfEleFromTICL_iso_trackSumPtRatio_PU200"



python -u -W ignore plotROC.py \
    --nEventMax 500000 \
    --sigFiles \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
    --bkgFiles \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --varROC \
        "min(5.0, gsfEleFromTICL_HoverE_dR0p15)" \
        "min(5.0, gsfEleFromTICL_HoverE_dR0p2)" \
        "min(5.0, gsfEleFromTICL_HoverE_dR0p3)" \
    --cutSig \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
    --cutBkg \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
    --cutVars \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_genEl_minDeltaR" \
    --comparison \
        "<" \
        "<" \
        "<" \
    --labelList \
        "H/E_{0.15}" \
        "H/E_{0.2}" \
        "H/E_{0.3}" \
    --lineColorList \
        2 \
        4 \
        6 \
    --lineStyleList \
        1 \
        1 \
        1 \
    --detailSig "Sig.: Electron" \
    --detailBkg "Bkg.: Jet" \
    --xMin 0.7 \
    --xMax 1.0 \
    --yMin 8e-3 \
    --yMax 1.0 \
    --logY \
    --detailROC "" \
    --detailPos 0.75 0.95 \
    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
    --legendPos "UL" \
    --outDir "plots/ROC_ID" \
    --outFileName "gsfEleFromTICL_HoverE_PU200"



python -u -W ignore plotROC.py \
    --nEventMax 500000 \
    --sigFiles \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
    --bkgFiles \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --varROC \
        "gsfEleFromTICL_Rvar_cylR2p0" \
        "gsfEleFromTICL_Rvar_cylR2p8" \
        "gsfEleFromTICL_Rvar_cylR3p5" \
    --cutSig \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR3p5" \
    --cutBkg \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_Rvar_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_Rvar_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_Rvar_cylR3p5" \
    --cutVars \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_genEl_minDeltaR" \
    --comparison \
        ">" \
        ">" \
        ">" \
    --labelList \
        "R_{2.0}" \
        "R_{2.8}" \
        "R_{3.5}" \
    --lineColorList \
        2 \
        4 \
        6 \
    --lineStyleList \
        1 \
        1 \
        1 \
    --detailSig "Sig.: Electron" \
    --detailBkg "Bkg.: Jet" \
    --xMin 0.7 \
    --xMax 1.0 \
    --yMin 9e-2 \
    --yMax 1.0 \
    --logY \
    --detailROC "" \
    --detailPos 0.75 0.95 \
    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
    --legendPos "UL" \
    --outDir "plots/ROC_ID" \
    --outFileName "gsfEleFromTICL_Rvar_PU200"



python -u -W ignore plotROC.py \
    --nEventMax 500000 \
    --sigFiles \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
    --bkgFiles \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --varROC \
        "sqrt(gsfEleFromTICL_sigma2uu_cylR2p0)" \
        "sqrt(gsfEleFromTICL_sigma2uu_cylR2p8)" \
        "sqrt(gsfEleFromTICL_sigma2uu_cylR3p5)" \
    --cutSig \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2uu_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2uu_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2uu_cylR3p5" \
    --cutBkg \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2uu_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2uu_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2uu_cylR3p5" \
    --cutVars \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_genEl_minDeltaR" \
    --comparison \
        "<" \
        "<" \
        "<" \
    --labelList \
        "#sigma_{uu} (R_{cyl}=2.0cm)" \
        "#sigma_{uu} (R_{cyl}=2.8cm)" \
        "#sigma_{uu} (R_{cyl}=3.5cm)" \
    --lineColorList \
        2 \
        4 \
        6 \
    --lineStyleList \
        1 \
        1 \
        1 \
    --detailSig "Sig.: Electron" \
    --detailBkg "Bkg.: Jet" \
    --xMin 0.7 \
    --xMax 1.0 \
    --yMin 9e-2 \
    --yMax 1.0 \
    --logY \
    --detailROC "" \
    --detailPos 0.75 0.95 \
    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
    --legendPos "UL" \
    --outDir "plots/ROC_ID" \
    --outFileName "gsfEleFromTICL_sigmaUU_PU200"



python -u -W ignore plotROC.py \
    --nEventMax 500000 \
    --sigFiles \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
    --bkgFiles \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --varROC \
        "sqrt(gsfEleFromTICL_sigma2vv_cylR2p0)" \
        "sqrt(gsfEleFromTICL_sigma2vv_cylR2p8)" \
        "sqrt(gsfEleFromTICL_sigma2vv_cylR3p5)" \
    --cutSig \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2vv_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2vv_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2vv_cylR3p5" \
    --cutBkg \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2vv_cylR2p0" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2vv_cylR2p8" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2vv_cylR3p5" \
    --cutVars \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_genEl_minDeltaR" \
    --comparison \
        "<" \
        "<" \
        "<" \
    --labelList \
        "#sigma_{vv} (R_{cyl}=2.0cm)" \
        "#sigma_{vv} (R_{cyl}=2.8cm)" \
        "#sigma_{vv} (R_{cyl}=3.5cm)" \
    --lineColorList \
        2 \
        4 \
        6 \
    --lineStyleList \
        1 \
        1 \
        1 \
    --detailSig "Sig.: Electron" \
    --detailBkg "Bkg.: Jet" \
    --xMin 0.7 \
    --xMax 1.0 \
    --yMin 9e-2 \
    --yMax 1.0 \
    --logY \
    --detailROC "" \
    --detailPos 0.75 0.95 \
    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
    --legendPos "UL" \
    --outDir "plots/ROC_ID" \
    --outFileName "gsfEleFromTICL_sigmaVV_PU200"



#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --varROC \
#        "sqrt(gsfEleFromTICL_sigma2ww_cylR2p0)" \
#        "sqrt(gsfEleFromTICL_sigma2ww_cylR2p8)" \
#        "sqrt(gsfEleFromTICL_sigma2ww_cylR3p5)" \
#    --cutSig \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2ww_cylR2p0" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2ww_cylR2p8" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_sigma2ww_cylR3p5" \
#    --cutBkg \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2ww_cylR2p0" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2ww_cylR2p8" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4 && gsfEleFromTICL_sigma2ww_cylR3p5" \
#    --cutVars \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "#sigma_{ww} (R_{cyl}=2.0cm)" \
#        "#sigma_{ww} (R_{cyl}=2.8cm)" \
#        "#sigma_{ww} (R_{cyl}=3.5cm)" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 9e-2 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
#    --legendPos "UL" \
#    --outDir "plots/ROC_ID" \
#    --outFileName "gsfEleFromTICL_sigmaWW_PU200"



#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    --treeNames \
#        "treeMaker/tree" \
#    --varROC \
#        "(gsfEleFromTICL_superClus_sigma2etaEta)**0.5" \
#    --cutSig \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --cutBkg \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#    --cutVars \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "#sigma_{#eta#eta}" \
#    --lineColorList \
#        2 \
#    --lineStyleList \
#        1 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 9e-2 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
#    --legendPos "UL" \
#    --outDir "plots/ROC_ID" \
#    --outFileName "gsfEleFromTICL_sigmaEtaEta_PU200"
#
#
#
#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW/TreeMaker_TTToSemiLepton_TuneCP5_14TeV-powheg-pythia8_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3-v2_GEN-SIM-DIGI-RAW.txt \
#    --treeNames \
#        "treeMaker/tree" \
#    --varROC \
#        "(gsfEleFromTICL_superClus_sigma2phiPhi)**0.5" \
#    --cutSig \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --cutBkg \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR > 0.4" \
#    --cutVars \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "#sigma_{#phi#phi}" \
#    --lineColorList \
#        2 \
#    --lineStyleList \
#        1 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 9e-2 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{Phase-II HGCal (PU 200)}" \
#    --legendPos "UL" \
#    --outDir "plots/ROC_ID" \
#    --outFileName "gsfEleFromTICL_sigmaPhiPhi_PU200"



#python -u -W ignore plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        /media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root \
#        /media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root \
#    --bkgFiles \
#        /media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root \
#        /media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root \
#    --treeNames \
#        "dataset/TrainTree" \
#        "dataset/TestTree" \
#    --varROC \
#        "BDT" \
#        "BDT" \
#    --cutSig \
#        "classID == 0" \
#        "classID == 0" \
#    --cutBkg \
#        "classID == 1" \
#        "classID == 1" \
#    --cutVars \
#        "classID" \
#        "classID" \
#    --comparison \
#        ">" \
#        ">" \
#    --labelList \
#        "BDT (Train)" \
#        "BDT (Test)" \
#    --lineColorList \
#        2 \
#        4 \
#    --lineStyleList \
#        1 \
#        1 \
#    --detailSig "Sig.: Electron" \
#    --detailBkg "Bkg.: Jet" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 1e-3 \
#    --yMax 1.0 \
#    --logY \
#    --detailROC "" \
#    --detailPos 0.75 0.95 \
#    --legendTitle "#scale[1.2]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}" \
#    --legendPos "UL" \
#    --outDir "plots/ID_TMVA/ROC" \
#    --outFileName "TMVA_BDT"
