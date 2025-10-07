# email_spoof_simulator.py

from email.message import EmailMessage
import os

def simulate_email_spoof(sender, recipient, subject, body, save_as="spoofed_email.eml"):
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.set_content(body)

    with open(save_as, 'wb') as f:
        f.write(bytes(msg))

    print(f"✅ Spoofed email simulated and saved as '{save_as}'")

if __name__ == "__main__":
    print("📧 Email Spoof Simulation (for educational purpose only)")
    fake_sender = input("Enter fake sender email: ")
    recipient = input("Enter recipient email: ")
    subject = input("Enter subject: ")
    body = input("Enter message body: ")

    simulate_email_spoof(fake_sender, recipient, subject, body)
