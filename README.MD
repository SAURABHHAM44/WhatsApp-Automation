WhatsApp Message Scheduler using Twilio
This Python script allows you to schedule WhatsApp messages using Twilio's WhatsApp API. You can specify the recipient’s name, WhatsApp number, message content, and the exact date & time when the message should be delivered.
🚀 Features
• Send WhatsApp messages via Twilio API
• Schedule messages for a future date and time
• Simple command-line interface for user input
• Environment variable support for security
🛠️ Requirements
• Python 3.7+
• A Twilio account with WhatsApp sandbox enabled
• Installed Python packages: twilio, python-dotenv
📦 Installation

   cd whatsapp-scheduler
1. Install required dependencies:
   pip install twilio python-dotenv
2. Create a .env file in the project directory and add your Twilio credentials:
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
▶️ Usage
Run the script in your terminal:
   python whatsapp_scheduler.py
You will be prompted to enter recipient details, message, and schedule time. The script will wait until the scheduled time and then send the message.
⚠️ Notes
• Make sure you have set up Twilio WhatsApp Sandbox and joined the sandbox using the code provided by Twilio.
• This script runs synchronously (it will pause execution until the scheduled time). For production use, consider using background schedulers like APScheduler or cron jobs.
• Ensure your system is running at the scheduled time, otherwise, the message will not be sent.
📜 Example Run
Enter the recipient's name: John
Enter the recipient's WhatsApp number with country code: xxxxxxxxxxx.
Enter the message you want to send to John: Hello John! This is a scheduled message.
Enter the date to send the message (YYYY-MM-DD).
Enter the time to send the message (HH:MM in 24-hour format).
Message will be sent to John at the input date and time

At the scheduled time, you’ll see:
Message sent successfully! Message SID: SMxxxxxxxxxxxxxxxx
📌 Future Improvements
• Add support for multiple scheduled messages
• Run in background using schedulers (APScheduler / Celery)
• Web or GUI interface for easy scheduling

