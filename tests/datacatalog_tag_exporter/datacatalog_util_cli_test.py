import unittest
from unittest import mock

import datacatalog_tag_exporter
from datacatalog_tag_exporter import datacatalog_tag_exporter_cli


class TagManagerCLITest(unittest.TestCase):

    def test_parse_args_invalid_subcommand_should_raise_system_exit(self):
        self.assertRaises(SystemExit,
                          datacatalog_tag_exporter_cli.DatacatalogTagExporterCLI._parse_args,
                          ['invalid-subcommand'])

    def test_parse_args_create_tags_missing_mandatory_args_should_raise_system_exit(self):
        self.assertRaises(SystemExit,
                          datacatalog_tag_exporter_cli.DatacatalogTagExporterCLI._parse_args,
                          ['tags', 'export'])

    def test_run_no_args_should_raise_attribute_error(self):
        self.assertRaises(AttributeError,
                          datacatalog_tag_exporter_cli.DatacatalogTagExporterCLI.run, None)

    @mock.patch('datacatalog_tag_exporter.tag_datasource_exporter.TagDatasourceExporter')
    def test_run_export_tags_should_call_correct_method(self, mock_tag_datasource_exporter):
        datacatalog_tag_exporter_cli.DatacatalogTagExporterCLI.run([
            'tags', 'export', '--dir-path', 'test.csv', '--project-ids', 'my-project1,my-project2'
        ])

        tag_datasource_processor = mock_tag_datasource_exporter.return_value
        tag_datasource_processor.export_tags.assert_called_once()
        tag_datasource_processor.export_tags.assert_called_with(
            project_ids='my-project1,my-project2', dir_path='test.csv')

    @mock.patch('datacatalog_tag_exporter.datacatalog_tag_exporter_cli.DatacatalogTagExporterCLI')
    def test_main_should_call_cli_run(self, mock_cli):
        datacatalog_tag_exporter.main()
        mock_cli.run.assert_called_once()
