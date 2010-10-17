from __future__ import print_function
from random import choice
import string
import subprocess

cipher = "aes-256-cbc"
encryptcommand = "openssl enc -"+cipher+" -base64"
decryptcommand = encryptcommand+" -d"


def genpass(length=12, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

def encryptpass(plaintextpass, salt):
    """Returns an encrypted password.
    openssl enc -aes-256-cbc -salt -base64
    """
    cmdline = encryptcommand+' -S '+salt
    proc=subprocess.Popen(cmdline,
                          shell=True,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE)
    proc.stdin.write(plaintextpass)
    out,err=proc.communicate()
    return out.strip()

def decryptpass(encryptedpass, salt):
    """Returns plaintext password.

    Extracts the embedded salt and encrypted password.
    Here is what this looks like on the commandline.
 
    openssl enc -aes-256-cbc -salt -base64 -d
    """
    cmdline = decryptcommand+' -S '+salt
    print(cmdline)
    proc=subprocess.Popen(cmdline,
                          shell=True,
                          stdin=subprocess.PIPE,
                          stdout=subprocess.PIPE)
    proc.stdin.write(encryptedpass+'\n')
    out,err=proc.communicate()
    return out.strip()

def printpass(encryptedpass):
    plaintextpass = decryptpass(encryptedpass)
    print('Plaintext password: '+plaintextpass)

def getpass():
    generate_pass = raw_input("Generate passwd [y/n]: ")

    if generate_pass == 'y':
        plaintextpass = genpass()
    else:
        plaintextpass = raw_input("Password: ")

    salt = makesalt()
    encryptedpass = encryptpass(plaintextpass, salt)
    return encryptedpass
