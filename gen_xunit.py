#!/usr/bin/env python
import unittest
import sys

class CompilerTestCase(unittest.TestCase):

    compiler = ""


    def test_isThreeLetters(self):
        cls = self.__class__
        self.assertEqual(len(cls.compiler),3, "%s is not 3 chars long" % cls.compiler)

    def test_isGNU(self):
        cls = self.__class__
        self.assertEqual(cls.compiler, "GNU", "%s is not equal to GNU" % cls.compiler)


if __name__ == '__main__':
    compiler = sys.argv[1]
    suite = unittest.TestSuite()
    cls = type("%sTestCase" % compiler, (CompilerTestCase,), dict(compiler=compiler))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(cls))

    try:
        import xmlrunner
    except ImportError:
        result = unittest.TextTestRunner(verbosity=2).run(suite)
    else:
        result = xmlrunner.XMLTestRunner(verbosity=2, output='test-reports').run(suite)
