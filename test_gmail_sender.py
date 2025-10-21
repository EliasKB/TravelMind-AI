from gmail_sender import test_gmail, send_analysis_email

# Verify Gmail connection
test_gmail()

# Send a test email
send_analysis_email("This is only a test email.")