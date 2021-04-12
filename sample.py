from scriptYaml2 import mergingscript
import yaml
import unittest
import os

class Test(unittest.TestCase):

    def test_should_correctly_merge_single_yaml_file(self):
        test1 = os.path.normpath(os.path.join(dirname,r'Testcase\1\file','test.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'Testcase\expected','1.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(mergingscript(test1).main(), documents)
        


if __name__== "__main__":
    dirname = os.path.dirname(__file__)
    unittest.main()
