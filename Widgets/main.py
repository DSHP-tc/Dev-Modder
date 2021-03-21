from PyQt5 import QtCore, QtGui, QtWidgets
import datetime  
from datetime import date 
from PyQt5.QtCore import QTimer, QTime,Qt
from PyQt5.QtGui import QMouseEvent, QCursor
from Clock.clock_window import Ui_Form
from Visualizer.balls import Ui_Form_Vi

class Main_clock(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form(self)
        self.ui.combo.hide()

    def mousePressEvent(self, event):
        print("MOuse press event")
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            print("self.m_Position",self.m_Position)
            self.ui.combo.hide()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon

        if event.button()==Qt.RightButton:
            self.ui.combo.show()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))


class Main_vi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui=Ui_Form_Vi(self)
        self.ui.combo.hide()

    def mousePressEvent(self, event):
        print("MOuse press event")
        if event.button()==Qt.LeftButton:
            self.m_flag=True
            self.m_Position=event.globalPos()-self.pos() #Get the position of the mouse relative to the window
            print("self.m_Position",self.m_Position)
            self.ui.combo.hide()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  #Change mouse icon

        if event.button()==Qt.RightButton:
            self.ui.combo.show()
            
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:  
            self.move(QMouseEvent.globalPos()-self.m_Position)#Change window position
            QMouseEvent.accept()
            
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag=False
        self.setCursor(QCursor(Qt.ArrowCursor))

   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    clock_obj = Main_clock()
    clock_obj.show()
    vi_obj=Main_vi()
    vi_obj.show()
    sys.exit(app.exec_())

