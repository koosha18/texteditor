# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(913, 617)
        MainWindow.setToolTip("")
        MainWindow.setToolTipDuration(0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setToolTipDuration(0)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.htmlEdit = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.htmlEdit.setFont(font)
        self.htmlEdit.setStyleSheet("background-color: rgb(58, 58, 58);\n"
"color: rgb(0, 144, 0);\n"
"border: 0px solid;\n"
"border-left: 1px solid;\n"
"")
        self.htmlEdit.setObjectName("htmlEdit")
        self.horizontalLayout.addWidget(self.htmlEdit)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 913, 26))
        self.menuBar.setMinimumSize(QtCore.QSize(0, 0))
        self.menuBar.setToolTipDuration(0)
        self.menuBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-bottom: 1px solid;")
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setToolTipDuration(0)
        self.menuFile.setStyleSheet("border : 1px solid;\n"
"border-color: rgb(255, 255, 255);")
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setAutoFillBackground(False)
        self.statusBar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setEnabled(True)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.toolBar.setAcceptDrops(False)
        self.toolBar.setToolTipDuration(0)
        self.toolBar.setAutoFillBackground(False)
        self.toolBar.setStyleSheet("background-color: rgb(254, 254, 254);\n"
"color: rgb(0, 0, 0);\n"
"border: none;\n"
"border-bottom: 0px solid;\n"
"")
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionOpen.setObjectName("actionOpen")
        self.actioncolor = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioncolor.setIcon(icon2)
        self.actioncolor.setStatusTip("")
        self.actioncolor.setWhatsThis("")
        self.actioncolor.setMenuRole(QtWidgets.QAction.TextHeuristicRole)
        self.actioncolor.setObjectName("actioncolor")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/save as.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon3)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionTable = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/table.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTable.setIcon(icon4)
        self.actionTable.setObjectName("actionTable")
        self.actionBullet_Points = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/bullet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBullet_Points.setIcon(icon5)
        self.actionBullet_Points.setObjectName("actionBullet_Points")
        self.actionIndents = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/right with arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionIndents.setIcon(icon6)
        self.actionIndents.setObjectName("actionIndents")
        self.actionHighlight_text = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/pen.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHighlight_text.setIcon(icon7)
        self.actionHighlight_text.setObjectName("actionHighlight_text")
        self.actionalignLeft = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/left indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionalignLeft.setIcon(icon8)
        self.actionalignLeft.setObjectName("actionalignLeft")
        self.actionAlignRight = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/right indent.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlignRight.setIcon(icon9)
        self.actionAlignRight.setObjectName("actionAlignRight")
        self.actionAlign_center = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/middle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAlign_center.setIcon(icon10)
        self.actionAlign_center.setObjectName("actionAlign_center")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPrint.setIcon(icon11)
        self.actionPrint.setObjectName("actionPrint")
        self.actionBold = QtWidgets.QAction(MainWindow)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icons/bold.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon12)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(MainWindow)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icons/italic.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon13)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(MainWindow)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icons/underline.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon14)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionNumber_List = QtWidgets.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("icons/number.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNumber_List.setIcon(icon15)
        self.actionNumber_List.setObjectName("actionNumber_List")
        self.actionCut = QtWidgets.QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionHTML = QtWidgets.QAction(MainWindow)
        self.actionHTML.setObjectName("actionHTML")
        self.actionTEXT = QtWidgets.QAction(MainWindow)
        self.actionTEXT.setObjectName("actionTEXT")
        self.actionimage = QtWidgets.QAction(MainWindow)
        self.actionimage.setObjectName("actionimage")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionPrint)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.toolBar.addAction(self.actioncolor)
        self.toolBar.addAction(self.actionHighlight_text)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionimage)
        self.toolBar.addAction(self.actionTable)
        self.toolBar.addAction(self.actionBullet_Points)
        self.toolBar.addAction(self.actionNumber_List)
        self.toolBar.addAction(self.actionIndents)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionalignLeft)
        self.toolBar.addAction(self.actionAlign_center)
        self.toolBar.addAction(self.actionAlignRight)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHTML)
        self.toolBar.addAction(self.actionTEXT)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.htmlEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSave.setText(_translate("MainWindow", "Save File"))
        self.actionSave.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Save File</span></p></body></html>"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionOpen.setText(_translate("MainWindow", "Open File"))
        self.actionOpen.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Open File</p></body></html>"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actioncolor.setText(_translate("MainWindow", "Text Color"))
        self.actioncolor.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">text color</span></p></body></html>"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As "))
        self.actionSave_As.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Save file as</p></body></html>"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionTable.setText(_translate("MainWindow", "Table"))
        self.actionTable.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Insert Table</p></body></html>"))
        self.actionBullet_Points.setText(_translate("MainWindow", "Bullet Points "))
        self.actionBullet_Points.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Adding Bullet points </p></body></html>"))
        self.actionIndents.setText(_translate("MainWindow", "Indents"))
        self.actionIndents.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Indents</p></body></html>"))
        self.actionHighlight_text.setText(_translate("MainWindow", "Highlight text"))
        self.actionHighlight_text.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Highlight text</p></body></html>"))
        self.actionalignLeft.setText(_translate("MainWindow", "alignLeft"))
        self.actionalignLeft.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Align left</span></p></body></html>"))
        self.actionAlignRight.setText(_translate("MainWindow", "AlignRight"))
        self.actionAlignRight.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Align Right</span></p></body></html>"))
        self.actionAlign_center.setText(_translate("MainWindow", "Aligncenter"))
        self.actionAlign_center.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Align center</span></p></body></html>"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionPrint.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Print</span></p></body></html>"))
        self.actionPrint.setShortcut(_translate("MainWindow", "Ctrl+P"))
        self.actionBold.setText(_translate("MainWindow", "Bold"))
        self.actionBold.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Bold</span></p></body></html>"))
        self.actionBold.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindow", "Italic"))
        self.actionItalic.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Italic</span></p></body></html>"))
        self.actionItalic.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindow", "Underline"))
        self.actionUnderline.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Underline</span></p></body></html>"))
        self.actionUnderline.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionNumber_List.setText(_translate("MainWindow", "Number List"))
        self.actionNumber_List.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Number List</span></p></body></html>"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Cut</span></p></body></html>"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Paste</span></p></body></html>"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Undo</span></p></body></html>"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">Redo</span></p></body></html>"))
        self.actionHTML.setText(_translate("MainWindow", "HTML"))
        self.actionHTML.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">HTML</span></p></body></html>"))
        self.actionTEXT.setText(_translate("MainWindow", "TEXT"))
        self.actionTEXT.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">To Text</span></p></body></html>"))
        self.actionimage.setText(_translate("MainWindow", "Image"))
        self.actionimage.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#000000;\">insert image</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
