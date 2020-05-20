# Datacatalog Tag Exporter

[![CircleCI][1]][2] [![PyPi][4]][5] [![License][6]][6] [![Issues][7]][8]

A Python package to manage Google Cloud Data Catalog Tag export scripts.

**Disclaimer: This is not an officially supported Google product.**

<!--
  ⚠️ DO NOT UPDATE THE TABLE OF CONTENTS MANUALLY ️️⚠️
  run `npx markdown-toc -i README.md`.

  Please stick to 80-character line wraps as much as you can.
-->

## Table of Contents

<!-- toc -->

- [Executing in Cloud Shell](#executing-in-cloud-shell)
- [1. Environment setup](#1-environment-setup)
  * [1.1. Python + virtualenv](#11-python--virtualenv)
    + [1.1.1. Install Python 3.6+](#111-install-python-36)
    + [1.1.2. Get the source code](#112-get-the-source-code)
    + [1.1.3. Create and activate an isolated Python environment](#113-create-and-activate-an-isolated-python-environment)
    + [1.1.4. Install the package](#114-install-the-package)
  * [1.2. Docker](#12-docker)
  * [1.3. Auth credentials](#13-auth-credentials)
    + [1.3.1. Create a service account and grant it below roles](#131-create-a-service-account-and-grant-it-below-roles)
    + [1.3.2. Download a JSON key and save it as](#132-download-a-json-key-and-save-it-as)
    + [1.3.3. Set the environment variables](#133-set-the-environment-variables)
- [2. Export Tags to CSV file](#2-export-tags-to-csv-file)
  * [2.1. A list of CSV files, each representing one Template will be created.](#21-a-list-of-csv-files-each-representing-one-template-will-be-created)
  * [2.2. Run the datacatalog-tag-exporter script](#22-run-the-datacatalog-tag-exporter-script)
  * [2.2.1 Run the datacatalog-tag-exporter filtering Tag Templates](#221-run-the-datacatalog-tag-exporter-filtering-tag-templates)

<!-- tocstop -->

-----

## Executing in Cloud Shell
````bash
# Set your SERVICE ACCOUNT, for instructions go to 1.3. Auth credentials
# This name is just a suggestion, feel free to name it following your naming conventions
export GOOGLE_APPLICATION_CREDENTIALS=~/datacatalog-tag-exporter-sa.json

# Install datacatalog-tag-exporter 
pip3 install datacatalog-tag-exporter --user

# Add to your PATH
export PATH=~/.local/bin:$PATH

# Look for available commands
datacatalog-tag-exporter --help
````

## 1. Environment setup

### 1.1. Python + virtualenv

Using [virtualenv][3] is optional, but strongly recommended unless you use [Docker](#12-docker).

#### 1.1.1. Install Python 3.6+

#### 1.1.2. Get the source code
```bash
git clone https://github.com/mesmacosta/datacatalog-tag-exporter
cd ./datacatalog-tag-exporter
```

_All paths starting with `./` in the next steps are relative to the `datacatalog-tag-exporter`
folder._

#### 1.1.3. Create and activate an isolated Python environment

```bash
pip install --upgrade virtualenv
python3 -m virtualenv --python python3 env
source ./env/bin/activate
```

#### 1.1.4. Install the package

```bash
pip install --upgrade .
```

### 1.2. Docker

Docker may be used as an alternative to run the script. In this case, please disregard the
[Virtualenv](#11-python--virtualenv) setup instructions.

### 1.3. Auth credentials

#### 1.3.1. Create a service account and grant it below roles

- Data Catalog Admin

#### 1.3.2. Download a JSON key and save it as
This name is just a suggestion, feel free to name it following your naming conventions
- `./credentials/datacatalog-tag-exporter-sa.json`

#### 1.3.3. Set the environment variables

_This step may be skipped if you're using [Docker](#12-docker)._

```bash
export GOOGLE_APPLICATION_CREDENTIALS=~/credentials/datacatalog-tag-exporter-sa.json
```

## 2. Export Tags to CSV file

### 2.1. A list of CSV files, each representing one Template will be created.
One file with summary with stats about each template, will also be created on the same directory.

The columns for the summary file are described as follows:

| Column                         | Description                                              | 
| ---                            | ---                                                      | 
| **template_name**              | Resource name of the Tag Template for the Tag.           | 
| **tags_count**                 | Number of tags found from the template.                  | 
| **tagged_entries_count**       | Number of tagged entries with the template.              | 
| **tagged_columns_count**       | Number of tagged columns with the template.              | 
| **tag_string_fields_count**    | Number of used String fields on tags of the template.    | 
| **tag_bool_fields_count**      | Number of used Bool fields on tags of the template.      | 
| **tag_double_fields_count**    | Number of used Double fields on tags of the template.    | 
| **tag_timestamp_fields_count** | Number of used Timestamp fields on tags of the template. | 
| **tag_enum_fields_count**      | Number of used Enum fields on tags of the template.      | 

The columns for each template file are described as follows:

| Column                     | Description                                            | 
| ---                        | ---                                                    |
| **relative_resource_name** | Full resource name of the asset the Entry refers to.   |
| **linked_resource**        | Full name of the asset the Entry refers to.            |
| **template_name**          | Resource name of the Tag Template for the Tag.         | 
| **tag_name**               | Resource name of the Tag.                              |
| **column**                 | Attach Tags to a column belonging to the Entry schema. |
| **field_id**               | Id of the Tag field.                                   |
| **field_type**             | Type of the Tag field.                                 | 
| **field_value**            | Value of the Tag field.                                | 

### 2.2. Run the datacatalog-tag-exporter script

- Python + virtualenv

```bash
datacatalog-tag-exporter tags export --project-ids my-project --dir-path DIR_PATH
```

### 2.2.1 Run the datacatalog-tag-exporter filtering Tag Templates

- Python + virtualenv

```bash
datacatalog-tag-exporter tags export --project-ids my-project \
--dir-path DIR_PATH \
--tag-templates-names projects/my-project/locations/us-central1/tagTemplates/my-template,\
projects/my-project/locations/us-central1/tagTemplates/my-template-2 

```

[1]: https://circleci.com/gh/mesmacosta/datacatalog-tag-exporter.svg?style=svg
[2]: https://circleci.com/gh/mesmacosta/datacatalog-tag-exporter
[3]: https://virtualenv.pypa.io/en/latest/
[4]: https://img.shields.io/pypi/v/datacatalog-tag-exporter.svg?force_cache=true
[5]: https://pypi.org/project/datacatalog-tag-exporter/
[6]: https://img.shields.io/github/license/mesmacosta/datacatalog-tag-exporter.svg
[7]: https://img.shields.io/github/issues/mesmacosta/datacatalog-tag-exporter.svg
[8]: https://github.com/mesmacosta/datacatalog-tag-exporter/issues

