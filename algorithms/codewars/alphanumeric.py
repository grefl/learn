def alphanumeric(password):
    for c in password:
        c = ord(c)
        if (c >= ord('0') and c <= ord('9')) or (c >= ord('a') and c <= ord('z')) or (c >= ord('A') and c <= ord('Z')):
            continue 
        else:
            return False
    return True if len(password) > 0 else False
string = "PassW0rd"
res = alphanumeric(string)
print(res)
