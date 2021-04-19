from scriptYaml2 import MergingScript
import yaml
import unittest
import os

class Test(unittest.TestCase):
    
    def test_empty_file_inner(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\6\test\test','test6.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','6.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertRaises(TypeError, MergingScript(test1).main())

    def test_empty_file_outer(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\7\test\test','test7.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','7.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertRaises(TypeError, MergingScript(test1).main())
       
    def test_given_int_and_string(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\1\test','test1.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','1.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_given_yaml_lists(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\2\test','test2.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','2.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_given_nested_key_value(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\3\test','test3.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','3.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_sister_folder_present(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\4\test\test','test4.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','4.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_complex(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase\5\test','test5.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase\expected','5.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)
    
if __name__== "__main__":
    dirname = os.path.dirname(__file__)
    unittest.main()
