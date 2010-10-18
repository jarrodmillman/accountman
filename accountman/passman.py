from __future__ import print_function
from random import choice
import string
from  subprocess import Popen, PIPE

cipher = "aes-256-cbc"
encryptcommand = "openssl enc -"+cipher+" -base64"
decryptcommand = encryptcommand+" -d"


def randomstring(length=12, chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

def encrypt(plaintextpass, salt):
    """Returns an encrypted password.
    openssl enc -aes-256-cbc -salt -base64
    """
    cmdline = encryptcommand+' -S '+salt
    proc=Popen(cmdline, shell=True, stdin=PIPE, stdout=PIPE)
    proc.stdin.write(plaintextpass)
    out,err=proc.communicate()
    return dict(salt=salt, cipherpasswd=out.strip())

def decrypt(ciphertext):
    """Returns plaintext password.

    Extracts the embedded salt and encrypted password.
    Here is what this looks like on the commandline.
 
    openssl enc -aes-256-cbc -salt -base64 -d
    """
    cipherpass, salt = ciphertext['cipherpasswd'], ciphertext['salt']
    cmdline = decryptcommand+' -S '+salt
    proc=Popen(cmdline, shell=True, stdin=PIPE, stdout=PIPE)
    proc.stdin.write(cipherpass+'\n')
    out,err=proc.communicate()
    return out.strip()

def getpass():
    generate_pass = raw_input("Generate passwd [y/n]: ")

    if generate_pass == 'y':
        plaintextpass = randomstring()
    else:
        plaintextpass = raw_input("Password: ")

    salt = randomstring(length=6).encode("hex")
    return encrypt(plaintextpass, salt)
