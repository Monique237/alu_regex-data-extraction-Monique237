from main import extract_currency

assert extract_currency("Price: $1,234.56.") == ["$1,234.56"], (
    "Should extract a valid price followed by a period"
)
print("PASS: valid currency")

assert extract_currency("Wrong price: $19.999") == [], (
    "Should reject a price with three decimal digits"
)
print("PASS: malformed currency")

from main import extract_phone_numbers

assert extract_phone_numbers(
    "Call 123-456-7890, 123.456.7890, or (123) 456-7890."
) == ["123-456-7890", "123.456.7890", "(123) 456-7890"]

assert extract_phone_numbers("Invalid number: 9123-456-78900") == [], (
    "Should reject a phone number with extra digits"
)

print("PASS: phone numbers")

from main import extract_emails

assert extract_emails("Contact support@company.co.uk.") == [
    "support@company.co.uk"
]

assert extract_emails("Invalid email: user@example..com") == [], (
    "Should reject consecutive dots in the email domain"
)
assert extract_emails("Invalid email: user..name@example.com") == [], (
    "Should reject consecutive dots before @"
)

print("PASS: emails")

from main import extract_urls

assert extract_urls("Visit https://example.org/page?topic=regex") == [
    "https://example.org/page?topic=regex"
], "Should keep the query string"

assert extract_urls("Visit https://example.org/page.") == [
    "https://example.org/page"
], "Should exclude the sentence-ending period"

print("PASS: URLs")

from main import extract_credit_cards

assert extract_credit_cards(
    "Examples: 1234 5678 9012 3456 and 1234-5678-9012-3456"
) == ["1234 5678 9012 3456", "1234-5678-9012-3456"]

assert extract_credit_cards("Mixed separators: 1234 5678-9012 3456") == [], (
    "Should reject a card number that mixes spaces and hyphens"
)

print("PASS: credit cards")

from main import extract_hashtags

assert extract_hashtags("Tags: #example #ThisIsAHashtag") == [
    "#example",
    "#ThisIsAHashtag",
]

assert extract_hashtags("A standalone # is punctuation.") == [], (
    "Should ignore a hash with no tag text"
)

print("PASS: hashtags")