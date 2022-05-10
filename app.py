import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sensivel import senha, endereco

# Configuração
host = 'smtp.gmail.com'
port = 587
user = 'digite aqui seu e-mail'
password = 'digite aqui sua senha'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP(host, port)

# Login com servidor
print('Login...')
server.ehlo()
server.starttls()
server.login(user, password)

# Criando mensagem
message = 'Corpo do e-mail'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['From'] = user
email_msg['To'] = 'Destinatário do e-mail'
email_msg['Subject'] = 'Assunto do e-mail'
print('Adicionando texto...')
email_msg.attach(MIMEText(message, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
print('Mensagem enviada!')
server.quit()