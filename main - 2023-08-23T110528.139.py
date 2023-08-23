import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace these with your actual API endpoint and email settings
API_URL = "https://api.example.com/tasks"
EMAIL_HOST = "smtp.example.com"
EMAIL_PORT = 587
EMAIL_USERNAME = "your_email@example.com"
EMAIL_PASSWORD = "your_email_password"

def fetch_tasks():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        return []

def send_email(subject, message, to_email):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_USERNAME
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, to_email, msg.as_string())
        server.quit()
        print("Email sent successfully to", to_email)
    except Exception as e:
        print("Error sending email:", e)

def main():
    tasks = fetch_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        recipient_email = task['email']
        task_summary = "\n".join(task['tasks'])
        subject = "Your Daily Task Summary"
        message = f"Hello,\n\nHere are your tasks for today:\n\n{task_summary}\n\nBest regards,\nYour Remote Work Assistant"
        
        send_email(subject, message, recipient_email)

if __name__ == "__main__":
    main()
