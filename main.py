from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',
            to=f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID: {message.sid}')
    except Exception as e:
        print('An error occurred while sending the message.')

name = input("Enter the recipient's name: ")
recipient_number = input("Enter the recipient's WhatsApp number with country code: ")
message_body = input(f'Enter the message you want to send to {name}: ')

date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24-hour format): ')
scheduled_datetime = datetime.strptime(f'{date_str} {time_str}', '%Y-%m-%d %H:%M')
current_datetime = datetime.now()

time_difference = scheduled_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in past enter the future date and time: ')
else:
    print(f'Message will be sent to {name} at {scheduled_datetime}.')
    time.sleep(delay_seconds)
    send_whatsapp_message(recipient_number, message_body)
