# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)
import Icons_rc

class Ui_w_LoginForm(object):
    def setupUi(self, w_LoginForm):
        if not w_LoginForm.objectName():
            w_LoginForm.setObjectName(u"w_LoginForm")
        w_LoginForm.resize(643, 305)
        font = QFont()
        font.setPointSize(12)
        w_LoginForm.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        w_LoginForm.setWindowIcon(icon)
        self.gridLayout = QGridLayout(w_LoginForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_cancel = QPushButton(w_LoginForm)
        self.pb_cancel.setObjectName(u"pb_cancel")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/excel_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_cancel.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_cancel, 2, 1, 1, 1)

        self.lb_Message = QLabel(w_LoginForm)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 3, 0, 1, 2)

        self.groupBox = QGroupBox(w_LoginForm)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_user_id = QLineEdit(self.groupBox)
        self.le_user_id.setObjectName(u"le_user_id")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_user_id)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_password = QLineEdit(self.groupBox)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.Password)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_password)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 2)

        self.pb_Ok = QPushButton(w_LoginForm)
        self.pb_Ok.setObjectName(u"pb_Ok")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/canva_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Ok.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Ok, 2, 0, 1, 1)

        QWidget.setTabOrder(self.le_user_id, self.le_password)
        QWidget.setTabOrder(self.le_password, self.pb_cancel)
        QWidget.setTabOrder(self.pb_cancel, self.pb_Ok)

        self.retranslateUi(w_LoginForm)

        QMetaObject.connectSlotsByName(w_LoginForm)
    # setupUi

    def retranslateUi(self, w_LoginForm):
        w_LoginForm.setWindowTitle(QCoreApplication.translate("w_LoginForm", u"Sample App", None))
        self.pb_cancel.setText(QCoreApplication.translate("w_LoginForm", u"Cancel", None))
        self.lb_Message.setText(QCoreApplication.translate("w_LoginForm", u"Message", None))
        self.groupBox.setTitle(QCoreApplication.translate("w_LoginForm", u"Wellcome. Please Login", None))
        self.label.setText(QCoreApplication.translate("w_LoginForm", u"user ID", None))
        self.label_2.setText(QCoreApplication.translate("w_LoginForm", u"PassWord", None))
        self.pb_Ok.setText(QCoreApplication.translate("w_LoginForm", u"Ok", None))
    # retranslateUi

