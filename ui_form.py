# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpinBox, QStatusBar,
    QToolButton, QVBoxLayout, QWidget,QListWidget)

class Ui_PyRD(object):
    def setupUi(self, PyRD):
        if not PyRD.objectName():
            PyRD.setObjectName(u"PyRD")
        PyRD.resize(800, 600)
        self.importFile = QAction(PyRD)
        self.importFile.setObjectName(u"importFile")
        self.exportFile = QAction(PyRD)
        self.exportFile.setObjectName(u"exportFile")
        self.compile = QAction(PyRD)
        self.compile.setObjectName(u"compile")
        self.compileSave = QAction(PyRD)
        self.compileSave.setObjectName(u"compileSave")
        self.clearEvent = QAction(PyRD)
        self.clearEvent.setObjectName(u"clearEvent")
        self.metadataSetEvent = QAction(PyRD)
        self.metadataSetEvent.setObjectName(u"metadataSetEvent")
        self.characterSetEvent = QAction(PyRD)
        self.characterSetEvent.setObjectName(u"characterSetEvent")
        self.customPatternEvent = QAction(PyRD)
        self.customPatternEvent.setObjectName(u"customPatternEvent")
        self.centralwidget = QWidget(PyRD)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 781, 531))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.delEvent = QToolButton(self.layoutWidget)
        self.delEvent.setObjectName(u"delEvent")

        self.horizontalLayout_5.addWidget(self.delEvent)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.barEventList = QListWidget(self.layoutWidget)
        self.barEventList.setObjectName(u"barEventList")

        self.verticalLayout_3.addWidget(self.barEventList)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.eventList = QListWidget(self.layoutWidget)
        self.eventList.setObjectName(u"eventList")

        self.verticalLayout.addWidget(self.eventList)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.selectPara = QListWidget(self.layoutWidget)
        self.selectPara.setObjectName(u"selectPara")

        self.verticalLayout_2.addWidget(self.selectPara)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.currentBar = QSpinBox(self.layoutWidget)
        self.currentBar.setObjectName(u"currentBar")

        self.horizontalLayout_2.addWidget(self.currentBar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.eventEdit = QLineEdit(self.layoutWidget)
        self.eventEdit.setObjectName(u"eventEdit")

        self.horizontalLayout.addWidget(self.eventEdit)

        self.addEvent = QPushButton(self.layoutWidget)
        self.addEvent.setObjectName(u"addEvent")

        self.horizontalLayout.addWidget(self.addEvent)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        PyRD.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PyRD)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.fileBar = QMenu(self.menubar)
        self.fileBar.setObjectName(u"fileBar")
        self.compileBar = QMenu(self.menubar)
        self.compileBar.setObjectName(u"compileBar")
        self.editBar = QMenu(self.menubar)
        self.editBar.setObjectName(u"editBar")
        PyRD.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PyRD)
        self.statusbar.setObjectName(u"statusbar")
        PyRD.setStatusBar(self.statusbar)

        self.menubar.addAction(self.fileBar.menuAction())
        self.menubar.addAction(self.compileBar.menuAction())
        self.menubar.addAction(self.editBar.menuAction())
        self.fileBar.addAction(self.importFile)
        self.fileBar.addAction(self.exportFile)
        self.compileBar.addAction(self.compile)
        self.compileBar.addAction(self.compileSave)
        self.editBar.addAction(self.clearEvent)
        self.editBar.addAction(self.metadataSetEvent)
        self.editBar.addAction(self.characterSetEvent)
        self.editBar.addAction(self.customPatternEvent)
        
        self.retranslateUi(PyRD)

        QMetaObject.connectSlotsByName(PyRD)
    # setupUi

    def retranslateUi(self, PyRD):
        PyRD.setWindowTitle(QCoreApplication.translate("PyRD", u"PyRD", None))# type: ignore
        self.importFile.setText(QCoreApplication.translate("PyRD", u"\u52a0\u8f7d\u6587\u4ef6", None))# type: ignore
        self.exportFile.setText(QCoreApplication.translate("PyRD", u"\u4fdd\u5b58\u6587\u4ef6", None))# type: ignore
        self.compile.setText(QCoreApplication.translate("PyRD", u"\u7f16\u8bd1", None))# type: ignore
        self.compileSave.setText(QCoreApplication.translate("PyRD", u"\u7f16\u8bd1\u5e76\u4fdd\u5b58", None))# type: ignore
        self.clearEvent.setText(QCoreApplication.translate("PyRD", u"\u6e05\u7a7a\u4e8b\u4ef6", None))# type: ignore
        self.label.setText(QCoreApplication.translate("PyRD", u"\u672c\u5c0f\u8282\u4e8b\u4ef6", None))# type: ignore
        self.delEvent.setText(QCoreApplication.translate("PyRD", u"\u5220\u9664\u4e8b\u4ef6", None))# type: ignore
        self.label_5.setText(QCoreApplication.translate("PyRD", u"\u4e8b\u4ef6\u5217\u8868", None))# type: ignore
        self.label_2.setText(QCoreApplication.translate("PyRD", u"\u53c2\u6570\u9009\u53d6", None))# type: ignore
        self.label_4.setText(QCoreApplication.translate("PyRD", u"\u5f53\u524d\u5c0f\u8282", None))# type: ignore
        self.label_3.setText(QCoreApplication.translate("PyRD", u"\u53c2\u6570\u8f93\u5165", None))# type: ignore
        self.addEvent.setText(QCoreApplication.translate("PyRD", u"\u6dfb\u52a0\u4e8b\u4ef6", None))# type: ignore
        self.fileBar.setTitle(QCoreApplication.translate("PyRD", u"\u6587\u4ef6", None))# type: ignore
        self.compileBar.setTitle(QCoreApplication.translate("PyRD", u"\u7f16\u8bd1", None))# type: ignore
        self.editBar.setTitle(QCoreApplication.translate("PyRD", u"\u7f16\u8f91", None)) # type: ignore
        self.metadataSetEvent.setText(QCoreApplication.translate("PyRD", u"设置metadata", None)) # type: ignore
        self.characterSetEvent.setText(QCoreApplication.translate("PyRD", u"设置角色", None)) # type: ignore
        self.customPatternEvent.setText(QCoreApplication.translate("PyRD", u"自定义拍型管理", None)) # type: ignore
        
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
    # retranslateUi

