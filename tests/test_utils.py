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

    def test_detect_file_sep(self):
        fn = "tests/data/sample.csv"
        assert detect_file_sep(fn) == ","

    def test_detect_file_encoding(self):
        fn = 'tests/data/sample.vcf.gz'
        assert "ascii" == detect_file_encoding(fn)
