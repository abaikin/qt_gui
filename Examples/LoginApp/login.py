import sys 
import os
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtg

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path+'/Application_Login/Icons/')


from Application_Login.UI.login_window_ui import Ui_w_LoginForm

class LoginForm(qtw.QWidget, Ui_w_LoginForm):

    login_success = qtc.Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pb_cancel.clicked.connect(self.close)

        self.pb_Ok.clicked.connect(self.process_login)

    @qtc.Slot()
    def process_login(self):
        if self.le_user_id.text() == "Jason" and self.le_password.text()=="Password":
            self.login_success.emit()
            self.close()
        else:
            self.lb_Message.setText("Login incorrect!")

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = LoginForm()
    window.show()
    sys.exit(app.exec())