import argparse
import logging
import sys

from datacatalog_tag_exporter import tag_datasource_exporter


class DatacatalogTagExporterCLI:

    @classmethod
    def run(cls, argv):
        cls.__setup_logging()

        args = cls._parse_args(argv)
        args.func(args)

    @classmethod
    def __setup_logging(cls):
        logging.basicConfig(level=logging.INFO)

    @classmethod
    def _parse_args(cls, argv):
        parser = argparse.ArgumentParser(description=__doc__,
                                         formatter_class=argparse.RawDescriptionHelpFormatter)

        subparsers = parser.add_subparsers()

        cls.add_tags_cmd(subparsers)

        return parser.parse_args(argv)

    @classmethod
    def add_tags_cmd(cls, subparsers):
        tags_parser = subparsers.add_parser("tags", help="Tags commands")

        tags_subparsers = tags_parser.add_subparsers()

        cls.add_export_tags_cmd(tags_subparsers)

    @classmethod
    def add_export_tags_cmd(cls, subparsers):
        export_tags_parser = subparsers.add_parser('export',
                                                   help='Export Tags to CSV,'
                                                   ' creates one file'
                                                   ' for each teamplate')
        export_tags_parser.add_argument('--dir-path',
                                        help='Directory path where files will be exported')
        export_tags_parser.add_argument('--project-ids',
                                        help='Project ids to narrow down Templates list,'
                                        'split by comma',
                                        required=True)
        export_tags_parser.set_defaults(func=cls.__export_tags)

    @classmethod
    def __export_tags(cls, args):
        tag_datasource_exporter.TagDatasourceExporter().export_tags(project_ids=args.project_ids,
                                                                    dir_path=args.dir_path)


def main():
    argv = sys.argv
    DatacatalogTagExporterCLI.run(argv[1:] if len(argv) > 0 else argv)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
