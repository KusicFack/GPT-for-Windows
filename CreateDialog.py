# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateDialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CreateDialog(object):
    def setupUi(self, CreateDialog):
        if not CreateDialog.objectName():
            CreateDialog.setObjectName(u"CreateDialog")
        CreateDialog.setWindowModality(Qt.ApplicationModal)
        CreateDialog.resize(300, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateDialog.sizePolicy().hasHeightForWidth())
        CreateDialog.setSizePolicy(sizePolicy)
        CreateDialog.setMinimumSize(QSize(300, 160))
        CreateDialog.setMaximumSize(QSize(300, 160))
        CreateDialog.setAutoFillBackground(False)
        self.verticalLayout = QVBoxLayout(CreateDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CreateDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(False)

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(CreateDialog)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout.addWidget(self.comboBox)

        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ContinueSwitch = QCheckBox(CreateDialog)
        self.ContinueSwitch.setObjectName(u"ContinueSwitch")
        self.ContinueSwitch.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_2.addWidget(self.ContinueSwitch)

        self.HelpButton = QPushButton(CreateDialog)
        self.HelpButton.setObjectName(u"HelpButton")

        self.horizontalLayout_2.addWidget(self.HelpButton)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.buttonBox = QDialogButtonBox(CreateDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.horizontalLayout_3.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(CreateDialog)
        self.buttonBox.accepted.connect(CreateDialog.accept)
        self.buttonBox.rejected.connect(CreateDialog.reject)

        QMetaObject.connectSlotsByName(CreateDialog)
    # setupUi

    def retranslateUi(self, CreateDialog):
        CreateDialog.setWindowTitle(QCoreApplication.translate("CreateDialog", u"\u65b0\u5efa\u5bf9\u8bdd", None))
        self.label.setText(QCoreApplication.translate("CreateDialog", u"\u8bf7\u9009\u62e9OpenAI\u6a21\u578b\uff1a", None))
        self.ContinueSwitch.setText(QCoreApplication.translate("CreateDialog", u"\u542f\u7528\u8fde\u7eed\u5bf9\u8bdd", None))
        self.HelpButton.setText(QCoreApplication.translate("CreateDialog", u"\u5e2e\u52a9", None))
    # retranslateUi

