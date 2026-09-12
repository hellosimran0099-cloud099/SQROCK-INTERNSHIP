
# ============================================================
# Day 7 - Password Attacks & Credential Stuffing
# Defensive Implementation: Flask Rate Limiter
# ============================================================

from flask import Flask, request

app = Flask(__name__)

# ------------------------------------------------------------
# Demo account
# ------------------------------------------------------------
USERNAME = "admin"
PASSWORD = "admin123"

# Maximum number of failed login attempts allowed
MAX_ATTEMPTS = 5

# Store failed login attempts
failed_attempts = 0


# ------------------------------------------------------------
# Home Page
# ------------------------------------------------------------
@app.route("/")
def home():
    return """
    <h1>Day 7 Password Security Lab</h1>
    <p>Flask Rate Limiting Demo</p>
    <a href="/login">Go to Login Page</a>
    """


# ------------------------------------------------------------
# Login Page
# ------------------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    global failed_attempts

    # --------------------------------------------------------
    # Check whether the account has already reached the limit
    # --------------------------------------------------------
    if failed_attempts >= MAX_ATTEMPTS:
        return """
        <h2>🚫 ACCOUNT LOCKED</h2>
        <p>Too many failed login attempts.</p>
        <p>Rate limit has been triggered.</p>
        """

    # --------------------------------------------------------
    # Process login form
    # --------------------------------------------------------
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # ----------------------------------------------------
        # Check username and password
        # ----------------------------------------------------
        if username == USERNAME and password == PASSWORD:

            # Reset failed attempts after successful login
            failed_attempts = 0

            return """
            <h2>✅ Login Successful!</h2>
            <p>Welcome to the Day 7 local security lab.</p>
            """

        # ----------------------------------------------------
        # Wrong username/password
        # Increase failed attempt counter
        # ----------------------------------------------------
        failed_attempts += 1

        print("Failed login attempts:", failed_attempts)

        # ----------------------------------------------------
        # Trigger rate limit after 5 failed attempts
        # ----------------------------------------------------
        if failed_attempts >= MAX_ATTEMPTS:
            return """
            <h2>🚫 RATE LIMIT TRIGGERED</h2>
            <p>Too many failed login attempts.</p>
            <p>Account has been temporarily locked.</p>
            """

        # ----------------------------------------------------
        # Show remaining attempts
        # ----------------------------------------------------
        remaining = MAX_ATTEMPTS - failed_attempts

        return f"""
        <h2>❌ Invalid Username or Password</h2>
        <p>Failed Attempts: {failed_attempts}</p>
        <p>Remaining Attempts: {remaining}</p>
        """

    # --------------------------------------------------------
    # Display login form
    # --------------------------------------------------------
    return """
    <h2>Day 7 Login Lab</h2>

    <form method="POST">

        <label>Username:</label><br>
        <input type="text" name="username" required>

        <br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required>

        <br><br>

        <button type="submit">Login</button>

    </form>

    <hr>

    <p><b>Lab Account:</b></p>
    <p>Username: admin</p>
    <p>Password: admin123</p>
    """


# ------------------------------------------------------------
# Start Flask Server
# ------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)

