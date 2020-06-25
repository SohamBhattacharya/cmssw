/////////////////////////////////////////////////////////////////////////
//   This class has been automatically generated 
//   (at Thu Jun 18 22:35:32 2020 by ROOT version 6.06/06)
//   from TTree tree/tree
//   found on file: output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root
/////////////////////////////////////////////////////////////////////////


#ifndef generatedSel_h
#define generatedSel_h

#define R__BRANCHPROXY_GENERATOR_VERSION 2

// ROOT headers needed by the proxy
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TPad.h>
#include <TH1.h>
#include <TSelector.h>
#include <TBranchProxy.h>
#include <TBranchProxyDirector.h>
#include <TBranchProxyTemplate.h>
#include <TFriendProxy.h>
using namespace ROOT::Internal;
using ROOT::Detail::TBranchProxy;

// forward declarations needed by this particular proxy


// Header needed by this particular proxy
#include <vector>


class ntupleTree_Interface {
   // This class defines the list of methods that are directly used by generatedSel,
   // and that can be overloaded in the user's script
public:
   void ntupleTree_Begin(TTree*) {}
   void ntupleTree_SlaveBegin(TTree*) {}
   Bool_t ntupleTree_Notify() { return kTRUE; }
   Bool_t ntupleTree_Process(Long64_t) { return kTRUE; }
   void ntupleTree_SlaveTerminate() {}
   void ntupleTree_Terminate() {}
};


class generatedSel : public TSelector, public ntupleTree_Interface {
public :
   TTree          *fChain;         //!pointer to the analyzed TTree or TChain
   TH1            *htemp;          //!pointer to the histogram
   TBranchProxyDirector fDirector; //!Manages the proxys

   // Optional User methods
   TClass         *fClass;    // Pointer to this class's description

   // Wrapper class for each unwounded class
   struct TStlPx_vector_double_
   {
      TStlPx_vector_double_(TBranchProxyDirector* director,const char *top,const char *mid=0) :
         ffPrefix(top,mid),
         obj(director, top, mid)
      {};
      TStlPx_vector_double_(TBranchProxyDirector* director, TBranchProxy *parent, const char *membername, const char *top=0, const char *mid=0) :
         ffPrefix(top,mid),
         obj(director, parent, membername)
      {};
      ROOT::Internal::TBranchProxyHelper ffPrefix;
      InjecTBranchProxyInterface();
      const vector<double>& At(UInt_t i) {
         static vector<double> default_val;
         if (!obj.Read()) return default_val;
         vector<double> *temp = & obj.GetPtr()->at(i);
         if (temp) return *temp; else return default_val;
      }
      const vector<double>& operator[](Int_t i) { return At(i); }
      const vector<double>& operator[](UInt_t i) { return At(i); }
      Int_t GetEntries() { return obj.GetPtr()->size(); }
      const vector<vector<double> >* operator->() { return obj.GetPtr(); }
      operator vector<vector<double> >*() { return obj.GetPtr(); }
      TObjProxy<vector<vector<double> > > obj;

   };

   // Proxy for each of the branches, leaves and friends of the tree
   TULong64Proxy                      runNumber;
   TULong64Proxy                      eventNumber;
   TULong64Proxy                      luminosityNumber;
   TULong64Proxy                      bunchCrossingNumber;
   TIntProxy                          genEl_n;
   TStlSimpleProxy<vector<double> >   genEl_E;
   TStlSimpleProxy<vector<double> >   genEl_px;
   TStlSimpleProxy<vector<double> >   genEl_py;
   TStlSimpleProxy<vector<double> >   genEl_pz;
   TStlSimpleProxy<vector<double> >   genEl_pT;
   TStlSimpleProxy<vector<double> >   genEl_eta;
   TIntProxy                          pileup_n;
   TDoubleProxy                       rho;
   TDoubleProxy                       PV_t;
   TDoubleProxy                       PV_tErr;
   TDoubleProxy                       slimmedEle_n;
   TStlSimpleProxy<vector<double> >   slimmedEle_idx;
   TStlSimpleProxy<vector<double> >   slimmedEle_E;
   TStlSimpleProxy<vector<double> >   slimmedEle_px;
   TStlSimpleProxy<vector<double> >   slimmedEle_py;
   TStlSimpleProxy<vector<double> >   slimmedEle_pz;
   TStlSimpleProxy<vector<double> >   slimmedEle_pT;
   TStlSimpleProxy<vector<double> >   slimmedEle_eta;
   TStlSimpleProxy<vector<double> >   slimmedEle_phi;
   TStlSimpleProxy<vector<double> >   slimmedEle_ET;
   TStlSimpleProxy<vector<double> >   slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values;
   TStlSimpleProxy<vector<double> >   slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues;
   TStlSimpleProxy<vector<double> >   slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values;
   TStlSimpleProxy<vector<double> >   slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues;
   TStlSimpleProxy<vector<double> >   slimmedEle_genEl_minDeltaR;
   TStlSimpleProxy<vector<double> >   slimmedEle_nearestGenEl_idx;
   TStlSimpleProxy<vector<double> >   slimmedEle_matchedGenEl_E;
   TStlSimpleProxy<vector<double> >   slimmedEle_matchedGenEl_pT;
   TStlSimpleProxy<vector<double> >   slimmedEle_matchedGenEl_eta;
   TStlSimpleProxy<vector<double> >   slimmedEle_matchedGenEl_phi;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_eleIdx;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_ET;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_t;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_tErr;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_PV_dt;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_PV_dtSigni;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_PV_dz;
   TStlPx_vector_double_              slimmedEle_sig_pfCand_PV_dzSigni;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_eleIdx;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_ET;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_t;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_tErr;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_PV_dt;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_PV_dtSigni;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_PV_dz;
   TStlPx_vector_double_              slimmedEle_isoDR0p3_pfCand_PV_dzSigni;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand_n_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand1_PV_dtSigni_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand2_PV_dtSigni_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand_PV_dtSigniMean_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand1_PV_dz_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand2_PV_dz_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand_PV_dzMean_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt4;
   TStlSimpleProxy<vector<double> >   slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4;


   generatedSel(TTree *tree=0) : 
      fChain(0),
      htemp(0),
      fDirector(tree,-1),
      fClass                (TClass::GetClass("generatedSel")),
      runNumber                         (&fDirector,"runNumber"),
      eventNumber                       (&fDirector,"eventNumber"),
      luminosityNumber                  (&fDirector,"luminosityNumber"),
      bunchCrossingNumber               (&fDirector,"bunchCrossingNumber"),
      genEl_n                           (&fDirector,"genEl_n"),
      genEl_E                           (&fDirector,"genEl_E"),
      genEl_px                          (&fDirector,"genEl_px"),
      genEl_py                          (&fDirector,"genEl_py"),
      genEl_pz                          (&fDirector,"genEl_pz"),
      genEl_pT                          (&fDirector,"genEl_pT"),
      genEl_eta                         (&fDirector,"genEl_eta"),
      pileup_n                          (&fDirector,"pileup_n"),
      rho                               (&fDirector,"rho"),
      PV_t                              (&fDirector,"PV_t"),
      PV_tErr                           (&fDirector,"PV_tErr"),
      slimmedEle_n                      (&fDirector,"slimmedEle_n"),
      slimmedEle_idx                    (&fDirector,"slimmedEle_idx"),
      slimmedEle_E                      (&fDirector,"slimmedEle_E"),
      slimmedEle_px                     (&fDirector,"slimmedEle_px"),
      slimmedEle_py                     (&fDirector,"slimmedEle_py"),
      slimmedEle_pz                     (&fDirector,"slimmedEle_pz"),
      slimmedEle_pT                     (&fDirector,"slimmedEle_pT"),
      slimmedEle_eta                    (&fDirector,"slimmedEle_eta"),
      slimmedEle_phi                    (&fDirector,"slimmedEle_phi"),
      slimmedEle_ET                     (&fDirector,"slimmedEle_ET"),
      slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values(&fDirector,"slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2Values"),
      slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues(&fDirector,"slimmedEle_ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
      slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values(&fDirector,"slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
      slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues(&fDirector,"slimmedEle_ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
      slimmedEle_genEl_minDeltaR        (&fDirector,"slimmedEle_genEl_minDeltaR"),
      slimmedEle_nearestGenEl_idx       (&fDirector,"slimmedEle_nearestGenEl_idx"),
      slimmedEle_matchedGenEl_E         (&fDirector,"slimmedEle_matchedGenEl_E"),
      slimmedEle_matchedGenEl_pT        (&fDirector,"slimmedEle_matchedGenEl_pT"),
      slimmedEle_matchedGenEl_eta       (&fDirector,"slimmedEle_matchedGenEl_eta"),
      slimmedEle_matchedGenEl_phi       (&fDirector,"slimmedEle_matchedGenEl_phi"),
      slimmedEle_sig_pfCand_eleIdx      (&fDirector,"slimmedEle_sig_pfCand_eleIdx"),
      slimmedEle_sig_pfCand_ET          (&fDirector,"slimmedEle_sig_pfCand_ET"),
      slimmedEle_sig_pfCand_t           (&fDirector,"slimmedEle_sig_pfCand_t"),
      slimmedEle_sig_pfCand_tErr        (&fDirector,"slimmedEle_sig_pfCand_tErr"),
      slimmedEle_sig_pfCand_PV_dt       (&fDirector,"slimmedEle_sig_pfCand_PV_dt"),
      slimmedEle_sig_pfCand_PV_dtSigni  (&fDirector,"slimmedEle_sig_pfCand_PV_dtSigni"),
      slimmedEle_sig_pfCand_PV_dz       (&fDirector,"slimmedEle_sig_pfCand_PV_dz"),
      slimmedEle_sig_pfCand_PV_dzSigni  (&fDirector,"slimmedEle_sig_pfCand_PV_dzSigni"),
      slimmedEle_isoDR0p3_pfCand_eleIdx (&fDirector,"slimmedEle_isoDR0p3_pfCand_eleIdx"),
      slimmedEle_isoDR0p3_pfCand_ET     (&fDirector,"slimmedEle_isoDR0p3_pfCand_ET"),
      slimmedEle_isoDR0p3_pfCand_t      (&fDirector,"slimmedEle_isoDR0p3_pfCand_t"),
      slimmedEle_isoDR0p3_pfCand_tErr   (&fDirector,"slimmedEle_isoDR0p3_pfCand_tErr"),
      slimmedEle_isoDR0p3_pfCand_PV_dt  (&fDirector,"slimmedEle_isoDR0p3_pfCand_PV_dt"),
      slimmedEle_isoDR0p3_pfCand_PV_dtSigni(&fDirector,"slimmedEle_isoDR0p3_pfCand_PV_dtSigni"),
      slimmedEle_isoDR0p3_pfCand_PV_dz  (&fDirector,"slimmedEle_isoDR0p3_pfCand_PV_dz"),
      slimmedEle_isoDR0p3_pfCand_PV_dzSigni(&fDirector,"slimmedEle_isoDR0p3_pfCand_PV_dzSigni"),
      slimmedEle_sig_pfCand_n_all       (&fDirector,"slimmedEle_sig_pfCand_n_all"),
      slimmedEle_sig_pfCand1_PV_dtSigni_all(&fDirector,"slimmedEle_sig_pfCand1_PV_dtSigni_all"),
      slimmedEle_sig_pfCand2_PV_dtSigni_all(&fDirector,"slimmedEle_sig_pfCand2_PV_dtSigni_all"),
      slimmedEle_sig_pfCand_PV_dtSigniMean_all(&fDirector,"slimmedEle_sig_pfCand_PV_dtSigniMean_all"),
      slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all(&fDirector,"slimmedEle_sig_pfCand_PV_dtSigniMean_ETwtd_all"),
      slimmedEle_sig_pfCand1_PV_dz_all  (&fDirector,"slimmedEle_sig_pfCand1_PV_dz_all"),
      slimmedEle_sig_pfCand2_PV_dz_all  (&fDirector,"slimmedEle_sig_pfCand2_PV_dz_all"),
      slimmedEle_sig_pfCand_PV_dzMean_all(&fDirector,"slimmedEle_sig_pfCand_PV_dzMean_all"),
      slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all(&fDirector,"slimmedEle_sig_pfCand_PV_dzMean_ETwtd_all"),
      slimmedEle_iso_pfCand_n_dR0p3     (&fDirector,"slimmedEle_iso_pfCand_n_dR0p3"),
      slimmedEle_iso_sumETratio_dR0p3   (&fDirector,"slimmedEle_iso_sumETratio_dR0p3"),
      slimmedEle_iso_sumETratio_charged_dR0p3(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3"),
      slimmedEle_iso_sumETratio_neutral_dR0p3(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3"),
      slimmedEle_iso_sumETratio_ecal_dR0p3(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3"),
      slimmedEle_iso_sumETratio_hcal_dR0p3(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3"),
      slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5"),
      slimmedEle_iso_sumETratio_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dzLt0p5"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5"),
      slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt2"),
      slimmedEle_iso_sumETratio_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dTsigniLt2"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt2"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt2"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt2"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt2"),
      slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt2"),
      slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt3"),
      slimmedEle_iso_sumETratio_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dTsigniLt3"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt3"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt3"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt3"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt3"),
      slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt3"),
      slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dTsigniLt4"),
      slimmedEle_iso_sumETratio_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dTsigniLt4"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dTsigniLt4"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dTsigniLt4"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dTsigniLt4"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dTsigniLt4"),
      slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_n_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_charged_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_neutral_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_ecal_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_sumETratio_hcal_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand1_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand2_PV_dtSigni_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dtSigniMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand1_PV_dz_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand2_PV_dz_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_dR0p3_dzLt0p5_dTsigniLt4"),
      slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4(&fDirector,"slimmedEle_iso_pfCand_PV_dzMean_ETwtd_dR0p3_dzLt0p5_dTsigniLt4")
      { }
   ~generatedSel();
   Int_t   Version() const {return 1;}
   void    Begin(::TTree *tree);
   void    SlaveBegin(::TTree *tree);
   void    Init(::TTree *tree);
   Bool_t  Notify();
   Bool_t  Process(Long64_t entry);
   void    SlaveTerminate();
   void    Terminate();

   ClassDef(generatedSel,0);


//inject the user's code
#include "output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root"
};

#endif


#ifdef __MAKECINT__
#pragma link C++ class generatedSel::TStlPx_vector_double_-;
#pragma link C++ class generatedSel;
#endif


inline generatedSel::~generatedSel() {
   // destructor. Clean up helpers.

}

inline void generatedSel::Init(TTree *tree)
{
//   Set branch addresses
   if (tree == 0) return;
   fChain = tree;
   fDirector.SetTree(fChain);
   if (htemp == 0) {
      htemp = fDirector.CreateHistogram(GetOption());
      htemp->SetTitle("output/TreeMaker_RelValQCD_Pt15To7000_Flat_14_CMSSW_11_1_0_pre6-PU25ns_110X_mcRun4_realistic_v3_2026D49PU200-v1_MINIAODSIM/ntupleTree.root");
      fObject = htemp;
   }
}

Bool_t generatedSel::Notify()
{
   // Called when loading a new file.
   // Get branch pointers.
   fDirector.SetTree(fChain);
   ntupleTree_Notify();
   
   return kTRUE;
}
   

inline void generatedSel::Begin(TTree *tree)
{
   // The Begin() function is called at the start of the query.
   // When running with PROOF Begin() is only called on the client.
   // The tree argument is deprecated (on PROOF 0 is passed).

   TString option = GetOption();
   ntupleTree_Begin(tree);

}

inline void generatedSel::SlaveBegin(TTree *tree)
{
   // The SlaveBegin() function is called after the Begin() function.
   // When running with PROOF SlaveBegin() is called on each slave server.
   // The tree argument is deprecated (on PROOF 0 is passed).

   Init(tree);

   ntupleTree_SlaveBegin(tree);

}

inline Bool_t generatedSel::Process(Long64_t entry)
{
   // The Process() function is called for each entry in the tree (or possibly
   // keyed object in the case of PROOF) to be processed. The entry argument
   // specifies which entry in the currently loaded tree is to be processed.
   // It can be passed to either TTree::GetEntry() or TBranch::GetEntry()
   // to read either all or the required parts of the data. When processing
   // keyed objects with PROOF, the object is already loaded and is available
   // via the fObject pointer.
   //
   // This function should contain the "body" of the analysis. It can contain
   // simple or elaborate selection criteria, run algorithms on the data
   // of the event and typically fill histograms.

   // WARNING when a selector is used with a TChain, you must use
   //  the pointer to the current TTree to call GetEntry(entry).
   //  The entry is always the local entry number in the current tree.
   //  Assuming that fChain is the pointer to the TChain being processed,
   //  use fChain->GetTree()->GetEntry(entry).


   fDirector.SetReadEntry(entry);
   htemp->Fill(ntupleTree());
   ntupleTree_Process(entry);
   return kTRUE;

}

inline void generatedSel::SlaveTerminate()
{
   // The SlaveTerminate() function is called after all entries or objects
   // have been processed. When running with PROOF SlaveTerminate() is called
   // on each slave server.
   ntupleTree_SlaveTerminate();
}

inline void generatedSel::Terminate()
{
   // Function called at the end of the event loop.
   htemp = (TH1*)fObject;
   Int_t drawflag = (htemp && htemp->GetEntries()>0);
   
   if (gPad && !drawflag && !fOption.Contains("goff") && !fOption.Contains("same")) {
      gPad->Clear();
   } else {
      if (fOption.Contains("goff")) drawflag = false;
      if (drawflag) htemp->Draw(fOption);
   }
   ntupleTree_Terminate();
}
