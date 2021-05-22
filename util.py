import smtplib
try:
    conn = smtplib.SMTP_SSL('smtp.gmail.com', 465)
except:
    conn = None