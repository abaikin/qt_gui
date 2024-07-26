import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

from PySide6.QtWidgets import QFileDialog

from ProjectStackedWidget import ProjectStackedWidget

from Backend.ProjectData import ProjectData

import json

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path+'/UI/')

from UI.XFEMMainWindowUI_ui import Ui_MainWindow
# from UI.ProjectViewUI_ui import Ui_ProjectView
# from XFEMWindow.ProjectView import ProjectView

# from add_person import AddPerson
# from login import LoginForm

# The login app from tutorial https://www.youtube.com/watch?v=uzqDnB44qf4 

class XFEMMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set slot for openProject button
        # connect(openProjectButton, SIGNAL(clicked()), this, SLOT(sl_openProject()));

        self.openProjectLinkButton.clicked.connect(self.sl_open_project)


        self.startPage = self.centralWidget() # Init startPage as default central widget

       
    @QtCore.Slot()
    def sl_open_project(self):
        # fname, type = QFileDialog.getOpenFileName(
        #     self,
        #     "Open a folder",
        #     r"C:\AllDocs\Work\Repositories\qt_gui"
        # )

        fname = r'C:/AllDocs/Work/Repositories/qt_gui/Project1.json'

        # self.le_filepath.text = 
        # self.le_filepath.setText(str(fname))

        file_obj2 = open(fname)
        file_content=file_obj2.read()
        file_obj2.close()

        project_data_json = None
        with open(fname) as file_obj:
            project_data_json = json.load(file_obj)  # ok

            # project_data_json = json.loads(file_obj)

            # json.dump(project_data_json)
        print('project filename ',fname)
        print('project content ',file_content)


        # self.te_filecontent.setPlainText(text)

        self.open_project()

    def change(self, project_):

        project_.x = 50

    def open_project(self):
        self.startPage.setParent(None)
        
        project = ProjectData()
        
        stackedWidget = ProjectStackedWidget(project, self)
        self.setCentralWidget(stackedWidget)
        self.startPage.setParent(self)

        # projectView->setProject(proj);

       


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = XFEMMainWindow() # Create main window object
    window.show() # Show window on screen
    sys.exit(app.exec())