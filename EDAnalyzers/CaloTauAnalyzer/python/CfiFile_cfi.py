import FWCore.ParameterSet.Config as cms

demo = cms.EDAnalyzer('CaloTauAnalyzer'
     ,tracks = cms.untracked.InputTag('ctfWithMaterialTracks')
)
