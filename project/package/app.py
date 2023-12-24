import sys
from PySide6 import QtWidgets

from package.UI.MainWindow import Ui_MainWindow
from package.reader import ReaderWidget


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addDocument.clicked.connect(self.add_document)
        self.documents.itemClicked.connect(self.open)


    def add_document(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Add Document', '', '(*.pdf)')
        list_item = QtWidgets.QListWidgetItem()
        list_item.setText(fileName[0])
        self.sub_window = ReaderWidget()
        self.sub_window.show()
        # self.documents.addItem(list_item)
        # self.document.load("/home/jovan/Documents/books/novels/german/Alexandre_Dumas-Der_Graf_von_Monte_Christo.pdf")
        # QtPdf.QPdfDocument.load(QUrl("file:///" + "/home/jovan/Documents/books/novels/german/Alexandre_Dumas-Der_Graf_von_Monte_Christo.pdf"))
        # self.webView.setUrl(QUrl("file:///" + "/home/jovan/Documents/books/novels/german/Alexandre_Dumas-Der_Graf_von_Monte_Christo.pdf"))
        # self.setCentralWidget(self.webView)
        print(fileName)

    def open(self):
        print("opening")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
