from unittest import TestCase

from bv.config import init_configure
from bv.io import GeneralReader

vcf_path = "data/sample.vcf"
vcf_config = init_configure().get("vcf")


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
