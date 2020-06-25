from __future__ import print_function

import argparse
import array
import copy
import getpass
#import matplotlib
#matplotlib.use("Agg")
#import matplotlib.pyplot
#import mxnet
import multiprocessing
import numpy
import os
import pprint
import scipy
import scipy.interpolate
import scipy.special
import tabulate
import time

import Common

import ROOT


def getEfficiency(arr, val, norm = 1.0, comparison = "<") :
    
    if (comparison == ">") :
        
        eff = float(sum(arr > val)) / norm
    
    elif (comparison == "<") :
        
        eff = float(sum(arr < val)) / norm
    
    else :
        
        print("Error in getEfficiency(...): Invalid comparison \"%s\"" %(comparison))
    
    return eff


pprinter = pprint.PrettyPrinter(width = 500, depth = 2)


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)


parser.add_argument(
    "--nEventMax",
    help = "Number of signal and background (each) events to be used",
    type = int,
    required = False,
    default = 500000,
)

#parser.add_argument(
#    "--splitEvery",
#    help = "Load how many images per (multiprocessing) process",
#    type = int,
#    required = False,
#    default = 20000,
#)

parser.add_argument(
    "--sigFiles",
    help = "File containing the list of input files OR :-separated list of inputfiles",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--bkgFiles",
    help = "File containing the list of input files OR :-separated list of inputfiles",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--treeNames",
    help = "List of tree names",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--varROC",
    help = "Variable to be used for evaluating the ROC",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--cutSig",
    help = "Selection on signal",
    type = str,
    nargs = "*",
    required = False,
    default = "1"
)

parser.add_argument(
    "--cutBkg",
    help = "Selection on background",
    type = str,
    nargs = "*",
    required = False,
    default = "1"
)

parser.add_argument(
    "--cutVars",
    help = "List of the variables used in the cuts",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--comparison",
    help = "Comparison to use for the ROC variable cut (>, <)",
    type = str,
    nargs = "*",
    required = True,
    choices = [">", "<"],
)

parser.add_argument(
    "--labelList",
    help = "List of plot labels",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--lineColorList",
    help = "List of line colors",
    type = int,
    nargs = "*",
    required = False,
)

parser.add_argument(
    "--lineStyleList",
    help = "List of line styles",
    type = int,
    nargs = "*",
    required = False,
)


parser.add_argument(
    "--logY",
    help = "Y-axis in log scale",
    default = False,
    action = "store_true",
)

parser.add_argument(
    "--xMin",
    help = "X-axis minumum",
    type = float,
    required = False,
    default = 0,
)

parser.add_argument(
    "--xMax",
    help = "X-axis maximum",
    type = float,
    required = False,
    default = 1.0,
)

parser.add_argument(
    "--yMin",
    help = "Y-axis minumum",
    type = float,
    required = False,
    default = 1e-5,
)

parser.add_argument(
    "--yMax",
    help = "Y-axis maximum",
    type = float,
    required = False,
    default = 1.0,
)

parser.add_argument(
    "--title",
    help = "Plot title",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--detailROC",
    help = "ROC variable detail",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--detailSig",
    help = "Training detail for signal",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--detailBkg",
    help = "Training detail for background",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--detailPos",
    help = "Position of the detail (LL coordinate)",
    type = float,
    nargs = 2,
    required = False,
    default = [0, 0],
)

parser.add_argument(
    "--legendTitle",
    help = "Title of the legend",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--legendPos",
    help = "Position of the legend (UR, LR, UL)",
    type = str,
    required = False,
    default = "UR",
)

parser.add_argument(
    "--outDir",
    help = "Output directory",
    type = str,
    required = True,
)

parser.add_argument(
    "--outFileName",
    help = "Output file name (\"ROC_\" will be appended to this)",
    type = str,
    required = True,
)


# Parse arguments
args = parser.parse_args()
d_args = vars(args)


l_histDetail = []

for iROC in range(0, len(args.varROC)) :
    
    sigFiles = args.sigFiles[iROC]
    bkgFiles = args.bkgFiles[iROC]
    
    if (".root" in sigFiles) :
        
        l_inFileName_sig = sigFiles.split(":")
    
    else :
        
        l_inFileName_sig = numpy.loadtxt(sigFiles, delimiter = "someNonExistantString", dtype = str, ndmin = 1)
    
    
    if (".root" in bkgFiles) :
        
        l_inFileName_bkg = bkgFiles.split(":")
    
    else :
        
        l_inFileName_bkg = numpy.loadtxt(bkgFiles, delimiter = "someNonExistantString", dtype = str, ndmin = 1)
    
    
    tree_sig = ROOT.TChain("chain_sig")
    tree_bkg = ROOT.TChain("chain_bkg")
    
    l_treeName = args.treeNames[iROC].split(":")
    
    for iTree, treeName in enumerate(l_treeName) :
        
        for iFile in range(0, len(l_inFileName_sig)) :
            
            tree_sig.AddFile(l_inFileName_sig[iFile], -1, treeName)
        
        for iFile in range(0, len(l_inFileName_bkg)) :
            
            tree_bkg.AddFile(l_inFileName_bkg[iFile], -1, treeName)
    
    nEvent_tree_sig = tree_sig.GetEntries()
    nEvent_tree_bkg = tree_bkg.GetEntries()
    
    outFileName_ROC = "%s/ROC_%s" %(args.outDir, args.outFileName)
    outFileName_config = "%s/ROC_%s_config.txt" %(args.outDir, args.outFileName)
    
    
    os.system("mkdir -p %s" %(outFileName_ROC[:outFileName_ROC.rfind("/")]))
    
    
    # Save the configuration
    
    print("Saving the configuration to: %s" %(outFileName_config))
    
    with open(outFileName_config, "w") as configOutFile :
        
        configOutFile.write(pprint.pformat(d_args, width = 1))
        configOutFile.write("\n")
    
    print("\n")
    
    
    a_var_sig = Common.getArrayFromTBranch(
        tree = tree_sig,
        varName = args.varROC[iROC],
        l_cutVar = args.cutVars,
        cutStr = args.cutSig[iROC],
        nSel_max = args.nEventMax,
    )
    
    
    a_var_bkg = Common.getArrayFromTBranch(
        tree = tree_bkg,
        varName = args.varROC[iROC],
        l_cutVar = args.cutVars,
        cutStr = args.cutBkg[iROC],
        nSel_max = args.nEventMax,
    )
    
    
    discMin = min(min(a_var_sig), min(a_var_bkg))
    discMax = max(max(a_var_sig), max(a_var_bkg))
    disc_nSample = 4000
    disc_stepSize = float(discMax-discMin) / disc_nSample
    #disc_stepSize_small = disc_stepSize / 500.0
    
    l_discr = numpy.arange(discMin, discMax, disc_stepSize)
    
    
    l_eff_sig = numpy.zeros(len(l_discr)+2)
    l_eff_bkg = numpy.zeros(len(l_discr)+2)
    
    # The first/last point will be (1, 1)/(0, 0)
    # So include these
    #l_eff_sig = [1.0]
    #l_eff_bkg = [1.0]
    l_eff_sig[0] = 1.0
    l_eff_bkg[0] = 1.0
    
    
    nCPU = min(multiprocessing.cpu_count(), len(l_eff_sig))
    
    pool = multiprocessing.Pool(processes = nCPU)
    
    l_job_sig = []
    l_job_bkg = []
    
    nEventTot_sig = a_var_sig.shape[0]
    nEventTot_bkg = a_var_bkg.shape[0]
    
    print("\n")
    print("Calculating signal and background efficiencies. \n")
    
    
    for iDiscr, discVal in enumerate(l_discr) :
        
        #nEventTot_sig = a_var_sig.shape[0]
        #nEventTot_bkg = a_var_bkg.shape[0]
        #
        #nEventSel_sig = float(sum(a_var_sig > discVal))
        #nEventSel_bkg = float(sum(a_var_bkg > discVal))
        #
        #eff_sig = nEventSel_sig / nEventTot_sig
        #eff_bkg = nEventSel_bkg / nEventTot_bkg
        #
        ## Background rejection efficiency
        ##eff_bkg = 1 - eff_bkg
        #eff_bkg = eff_bkg
        #
        #print(
        #    "%d/%d: %0.8f: "
        #    "eff_sig %0.8f, "
        #    "eff_bkg %0.8f, "
        #    "\n" %(
        #    
        #    iDiscr+1, len(l_discr),
        #    discVal,
        #    eff_sig,
        #    eff_bkg
        #))
        #
        #l_eff_sig.append(eff_sig)
        #l_eff_bkg.append(eff_bkg)
        
        
        job = pool.apply_async(
            getEfficiency,
            (),
            dict(
                arr = a_var_sig,
                val = discVal,
                norm = nEventTot_sig,
                comparison = args.comparison[iROC],
            ),
        )
        
        l_job_sig.append(job)
        
        
        job = pool.apply_async(
            getEfficiency,
            (),
            dict(
                arr = a_var_bkg,
                val = discVal,
                norm = nEventTot_bkg,
                comparison = args.comparison[iROC],
            ),
        )
        
        l_job_bkg.append(job)
    
    
    pool.close()
    pool.join()
    
    
    for iJob in range(0, len(l_job_sig)) :
        
        l_eff_sig[iJob+1] = l_job_sig[iJob].get()
        l_eff_bkg[iJob+1] = l_job_bkg[iJob].get()
        
        
        if (not iJob%10) :
            
            print(
                "%d/%d: %0.8f: "
                "eff_sig %0.8f, "
                "eff_bkg %0.8f, "
                "\n" %(
                
                iJob+1, len(l_discr),
                l_discr[iJob],
                l_eff_sig[iJob+1],
                l_eff_bkg[iJob+1]
            ))
    
    
    
    ## The last point will be (0, 0)
    ## So include this
    #l_eff_sig.extend([0.0])
    #l_eff_bkg.extend([0.0])
    
    #print(list(zip(l_eff_sig, l_eff_bkg)))
    
    
    # Get the unique x-values (i.e. the signal efficiency)
    # Required for the interpolation
    l_uniqueIndex = numpy.unique(l_eff_sig, return_index = True)[1]
    
    l_eff_sig_unique = numpy.array(l_eff_sig)[l_uniqueIndex]
    l_eff_bkg_unique = numpy.array(l_eff_bkg)[l_uniqueIndex]
    
    #l_significance_unique = numpy.array(l_significance)[l_uniqueIndex]
    
    #print(list(zip(l_eff_sig_unique, l_eff_bkg_unique)))
    
    # Add the x=0 point by hand if not already there
    if (0 not in l_eff_sig_unique) :
        
        l_eff_sig_unique = numpy.append(l_eff_sig_unique, 0.0)
        l_eff_bkg_unique = numpy.append(l_eff_bkg_unique, max(l_eff_bkg_unique))
        
        #l_significance_unique = numpy.append(l_significance_unique, 0.0)
    
    # Sort by the x-axis values (i.e. the signal efficiency)
    # Required for the interpolation
    l_sortedIndex = numpy.argsort(l_eff_sig_unique)
    
    l_eff_sig_unique = l_eff_sig_unique[l_sortedIndex]
    l_eff_bkg_unique = l_eff_bkg_unique[l_sortedIndex]
    
    #l_significance_unique = l_significance_unique[l_sortedIndex]
    
    #fInter_ROC = scipy.interpolate.InterpolatedUnivariateSpline(l_eff_sig_unique, l_eff_bkg_unique, bbox = [0, 1], ext = "zeros")
    fInter_ROC = scipy.interpolate.InterpolatedUnivariateSpline(l_eff_sig_unique, l_eff_bkg_unique, bbox = [0, 1], k = 1, ext = "zeros")
    print([fInter_ROC(ele) for ele in numpy.arange(0, 1, 0.0999)])
    
    areaROC = fInter_ROC.integral(0, 1)
    print("Area under ROC: %0.4f" %(areaROC))
    
    
    #print(len(l_discr), len(l_significance))
    ##fInter_signi_vs_disc = scipy.interpolate.InterpolatedUnivariateSpline(l_discr, l_significance, bbox = [0, 1], k = 1, ext = "zeros")
    #fInter_signi_vs_sigEff = scipy.interpolate.InterpolatedUnivariateSpline(l_eff_sig_unique, l_significance_unique, bbox = [0, 1], k = 1, ext = "zeros")
    
    
    colorAxis1 = "r"
    colorAxis2 = "b"
    
    
    #################### Plot ROC ####################
    
    AUC_str = "#scale[1.65]{AUC=%0.2g}" %(areaROC)
    
    
    a_x = array.array("f", numpy.linspace(0, 1, 1000))
    a_y = array.array("f", [fInter_ROC(ele) for ele in a_x])
    
    #print(list(zip(a_x, a_y)))
    
    gr_ROC = ROOT.TGraph(len(a_x), a_x, a_y)
    h1_ROC = Common.TGraphToTH1(graph = gr_ROC, setError = False)
    
    h1_ROC.SetName("ROC_%d" %(iROC+1))
    
    h1_ROC.GetXaxis().SetRangeUser(0.0, 1.0)
    h1_ROC.SetMinimum(args.yMin)
    h1_ROC.SetMaximum(args.yMax)
    
    histDetail_ROC = Common.HistogramDetails()
    histDetail_ROC.hist = h1_ROC.Clone()
    histDetail_ROC.hist.SetFillStyle(0)
    histDetail_ROC.drawOption = "L"
    histDetail_ROC.lineColor = args.lineColorList[iROC]
    histDetail_ROC.lineStyle = args.lineStyleList[iROC]
    histDetail_ROC.lineWidth = 3
    histDetail_ROC.markerSize = 0
    #histDetail_ROC.histLabel = "#splitline{#splitline{%s}{%s}}{AUC=%0.2g}" %(args.detailSig, args.detailBkg, areaROC)
    histDetail_ROC.histLabel = "%s [AUC=%0.3g]" %(args.labelList[iROC], areaROC)
    histDetail_ROC.histTitle = args.title
    
    
    l_histDetail.append(histDetail_ROC)
    
    
    #tree_sig.Close()
    #tree_bkg.Close()


#detailStr = "#splitline{%s}{%s}" %(args.detailSig, args.detailBkg)
#detailStr = "#splitline{%s}{%s}" %(AUC_str, detailStr)
#detailStr = "#splitline{#scale[1.75]{%s}}{%s}" %(args.detailStr, detailStr)


Common.plot1D(
    list_histDetails = l_histDetail,
    stackDrawOption = "nostack",
    title = args.title,
    #titleSizeScale = 0.9,
    xTitle = "Signal efficiency", yTitle = "Background efficiency",
    xMin = args.xMin, xMax = args.xMax,
    yMin = args.yMin, yMax = args.yMax,
    logX = False, logY = args.logY,
    gridX = True, gridY = True,
    nDivisionsX = [10, 5, 2],
    #xTitleSizeScale = 1.0, yTitleSizeScale = 1.0,
    #xTitleOffset = 1.0, yTitleOffset = 1.0,
    #xLabelSizeScale = 1.0, yLabelSizeScale = 1.0,
    #centerLabelsX = True, centerLabelsY = True,
    drawLegend = True,
    #legendHeightScale = 0.3,
    transparentLegend = True,
    legendTextSize = 0.04,
    legendBorderSize = 0,
    legendPos = args.legendPos,
    #legendTitle = "#scale[1.7]{Phase-II EB}",
    legendTitle = args.legendTitle,
    l_extraText = [[args.detailPos[0], args.detailPos[1], args.detailROC]],
    CMSextraText = "Simulation Preliminary",
    outFileName = outFileName_ROC.replace(".pdf", ""),
    outFileName_suffix = "",
)
