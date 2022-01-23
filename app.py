import smtplib
from email.message import EmailMessage
from secrets import password

# Configurar email, senha
EMAIL_ADDRESS = '<seuemail@email.com>'
EMAIL_PASSWORD = password

# Criar um email
message = EmailMessage()
message['Subject'] = 'Teste de Mensagem 2'
message['From'] = '<from@email.com>'
message['To'] = '<to@email.com.br>'
message.set_content('Testando o envio de email com o Python')

#Enviando o email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(message)
