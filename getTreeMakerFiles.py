from __future__ import print_function

import argparse
import numpy
import os
import subprocess


cwd = os.getcwd()


# Argument parser
parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter)

parser.add_argument(
    "--idir",
    help = "TreeMaker directory",
    type = str,
    required = False,
    default = "/eos/cms/store/group/phys_egamma/sobhatta/HGCal_TreeMaker",
)

parser.add_argument(
    "--iprefix",
    help = "TreeMaker directory prefix (WITHOUT trailing underscore)",
    type = str,
    required = False,
    default = "",
)

parser.add_argument(
    "--odir",
    help = "Output directory",
    type = str,
    required = False,
    default = "sourceFiles",
)

parser.add_argument(
    "--samples",
    help = "Names of the samples",
    type = str,
    nargs = "*",
    required = True,
)

parser.add_argument(
    "--replace",
    help = "Will replace output file if it exists",
    action = "store_true",
    default = False,
)

parser.add_argument(
    "--get",
    help = "Will actually create the file list",
    action = "store_true",
    default = False,
)

# Parse arguments
args = parser.parse_args()


d_textStyle = {
    "HEADER"    : "\033[95m",
    "BLUE"    : "\033[94m",
    "CYAN"    : "\033[96m",
    "GREEN"   : "\033[92m",
    "WARNING"   : "\033[93m",
    "ERROR"     : "\033[91m",
    "ENDC"      : "\033[0m",
    "BOLD"      : "\033[1m",
    "UNDERLINE" : "\033[4m",
}


def fancify(msg, style) :
    
    if (not len(style)) :
        
        return msg
    
    msg_mod = d_textStyle[style] + msg + d_textStyle["ENDC"]
    
    return msg_mod



for iSamp, sampleName in enumerate(args.samples) :
    
    print(fancify("*"*100, "BLUE"))
    print(fancify("Sample %d/%d: %s" %(iSamp+1, len(args.samples), sampleName), "BLUE"))
    print(fancify("*"*100, "BLUE"))
    
    processName = "%s%s%s" %(args.iprefix, "_"*int(len(args.iprefix) > 0), sampleName)
    inDir = "%s/%s" %(args.idir, processName)
    outDir = "%s/%s" %(args.odir, processName)
    outFileName = "%s/%s.txt" %(outDir, processName)
    
    print("Name        : %s" %(processName))
    print("Input dir.  : %s" %(inDir))
    
    if (not os.path.exists(inDir)) :
        
        print(fancify("ERROR: Directory does not exist! Exiting...", "ERROR"))
        exit(1)
    
    print("Output dir. : %s" %(outDir))
    print("Output file.: %s" %(outFileName))
    
    if (args.get) :
        
        if (not args.replace and os.path.exists(outFileName)) :
            
            print(fancify("ERROR: Output file exists! Exiting...", "ERROR"))
            exit(1)
        
        cmd = "mkdir -p %s" %(outDir)
        print("Executing: %s" %(cmd))
        os.system(cmd)
        
        cmd = "find %s/*.root | sort -V > %s" %(inDir, outFileName)
        print("Executing: %s" %(cmd))
        os.system(cmd)
        
        # Count the number of entries
        cmd = "wc -l < %s" %(outFileName)
        nLine = subprocess.check_output(cmd, shell = True).strip()
        nLine = int(nLine)
        
        print(fancify("Count: %d" %(nLine), "GREEN"))
        
        if (not nLine) :
            
            print(fancify("WARNING: No entries in output file!", "WARNING"))


    
    print("\n")
