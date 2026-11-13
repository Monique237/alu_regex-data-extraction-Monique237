import re

#Extracting emails
def extract_emails(text):
    pattern = (
        r"(?<![a-zA-Z0-9._%+-])"
        r"[a-zA-Z0-9_%+-]+(?:\.[a-zA-Z0-9_%+-]+)*"
        r"@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"
    )
    return re.findall(pattern, text)

#Extracting urls
def extract_urls(text):
    pattern = r"https?://[^\s]+"
    matches = re.findall(pattern, text)
    return [url.rstrip(".,") for url in matches]

#Extracting phone numbers
def extract_phone_numbers(text):
    pattern = r"(?<!\d)(?:\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\(\d{3}\)\s\d{3}-\d{4})(?!\d)"
    return re.findall(pattern, text)

#Extracting hashtags
def extract_hashtags(text):
    pattern = r"#\w+"
    return re.findall(pattern, text)

#Extracting credit cards
def extract_credit_cards(text):
    pattern = r"(?<!\d)\d{4}([ -])\d{4}\1\d{4}\1\d{4}(?!\d)"
    return [match.group(0) for match in re.finditer(pattern, text)]

#Extracting currency amounts
def extract_currency(text):
    pattern = r"\$\d{1,3}(?:,\d{3})*\.\d{2}(?!\d)"
    return re.findall(pattern, text)

if __name__ == "__main__":
    
    sample_text = """
    Contact us at user@example.com
    or support@company.co.uk

    Visit:
    https://www.example.com
    https://subdomain.example.org/page

    Call us:
    123-456-7890
    123.456.7890
    (123) 456-7890

    Hashtags:
    #example
    #ThisIsAHashtag 
    

    Credit card numbers:
    1234 5678 9012 3456
    1234-5678-9012-3456

    Prices:
    $19.99
    $1,234.56
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