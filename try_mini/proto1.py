# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proto1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
from try_mini import pdf2, python2


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.open_pdf.setGeometry(QtCore.QRect(130, 140, 75, 24))
        self.open_pdf.setObjectName("open_pdf")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(500, 50, 256, 192))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 141, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 270, 49, 16))
        self.label_3.setObjectName("label_3")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(50, 350, 291, 181))
        self.outputlabel.setText("")
        self.outputlabel.setObjectName("outputlabel")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 390, 101, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Export = QtWidgets.QAction(MainWindow)
        self.actionSave_Export.setObjectName("actionSave_Export")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Export)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionOpen.triggered.connect(self.openFile)
        self.open_pdf.clicked.connect(self.openFile
                                      )
    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            QtCore.QDir.homePath(),
            'Text Files (*.txt) ;;Pdf Files (*.pdf) ;;All Files (*)',
            'Python Files (*.py)',
            QtWidgets.QFileDialog.DontUseNativeDialog |
            QtWidgets.QFileDialog.DontResolveSymlinks
        )
        if filename:
            print(filename)
            if filename.endswith('.pdf'):
                pdf2.pdf_to_txt(filename)
            # try:
            #     with open(filename, 'r') as fh:
            #         pdf2.pdf_to_txt(fh)
            # except Exception as e:
            #     # Errata:  Book contains the following line:
            #     # qtw.QMessageBox.critical(f"Could not load file: {e}")
            #     # It should read like this:
            #     QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_pdf.setText(_translate("MainWindow", "Open pdf"))
        self.label.setText(_translate("MainWindow", "OR"))
        self.label_2.setText(_translate("MainWindow", "Input Pdf or Paste text"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.pushButton.setText(_translate("MainWindow", "Export as pdf"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "open a pdf file or text file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Export.setText(_translate("MainWindow", "Save/Export"))
        self.actionSave_Export.setStatusTip(_translate("MainWindow", "save the file"))
        self.actionSave_Export.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
