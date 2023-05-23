import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email Configuration
smtpServer = 'your_smtp_server'  # Replace with your SMTP server
smtpPort = 587
smtpUsername = 'your_username'  # Replace with your SMTP username
smtpPassword = 'your_password'  # Replace with your SMTP password

# Phishing Email Template
senderName = 'Your Company'
emailSubject = 'Important Notification'
emailContent = '''
Dear User,

This is an important notification. Please click on the following link to verify your account:

{{LINK}}

Thank you,
{{SENDER_NAME}}
'''

# User Database (Example)
users = [
    {'email': 'user1@example.com', 'name': 'User One'},
    {'email': 'user2@example.com', 'name': 'User Two'},
    {'email': 'user3@example.com', 'name': 'User Three'}
]

def sendPhishingEmail(userEmail, userName, phishingLink):
    senderEmail = smtpUsername
    message = MIMEMultipart()
    message['From'] = f'{senderName} <{senderEmail}>'
    message['To'] = userEmail
    message['Subject'] = emailSubject.replace('{{SENDER_NAME}}', senderName)

    emailContent = emailContent.replace('{{LINK}}', phishingLink)
    emailContent = emailContent.replace('{{SENDER_NAME}}', senderName)
    emailContent = emailContent.replace('{{USER_NAME}}', userName)

    message.attach(MIMEText(emailContent, 'plain'))

    try:
        server = smtplib.SMTP(smtpServer, smtpPort)
        server.starttls()
        server.login(smtpUsername, smtpPassword)
        server.sendmail(senderEmail, userEmail, message.as_string())
        server.quit()
        print(f"Phishing email sent successfully to {userEmail}")
    except Exception as e:
        print(f"Error sending email to {userEmail}: {str(e)}")

# Simulate Phishing Campaign
def simulatePhishingCampaign():
    for user in users:
        phishingLink = 'http://www.example.com/verify'  # Replace with your phishing link
        sendPhishingEmail(user['email'], user['name'], phishingLink)

        # Track email sent and user response
        # Update your reporting database accordingly

# Run the Phishing Simulation
simulatePhishingCampaign()