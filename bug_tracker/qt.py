import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QAction, QLineEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):
	
	def __init__(self):
		super().__init__()
		self.title = 'PyQt'
		self.left = 10
		self.top = 10
		self.width = 220
		self.height = 120
		self.initUI()
	
	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left, self.top, self.width, self.height)

		#Textbox
		self.textbox = QLineEdit(self)
		self.textbox.move(20,20)
		self.textbox.resize(180, 80)

		#Button
		self.button = QPushButton('Show Text', self)
		self.button.move(20,80)

		self.button.clicked.connect(self.on_click)
		self.show()

	def on_click(self):
		textboxValue = self.textbox.text()
		QMessageBox.question(self, 'Message', 'You entered: ' + textboxValue , QMessageBox.Ok , QMessageBox.Ok)
		self.textbox.setText("")

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Window()
	sys.exit(app.exec_())