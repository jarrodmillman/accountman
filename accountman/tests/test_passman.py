import unittest

import passman

passpair1 = {'plain':  'passwordtest',
             'salt':   '\'0102030405\'',
             'cipher': 'U2FsdGVkX18BAgMEBQAAAGAFC+a2maATJIbXa+Y3mL4='}

class testpassman(unittest.TestCase):

    def test_genpass(self):
        pass
    
    def test_encryptpass(self):
        a = passman.encryptpass(passpair1['plain'],passpair1['salt'])
        assert a == passpair1['cipher']

    def test_decryptpass(self):
        a = passman.decryptpass(passpair1['cipher'],passpair1['salt'])
        print(a)
        assert a == passpair1['plain']
    
    def test_printpass(self):
        pass
    
    def test_getpass(self):
        pass

if __name__ == '__main__':
    unittest.main()
