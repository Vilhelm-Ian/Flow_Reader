from package.UI.Reader import Ui_reader
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QMargins, QPoint
from PySide6.QtPdfWidgets import QPdfView
from PySide6.QtGui import QMouseEvent
from PySide6 import QtPdf



class ReaderWidget(QWidget, Ui_reader):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.document = QtPdf.QPdfDocument(self)
        self.viewer = QPdfView(self)
        self.viewer.setDocument(self.document)
        self.viewer.resize(300,300)
        self.document.load("/home/jovan/Documents/books/Mastering-Your-Adult-ADHD.pdf")
        self.next.clicked.connect(self.next_page)
        self.viewer.mousePressEvent = self.handle_mouse_press

    def next_page(self):
        nav = self.viewer.pageNavigator()
        nav.jump(nav.currentPage() + 1, QPoint(), nav.currentZoom())
        print("clicked")

    def handle_mouse_press(self, event):
        self.start_pos = event.pos()
        print(self.start_pos)



