# Email Spoof Detector
sender_domain = input("Enter sender domain (example: mail.google.com): ").strip().lower()
from_email = input("Enter From email (example: user@gmail.com): ").strip().lower()

if "@" in from_email:
    email_domain = from_email.split("@")[1]

    if email_domain in sender_domain:
        print("✅ No spoofing detected. Domains match.")
    else:
        print("⚠️ Possible spoofing detected! Domains do not match.")
else:
    print("Invalid email format.")
