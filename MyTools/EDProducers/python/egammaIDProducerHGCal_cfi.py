import FWCore.ParameterSet.Config as cms

from MyTools.EDProducers.producers_cfi import *


def customize_eleHGCalID(process, processName = "") :
    
    l_var = []
    l_mapProdVars = []
    var_task = cms.Task()
    
    
    ########## H/E ##########
    prodLabel = "TICLeleHoverEProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalElectronHoverEProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    
    ########## Cluster isolation ##########
    prodLabel = "TICLeleClusIsoProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalElectronClusIsoProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    ########## Rvar ##########
    prodLabel = "TICLeleRvarProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalElectronRvarProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    
    ########## PCA ##########
    prodLabel = "TICLelePCAProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalElectronPCAProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2UU", processName))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2VV", processName))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2WW", processName))
    
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2UU"))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2VV"))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2WW"))
    
    
    # Variable map
    process.HGCalElectronVarMap = mapProducer.clone(
        collections = cms.VInputTag(l_mapProdVars),
        
        debug = cms.bool(False),
    )
    
    process.electronMVAIDProducerHGCal = cms.EDProducer(
        "ElectronMVAIDProducerHGCal",
        
        instanceName = cms.string(""),
        
        weightFile = cms.string("MyTools/EDProducers/data/ElectronID_MVA_endcap_Egamma_PhaseII_weight.xml"),
        
        electrons = cms.InputTag("ecalDrivenGsfElectronsFromMultiCl"),
        PFRecHits = cms.InputTag("particleFlowRecHitHGC"),
        vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        
        varMap = cms.InputTag("HGCalElectronVarMap", "MapProducer"),
        
        minPt = cms.double(0.0),
        
        debug = cms.bool(True),
    )
    
    
    process.eleHGCalID_seq = cms.Sequence(
        process.HGCalElectronVarMap *
        process.electronMVAIDProducerHGCal
    )
    
    process.eleHGCalID_seq.associate(var_task)
    
    return process



def customize_phoHGCalID(process, processName = "") :
    
    l_var = []
    l_mapProdVars = []
    var_task = cms.Task()
    
    
    ########## H/E ##########
    prodLabel = "TICLphoHoverEProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalPhotonHoverEProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    
    ########## Cluster isolation ##########
    prodLabel = "TICLphoClusIsoProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalPhotonClusIsoProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    ########## Rvar ##########
    prodLabel = "TICLphoRvarProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalPhotonRvarProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value(), processName))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()))
    
    
    ########## PCA ##########
    prodLabel = "TICLphoPCAProducer"
    
    setattr(
        process,
        prodLabel,
        HGCalPhotonPCAProducer.clone(
            #debug = cms.bool(True),
        )
    )
    
    var_task.add(getattr(process, prodLabel))
    
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2UU", processName))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2VV", processName))
    l_mapProdVars.append(cms.InputTag(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2WW", processName))
    
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2UU"))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2VV"))
    l_var.append("%s_%s" %(prodLabel, getattr(process, prodLabel).instanceName.value()+"Sigma2WW"))
    
    
    # Variable map
    process.HGCalPhotonVarMap = mapProducer.clone(
        collections = cms.VInputTag(l_mapProdVars),
        
        debug = cms.bool(False),
    )
    
    process.photonMVAIDProducerHGCal = cms.EDProducer(
        "PhotonMVAIDProducerHGCal",
        
        instanceName = cms.string(""),
        
        weightFile = cms.string("MyTools/EDProducers/data/PhotonID_MVA_endcap_Egamma_PhaseII_weight.xml"),
        
        photons = cms.InputTag("photonsFromMultiCl"),
        PFRecHits = cms.InputTag("particleFlowRecHitHGC"),
        vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
        rho = cms.InputTag("fixedGridRhoFastjetAll"),
        
        varMap = cms.InputTag("HGCalPhotonVarMap", "MapProducer"),
        
        minPt = cms.double(0.0),
        
        debug = cms.bool(True),
    )
    
    
    process.phoHGCalID_seq = cms.Sequence(
        process.HGCalPhotonVarMap *
        process.photonMVAIDProducerHGCal
    )
    
    process.phoHGCalID_seq.associate(var_task)
    
    return process

