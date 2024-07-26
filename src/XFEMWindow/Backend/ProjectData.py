import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 


class ProjectData(QtCore.QObject):

    def __init__(self):
        super().__init__()

        self.x = 5


    def getProjectFilePath(self):

        return ''