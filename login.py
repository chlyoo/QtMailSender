import sys
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtGui import *
# Create a Qt application
from work import WorkSpace
from util import conn

class LoginDialog(QWidget):
	def __init__(self, _parent=None):
		super(LoginDialog,self).__init__(_parent)     
		self.obj = _parent
		self.initUI()
		self.show()
		self.accept_btn.clicked.connect(self.loginSMTP)
		self.reject_btn.clicked.connect(self.reject)
		self.workspace = WorkSpace
		pass

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

	def show(self):
		self.obj.show()

	def initUI(self):
		self.setWindowTitle("로그인")
		self.show()

	def loginSMTP(self):
		print("accept")
		id = self.id.text()
		pw = self.password.text()
		print(id, pw, end="\n\n\n\n\n")
		# print(type(id))
		try:
			conn.login(id, pw)
		except smtplib.SMTPAuthenticationError:
			message = QMessageBox()
			message.setModal(True)
			message.setText("로그인 정보가 잘못되었습니다. 앱 비밀번호를 입력하셔야 합니다.")
			message.show()
			self.password.setText("")
		except TypeError:
			message = QMessageBox()
			message.setModal(True)
			message.setText("아이디 비밀번호를 제대로 입력하세요")
			message.show() 
		self.open_workspace()

	def eventSET(self):
		self.buttonBox.clicked.connect(self.loginSMTP)

	def open_workspace(self):
		ui_file = QFile("MainWindow.ui")
		loader = QUiLoader()
		window= loader.load(ui_file)
		self.workspace = WorkSpace(window)
		ui_file.close()
		self.workspace.show()
		self.accept()
 
# QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
# app = QApplication(sys.argv)
# ui_file = QFile("login.ui")
# loader = QUiLoader()
# window = loader.load(ui_file)
# ui_file.close()
# window.show()
# # Enter Qt application main loop
# sys.exit(app.exec_())