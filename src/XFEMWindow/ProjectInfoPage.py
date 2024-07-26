import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

from UI.ProjectInfoPageUI_ui import Ui_ProjectInfoPage

from Backend.ProjectData import ProjectData

class ProjectInfoPage(QtWidgets.QWidget, Ui_ProjectInfoPage):

    def __init__(self, project_:ProjectData, parent:QtWidgets.QTabWidget):
        super().__init__(parent)
        self.setupUi(self)
        self.project = project_

        self.projectNameLabel.setText("Project 1212")
        self.projectAuthorLineEdit.setText("Alexey")
        self.projectDateLabel.setText("Alexey")
