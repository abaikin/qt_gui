import sys 
import os

import numpy as np
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

import json

from Backend.Mesh1d import Mesh1d
class State(QtCore.QObject):

    def __init__(self, jsonFilepath=None):
        super().__init__()

        if jsonFilepath is not None: 
            self.loadStateFromJson(jsonFilepath)


    def loadStateFromJson(self, jsonFilepath):


        absPath = os.path.abspath(jsonFilepath)

        with open(jsonFilepath) as file_obj:
            stateJson = json.load(file_obj)  # ok

            self.stateId = stateJson["Info"]["StateId"]
            self.time = stateJson["Info"]["Time"]
            self.timeStep = stateJson["Info"]["TimeStep"]

            self.iGrow = stateJson["Info"]["iGrow"]
            self.iItertation = stateJson["Info"]["iItertation"]
            self.iOverallItertation = stateJson["Info"]["iOverallItertation"]
            self.tipX0 = stateJson["Info"]["tipX0"]
            self.tipX1 = stateJson["Info"]["tipX1"]
            self.widthRelError = stateJson["Info"]["widthRelError"]

            XY = np.array(stateJson["Data"]["CrackMesh"]["VertexCoord"])
            self.crackMesh = Mesh1d(XY[:,0], XY[:,1])
            self.vCrackJump = np.array(stateJson["Data"]["CrackMesh"]["VCrackJump"])
            self.pCrack = np.array(stateJson["Data"]["CrackMesh"]["PCrack"])

        return ''