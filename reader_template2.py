# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import re, os, pprint, qdarkstyle


class Ui_MainWindow(QtWidgets.QWidget):

    def setupUi(self, MainWindow):
        #################################################################################################
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        #MAIN WINDOW SETUP AND LAYOUT
        #################################################################################################
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
        self.zoomInButton.clicked.connect(self.on_click)

        self.verticalLayout.addLayout(self.topHorizontalLayout)
        #ATTACH TOP NAVIGATION BAR
        #################################################################################################
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
        #ATTACH MIDDLE SCROLL AREA FOR MANGA READING
        #################################################################################################

        content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(content_widget)
        self.image_viewer_layout = QtWidgets.QVBoxLayout(content_widget)
        # self.image_viewer_layout.setContentsMargins(50, 50, 50, 50)

        url = "/home/emsee/Documents/Manga/Tokyo Ghoul/chapter_1"

        # gets all the images from given url
        image_url_list = self.sorted_nicely([os.path.join(url, file) for file in os.listdir(url)])
        self.files_it = iter(image_url_list)
        
        pprint.pprint(image_url_list)

        self.counter = 0 # This counts the pages as window gets populated w/ images

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.on_timeout)
        self.timer.start(1000)

        #STILL UNDER CONSTRUCTION
        #################################################################################################
        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")

        self.mangaChapterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.mangaChapterComboBox.setEditable(False)
        self.mangaChapterComboBox.setObjectName("mangaChapterComboBox")
        self.bottomHorizontalLayout.addWidget(self.mangaChapterComboBox)

        self.lastChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastChapterButton.setObjectName("lastChapterButton")
        self.bottomHorizontalLayout.addWidget(self.lastChapterButton)
        self.verticalLayout.addLayout(self.bottomHorizontalLayout)

        self.nextChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextChapterButton.setObjectName("nextChapterButton")
        self.bottomHorizontalLayout.addWidget(self.nextChapterButton)
        

        #ATTACH BOTTOM NAVIGATION BAR
        #################################################################################################
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #UI TRANSLATE
        #################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manga Centipede Reader"))
        self.backToLibraryButton.setText(_translate("MainWindow", "Back to Library"))
        self.zoomOutButton.setText(_translate("MainWindow", "Zoom Out"))
        self.zoomInButton.setText(_translate("MainWindow", "Zoom In"))
        self.nextChapterButton.setText(_translate("MainWindow", "Next Chapter"))
        self.lastChapterButton.setText(_translate("MainWindow", "Last Chapter"))

    def sorted_nicely(self, l ): 
        """ Sort the given iterable in the way that humans expect.""" 
        convert = lambda text: int(text) if text.isdigit() else text 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)

    def on_timeout(self):
        try:
            file = next(self.files_it)
            pixmap = QtGui.QPixmap(file)
            # pixmap.scaled(100, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            # pixmap
            self.add_pixmap(pixmap.scaledToWidth(400))
            #400 is the smallest size
            #720 is the optimal size
            #1000 is the largest size
            # self.add_pixmap(pixmap)

        except StopIteration:
            self.timer.stop()

    def add_pixmap(self, pixmap):
        if not pixmap.isNull():
            label = QtWidgets.QLabel(pixmap=pixmap)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setStyleSheet("QLabel {background-color: black;}")
            label.setToolTip('Page: ' + str(self.counter) )
            self.counter+=1# add one to counter everytime an image is added
            self.image_viewer_layout.addWidget(label)

    # @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
    #CLASS FUNCTION DECLARATION
    #################################################################################################


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # screen_rect = app.desktop().screenGeometry()
    # width, height = screen_rect.width(), screen_rect.height()

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.setStyleSheet(qdarkstyle.load_stylesheet())
    # MainWindow.setMinimumSize(width/2, height-100)
    sys.exit(app.exec_())
