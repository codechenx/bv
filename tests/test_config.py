from unittest import TestCase

from bv.config import TypeConfig, init_configure


class TestTypeConfig(TestCase):
    vcf_config_path = "tests/data/config_format.cfg"

    def test_check_format(self):
        vcf_tyepeconfig = TypeConfig(self.vcf_config_path)
        assert vcf_tyepeconfig.check_format()

    def test_format_config(self):
        vcf_tyepeconfig = TypeConfig(self.vcf_config_path)
        assert {'name': 'test', "extension": '.test', 'description': 'test'} == vcf_tyepeconfig.format_config

    def test_header_config(self):
        vcf_tyepeconfig = TypeConfig(self.vcf_config_path)
        assert {'description': 'test_header', 'regex': '^##'} == vcf_tyepeconfig.metadata_config

    def test_body_config(self):
        vcf_tyepeconfig = TypeConfig(self.vcf_config_path)
        assert {'description': 'test_body', 'sep': '\\t'} == vcf_tyepeconfig.body_config

    def test_ignore_config(self):
        vcf_tyepeconfig = TypeConfig(self.vcf_config_path)
        assert {'description': 'test_ignore', 'regex': '^##'} == vcf_tyepeconfig.ignore_config

    def test_init_configure(self):
        assert isinstance(init_configure(), dict)
