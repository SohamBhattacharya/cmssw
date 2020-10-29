import argparse
import glob
import os


# Argument parser
parser = argparse.ArgumentParser()

# List of directories
parser.add_argument(
    "-d",
    "--directories",
    help = "List of directories",
    nargs = "*",
    type = str,
    required = True
)

parser.add_argument(
    "--submit",
    help = "Submit the failed jobs",
    action = "store_true"
)

parser.add_argument(
    "--success",
    help = "Will also show the jobs that have succeeded",
    action = "store_true"
)

# Parse arguments
args = parser.parse_args()


l_directory = args.directories

print "You have entered:"
print "\n".join(l_directory)
print ""

if (args.submit) :
    
    print "Will SUBMIT the failed jobs."

else :
    
    print "Will NOT submit the failed jobs."

print ""
print "Enter YES to proceed, or anything else to cancel."
choice = raw_input("Input: ")

if (choice != "YES") :
    
    print "Exiting."
    exit()


extension_log = ".log"
extension_err = ".err"
extension_out = ".out"

# Case insentitive
#l_errorStr = ["error", "segmentation", "killed", "SCRAM fatal"]
l_errorStr = ["Fatal Exception", "FatalRootError", "fatal system signal has occurred"]
l_errorStrSkip = ["unknown branch"]

# The format is: (return value <value>)
retValStr_start = "(return value "
retValStr_end = ")"

jobSubStr = "Job submitted"


condorConfig_nameTemplate = "condor_config_%s.sub"
command_template = "condor_submit %s"


nJob_total = 0
nJob_succ = 0
nJob_fail = 0


# Check if all the directories exist
for iDir in range(0, len(l_directory)) :
    
    directory = l_directory[iDir]
    
    if (not os.path.isdir(directory)) :
        
        print "Directory does not exist: %s" %(directory)
        exit(1)


for iDir in range(0, len(l_directory)) :
    
    directory = l_directory[iDir]
    
    print "\n"
    print "**************************************************"
    print "Directory:", directory
    print "**************************************************"
    
    l_fileName = glob.glob(directory + "/**")
    l_fileName = [f for f in l_fileName if extension_log in f]
    l_fileName.sort(key = lambda l: int(l[l.rfind("_")+1: l.rfind(extension_log)]))
    
    nJob_total += len(l_fileName)
    
    count = 0
    
    for iFile in range(0, len(l_fileName)) :
        
        fileName = l_fileName[iFile]
        
        fileContent = []
        
        with open(fileName) as f :
            
            fileContent = f.readlines()
        
        
        hasCompleted = False
        hasError = False
        retVal = 0
        
        
        # N.B. Log files are appended to (not overwritten) on resubmitting the job
        # Hence use the last occurence of the job summary
        for line in fileContent :
            
            if (retValStr_start in line) :
                
                hasCompleted = True
                retValStr = line
            
            # The job must not have been resubmitted
            if (jobSubStr in line) :
                
                hasCompleted = False
        
        
        if (not hasCompleted) :
            
            continue
        
        
        retValStr = retValStr[retValStr.find(retValStr_start) + len(retValStr_start):]
        retValStr = retValStr[: retValStr.find(retValStr_end)]
        retVal = int(retValStr)
        
        hasError = bool(retVal)
        
        
        nJob_succ += int(not hasError)
        nJob_fail += int(hasError)
        
        
        hasPrinted = False
        
        if (hasError or args.success) :
            
            count += 1
            
            number = fileName[fileName.rfind("_")+1: fileName.rfind(extension_log)]
            
            condorConfig_name = condorConfig_nameTemplate %(number)
            condorConfig_name = "%s/%s" %(directory, condorConfig_name)
            command = command_template %(condorConfig_name)
            
            print "Count:", count
            print "Total count:", nJob_fail
            print "File:", fileName
            print "Return value: %d" %(retVal)
            print "Condor config:", condorConfig_name
            
            hasPrinted = True
        
        if (hasError and args.submit) :
            
            # Delete the err and out files
            fileName_err = fileName.replace(extension_log, extension_err)
            print "Deleting error file: %s" %(fileName_err)
            os.system("rm %s" %(fileName_err))
            
            fileName_out = fileName.replace(extension_log, extension_out)
            print "Deleting output file: %s" %(fileName_out)
            os.system("rm %s" %(fileName_out))
            
            print "Command:", command
            os.system(command)
            
            hasPrinted = True
        
        if (hasPrinted) :
            
            print "\n"


nDigit = len(str(nJob_total))

print "\n"
print "Total number of succeeded jobs: %0*d/%d" %(nDigit, nJob_succ, nJob_total)
print "Total number of failed jobs   : %0*d/%d" %(nDigit, nJob_fail, nJob_total)
print "\n"
