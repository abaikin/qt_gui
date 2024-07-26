# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectInfoPageUI.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_ProjectInfoPage(object):
    def setupUi(self, ProjectInfoPage):
        if not ProjectInfoPage.objectName():
            ProjectInfoPage.setObjectName(u"ProjectInfoPage")
        ProjectInfoPage.resize(400, 300)
        self.formLayout = QFormLayout(ProjectInfoPage)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(ProjectInfoPage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(ProjectInfoPage)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.formLayout.setItem(0, QFormLayout.FieldRole, self.verticalSpacer)

        self.projectNameLabel = QLabel(ProjectInfoPage)
        self.projectNameLabel.setObjectName(u"projectNameLabel")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.projectNameLabel)

        self.label_3 = QLabel(ProjectInfoPage)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.projectAuthorLineEdit = QLineEdit(ProjectInfoPage)
        self.projectAuthorLineEdit.setObjectName(u"projectAuthorLineEdit")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.projectAuthorLineEdit)

        self.label_4 = QLabel(ProjectInfoPage)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.projectDateLabel = QLabel(ProjectInfoPage)
        self.projectDateLabel.setObjectName(u"projectDateLabel")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.projectDateLabel)


        self.retranslateUi(ProjectInfoPage)

        QMetaObject.connectSlotsByName(ProjectInfoPage)
    # setupUi

    def retranslateUi(self, ProjectInfoPage):
        ProjectInfoPage.setWindowTitle(QCoreApplication.translate("ProjectInfoPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("ProjectInfoPage", u"Project Info", None))
        self.label_2.setText(QCoreApplication.translate("ProjectInfoPage", u"Project name", None))
        self.projectNameLabel.setText(QCoreApplication.translate("ProjectInfoPage", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("ProjectInfoPage", u"Author", None))
        self.label_4.setText(QCoreApplication.translate("ProjectInfoPage", u"Creation date", None))
        self.projectDateLabel.setText("")
    # retranslateUi

