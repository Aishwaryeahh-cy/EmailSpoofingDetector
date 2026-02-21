# Email Spoof Detector - Beginner Friendly Version

# Ask user for sender domain
sender_domain = input("Enter sender domain (example: mail.google.com): ")
sender_domain = sender_domain.strip().lower()

# Ask user for From email
from_email = input("Enter From email (example: user@gmail.com): ")
from_email = from_email.strip().lower()

# Check if email contains @
if "@" in from_email:
    # Get domain after @
    email_domain = from_email.split("@")[1]

    # Compare domains
    if email_domain in sender_domain:
        print("No spoofing detected. Domains match.")
    else:
        print("Possible spoofing detected! Domains do not match.")
else:
    print("Invalid email format.")
