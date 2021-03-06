#-*- coding:utf-8 -*-
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from config import * 

def send_email(who, msg):
	msg = MIMEText(msg)
	msg['Subject'] = MAIL_SUBJECT
	msg['To'] = who
	s.sendmail(MAIL_SENDER, who, msg.as_string())
	print(f"sent to{who}")

if __name__ == '__main__':
	df = pd.read_excel("data.xlsx", header=0 )
	s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	s.login(MAIL_SENDER, MAIL_PASSWORD)
	count = 0
	cnt = 0
	for index, row in df.iterrows():
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
		# thr = Thread(target=send_async_email, args=[who,msg])
		# thr.start()
	input("종료하려면 아무키나 누르세요")
	s.quit()