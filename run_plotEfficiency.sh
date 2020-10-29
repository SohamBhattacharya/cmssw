#!/usr/bin/env python3

import multiprocessing
import os


nCPU = multiprocessing.cpu_count()-1

pool = multiprocessing.Pool(processes = nCPU)
l_job = []


def cleanSpaces(string) :
    
    while ("  " in string) :
        
        string = string.replace("  ", " ")
    
    return string



# ########## sigEff_vs_pileup_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "pileup_n" \
#        "pileup_n" \
#        "pileup_n" \
#    --plotDenList \
#        "pileup_n" \
#        "pileup_n" \
#        "pileup_n" \
#    --cutNumList \
#        "classID == 0 && BDT > 0.1688" \
#        "classID == 0 && BDT > 0.1427" \
#        "classID == 0 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 0" \
#        "classID == 0" \
#        "classID == 0" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "N_{PU}" \
#    --yTitle "Signal efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 30 \
#    --xMinDraw 150 \
#    --xMaxDraw 250 \
#    --yMin 0 \
#    --yMax 1 \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "LL" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "sigEff_vs_pileup_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
# ########## bkgEff_vs_pileup_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "pileup_n" \
#        "pileup_n" \
#        "pileup_n" \
#    --plotDenList \
#        "pileup_n" \
#        "pileup_n" \
#        "pileup_n" \
#    --cutNumList \
#        "classID == 1 && BDT > 0.1688" \
#        "classID == 1 && BDT > 0.1427" \
#        "classID == 1 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 1" \
#        "classID == 1" \
#        "classID == 1" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "N_{PU}" \
#    --yTitle "Background efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 30 \
#    --xMinDraw 150 \
#    --xMaxDraw 250 \
#    --yMin 1e-3 \
#    --yMax 1 \
#    --logY \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "UR" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "bkgEff_vs_pileup_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
# ########## sigEff_vs_pT_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --plotDenList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --cutNumList \
#        "classID == 0 && BDT > 0.1688" \
#        "classID == 0 && BDT > 0.1427" \
#        "classID == 0 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 0" \
#        "classID == 0" \
#        "classID == 0" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "p_{T}" \
#    --yTitle "Signal efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 30 \
#    --xMinDraw 15 \
#    --xMaxDraw 200 \
#    --yMin 0 \
#    --yMax 1 \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "LR" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "sigEff_vs_pT_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
# ########## bkgEff_vs_pT_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --plotDenList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --cutNumList \
#        "classID == 1 && BDT > 0.1688" \
#        "classID == 1 && BDT > 0.1427" \
#        "classID == 1 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 1" \
#        "classID == 1" \
#        "classID == 1" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "p_{T}" \
#    --yTitle "Background efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 30 \
#    --xMinDraw 15 \
#    --xMaxDraw 200 \
#    --yMin 1e-3 \
#    --yMax 1 \
#    --logY \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "UR" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "bkgEff_vs_pT_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
# ########## sigEff_vs_eta_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#    --plotDenList \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#    --cutNumList \
#        "classID == 0 && BDT > 0.1688" \
#        "classID == 0 && BDT > 0.1427" \
#        "classID == 0 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 0" \
#        "classID == 0" \
#        "classID == 0" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "#||{#eta}" \
#    --yTitle "Signal efficiency" \
#    --xMin 0 \
#    --xMax 4 \
#    --nBinX 40 \
#    --xMinDraw 1.4 \
#    --xMaxDraw 3.1 \
#    --yMin 0 \
#    --yMax 1 \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "LR" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "sigEff_vs_eta_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)
#
#
#
# ########## bkgEff_vs_eta_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#        "/media/soham/D/Programs/TIFR/serviceTask_HGCal_ele-reco/ID/TMVA/result/TMVA.root" \
#    --treeNames \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#        "dataset/TrainTree:dataset/TestTree" \
#    --plotNumList \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#    --plotDenList \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#        "fabs_gsfEleFromTICL_eta_" \
#    --cutNumList \
#        "classID == 1 && BDT > 0.1688" \
#        "classID == 1 && BDT > 0.1427" \
#        "classID == 1 && BDT > 0.1038" \
#    --cutDenList \
#        "classID == 1" \
#        "classID == 1" \
#        "classID == 1" \
#    --labelList \
#        "70% sig. eff. WP" \
#        "80% sig. eff. WP" \
#        "90% sig. eff. WP" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#    --xTitle "#||{#eta}" \
#    --yTitle "Background efficiency" \
#    --xMin 0 \
#    --xMax 4 \
#    --nBinX 40 \
#    --xMinDraw 1.4 \
#    --xMaxDraw 3.1 \
#    --yMin 1e-3 \
#    --yMax 1 \
#    --logY \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "UR" \
#    --legendTextSize 0.04 \
#    --outDir "plots/ID_TMVA/efficiencies" \
#    --outFileName "bkgEff_vs_eta_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



# ########## HoverE sigEff_vs_pT_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --plotNumList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --plotDenList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --cutNumList \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (3.0/gsfEleFromTICL_pT + 0.15)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (5.0/gsfEleFromTICL_pT + 0.15)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (7.0/gsfEleFromTICL_pT + 0.15)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (3.0/gsfEleFromTICL_pT + 0.10)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (5.0/gsfEleFromTICL_pT + 0.10)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_HoverE_dR0p15 < (7.0/gsfEleFromTICL_pT + 0.10)" \
#    --cutDenList \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --labelList \
#        "H/E_{0.15}<3.0/p_{T}+0.15" \
#        "H/E_{0.15}<5.0/p_{T}+0.15" \
#        "H/E_{0.15}<7.0/p_{T}+0.15" \
#        "H/E_{0.15}<3.0/p_{T}+0.10" \
#        "H/E_{0.15}<5.0/p_{T}+0.10" \
#        "H/E_{0.15}<7.0/p_{T}+0.10" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#        7 \
#        7 \
#        7 \
#    --xTitle "p^{reco}_{T}" \
#    --yTitle "Signal efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 60 \
#    --xMinDraw 15 \
#    --xMaxDraw 200 \
#    --yMin 0.7 \
#    --yMax 1 \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "UR" \
#    --legendTextSize 0.03 \
#    --outDir "plots/efficiencies" \
#    --outFileName "gsfEleFromTICL_HoverE_sigEff_vs_pT_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



# ########## sigmaUU sigEff_vs_pT_PU200 ##########
#cmdStr = """ \
#    python -u plotEfficiency.py \
#    --inputFiles \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
#    --treeNames \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#        "treeMaker/tree" \
#    --plotNumList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --plotDenList \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#        "gsfEleFromTICL_pT" \
#    --cutNumList \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (20/gsfEleFromTICL_pT + 1.3)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (30/gsfEleFromTICL_pT + 1.3)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (35/gsfEleFromTICL_pT + 1.3)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (20/gsfEleFromTICL_pT + 1.5)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (30/gsfEleFromTICL_pT + 1.5)" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && sqrt(gsfEleFromTICL_sigma2uu_cylR2p8) < (35/gsfEleFromTICL_pT + 1.5)" \
#    --cutDenList \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
#    --labelList \
#        "#sigma_{uu}<20/p_{T}+1.3" \
#        "#sigma_{uu}<30/p_{T}+1.3" \
#        "#sigma_{uu}<35/p_{T}+1.3" \
#        "#sigma_{uu}<20/p_{T}+1.5" \
#        "#sigma_{uu}<30/p_{T}+1.5" \
#        "#sigma_{uu}<35/p_{T}+1.5" \
#    --lineColorList \
#        2 \
#        4 \
#        6 \
#        2 \
#        4 \
#        6 \
#    --lineStyleList \
#        1 \
#        1 \
#        1 \
#        7 \
#        7 \
#        7 \
#    --drawStyle \
#        "hist" \
#    --xTitle "p^{reco}_{T}" \
#    --yTitle "Signal efficiency" \
#    --xMin 0 \
#    --xMax 300 \
#    --nBinX 60 \
#    --xMinDraw 15 \
#    --xMaxDraw 200 \
#    --yMin 0.85 \
#    --yMax 1 \
#    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
#    --legendPos "LR" \
#    --legendTextSize 0.03 \
#    --outDir "plots/efficiencies" \
#    --outFileName "gsfEleFromTICL_sigmaUU_sigEff_vs_pT_PU200" \
#"""
#
#cmdStr = cleanSpaces(cmdStr)
#job = pool.apply_async(os.system, (), dict(command = cmdStr))
#l_job.append(job)



 ########## R2p8 sigEff_vs_pT_PU200 ##########
cmdStr = """ \
    python -u plotEfficiency.py \
    --inputFiles \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
        "sourceFiles/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO/TreeMaker_SingleElectron_PT2to200_Phase2HLTTDRWinter20DIGI-PU200_110X_mcRun4_realistic_v3_ext2-v2_GEN-SIM-modRECO.txt" \
    --treeNames \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
        "treeMaker/tree" \
    --plotNumList \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
    --plotDenList \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
        "gsfEleFromTICL_pT" \
    --cutNumList \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.02*(gsfEleFromTICL_pT+10))" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.02*(gsfEleFromTICL_pT+30))" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.02*(gsfEleFromTICL_pT+50))" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.03*(gsfEleFromTICL_pT+10))" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.03*(gsfEleFromTICL_pT+30))" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4 && gsfEleFromTICL_Rvar_cylR2p8 > 0.8-exp(-0.03*(gsfEleFromTICL_pT+50))" \
    --cutDenList \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
        "gsfEleFromTICL_pT > 15 && gsfEleFromTICL_genEl_minDeltaR < 0.4" \
    --labelList \
        "R_{2.8}>0.8-exp(-0.02(p_{T}+10))" \
        "R_{2.8}>0.8-exp(-0.02(p_{T}+30))" \
        "R_{2.8}>0.8-exp(-0.02(p_{T}+50))" \
        "R_{2.8}>0.8-exp(-0.03(p_{T}+10))" \
        "R_{2.8}>0.8-exp(-0.03(p_{T}+30))" \
        "R_{2.8}>0.8-exp(-0.03(p_{T}+50))" \
    --lineColorList \
        2 \
        4 \
        6 \
        2 \
        4 \
        6 \
    --lineStyleList \
        1 \
        1 \
        1 \
        7 \
        7 \
        7 \
    --drawStyle \
        "hist" \
    --xTitle "p^{reco}_{T}" \
    --yTitle "Signal efficiency" \
    --xMin 0 \
    --xMax 300 \
    --nBinX 60 \
    --xMinDraw 15 \
    --xMaxDraw 200 \
    --yMin 0.85 \
    --yMax 1 \
    --legendTitle "#scale[1.1]{#splitline{Phase-II HGCal (PU 200)}{Electron vs. jet}}"\
    --legendPos "LR" \
    --legendTextSize 0.03 \
    --outDir "plots/efficiencies" \
    --outFileName "gsfEleFromTICL_R2p8_sigEff_vs_pT_PU200" \
"""

cmdStr = cleanSpaces(cmdStr)
job = pool.apply_async(os.system, (), dict(command = cmdStr))
l_job.append(job)



# Close the pool and wait for jobs to complete
pool.close()
pool.join()

for iJob, job in enumerate(l_job) :
    
    job.get()
