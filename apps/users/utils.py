

def check_password_in_signup(password: str, confirm_password: str):
    if not password:
        return False

    if not confirm_password:
        return False

    if not password == confirm_password:
        return False

    return True