# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reader.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_reader(object):
    def setupUi(self, reader):
        if not reader.objectName():
            reader.setObjectName(u"reader")
        reader.resize(400, 300)
        self.next = QPushButton(reader)
        self.next.setObjectName(u"next")
        self.next.setGeometry(QRect(280, 10, 110, 30))

        self.retranslateUi(reader)

        QMetaObject.connectSlotsByName(reader)
    # setupUi

    def retranslateUi(self, reader):
        reader.setWindowTitle(QCoreApplication.translate("reader", u"Form", None))
        self.next.setText(QCoreApplication.translate("reader", u"next", None))
    # retranslateUi

