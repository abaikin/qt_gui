import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

from Backend.State import State

import json

class ProjectData(QtCore.QObject):

    def __init__(self, fileName=None):
        super().__init__()

        if (fileName is not None):
            project_data_json = None
            with open(fileName) as file_obj:
                project_data_json = json.load(file_obj)  # ok

                self.projectName = project_data_json["ProjectName"]
                self.simulationDirectory = project_data_json["SimulationDirectory"]


    def loadStatesFromFolder(self, folderPath=None):
        folderPath = self.simulationDirectory

        self.states = []
        i = 1
        filePath = os.path.join(folderPath, "dump", "dump"+ str(i) + ".json")

        self.states.append(State(filePath))

    def getProjectFilePath(self):

        return ''