import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

from Backend.ProjectData import ProjectData

from ProjectInfoPage import ProjectInfoPage

class ProjectStackedWidget(QtWidgets.QStackedWidget):

    def __init__(self, project_:ProjectData, parent:QtWidgets.QTabWidget):
        super().__init__(parent)

        self.project = project_
        
        # ProjectInfoPage *projectInfoPage;

        projectInfoPage = ProjectInfoPage(self.project, self)
        self.addWidget(projectInfoPage)