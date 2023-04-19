# This Python file uses the following encoding: utf-8

import inspect
import sys



from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog

from ui_form import Ui_PyRD
import pyrd

def listAllEditableFunctions():
    functions=pyrd.__all__
    functions.remove("SetLevelMeta")
    functions.remove("parseIf")
    functions.remove("AddCharacter")
    functions.remove("Export")
    return functions

class PyRD(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_PyRD()
        self.ui.setupUi(self)
        self.ui.importFile.triggered.connect(self.select_file) # 当按下self.ui.importFile,执行select_file函数
        self._lastPara=""
        self.id = 0
        self.sprdDict={
            "metadata":{
            
            },
            "charcaters":{
            
            },
            "bars":{
            
            }
        }
        self.curBarList=[]
        self.curParaDict={}
        #在self.ui.eventList里输出所有pyrd支持的函数,调用pyrd.__all__
        self.ui.eventList.addItems(listAllEditableFunctions())
        #在点击self.ui.eventList的一个项目的时候,使用inspect模块在self.ui.selectPara里展示
        self.ui.eventList.itemClicked.connect(self.showPara)
        self.ui.barEventList.itemClicked.connect(self.showBarPara)
        self.ui.selectPara.itemClicked.connect(self.saveAndRefreshPara)
        self.ui.addEvent.clicked.connect(self.addEvent)

    def saveAndRefreshPara(self):
        if not self._lastPara:
            self._lastPara = self.ui.selectPara.currentItem().text()
            return
        if self._lastPara == self.ui.selectPara.currentItem().text():
            return
        Arg=self.ui.eventEdit.text()
        if Arg:
            self.curParaDict[self._lastPara] = eval(Arg)
        if self.ui.selectPara.currentItem().text() in self.curParaDict:
            self.ui.eventEdit.setText(str(self.curParaDict[self.ui.selectPara.currentItem().text()]))
        else:
            self.ui.eventEdit.clear()
        self._lastPara = self.ui.selectPara.currentItem().text()
        print("curParaDict:",self.curParaDict)

    def showBarPara(self):
        #获取eventList点击的项目,并且使用inspect获取对应pyrd库函数的所有参数
        self.ui.selectPara.clear()
        self.ui.eventEdit.clear()
        selectedEvent=self.ui.barEventList.currentItem().text()
        para=inspect.getfullargspec(eval("pyrd."+selectedEvent)).args
        para.remove("bar")
        #清除lastPara与curParaDict
        self._lastPara = ""
        #self.curParaDict = self.curBarList
        for curParaDict in self.curBarList:
            if curParaDict["id"] == self.ui.barEventList.currentIndex():
                self.curParaDict = curParaDict
        #在self.ui.selectPara里展示参数
        self.ui.selectPara.addItems(para)

    def showPara(self):
        #获取eventList点击的项目,并且使用inspect获取对应pyrd库函数的所有参数
        self.ui.selectPara.clear()
        self.ui.eventEdit.clear()
        selectedEvent=self.ui.eventList.currentItem().text()
        para=inspect.getfullargspec(eval("pyrd."+selectedEvent)).args
        para.remove("bar")
        #清除lastPara与curParaDict
        self._lastPara = ""
        self.curParaDict = {"func":selectedEvent,"id":self.id}
        #在self.ui.selectPara里展示参数
        self.ui.selectPara.addItems(para)

    def addEvent(self):
        self.saveAndRefreshPara()
        self.curBarList.append(self.curParaDict)
        self.ui.barEventList.clear()
        for function in self.curBarList:
            self.ui.barEventList.addItem(function["func"])
        self.id = self.id+1
        print("curBarList:",self.curBarList)

    def select_file(self):
        file_path = QFileDialog.getOpenFileName(self,caption="请选择sprd文件", filter="(*.sprd)")
        self.file = file_path[0]

   
    

    

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = PyRD()

    widget.show() 

    sys.exit(app.exec())

