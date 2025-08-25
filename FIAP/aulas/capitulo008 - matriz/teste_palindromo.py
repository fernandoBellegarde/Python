def palindromo(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i = i + 1
        j = j - 1
    return True

# Ou return string == string[::-1] tb funciona pq o [::-1] inverte a string

import unittest

class TestesChiques(unittest.TestCase):

    def test01_pares(self):
        self.assertEqual(palindromo("abba"), True)
        self.assertEqual(palindromo("abbaabba"), True)
        self.assertEqual(palindromo("abca"), True)

    def test02_impares(self):
        self.assertEqual(palindromo("aba"), True)
        self.assertEqual(palindromo("abx"), False)

    def test01_pares(self):
        self.assertEqual(palindromo("a"), True)
        self.assertEqual(palindromo(""), True)


def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestesChiques)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

runTests()