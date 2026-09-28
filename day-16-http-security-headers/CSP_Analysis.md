# HTTP Security Header Analysis

## 1. Introduction

HTTP Security Header Analysis is a security assessment technique used to examine HTTP response headers provided by a web server. Security headers provide instructions to web browsers about how website content should be handled securely.

For this practical task, a Python-based HTTP Security Header Analyzer was used to inspect security-related HTTP response headers in a testing environment. The analyzer checked the presence of the following headers:

* Strict-Transport-Security (HSTS)
* Content-Security-Policy (CSP)
* X-Frame-Options
* X-Content-Type-Options

The purpose was to identify configured and missing security controls and understand the security role of Content Security Policy (CSP).


## 2. Testing Methodology

The Python `requests` library was used to send an HTTP GET request to the target website. After receiving the HTTP response, the script examined the response headers and checked whether the selected security headers were present.

The analysis followed this process:

```text
Target URL
    ↓
HTTP GET Request
    ↓
Server Response
    ↓
Response Headers
    ↓
Security Header Check
    ↓
Configured / Missing
    ↓
Analysis Report
```

The testing was performed for security-learning and internship purposes.


## 3. Executed Script Output Log

The following output was obtained during testing:

```text
[*] Auditing Target Headers: http://daraz.com

[+] CONFIGURED: Strict-Transport-Security
    -> max-age=31536000, max-age=31536000...

[-] VULNERABLE: Missing Security Header
    -> Content-Security-Policy

[+] CONFIGURED: X-Frame-Options
    -> SAMEORIGIN...

[+] CONFIGURED: X-Content-Type-Options
    -> nosniff...
```

### Result Summary

| Security Header           | Result                       | Purpose                                   |
| ------------------------- | ---------------------------- | ----------------------------------------- |
| Strict-Transport-Security | Configured                   | Helps enforce HTTPS connections           |
| Content-Security-Policy   | Missing in observed response | Controls permitted content/script sources |
| X-Frame-Options           | Configured                   | Helps protect against clickjacking        |
| X-Content-Type-Options    | Configured                   | Prevents MIME-type sniffing               |

**Note:** A missing security header does not automatically prove that a website is vulnerable. It indicates that the particular security control was not observed in the tested response.

---

# 4. Analytical Breakdown of Content Security Policy (CSP)

## What is CSP?

Content Security Policy (CSP) is a browser-enforced security mechanism that allows a website to define which sources of content are trusted. It is delivered through the HTTP `Content-Security-Policy` response header.

A simple CSP policy can look like:

```text
Content-Security-Policy: script-src 'self'
```

Here, `script-src` defines the permitted sources for JavaScript, while `'self'` means the browser should allow scripts from the same origin as the website.

---

## How CSP Controls Cross-Site Script Loading

A web application may load JavaScript from different sources. Without an appropriate policy, the browser may have fewer restrictions on where scripts can originate.

For example, consider an unauthorized external script:

```html
<script src="https://attacker.example/evil.js"></script>
```

If the website has the following policy:

```text
script-src 'self'
```

the browser evaluates the script's source against the CSP.

The decision process is:

```text
External Script Request
        ↓
Browser checks CSP
        ↓
Is the script source allowed?
        ↓
   ┌────┴────┐
   YES       NO
    ↓         ↓
  Load      Block
```

Because `attacker.example` is not the same origin as the protected website, the browser can block the script according to the policy.

Therefore, CSP can reduce the ability of unauthorized external JavaScript to execute in the browser.

---

## CSP and XSS Protection

Cross-Site Scripting (XSS) occurs when attacker-controlled content is executed as script in a victim's browser.

CSP provides an additional layer of defense by restricting where executable scripts may come from. This means that even if an application has an injection weakness, a restrictive CSP can reduce the ability of injected or externally hosted scripts to execute.

However, CSP should not be considered a replacement for secure application development. Input validation, output encoding, secure authentication, and other security controls remain important.

---

## Important CSP Directives

Some commonly used CSP directives include:

### `script-src`

Controls permitted JavaScript sources.

```text
script-src 'self'
```

### `default-src`

Provides a default policy for content types that do not have a more specific directive.

```text
default-src 'self'
```

### `style-src`

Controls permitted CSS sources.

### `img-src`

Controls permitted image sources.

### `connect-src`

Controls destinations for connections made by scripts, such as requests made using APIs.

---

# 5. Security Benefits of CSP

CSP can provide several security benefits:

1. **Restricts script sources**
   It can limit JavaScript to trusted origins.

2. **Reduces XSS impact**
   A restrictive policy can prevent some injected or unauthorized scripts from executing.

3. **Controls external resources**
   Websites can define which domains are permitted to provide scripts, images, styles, and other resources.

4. **Provides defense in depth**
   CSP adds another security layer alongside secure coding and input/output controls.

---

# 6. Limitations

CSP is not a complete solution for web application security. Its effectiveness depends on the policy configuration.

An overly permissive policy may provide limited protection. For example, allowing many untrusted script sources can weaken the purpose of CSP.

Therefore, CSP should be implemented together with:

* Input validation
* Output encoding
* Secure session management
* Authentication and authorization controls
* Regular vulnerability testing
* Secure application development practices

---

# 7. Conclusion

HTTP Security Header Analysis helps identify important browser security controls configured by a web server. During this practical assessment, HSTS, X-Frame-Options, and X-Content-Type-Options were observed in the tested response, while Content-Security-Policy was not observed.

CSP is particularly important because it allows a web application to define trusted content and script sources. The browser enforces these restrictions and can block resources that do not comply with the policy. As a result, a properly configured CSP can reduce the impact of certain cross-site scripting and unauthorized script-loading scenarios.

The practical exercise demonstrated how HTTP response headers can be analyzed programmatically and how CSP contributes to defense-in-depth web application security.
