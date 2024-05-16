import sys 
import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path+'/Application_Login/Icons/')

from Persons.UI.add_person_window_ui import Ui_d_Persons

class AddPerson(qtw.QDialog, Ui_d_Persons):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.le_FirstName.setFocus()

        self.gb_Person.setTitle("Add Person")
        self.lb_Message.clear()

        self.pb_Close.clicked.connect(self.reject)

        self.pb_Submit.clicked.connect(self.process_entry)

    @qtc.Slot()
    def process_entry(self):
        self.lb_Message.setText("New person added")
        self.le_LastName.clear()
        self.le_FirstName.clear()

        self.le_FirstName.setFocus()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = AddPerson()

    form.open()
    # window = LoginFrom()
    # window.show()
    sys.exit(app.exec())