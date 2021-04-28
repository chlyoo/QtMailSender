#-*- coding:utf-8 -*-
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from config import * 

def send_score(who, msg):
	msg = MIMEText(msg)
	msg['Subject'] = '글로컬시사영어 중간시험 성적 안내'
	s.sendmail(MAIL_SENDER, who, msg.as_string())
	s.quit()

if __name__ == '__main__':
	df = pd.read_excel("data.xlsx", header=0 )
	s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	# s.login(MAIL_SENDER, MAIL_PASSWORD)
	for index, row in df.iterrows():
		print(row['이메일 주소'], f"간호학과 {row['성명을 쓰시오.']} {row['점수']}/65 ")
		# send_score(row['이메일 주소'], f"간호학과 {row['성명을 쓰시오.']} {row['점수']}/65 ")