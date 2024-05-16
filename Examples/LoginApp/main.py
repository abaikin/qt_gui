import sys 
import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path+'/Application_Login/Icons/')

from Main.UI.main_window_ui import Ui_mw_Main
from add_person import AddPerson
from login import LoginForm

# The login app from tutorial https://www.youtube.com/watch?v=uzqDnB44qf4 

class MainWindow(qtw.QMainWindow, Ui_mw_Main):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.action_Quit.triggered.connect(self.close)

        self.action_AddPerson.triggered.connect(self.open_add_person)

        self.form = LoginForm()
        self.form.login_success.connect(self.show)
        self.form.show()


    @qtc.Slot()
    def open_add_person(self):
        self.form = AddPerson()
        self.form.exec() # like open but there is difference

    #     if self.le_user_id.text() == "Jason" and self.le_password.text()=="Password":
    #         self.login_success.emit()
    #         self.close()
    #     else:
    #         self.lb_Message.setText("Login incorrect!")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())