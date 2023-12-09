# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SP_Window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(800, 52)
        Form.setMinimumSize(QSize(800, 52))
        Form.setMaximumSize(QSize(800, 52))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.QuestionEdit = QLineEdit(Form)
        self.QuestionEdit.setObjectName(u"QuestionEdit")
        font = QFont()
        font.setPointSize(11)
        self.QuestionEdit.setFont(font)

        self.horizontalLayout.addWidget(self.QuestionEdit)

        self.SendButton = QPushButton(Form)
        self.SendButton.setObjectName(u"SendButton")

        self.horizontalLayout.addWidget(self.SendButton)

        self.ClearButton = QPushButton(Form)
        self.ClearButton.setObjectName(u"ClearButton")

        self.horizontalLayout.addWidget(self.ClearButton)

        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.AnswerShow = QWebEngineView(Form)
        self.AnswerShow.setObjectName(u"AnswerShow")
        self.AnswerShow.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.AnswerShow)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 50)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"GPT for Windows 3.3", None))
        self.SendButton.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.ClearButton.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
    # retranslateUi

