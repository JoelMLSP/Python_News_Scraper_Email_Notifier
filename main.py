import os
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from dotenv import load_dotenv

load_dotenv()

now = datetime.datetime.now()

content = ''

#extracting news stories
def extract_news(url):
    print("Extracting news stories...")
    cnt = ''
    cnt += ('<b> Top Stories:</b>\n' + '<br>' + '-'*50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('span',attrs={'class':'titleline'})):
        cnt += ((str(i+1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        print (tag.prettify)

    return (cnt)


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content += ('<br><br>End of Message')


#send email
print('Composing email')
server = smtplib.SMTP('smtp.gmail.com')
port = 587
FROM = os.environ['FROM_EMAIL']
TO = os.environ['TO_EMAIL']
PWD = os.environ['APP_SPECIFIC_PASSWORD']

msg = MIMEMultipart()

msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
print ('Initiating server...')
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(FROM, PWD)
server.sendmail(FROM, TO, msg.as_string())
print ('Email sent...')
server.quit()
