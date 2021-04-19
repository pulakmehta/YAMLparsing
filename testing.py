'''
Author: Pulak Mehta
Date: April 18,2021
Details - Nine Test cases have been developed and tested for
1) test_fail_invalid_dir: The directory provided does not exist
2) test_fail_invalid_yaml: The file provided is not a YAML file
3) test_given_int_and_string: Merging of simple int and string YAML
4) test_given_yaml_lists: Merging of simple list YAML
5) test_given_nested_key_value: Merging of nested key-value pair
6) test_sister_folder_present: Verifying that sister folders dont get merged
7) test_complex: Complex Case consisting of int, string, list, nested key-value and values contains lists
8) test_empty_file_inner: Leaf (inner most) YAML file is empty
9) test_empty_file_outer: Parent (outer most) YAML file is empty
'''

from scriptYaml import MergingScript
import yaml
import unittest
import os

class Test(unittest.TestCase):
    def test_fail_invalid_yaml(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/0','test0.docx'))
        self.assertRaises(TypeError,MergingScript(test1).main())

    def test_fail_invalid_dir(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/0/test/test','test0.yaml'))
        self.assertRaises(TypeError,MergingScript(test1).main())
        
    def test_given_int_and_string(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/1/test','test1.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','1.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_given_yaml_lists(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/2/test','test2.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','2.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_given_nested_key_value(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/3/test','test3.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','3.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_sister_folder_present(self):
        test1 = os.path.normpath(os.path.join(dirname,r'TestCase/4/test/test','test4.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,r'TestCase/expected','4.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_complex(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/5/test','test5.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','5.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_empty_file_inner(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/6/test/test','test6.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','6.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)

    def test_empty_file_outer(self):
        test1 = os.path.normpath(os.path.join(dirname,'TestCase/7/test/test','test7.yaml'))
        test1_ans = os.path.normpath(os.path.join(dirname,'TestCase/expected','7.yaml'))
        with open(test1_ans) as file:
            documents = yaml.load(file, Loader=yaml.FullLoader)
        self.assertEqual(MergingScript(test1).main(), documents)


if __name__== "__main__":
    dirname = os.path.dirname(__file__)
    unittest.main()
