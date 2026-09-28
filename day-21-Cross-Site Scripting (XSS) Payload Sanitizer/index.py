import html
import re
def sanitize_user_input(raw_payload):
    # Perform strict encoding step followed by active pattern strip-down
    encoded_string = html.escape(raw_payload)
    stripped_output = re.sub(r"(?i)script|onerror|onload", "[PROHIBITED_TOKEN]", 
encoded_string)
    return stripped_output
malicious_input = "<script>alert('XSS')</script>"
sanitized = sanitize_user_input(malicious_input)
print(f"Raw Input: {malicious_input}\nNeutralized Result: {sanitized}")
