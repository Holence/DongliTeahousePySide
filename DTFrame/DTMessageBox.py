from __future__ import annotations
from DTPySide import *

# MessageBox Module
from DTPySide.DTFrame.Ui_DTMessageBox import Ui_DTMessageBox
from DTPySide.DTFrame.DTDialog import DTDialog

class MessageModule(Ui_DTMessageBox,QWidget):
	def __init__(self,parent):
		super().__init__(parent)
		self.setupUi(self)

class DTMessageBox(DTDialog):
	def __init__(self,parent,title,text,icon=None):
		super().__init__(parent,title)
		self.module=MessageModule(self)
		self.setCentralWidget(self.module)
		
		self.module.label_text.setText(text)
		self.setButtonBox(QDialogButtonBox.Ok)
		self.setDefaultButton(QDialogButtonBox.Ok)

		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.module.label_icon.setPixmap(icon_pic)
		else:
			self.module.label_icon.setVisible(False)
			self.module.horizontalLayout.setContentsMargins(45,10,0,5)

		self.adjustSize()
		self.exec_()

class DTConfirmBox(DTDialog):
	def __init__(self,parent,title,text,icon=None):
		super().__init__(parent, title)
		self.module=MessageModule(self)
		self.setCentralWidget(self.module)
		
		self.module.label_text.setText(text)

		if icon!=None:
			icon_pic=icon.pixmap(QSize(64,64))
			self.module.label_icon.setPixmap(icon_pic)
		else:
			self.module.label_icon.setVisible(False)
			self.module.horizontalLayout.setContentsMargins(45,10,0,5)

		self.adjustSize()