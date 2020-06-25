#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --varROC \
#        "slimmedEle_iso_sumETratio_charged_dR0p3" \
#        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5" \
#        "slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3" \
#        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2" \
#        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3" \
#        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4" \
#    --cutSig \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#    --cutBkg \
#        "slimmedEle_pT > 15" \
#        "slimmedEle_pT > 15" \
#        "slimmedEle_pT > 15" \
#        "slimmedEle_pT > 15" \
#        "slimmedEle_pT > 15" \
#        "slimmedEle_pT > 15" \
#    --cutVars \
#        "slimmedEle_pT" \
#        "slimmedEle_genEl_minDeltaR" \
#    --comparison \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#        "<" \
#    --labelList \
#        "I^{ch}_{0.3}" \
#        "I^{ch}_{0.3} (dz<0.5cm)" \
#        "I^{ch}_{0.3} (#sigma_{t}<3)" \
#        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<2)" \
#        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<3)" \
#        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<4)" \
#    --lineColorList \
#        2 \
#        4 \
#        8 \
#        6 \
#        6 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#        7 \
#        1 \
#        9 \
#    --detailSig "#splitline{I_{0.3}}{Sig.: ZEE}" \
#    --detailBkg "Bkg.: QCD" \
#    --xMin 0.6 \
#    --xMax 1.0 \
#    --yMin 0.05 \
#    --yMax 1 \
#    --logY \
#    --legendTitle "#scale[1.2]{Phase-II EB (PU 200)}" \
#    --legendPos "UL" \
#    --outDir "plots/ROC" \
#    --outFileName "slimmedEle_iso_sumETratio_charged_ZEE-QCD_PU200"



python -u plotROC.py \
    --nEventMax 500000 \
    --sigFiles \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
    --bkgFiles \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --varROC \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5" \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2" \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3" \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4" \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt5" \
        "slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt6" \
    --cutSig \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
        "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
    --cutBkg \
        "slimmedEle_pT > 15" \
        "slimmedEle_pT > 15" \
        "slimmedEle_pT > 15" \
        "slimmedEle_pT > 15" \
        "slimmedEle_pT > 15" \
        "slimmedEle_pT > 15" \
    --cutVars \
        "slimmedEle_pT" \
        "slimmedEle_genEl_minDeltaR" \
    --comparison \
        "<" \
        "<" \
        "<" \
        "<" \
        "<" \
        "<" \
    --labelList \
        "I^{ch}_{0.3} (dz<0.5cm)" \
        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<2)" \
        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<3)" \
        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<4)" \
        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<5)" \
        "I^{ch}_{0.3} (dz<0.5cm, #sigma_{t}<6)" \
    --lineColorList \
        2 \
        4 \
        6 \
        8 \
        5 \
        7 \
    --lineStyleList \
        1 \
        1 \
        1 \
        1 \
        1 \
        1 \
    --detailSig "#splitline{I_{0.3}}{Sig.: ZEE}" \
    --detailBkg "Bkg.: QCD" \
    --xMin 0.7 \
    --xMax 1.0 \
    --yMin 0.08 \
    --yMax 0.2 \
    --legendTitle "#scale[1.2]{Phase-II EB (PU 200)}" \
    --legendPos "UL" \
    --outDir "plots/ROC" \
    --outFileName "slimmedEle_iso_sumETratio_charged_dzCut_dTsigniCut_ZEE-QCD_PU200"



#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --treeNames "treeMaker/tree" \
#    --varROC "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma" \
#    --cutSig "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#    --cutBkg "slimmedEle_pT > 15" \
#    --cutVars \
#        "slimmedEle_pT" \
#        "slimmedEle_genEl_minDeltaR" \
#    --comparison "<" \
#    --detailSig "#splitline{I^{cleaned}_{0.3} (#sigma_{t}<3)}{Sig.: ZEE}" \
#    --detailBkg "Bkg.: QCD" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 1e-1 \
#    --yMax 1 \
#    --detailROC "#scale[1]{Phase-II EB (PU 200)}" \
#    --detailPos 0.4 0.95 \
#    --legendPos "UR" \
#    --outDir "plots/ROC" \
#    --outFileName "slimmedEle_isoDR0p3_sumETratio_cleanedDT3sigma_ZEE-QCD_PU200"


#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        sourceFiles/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValZEE_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --bkgFiles \
#        sourceFiles/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM.txt \
#    --treeNames "treeMaker/tree" \
#    --varROC "slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues" \
#    --cutSig "slimmedEle_pT > 15 and slimmedEle_genEl_minDeltaR < 0.4" \
#    --cutBkg "slimmedEle_pT > 15" \
#    --cutVars \
#        "slimmedEle_pT" \
#        "slimmedEle_genEl_minDeltaR" \
#    --comparison ">" \
#    --detailSig "#splitline{Fall17IsoV2}{Sig.: ZEE}" \
#    --detailBkg "Bkg.: QCD" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 1e-4 \
#    --yMax 1 \
#    --logY \
#    --detailROC "#scale[1]{Phase-II EB (PU 200)}" \
#    --detailPos 0.825 0.8 \
#    --legendPos "UR" \
#    --outDir "plots/ROC" \
#    --outFileName "slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues_ZEE-QCD_PU200"


#python -u plotROC.py \
#    --nEventMax 500000 \
#    --sigFiles \
#        TMVA.root \
#    --bkgFiles \
#        TMVA.root \
#    --treeNames "TrainTree" "TestTree" \
#    --varROC "BDT" \
#    --cutSig "classID == 0" \
#    --cutBkg "classID == 1" \
#    --cutVars \
#        "classID" \
#    --comparison ">" \
#    --detailSig "#splitline{Fall17IsoV2+dz+MTD}{Sig.: ZEE}" \
#    --detailBkg "Bkg.: QCD" \
#    --xMin 0.7 \
#    --xMax 1.0 \
#    --yMin 1e-4 \
#    --yMax 1 \
#    --logY \
#    --detailROC "#scale[1]{Phase-II EB (PU 200)}" \
#    --detailPos 0.825 0.8 \
#    --legendPos "UR" \
#    --outDir "plots/TMVA/" \
#    --outFileName "BDT"

