# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectViewUI.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ProjectView(object):
    def setupUi(self, ProjectView):
        if not ProjectView.objectName():
            ProjectView.setObjectName(u"ProjectView")
        ProjectView.resize(400, 300)
        self.verticalLayout = QVBoxLayout(ProjectView)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(ProjectView)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setHeaderHidden(True)

        self.verticalLayout.addWidget(self.treeWidget)


        self.retranslateUi(ProjectView)

        QMetaObject.connectSlotsByName(ProjectView)
    # setupUi

    def retranslateUi(self, ProjectView):
        ProjectView.setWindowTitle(QCoreApplication.translate("ProjectView", u"Form", None))
    # retranslateUi

