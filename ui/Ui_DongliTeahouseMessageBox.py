# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_DongliTeahouseMessageBox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from DongliTeahousePySideWheel.DongliTeahouseTemplate import DongliTeahouseTitleBarCut

import DongliTeahousePySideWheel.DongliTeahouse_rc

class Ui_DongliTeahouseMessageBox(object):
    def setupUi(self, DongliTeahouseMessageBox):
        if not DongliTeahouseMessageBox.objectName():
            DongliTeahouseMessageBox.setObjectName(u"DongliTeahouseMessageBox")
        DongliTeahouseMessageBox.resize(558, 357)
        self.verticalLayout = QVBoxLayout(DongliTeahouseMessageBox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.TitleBar = DongliTeahouseTitleBarCut(DongliTeahouseMessageBox)
        self.TitleBar.setObjectName(u"TitleBar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleBar.sizePolicy().hasHeightForWidth())
        self.TitleBar.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.TitleBar)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(50, 20, 32, 30)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_icon = QLabel(DongliTeahouseMessageBox)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy1)
        self.label_icon.setMaximumSize(QSize(64, 64))
        self.label_icon.setPixmap(QPixmap(u":/icon/holoico_trans.ico"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_icon)

        self.verticalSpacer = QSpacerItem(0, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.label_message = QLabel(DongliTeahouseMessageBox)
        self.label_message.setObjectName(u"label_message")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy2)
        self.label_message.setMinimumSize(QSize(400, 0))
        self.label_message.setTextFormat(Qt.AutoText)
        self.label_message.setScaledContents(False)
        self.label_message.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_message.setWordWrap(True)
        self.label_message.setMargin(0)
        self.label_message.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.horizontalLayout.addWidget(self.label_message)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 32, 25)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(DongliTeahouseMessageBox)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy1.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy1)
        self.buttonBox.setLayoutDirection(Qt.RightToLeft)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(DongliTeahouseMessageBox)
        self.buttonBox.accepted.connect(DongliTeahouseMessageBox.accept)
        self.buttonBox.rejected.connect(DongliTeahouseMessageBox.reject)

        QMetaObject.connectSlotsByName(DongliTeahouseMessageBox)
    # setupUi

    def retranslateUi(self, DongliTeahouseMessageBox):
        DongliTeahouseMessageBox.setWindowTitle(QCoreApplication.translate("DongliTeahouseMessageBox", u"DongliTeahouseDialog", None))
        self.label_icon.setText("")
        self.label_message.setText("")
    # retranslateUi

