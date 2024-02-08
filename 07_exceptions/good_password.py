import sys
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def check_password(string):
    try:
        _ = 1 / (not len(string) < 9)
    except:
        raise LengthError("LengthError")
    try:
        _ = 1 / (any(i.isalpha() for i in string) and any(i.islower() for i in string) and any(i.isupper() for i in string))
    except:
        raise LetterError("LetterError")
    try:
        _ = 1 / any(i.isdigit() for i in string)
    except:
        raise DigitError("DigitError")
    return True

def is_good_password():
    for psswrd in [line.strip() for line in sys.stdin]:
        try:
            check_password(psswrd)
            return "Success!"
        except Exception as err:
            print(err)

print(is_good_password())
