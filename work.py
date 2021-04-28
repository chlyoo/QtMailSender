from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import pandas as pd
from util import conn

class WorkSpace(QWidget):
	def __init__(self, _parent):
		super(WorkSpace, self).__init__(_parent)     
		self.obj = _parent
		self.df= None
		self.getfile.clicked.connect(self.read_file)
		self.sendmail.clicked.connect(self.process_all)

	def __getattr__(self, attr):
		return getattr(self.obj, attr)

	def show(self):
		self.obj.show()

	def read_file(self):
		file = QFileDialog.getOpenFileName()
		if file[0]!='':
			filename = file[0].split('/')
			if(".xls" in filename):
				self.df = pd.read_excel(file,header=0)
			elif(".csv" in filename):
				self.df = pd.read_csv(file)

	def show_dftable(self):
		pass

	def select_columns(self):
		pass

	def select(self):
		pass

	def process_all(self):
		count = 0
		cnt =0
		for index, row in self.df.iterrows():
			count+=1
			cnt+=1
			who = row['이메일 주소']
			msg = f"간호학과 {row['성명을 쓰시오.']} {row['점수']}/65"
		# send_async_email('peterscience@naver.com','testemail')
			send_async_email(who, msg)
			if count>50:
				count=0
				time.sleep(60)
				print("Wait for 1 minute")
				print(f"sent {cnt}mails")
		pass



	def send_email(who, msg):
		msg = MIMEText(msg)
		msg['Subject'] = MAIL_SUBJECT
		msg['To'] = who
		conn.sendmail(MAIL_SENDER, who, msg.as_string())
		print(f"sent to{who}")

def main():
	import sys
	app = QApplication(sys.argv)
	ui_file = QFile("MainWindow.ui")
	loader = QUiLoader()
	window= loader.load(ui_file)
	workspace = WorkSpace(window)
	ui_file.close()
	workspace.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()