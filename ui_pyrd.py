# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyrd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_PyRD_gui(object):
    def setupUi(self, PyRD_gui):
        if not PyRD_gui.objectName():
            PyRD_gui.setObjectName(u"PyRD_gui")
        PyRD_gui.resize(332, 222)
        self.centralwidget = QWidget(PyRD_gui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 311, 201))
        self.verticalLayout_4 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fileName = QLineEdit(self.layoutWidget)
        self.fileName.setObjectName(u"fileName")

        self.horizontalLayout.addWidget(self.fileName)

        self.fileSelect = QPushButton(self.layoutWidget)
        self.fileSelect.setObjectName(u"fileSelect")
        self.fileSelect.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.fileSelect)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.layoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)


        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.output = QTextBrowser(self.layoutWidget)
        self.output.setObjectName(u"output")

        self.horizontalLayout_2.addWidget(self.output)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.create = QPushButton(self.layoutWidget)
        self.create.setObjectName(u"create")

        self.verticalLayout_3.addWidget(self.create)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        PyRD_gui.setCentralWidget(self.centralwidget)

        self.retranslateUi(PyRD_gui)

        self.fileSelect.setDefault(False)
        self.create.setDefault(True)


        QMetaObject.connectSlotsByName(PyRD_gui)
    # setupUi

    def retranslateUi(self, PyRD_gui):
        PyRD_gui.setWindowTitle(QCoreApplication.translate("PyRD_gui", u"PyRD GUI", None))
        self.fileSelect.setText(QCoreApplication.translate("PyRD_gui", u"\u9009\u62e9\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("PyRD_gui", "输入sprd文件名", None))
        self.label_2.setText(QCoreApplication.translate("PyRD_gui", u"然后\u6309\u56de\u8f66\u751f\u6210RD\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("PyRD_gui", "按ESC键退出", None))
        self.create.setText(QCoreApplication.translate("PyRD_gui", u"\u751f\u6210RD\u6587\u4ef6", None))
    # retranslateUi

