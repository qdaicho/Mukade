# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topHorizontalLayout.setObjectName("topHorizontalLayout")
        self.backToLibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToLibraryButton.setObjectName("backToLibraryButton")
        self.topHorizontalLayout.addWidget(self.backToLibraryButton)
        self.zoomOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.topHorizontalLayout.addWidget(self.zoomOutButton)
        self.zoomInButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButton.setObjectName("zoomInButton")
        self.topHorizontalLayout.addWidget(self.zoomInButton)
        self.verticalLayout.addLayout(self.topHorizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 508))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")
        self.mangaChapterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.mangaChapterComboBox.setEditable(False)
        self.mangaChapterComboBox.setObjectName("mangaChapterComboBox")
        self.bottomHorizontalLayout.addWidget(self.mangaChapterComboBox)
        self.nextChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextChapterButton.setObjectName("nextChapterButton")
        self.bottomHorizontalLayout.addWidget(self.nextChapterButton)
        self.lastChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastChapterButton.setObjectName("lastChapterButton")
        self.bottomHorizontalLayout.addWidget(self.lastChapterButton)
        self.verticalLayout.addLayout(self.bottomHorizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.backToLibraryButton.setText(_translate("MainWindow", "Back to Library"))
        self.zoomOutButton.setText(_translate("MainWindow", "Zoom Out"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom In"))
        self.nextChapterButton.setText(_translate("MainWindow", "Next Chapter"))
        self.lastChapterButton.setText(_translate("MainWindow", "Last Chapter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
