import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
class MyApp(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()
	def initUI(self):
		btn1 = QPushButton('&Button1', self)
		btn1.setCheckable(True)
		btn1.toggle()


		btn2 = QPushButton(self)
		btn2.setText('Button&2')


		btn3 = QPushButton('Button3', self)
		btn3.setEnabled(False)

		msg = ""
		btn4 = QPushButton('버튼4',self)
		if btn4.isChecked():
			btn4.setText('on')

		vbox = QVBoxLayout()
		vbox.addWidget(btn1)
		vbox.addWidget(btn2)
		vbox.addWidget(btn3)
		vbox.addWidget(btn4)

		self.setLayout(vbox)
		self.setWindowTitle('QPushButton')
		self.setGeometry(300, 300, 300, 200)
		self.show()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyApp()
	sys.exit(app.exec_())
