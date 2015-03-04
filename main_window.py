#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#


"""

"""

import sys, os, io
import ntpath
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt


class BtnTitlebar(QtGui.QPushButton):
    def __init__(self, *args, **kwargs):
        super(BtnTitlebar, self).__init__(*args, **kwargs)
        self.m_ishover = False
        
    def paintEvent(self, evt):
        super(BtnTitlebar, self).paintEvent(evt)
        
    def isHover(self):
        return self.m_ishover
        
    def enterEvent(self, evt):
        self.m_ishover = True
        
    def leaveEvent(self, evt):
        self.m_ishover = False

class BtnMinimize(BtnTitlebar):
    def __init__(self, *args, **kwargs):
        super(BtnMinimize, self).__init__(*args, **kwargs)
        
    def paintEvent(self, evt):
        super(BtnMinimize, self).paintEvent(evt)
        painter = QtGui.QPainter(self)
        if self.isDown() or self.isHover():
            painter.fillRect(QtCore.QRect(10,14,8,2), QtGui.QColor("#FFFFFF"))
        else:
            painter.fillRect(QtCore.QRect(10,14,8,2), QtGui.QColor("#282828"))

class BtnClose(BtnTitlebar):
    def __init__(self, *args, **kwargs):
        super(BtnClose, self).__init__(*args, **kwargs)
        
    def paintEvent(self, evt):
        super(BtnClose, self).paintEvent(evt)
        painter = QtGui.QPainter(self)
        if self.isDown() or self.isHover():
            painter.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor("#FFFFFF")), 1.42))
        else:
            painter.setPen(QtGui.QPen(QtGui.QBrush(QtGui.QColor("#282828")), 1.42))
        
        painter.drawLine(15,10,20,15)
        painter.drawPoint(14,9)
        painter.drawPoint(21,15)
        
        painter.drawLine(20,10,15,15)
        painter.drawPoint(21,9)
        painter.drawPoint(14,15)

class MainWindow(QtGui.QWidget):
    def __init__(self):

        QtGui.QWidget.__init__(self)

        # initial position
        self.m_DragPosition=self.pos()
        self.m_drag = False
        
        self.resize(552,245)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setMouseTracking(True)
        self.setStyleSheet("QWidget{background-color:#2C3E50;}")
        
#        self.setWindowTitle()
#        self.setWindowIcon(QtGui.QIcon())

        qlbl_title = QtGui.QLabel("Title", self)
        qlbl_title.setGeometry(0,0,552,40)
        qlbl_title.setStyleSheet("QLabel{background-color:#4a93ca;"
                                        "border:none;"
                                        "color:#ffffff;"
                                        "font:bold;"
                                        "font-size:16px;"
                                        "font-family:Meiryo UI;"
                                        "qproperty-alignment:AlignCenter;}")
        
        self.qbtn_minimize=BtnMinimize(self)
        self.qbtn_minimize.setGeometry(476,0,28,24)
        self.qbtn_minimize.setStyleSheet("QPushButton{background-color:#4a93ca;"
                                                      "border:none;"
#                                                      "color:#000000;"
                                                      "font-size:12px;"
                                                      "font-family:Tahoma;}"
                                        "QPushButton:hover{background-color:#295e87;}"
                                        "QPushButton:pressed{background-color:#204a6a;}")
        
        self.qbtn_close=BtnClose(self)
        self.qbtn_close.setGeometry(505,0,36,24)
        self.qbtn_close.setStyleSheet("QPushButton{background-color:#4a93ca;"
                                                  "border:none;"
#                                                  "color:#ffffff;"
                                                  "font-size:12px;"
                                                  "font-family:Tahoma;}"
                                      "QPushButton:hover{background-color:#ea5e00;}"
                                      "QPushButton:pressed{background-color:#994005;}")

        self.qbtn_minimize.clicked.connect(self.btnClicked_minimize)
        self.qbtn_close.clicked.connect(self.btnClicked_close)

    # reload method to support window draging
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()

    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton and self.m_drag:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False

    def btnClicked_minimize(self):
        self.showMinimized()

    def btnClicked_close(self):
        os._exit(0)


if __name__=="__main__":
    mapp=QtGui.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(mapp.exec_())
