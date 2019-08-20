```


1. Push changes:
    git add .
    git commit
    git push -u my-cmssw SohamBhattacharya/HGCal_ele-reco:HGCal_ele-reco 

2. Run ecalDrivenGsfElectronsFromTICL:
    from MyModules.Test.ecalDrivenGsfElectronsFromTICL_cff import ecalDrivenGsfElectronsFromTICL_customizeProcess
    process = ecalDrivenGsfElectronsFromTICL_customizeProcess(process, onReco = True)
    <Add process.ecalDrivenGsfElectronsFromTICL_step to the schedule>

3. 


```
