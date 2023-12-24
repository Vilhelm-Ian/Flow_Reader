import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWidgets import QVBoxLayout
from package.UI.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.addDocument.clicked.connect(self.add_document)
        self.documents.itemClicked.connect(self.open)
        self.webView = QWebEngineView()
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)

    def add_document(self):
        fileName = QtWidgets.QFileDialog.getOpenFileName(self, 'Add Document', '', '(*.pdf)')
        list_item = QtWidgets.QListWidgetItem()
        list_item.setText(fileName[0])
        self.documents.addItem(list_item)
        self.webView.setUrl(QUrl("file:///" + "/home/jovan/Documents/books/novels/german/Alexandre_Dumas-Der_Graf_von_Monte_Christo.pdf"))
        self.setCentralWidget(self.webView)
        print(fileName)

    def open(self):
        print("opening")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
