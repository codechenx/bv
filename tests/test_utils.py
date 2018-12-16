from unittest import TestCase

from bv.utils import *


class TestUtils(TestCase):
    def test_tabstr_to_tab(self):
        assert "\t" == tabstr_to_tab("\\t")
        assert "," == tabstr_to_tab(",")

    def test_check_unified_length(self):
        data = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        assert True == check_unified_length(data)
        data = [['1', '2'], ['7', '6', '5'], ['3', '2', '1']]
        assert False == check_unified_length(data)

    def test_convert_numeric_list(self):
        assert [1, 2, 3] == convert_numeric_list(['1', '2', '3'])
        assert [1.0, 2.0, 3.0] == convert_numeric_list(['1.0', '2', '3'])
        assert ['1.0', '2', '3E'] == convert_numeric_list(['1.0', '2', '3E'])

    def test_trans_data(self):
        data = [['1', '2', '3'], ['7', '6', '5']]
        assert [["1", "7"], ["2", "6"], ["3", "5"]] == trans_data(data)

    def test_get_file_extension(self):
        assert ("txt", False) == get_file_extension("/mnt/test.txt")
        assert ("vcf", True) == get_file_extension("/mnt/test.vcf.gz")

    def test_detect_sep(self):
        assert detect_sep("a,b,c") == ","
        assert detect_sep("a;b;c") == ";"

    def test_detect_encoding(self):
        fn = 'data/sample.vcf.gz'
        assert "ascii" == detect_encoding(fn)
