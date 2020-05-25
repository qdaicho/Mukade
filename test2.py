import os, re
import pprint
from PyQt5 import QtCore, QtGui, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def sorted_nicely(self, l ): 
        """ Sort the given iterable in the way that humans expect.""" 
        convert = lambda text: int(text) if text.isdigit() else text 
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
        return sorted(l, key = alphanum_key)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        url = "/home/emsee/Documents/Manga/Terror Man/chapter_1"

        self.scrollArea = QtWidgets.QScrollArea(widgetResizable=True)
        self.setCentralWidget(self.scrollArea)
        content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(content_widget)
        self._lay = QtWidgets.QVBoxLayout(content_widget)

        # gets all the images from given url
        image_list = self.sorted_nicely([os.path.join(url, file) for file in os.listdir(url)])
        self.files_it = iter(image_list)
        
        pprint.pprint(image_list)

        self.counter = 0 # This counts the pages as window gets populated w/ images
        self._timer = QtCore.QTimer(self, interval=1)
        self._timer.timeout.connect(self.on_timeout)
        self._timer.start()
        # self._lay.addLayout()

        self.setWindowTitle("Manga Centipede Reader")
        self.resize(800, 600)

    def on_timeout(self):
        try:
            file = next(self.files_it)
            pixmap = QtGui.QPixmap(file)
            pixmap.scaled(100, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
            self.add_pixmap(pixmap)

        except StopIteration:
            self._timer.stop()

    def add_pixmap(self, pixmap):
        if not pixmap.isNull():
            label = QtWidgets.QLabel(pixmap=pixmap)
            label.setAlignment(QtCore.Qt.AlignCenter)
            label.setStyleSheet("QLabel {background-color: black;}")
            label.setToolTip('Page Number: ' + str(self.counter) )
            self.counter+=1# add one to counter everytime an image is added
            self._lay.addWidget(label)



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.setStyleSheet("background-color: black;color:white;padding:2px;")

    w.showMaximized()
    sys.exit(app.exec_())