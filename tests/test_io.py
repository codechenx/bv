from unittest import TestCase

from bv.config import init_configure
from bv.io import GeneralReader, ExcelReader

vcf_path = "tests/data/sample.vcf"
vcf_config = init_configure().get("vcf")
excel_path = "tests/data/sample.xlsx"
excel_config = init_configure().get("xlsx")

class TestReader(TestCase):
    def test_path(self):
        reader = GeneralReader()
        reader.load_file(vcf_path, vcf_config)
        assert vcf_path == reader.path

    def test_data(self):
        reader = GeneralReader()
        reader.load_file(vcf_path, vcf_config)
        assert reader.data

    def test_config(self):
        reader = GeneralReader()
        reader.load_file(vcf_path, vcf_config)
        assert reader.config

    def test_load_file(self):
        reader = GeneralReader()
        reader.load_file(vcf_path, vcf_config)

class TestExcelReader(TestCase):
    def test_path(self):
        reader = ExcelReader()
        reader.load_file(excel_path, excel_config)
        assert excel_path == reader.path

    def test_data(self):
        reader = ExcelReader()
        reader.load_file(excel_path, excel_config)
        assert reader.data

    def test_config(self):
        reader = ExcelReader()
        reader.load_file(excel_path, excel_config)
        assert reader.config

    def test_load_file(self):
        reader = ExcelReader()
        reader.load_file(excel_path, excel_config)
