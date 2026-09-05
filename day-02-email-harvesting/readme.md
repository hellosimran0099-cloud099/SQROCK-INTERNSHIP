# Day 2 - Email Harvesting

## Objective

The objective of this task was to understand how publicly
available email addresses can be identified from an authorized
webpage using Python.

## Tools Used

- Python 3
- Requests
- Regular Expressions (re)
- VS Code

## Methodology

1. The program accepts an authorized website URL.
2. Python Requests sends an HTTP GET request.
3. The webpage HTML is retrieved using `response.text`.
4. Regular Expression is used to identify email patterns.
5. Duplicate email addresses are removed.
6. The results are displayed and saved in `results.txt`.

## Python Concepts Learned

### Requests

The Requests library is used to send HTTP requests and retrieve
webpage content.

### Regular Expression

The `re` module is used for pattern matching. In this project,
it is used to identify strings that follow an email-address pattern.

### File Handling

Python's `open()` function is used to save the results into
`results.txt`.

## Security Risk

Publicly exposed email addresses can provide useful information
during reconnaissance and may increase exposure to phishing,
spam, and social-engineering attempts.

## Mitigation

Organizations should avoid unnecessary exposure of employee
contact information and should provide security-awareness training.

## Ethical Consideration

Email harvesting should only be performed on systems and websites
where testing or collection is authorized.

## Conclusion

This exercise demonstrated a basic OSINT/reconnaissance technique
and showed how Python can automate the identification of
publicly exposed email addresses.
