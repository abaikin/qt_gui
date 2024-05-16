# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadPressureWindowUI.ui'
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
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableView, QTextEdit,
    QWidget)

class Ui_LoadPressureDialog(object):
    def setupUi(self, LoadPressureDialog):
        if not LoadPressureDialog.objectName():
            LoadPressureDialog.setObjectName(u"LoadPressureDialog")
        LoadPressureDialog.resize(779, 688)
        self.horizontalLayout = QHBoxLayout(LoadPressureDialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tab_get_data_steps = QTabWidget(LoadPressureDialog)
        self.tab_get_data_steps.setObjectName(u"tab_get_data_steps")
        self.tab_load = QWidget()
        self.tab_load.setObjectName(u"tab_load")
        self.formLayout = QFormLayout(self.tab_load)
        self.formLayout.setObjectName(u"formLayout")
        self.le_filepath = QLineEdit(self.tab_load)
        self.le_filepath.setObjectName(u"le_filepath")
        self.le_filepath.setMinimumSize(QSize(350, 20))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.le_filepath)

        self.pb_load_file = QPushButton(self.tab_load)
        self.pb_load_file.setObjectName(u"pb_load_file")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.pb_load_file)

        self.te_filecontent = QTextEdit(self.tab_load)
        self.te_filecontent.setObjectName(u"te_filecontent")
        palette = QPalette()
        brush = QBrush(QColor(62, 62, 186, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush1 = QBrush(QColor(255, 255, 127, 180))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.te_filecontent.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.te_filecontent.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.te_filecontent)

        self.pb_load_data_next = QPushButton(self.tab_load)
        self.pb_load_data_next.setObjectName(u"pb_load_data_next")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pb_load_data_next)

        self.tab_get_data_steps.addTab(self.tab_load, "")
        self.tab_parse = QWidget()
        self.tab_parse.setObjectName(u"tab_parse")
        self.gridLayout = QGridLayout(self.tab_parse)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tv_parsed_data = QTableView(self.tab_parse)
        self.tv_parsed_data.setObjectName(u"tv_parsed_data")

        self.gridLayout.addWidget(self.tv_parsed_data, 0, 0, 1, 1)

        self.tab_get_data_steps.addTab(self.tab_parse, "")

        self.horizontalLayout.addWidget(self.tab_get_data_steps)


        self.retranslateUi(LoadPressureDialog)

        self.tab_get_data_steps.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LoadPressureDialog)
    # setupUi

    def retranslateUi(self, LoadPressureDialog):
        LoadPressureDialog.setWindowTitle(QCoreApplication.translate("LoadPressureDialog", u"Dialog", None))
        self.pb_load_file.setText(QCoreApplication.translate("LoadPressureDialog", u"Load File", None))
        self.pb_load_data_next.setText(QCoreApplication.translate("LoadPressureDialog", u"Next", None))
        self.tab_get_data_steps.setTabText(self.tab_get_data_steps.indexOf(self.tab_load), QCoreApplication.translate("LoadPressureDialog", u"Load Data", None))
        self.tab_get_data_steps.setTabText(self.tab_get_data_steps.indexOf(self.tab_parse), QCoreApplication.translate("LoadPressureDialog", u"Parse Data", None))
    # retranslateUi

