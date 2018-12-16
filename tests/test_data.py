from unittest import TestCase

import pytest

from bv.data import Data


class TestData(TestCase):
    def test_type(self):
        new_data = Data()
        new_data.type = "vcf"
        assert new_data.type == "vcf"

        with pytest.raises(AssertionError):
            new_data.type = 0

    def test_metadata(self):
        new_data = Data()
        new_data.metadata = [['1', '2', '3'], ['4', '5', '6']]
        assert [['1', '2', '3'], ['4', '5', '6']] == new_data.metadata
        with pytest.raises(AssertionError):
            new_data.metadata = "something"

    def test_body(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['4', '5', '6']]
        assert [['1', '2', '3'], ['4', '5', '6']] == new_data.body

        with pytest.raises(AssertionError):
            new_data.body = "something"

    def test_empty(self):
        new_data = Data()
        new_data.type = "vcf"
        new_data.metadata = [['1', '2', '3'], ['4', '5', '6']]
        new_data.body = [['1', '2', '3'], ['4', '5', '6']]
        new_data.footer = [['1', '2', '3'], ['4', '5', '6']]
        new_data.empty()
        assert new_data.type == ""
        assert new_data.metadata == []
        assert new_data.body == []

    def test_size(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['4', '5', '6']]
        assert (2, 3) == new_data.size

    def test_sorted_by_row(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['6', '5', '7'], ['3', '2', '1']]
        new_data.sorted_by_row(0)
        assert [['1', '2', '3'], ['6', '5', '7'], ['3', '2', '1']] == new_data.body
        new_data.sorted_by_row(1)
        assert [['2', '1', '3'], ['5', '6', '7'], ['2', '3', '1']] == new_data.body
        new_data.sorted_by_row(2)
        assert [['3', '2', '1'], ['7', '5', '6'], ['1', '2', '3']] == new_data.body
        with pytest.raises(AssertionError):
            new_data.sorted_by_row(3)

    def test_sorted_by_col(self):
        new_data = Data()
        new_data.body = [['1', '7', '3'], ['2', '5', '2'], ['3', '6', '1']]
        new_data.sorted_by_col(0)
        assert [['1', '7', '3'], ['2', '5', '2'], ['3', '6', '1']] == new_data.body
        new_data.sorted_by_col(1)
        assert [['2', '5', '2'], ['3', '6', '1'], ['1', '7', '3']] == new_data.body
        new_data.sorted_by_col(2)
        assert [['3', '6', '1'], ['2', '5', '2'], ['1', '7', '3']] == new_data.body
        with pytest.raises(AssertionError):
            new_data.sorted_by_col(3)

    def test_get_sorted_row(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        assert ['5', '6', '7'] == new_data.get_sorted_row(1)
        with pytest.raises(AssertionError):
            new_data.get_sorted_row(3)

    def test_get_sorted_col(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        assert ['2', '2', '6'] == new_data.get_sorted_col(1)
        with pytest.raises(AssertionError):
            new_data.get_sorted_col(3)

    def test_get_col(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        assert ['2', '6', '2'] == new_data.get_col(1)
        with pytest.raises(AssertionError):
            new_data.get_col(3)

    def test_get_row(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        assert ['7', '6', '5'] == new_data.get_row(1)
        with pytest.raises(AssertionError):
            new_data.get_row(3)

    def test_rm_col(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        new_data.rm_col([1, 2])
        new_data_body = new_data.body
        print(new_data_body)
        assert [['1'], ['7'], ['3']] == new_data_body

    def test_rm_row(self):
        new_data = Data()
        new_data.body = [['1', '2', '3'], ['7', '6', '5'], ['3', '2', '1']]
        new_data.rm_row([1, 2])
        new_data_body = new_data.body
        print(new_data_body)
        assert [['1', '2', '3']] == new_data_body
