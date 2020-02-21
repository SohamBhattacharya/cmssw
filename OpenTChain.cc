#include <cstdlib>
#include <iostream>
#include <map>
#include <string>


int OpenTChain(std::string listFileName, TChain *chain, int nFileMax = -1)
{
    std::ifstream inFileList;
    inFileList.open(listFileName.c_str());
    
    std::string inFileName;
    
    //TChain *chain = new TChain(treeName.c_str());
    
    int nFile = 0;
    
    while(std::getline(inFileList, inFileName))
    {
        char inFileName_mod[1000];
        
        if(inFileName.find("/eos/cms") == 0)
        {
            sprintf(inFileName_mod, "root://eoscms.cern.ch/%s", inFileName.c_str());
        }
        
        else
        {
            sprintf(inFileName_mod, "%s", inFileName.c_str());
        }
        
        printf("Checking file: %s \n", inFileName_mod);
        TFile *inFile = (TFile*) TFile::Open(inFileName_mod);
        
        if(inFile && !inFile->IsZombie())
        {
            printf("Adding to chain...\n");
            
            //v_inFile.push_back(inFile);
            
            chain->Add(inFileName_mod);
            
            inFile->Close();
            
            nFile++;
        }
        
        if(nFileMax > 0 && nFile >= nFileMax)
        {
            break;
        }
    }
    
    
    return 0;
}
