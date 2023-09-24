# SUSpray.py
Scripts to automate pentesting processes
Certainly, here's a description for the Python password spray script:

---

**Title: Password Spray Script in Python**

**Description:**

The "Password Spray Script in Python" is a simple yet powerful tool designed for security professionals, ethical hackers, and system administrators to test the strength of user passwords on a system. Unlike traditional brute force attacks that attempt to guess a single user's password, this script takes a more stealthy approach, attempting a single password across multiple user accounts, hence the term "password spray."

**Key Features:**

1. **Customizable Password:** The script allows users to specify a single password as an argument when running the script. This password will be tested against multiple user accounts.

2. **User Account Enumeration:** It reads the system's `/etc/passwd` file to identify valid user accounts. Only users with shells ending in "sh" are considered, as these are typically interactive login accounts.

3. **Multi-User Testing:** The script iterates through the list of identified user accounts and attempts to log in using the provided password. If successful, it reports the user account that was able to log in.

4. **Informative Output:** The script provides clear and informative output, indicating whether each login attempt succeeded or failed. It prints messages like "Username 'username' was able to login" or "Username 'username' failed" for each user account.

**Usage:**

The script is run from the command line with the desired password as an argument. For example:

```bash
python3 passspray.py <password>
```

**Note:** Ensure that you have proper authorization and consent before using this script, as unauthorized penetration testing or hacking attempts are illegal and unethical. Use it only in authorized testing environments for security assessment purposes.

**Disclaimer:** This script is intended for educational and security assessment purposes only. It should only be used with proper authorization and in compliance with applicable laws and regulations. Unauthorized or malicious use is strictly prohibited.

---

