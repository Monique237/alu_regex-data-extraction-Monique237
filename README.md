# Regex Data Extraction

## Project Overview

This Python project uses regular expressions to extract six types of data from blocks of text. It uses Python 3 and the built-in `re` module.

## Supported Formats

| Extractor | Sample matches |
|---|---|
| Email addresses | `user@example.com`, `support@company.co.uk` |
| URLs | `https://www.example.com`, `https://subdomain.example.org/page` |
| Phone numbers | `123-456-7890`, `123.456.7890`, `(123) 456-7890` |
| Hashtags | `#example`, `#ThisIsAHashtag` |
| Credit card numbers | `1234 5678 9012 3456`, `1234-5678-9012-3456` |
| Currency amounts | `$19.99`, `$1,234.56` |

## Project Structure

```text
alu_regex-data-extraction-Monique237/
├── main.py             # Extractor functions and sample demo
├── test_extractors.py  # Tests for all six extractors
├── README.md
└── .gitignore
```

## Run the Demo

If you already have the repository on your computer, open the project folder and run `python main.py`. For a fresh setup, run:

```bash
git clone https://github.com/Monique237/alu_regex-data-extraction-Monique237.git
cd alu_regex-data-extraction-Monique237
python main.py
```

The demo prints six labeled lists of matches from the sample text in `main.py`.

## Run the Tests

From the project folder, run:

```bash
python test_extractors.py
```

The tests compare the returned matches with the expected results. They cover the supported formats and the following edge cases.

| Extractor | Edge case | Expected behavior |
|---|---|---|
| Email addresses | `user@example..com` | Reject consecutive dots in the domain. |
| URLs | `https://example.org/page.` | Remove the sentence-ending period. A separate test checks that a query string is preserved. |
| Phone numbers | `9123-456-78900` | Reject a phone number with extra digits. |
| Hashtags | A standalone `#` | Return no match. |
| Credit card numbers | `1234 5678-9012 3456` | Reject a number with mixed separators. |
| Currency amounts | `$19.999` | Reject an amount with three decimal digits. |

A successful test run ends with `PASS: hashtags`.

## Author

Monique-Esther Saingwea