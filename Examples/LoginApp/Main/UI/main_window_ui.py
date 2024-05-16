# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)
import Icons_rc

class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        if not mw_Main.objectName():
            mw_Main.setObjectName(u"mw_Main")
        mw_Main.resize(800, 600)
        font = QFont()
        font.setPointSize(12)
        mw_Main.setFont(font)
        icon = QIcon()
        icon.addFile(u":/Main/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        mw_Main.setWindowIcon(icon)
        self.action_Quit = QAction(mw_Main)
        self.action_Quit.setObjectName(u"action_Quit")
        icon1 = QIcon()
        icon1.addFile(u":/Buttons/canva_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_Quit.setIcon(icon1)
        self.action_Quit.setFont(font)
        self.actionAdd_Person = QAction(mw_Main)
        self.actionAdd_Person.setObjectName(u"actionAdd_Person")
        self.actionAdd_Person.setFont(font)
        self.action_AddPerson = QAction(mw_Main)
        self.action_AddPerson.setObjectName(u"action_AddPerson")
        icon2 = QIcon()
        icon2.addFile(u":/Buttons/excel_btn.png", QSize(), QIcon.Normal, QIcon.Off)
        self.action_AddPerson.setIcon(icon2)
        self.action_AddPerson.setFont(font)
        self.centralwidget = QWidget(mw_Main)
        self.centralwidget.setObjectName(u"centralwidget")
        mw_Main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mw_Main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 28))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuPerson = QMenu(self.menubar)
        self.menuPerson.setObjectName(u"menuPerson")
        mw_Main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mw_Main)
        self.statusbar.setObjectName(u"statusbar")
        mw_Main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPerson.menuAction())
        self.menuFile.addAction(self.action_Quit)
        self.menuPerson.addAction(self.action_AddPerson)

        self.retranslateUi(mw_Main)

        QMetaObject.connectSlotsByName(mw_Main)
    # setupUi

    def retranslateUi(self, mw_Main):
        mw_Main.setWindowTitle(QCoreApplication.translate("mw_Main", u"Sample App", None))
        self.action_Quit.setText(QCoreApplication.translate("mw_Main", u"Quit", None))
        self.actionAdd_Person.setText(QCoreApplication.translate("mw_Main", u"Add Person", None))
        self.action_AddPerson.setText(QCoreApplication.translate("mw_Main", u"Add Person", None))
        self.menuFile.setTitle(QCoreApplication.translate("mw_Main", u"File", None))
        self.menuPerson.setTitle(QCoreApplication.translate("mw_Main", u"Person", None))
    # retranslateUi

