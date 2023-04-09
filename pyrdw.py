# This Python file uses the following encoding: utf-8

import sys



from PySide6.QtWidgets import QApplication,QMainWindow,QFileDialog

from ui_form import Ui_PyRD
import pyrd

def listAllEditableFunctions():
    functions=pyrd.__all__
    functions.remove("SetLevelMeta")
    functions.remove("parseIf")
    functions.remove("AddCharacter")
    return functions

class PyRD(QMainWindow):

    def __init__(self, parent=None):

        super().__init__(parent)
        self.ui = Ui_PyRD()
        self.ui.setupUi(self)
        self.ui.importFile.triggered.connect(self.select_file) # 当按下self.ui.importFile,执行select_file函数
        #在self.ui.eventList里输出所有pyrd支持的函数,调用pyrd.__all__
        self.ui.eventList.addItems(listAllEditableFunctions())
        self.file = None
        #self.ui.exportFile.triggered.connect(self.export_file)
        #self.ui.compile.triggered.connect(self.compile_file)
        #self.ui.compileSave.triggered.connect(self.compile_save_file)
        #self.ui.clearEvent.triggered.connect(self.clear_event)
        #self.ui.metadataSetEvent.triggered.connect(self.metadata_set_event)
        #self.ui.characterSetEvent.triggered.connect(self.character_set_event)
        #self.ui.delEvent.clicked.connect(self.del_event)
        #self.ui.addEvent.clicked.connect(self.add_event)
        


    def select_file(self):
        file_path = QFileDialog.getOpenFileName(self,caption="请选择sprd文件", filter="(*.sprd)")
        self.file = file_path[0]

   
    

    

if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = PyRD()

    widget.show() 

    sys.exit(app.exec())

