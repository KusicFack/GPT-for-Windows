# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GPT.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        icon = QIcon()
        icon.addFile(u":/icos/GPT_ICO.ico", QSize(), QIcon.Selected, QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.actionlongin = QAction(MainWindow)
        self.actionlongin.setObjectName(u"actionlongin")
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionexport = QAction(MainWindow)
        self.actionexport.setObjectName(u"actionexport")
        self.actionshift = QAction(MainWindow)
        self.actionshift.setObjectName(u"actionshift")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Statelabel = QLabel(self.centralwidget)
        self.Statelabel.setObjectName(u"Statelabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Statelabel.sizePolicy().hasHeightForWidth())
        self.Statelabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(16)
        self.Statelabel.setFont(font)
        self.Statelabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.Statelabel)

        self.NewChat = QPushButton(self.centralwidget)
        self.NewChat.setObjectName(u"NewChat")

        self.horizontalLayout.addWidget(self.NewChat)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.ChatTabs = QTabWidget(self.centralwidget)
        self.ChatTabs.setObjectName(u"ChatTabs")
        self.ChatTabs.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ChatTabs.sizePolicy().hasHeightForWidth())
        self.ChatTabs.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.ChatTabs.setFont(font1)
        self.ChatTabs.setTabsClosable(True)

        self.verticalLayout.addWidget(self.ChatTabs)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 15)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.actionlongin)
        self.menu.addSeparator()
        self.menu.addAction(self.actionshift)
        self.menu.addSeparator()
        self.menu.addAction(self.actionabout)
        self.menu_2.addAction(self.actionDelete)
        self.menu_2.addAction(self.actionexport)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GPT for Windows 3.3", None))
        self.actionlongin.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actionlongin.setToolTip(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u5f53\u524d\u5bf9\u8bdd", None))
#if QT_CONFIG(tooltip)
        self.actionDelete.setToolTip(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e\u5f53\u524d\u5bf9\u8bdd", None))
#endif // QT_CONFIG(tooltip)
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.actionabout.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        self.actionexport.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5f53\u524d\u5bf9\u8bdd", None))
#if QT_CONFIG(tooltip)
        self.actionexport.setToolTip(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u5f53\u524d\u5bf9\u8bdd", None))
#endif // QT_CONFIG(tooltip)
        self.actionshift.setText(QCoreApplication.translate("MainWindow", u"\u60ac\u6d6e\u6a21\u5f0f", None))
#if QT_CONFIG(tooltip)
        self.actionshift.setToolTip(QCoreApplication.translate("MainWindow", u"\u5207\u6362\u4e3a\u60ac\u6d6e\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.Statelabel.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u72b6\u6001\uff1a\u672a\u8fde\u63a5\u81f3OpenAI", None))
        self.NewChat.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u5bf9\u8bdd", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5bf9\u8bdd", None))
    # retranslateUi

