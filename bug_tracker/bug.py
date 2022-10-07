import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox, QAction
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):
	
	def __init__(self):
		super(App,self).__init__()
		self.setWindowIcon(QIcon('favicon.png'))
		self.title ='Bug Tracker'
		self.left = 10
		self.top = 10
		self.width = 640
		self.height = 480
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)		
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('File')
		editMenu = mainMenu.addMenu('Edit')
		searchMenu = mainMenu.addMenu('Search')
		helpMenu = mainMenu.addMenu('Help') 

		openFile = QAction(QIcon('File'),'Load',self)
		openFile.setShortcut('Ctrl+N')
		openFile.setStatusTip('Load a Project')
		openFile.triggered.connect(self.clo)
		fileMenu.addAction(openFile)

		exitButton = QAction(QIcon('Critical'),'Exit',self)
		exitButton.setShortcut('Ctrl+Q')
		exitButton.setStatusTip('Exit Application')
		exitButton.triggered.connect(self.close)
		fileMenu.addAction(exitButton)


		add = QPushButton('Add Entry',self)
		add.setToolTip('For adding any new bugs')
		
		dele = QPushButton('Delete Entry',self)
		dele.setToolTip('For deleting any bugs')
		
		edit = QPushButton('Edit Entry',self)
		edit.setToolTip('To edit any entrys')
		
		add.move(340,20)
		dele.move(440,20)
		edit.move(540,20)

		add.clicked.connect(self.add)
		dele.clicked.connect(self.dele)
		edit.clicked.connect(self.edit)

		self.show() 

	def con(self):
		self.statusBar().showMessage('in Progress')
		dialog = Message()

	def clo(self):
		print('Hello')

	def add(self):
		print('Yeah')

	def dele(self):
		print('Delete')

	def edit(self):
		print('Edit')

class Message(QMessageBox):
	def __init__(self):
		super().__init__()
		self.title = "Error"
		self.left = 220
		self.top = 200
		self.width = 400
		self.height = 250
		self.Critical
		self.initUI()

	def initUI(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.left,self.top,self.width,self.height)
		QMessageBox.setIcon(self,QMessageBox.Critical)
		buttonReply = self.question(self, 'Confirmation', 'are you sure you want to do that', self.Yes | self.No, self.No)
		if buttonReply == self.Yes:
			print("Yeah")
		else:
			print("Nah")
		self.show()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	sys.exit(app.exec_())
	#dialog.exec_()



