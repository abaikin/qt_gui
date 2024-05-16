# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_person_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)
import Icons_rc

class Ui_d_Persons(object):
    def setupUi(self, d_Persons):
        if not d_Persons.objectName():
            d_Persons.setObjectName(u"d_Persons")
        d_Persons.setWindowModality(Qt.ApplicationModal)
        d_Persons.resize(523, 262)
        font = QFont()
        font.setPointSize(12)
        d_Persons.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        d_Persons.setWindowIcon(icon)
        self.gridLayout = QGridLayout(d_Persons)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pb_Submit = QPushButton(d_Persons)
        self.pb_Submit.setObjectName(u"pb_Submit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/canva_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Submit.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Submit, 1, 1, 1, 1)

        self.pb_Close = QPushButton(d_Persons)
        self.pb_Close.setObjectName(u"pb_Close")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/excel_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_Close.setIcon(icon2)

        self.gridLayout.addWidget(self.pb_Close, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gb_Person = QGroupBox(d_Persons)
        self.gb_Person.setObjectName(u"gb_Person")
        self.gb_Person.setAlignment(Qt.AlignCenter)
        self.formLayout = QFormLayout(self.gb_Person)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.gb_Person)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.le_FirstName = QLineEdit(self.gb_Person)
        self.le_FirstName.setObjectName(u"le_FirstName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.le_FirstName)

        self.label_2 = QLabel(self.gb_Person)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.le_LastName = QLineEdit(self.gb_Person)
        self.le_LastName.setObjectName(u"le_LastName")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.le_LastName)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer)


        self.gridLayout.addWidget(self.gb_Person, 0, 0, 1, 3)

        self.lb_Message = QLabel(d_Persons)
        self.lb_Message.setObjectName(u"lb_Message")

        self.gridLayout.addWidget(self.lb_Message, 2, 0, 1, 3)


        self.retranslateUi(d_Persons)

        QMetaObject.connectSlotsByName(d_Persons)
    # setupUi

    def retranslateUi(self, d_Persons):
        d_Persons.setWindowTitle(QCoreApplication.translate("d_Persons", u"Sample App", None))
        self.pb_Submit.setText(QCoreApplication.translate("d_Persons", u"Submit", None))
        self.pb_Close.setText(QCoreApplication.translate("d_Persons", u"Close", None))
        self.gb_Person.setTitle(QCoreApplication.translate("d_Persons", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("d_Persons", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("d_Persons", u"Last Name", None))
        self.lb_Message.setText(QCoreApplication.translate("d_Persons", u"Message", None))
    # retranslateUi

