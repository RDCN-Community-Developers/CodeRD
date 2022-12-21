import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PIL import Image, ImageFilter, ImageQt
from ui_pyrd import Ui_PyRD_gui
from compiler import *

class PyRD_gui(QMainWindow, Ui_PyRD_gui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.file = ""
        for i in os.listdir(os.getcwd()):
            if i[-5:]==".sprd":
                self.file = i
        
        self.fileName.setText(self.file)
        self.fileSelect.clicked.connect(self.select_file)
        self.create.clicked.connect(self.start)
        self.show()
    
    def select_file(self):
        file_path = QFileDialog.getOpenFileName(
            caption="请选择sprd文件", filter="(*.sprd)")
        self.file = file_path[0]
        self.fileName.setText(self.file)
    
    def start(self):
        if self.file:
            run(self.file)
            self.output.setText("生成完成")
        else:
            self.output.setText("未选择sprd文件")
    
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Return:
            self.start()
        if event.key() == Qt.Key_Escape:
            sys.exit(app.exec_())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyRD_gui()
    sys.exit(app.exec_())