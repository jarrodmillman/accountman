import unittest

import cli
from passman import encrypt, decrypt


passpair1 = {'passwd':  'passwordtest',
             'salt':   '\'0102030405\'',
             'cipherpasswd': 'U2FsdGVkX18BAgMEBQAAAGAFC+a2maATJIbXa+Y3mL4='}

class testpassman(unittest.TestCase):

    def test_genpass(self):
        pass
    
    def test_encrypt(self):
        acc = cli.load('tests/testaccounts.json')['acc1']['password']
        assert acc['cipherpasswd'] == encrypt(acc['passwd'],acc['salt'])['cipherpasswd']

    def test_decrypt(self):
        assert decrypt(passpair1) == passpair1['passwd']
    
    def test_getpass(self):
        pass

if __name__ == '__main__':
    unittest.main()
