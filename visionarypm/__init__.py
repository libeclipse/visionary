#!/usr/bin/python2

import hashlib
import re
from getpass import getpass

def banner():
    return """
                      _     _                              
               /\   /(_)___(_) ___  _ __   __ _ _ __ _   _ 
               \ \ / / / __| |/ _ \| '_ \ / _` | '__| | | |
                \ V /| \__ \ | (_) | | | | (_| | |  | |_| |
                 \_/ |_|___/_|\___/|_| |_|\__,_|_|   \__, |
                                     Password Manager|___/ """

def sha256(s):
    return hashlib.sha256(s).hexdigest()

    
def generate(master_password, keyword):
    password = sha256(sha256(master_password)+sha256(keyword))
    for iteration in range(200000):
        password = sha256(password)
    return password[0:32]

def strong(password):
    if len(password) >= 14:
        if re.search(r'\d', password):
            if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
                return True
            else:
                return 'Password must be a mix of uppercase and lowercase characters.'
        else:
            return 'Password must contain digits.'
    else:
        return 'Password must be at least 14 characters long.'

def main(first_run=True):
    if first_run == True:
        print '%s\n' % (banner())
    master_password = getpass('Master password: ')
    if strong(master_password):
        keyword = raw_input('Keyword: ')
        print '\nYour password: %s' % (generate(master_password, keyword))
    else:
        print '%s\n' % (strong(master_password))
        main(False)        
 
if __name__ == "__main__":
    try:
        print '%s\n' % (banner())
        main()
    except KeyboardInterrupt:
        print '\nKeyboard Interrupt.'