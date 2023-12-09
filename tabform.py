# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tabform.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Tab(object):
    def setupUi(self, Tab):
        if not Tab.objectName():
            Tab.setObjectName(u"Tab")
        Tab.resize(812, 612)
        self.verticalLayout_4 = QVBoxLayout(Tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.TextShow = QWebEngineView(Tab)
        self.TextShow.setObjectName(u"TextShow")
        font = QFont()
        font.setPointSize(9)
        self.TextShow.setFont(font)
        self.TextShow.setUrl(QUrl(u"about:blank"))

        self.verticalLayout_3.addWidget(self.TextShow)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MessageType = QComboBox(Tab)
        self.MessageType.setObjectName(u"MessageType")
        self.MessageType.setMaxVisibleItems(3)

        self.verticalLayout.addWidget(self.MessageType)

        self.CheckContent = QPushButton(Tab)
        self.CheckContent.setObjectName(u"CheckContent")

        self.verticalLayout.addWidget(self.CheckContent)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.SendText = QTextEdit(Tab)
        self.SendText.setObjectName(u"SendText")
        font1 = QFont()
        font1.setPointSize(11)
        self.SendText.setFont(font1)
        self.SendText.setFrameShape(QFrame.StyledPanel)
        self.SendText.setFrameShadow(QFrame.Plain)
        self.SendText.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.SendText.setAcceptRichText(False)

        self.horizontalLayout.addWidget(self.SendText)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.SendButton = QPushButton(Tab)
        self.SendButton.setObjectName(u"SendButton")

        self.verticalLayout_2.addWidget(self.SendButton)

        self.WordStatistic = QLabel(Tab)
        self.WordStatistic.setObjectName(u"WordStatistic")
        self.WordStatistic.setFont(font)
        self.WordStatistic.setAlignment(Qt.AlignCenter)
        self.WordStatistic.setWordWrap(False)

        self.verticalLayout_2.addWidget(self.WordStatistic)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 10)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(0, 10)
        self.verticalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(Tab)

        QMetaObject.connectSlotsByName(Tab)
    # setupUi

    def retranslateUi(self, Tab):
        Tab.setWindowTitle(QCoreApplication.translate("Tab", u"Form", None))
        self.CheckContent.setText(QCoreApplication.translate("Tab", u"\u68c0\u67e5\u5bf9\u8bdd\u8bbe\u7f6e", None))
        self.SendText.setHtml(QCoreApplication.translate("Tab", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.SendButton.setText(QCoreApplication.translate("Tab", u"\u53d1\u9001", None))
        self.WordStatistic.setText("")
    # retranslateUi

