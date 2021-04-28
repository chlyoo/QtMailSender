import sys
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import *

from login import LoginDialog
def main():
	QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
	app = QApplication(sys.argv)
	ui_file = QFile("Login.ui")
	loader = QUiLoader()
	window = loader.load(ui_file)
	ui_file.close()
	MailAPP = LoginDialog(window)
	sys.exit(app.exec_())

if __name__ == "__main__":
	main()