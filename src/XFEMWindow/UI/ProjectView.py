import sys 
import os
from PySide6 import QtCore 
from PySide6 import QtWidgets
from PySide6 import QtGui 

from PySide6.QtWidgets import QTreeWidgetItem, QTreeWidget

import json

# script_path = os.path.dirname(os.path.realpath(__file__))
# sys.path.append(script_path+'/Application_Login/Icons/')

from ProjectViewUI_ui import Ui_ProjectView
# from add_person import AddPerson
# from login import LoginForm

# The login app from tutorial https://www.youtube.com/watch?v=uzqDnB44qf4 

class ProjectView(QtWidgets.QWidget, Ui_ProjectView):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        items = []
        for i in range(0, 10):
            items.append(QTreeWidgetItem(self.treeWidget, ['item:' + str(i) ]))
        self.treeWidget.insertTopLevelItems(0, items)

        # root = QTreeWidgetItem(self.treeWidget, "roo22")
        # root.setData(0, QtCore.Qt.ItemDataRole.UserRole, 'rooooo')

        # self.treeWidget.insertTopLevelItem(0, root)
        # self.treeWidget.expandAll()

        # Set slot for openProject button
        # connect(openProjectButton, SIGNAL(clicked()), this, SLOT(sl_openProject()));

        # self.openProjectLinkButton.clicked.connect(self.sl_open_project)


        # startPage = self.centralWidget() # Init startPage as default central widget

   

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = ProjectView() # Create main window object
    window.show() # Show window on screen
    sys.exit(app.exec())