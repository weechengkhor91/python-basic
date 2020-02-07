import smtplib
#import email
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
#import csv
import csv

#Variable
#print(dir(email))
smtp_server = 'smtp.gmail.com'
from_addr= input('请输入登录邮箱：')
password = input('请输入邮箱授权码：')
#to_addr = input('请输入收件邮箱：')
to_addrs = []




#write - sender name and email
data = [['content001','weechengkhor911002@gmail.com'],['content002','chengkhor911002@gmail.com']]

    # while True:
    #     ask = input('Please insert exact email')
    #     to_addrs.append(ask)
    #     quit = input('Continue add email address, Exit insert q')
    #     if quit == 'q':
    #         break
# print(to_addrs)
with open('sender.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)

#read -recipient data
with open('sender1.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        to_addrs = row[1]
        text = ''' 
            gambateh...you can do it!!!
        '''
        msg = MIMEText(text, 'plain', 'utf-8')
        msg['From'] = Header('吴枫')
        msg['To'] = Header(','.join(to_addrs))
        msg['Subject'] = Header('Python Testing')
        


#Method
server = smtplib.SMTP_SSL(smtp_server)
#server.connect(host,port)
server.connect(smtp_server,465)
#server.login(username, password)
server.login(from_addr, password)

try:
    server.sendmail(from_addr, to_addrs, msg.as_string())
    print('success')
except:
    print('failed try again')
server.quit()



