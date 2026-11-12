import re

#Extracting emails
def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

#Extracting urls
def extract_urls(text):
    pattern = r"https?://[^\s]+"
    return re.findall(pattern, text)

def extract_phone_numbers(text):
    pattern = r"\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\(\d{3}\)\s\d{3}-\d{4}"
    return re.findall(pattern, text)

def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

def extract_credit_cards(text):
    pattern = r"\d{4}[ -]\d{4}[ -]\d{4}[ -]\d{4}"
    return re.findall(pattern, text)

def extract_currency(text):
    pattern = r"\$\d{1,3}(?:,\d{3})*\.\d{2}"
    return re.findall(pattern, text)

sample_text = """
Contact us at user@example.com
or support@company.co.uk

Visit:
https://www.company.co.uk

Call us:
123-456-7890
123.456.7890
(123) 456-7890

Trending tags:
#Python
#Regex

Prices:
$19.99
$250.50
$1,250.00
$12,500.03
"""

emails = extract_emails(sample_text)
urls= extract_urls(sample_text)
phones = extract_phone_numbers(sample_text)
hashtags = extract_hashtags(sample_text)
cards = extract_credit_cards(sample_text)
currencies = extract_currency(sample_text)

print("\n=== EMAILS ===")
print(emails)
print("\n=== URLS ===")
print (urls)
print("\n=== PHONE NUMBERS ===")
print(phones)
print("\n=== HASHTAGS ===")
print(hashtags)
print("\n=== CREDIT CARDS ===")
print(cards)
print("\n=== CURRENCY AMOUNTS ===")
print(currencies)