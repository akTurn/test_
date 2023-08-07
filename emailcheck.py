# import re
#
# regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
#
# def isValid(email):
#     if re.fullmatch(regex, email):
#       print("Valid email")
#     else:
#       print("Invalid email")


def isvalidEmail(email):
    pattern = "^\S+@\S+\.\S+$"
    objs = re.search(pattern, email)
    try:
        if objs.string == email:
            return True
    except:
        return False


VorNotV = isvalidEmail("haxrataligmail.com")
print(VorNotV)
