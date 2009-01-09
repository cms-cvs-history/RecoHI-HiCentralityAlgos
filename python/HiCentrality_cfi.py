import FWCore.ParameterSet.Config as cms

hiCentrality = cms.EDProducer("CentralityProducer",
                              recoLevel = cms.untracked.bool(True),
                              genLevel = cms.untracked.bool(True)
                              )

