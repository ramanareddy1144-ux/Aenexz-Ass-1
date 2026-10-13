# Q1: Username Validation System

username = input("Enter a username: ")

# strip() removes spaces from both ends; empty result means only spaces
if username.strip() == "":
    print("Invalid: username must not contain only spaces.")
# lower() makes the comparison case-insensitive
elif username.lower() == "admin":
    print("Invalid: username cannot be 'admin' (in any case).")
elif len(username) < 5:
    print("Invalid: username must contain at least 5 characters.")
else:
    print("Valid username.")

# Test inputs: "Anjali123" -> Valid
#              "abc"       -> too short
#              " "         -> only spaces
#              "ADMIN"     -> not allowed
