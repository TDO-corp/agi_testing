import re
import getpass
import math
import os
import sys
from datetime import datetime
import random
import warnings

def is_secure_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r'[!@#$%^&*(),.?:{}|<>]', password):
        return False, "Password must contain at least one special character."
    return True, "Password is secure."


if __name__ == "__main__":
    password = getpass.getpass("Enter a password: ")
    secure, message = is_secure_password(password)
    print(message)
