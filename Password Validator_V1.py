#CREATE A FUNCTION THAT CHECKS IF A PASSWORD IS STRONG
def password_validator(password):
    issues = []
    if len(password) < 8:
        issues.append("You need at least 8 character")
    if not any(c.islower() for c in password):
        issues.append("You need at least one lowercase")
    if not any(c.isupper() for c in password):
        issues.append("You need at least one uppercase")
    if not any(c.isdigit() for c in password):
        issues.append("You need at least one number")
    if not any(c in "!@#$%^&*" for c in password):
        issues.append("You need at least one special character")

    if not issues:
        return {"Valid": True}
    else:
        return {"Valid": False, "Issues": issues}
