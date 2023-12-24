import sys
from PyQt6 import QtWidgets, uic
from package.UI.MainWindow import Ui_MainWindow


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
        self.documents.addItem(list_item)
        print(fileName)

    def open(self):
        print("opening")

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
