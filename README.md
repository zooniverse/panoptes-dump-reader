# Panoptes Dump Reader

Panoptes' dumps are in CSV format, but since classifications are made in a richer structure of data than CSV can handle, we have chosen to have some columns (metadata, annotations) in JSON format. This means that no information is lost when working with these dumps.

However, that also means that it's somewhat harder to work with dumps in environments like R, SPSS, Excel etc. In order to bridge the gap between our dumps and those programs, we're providing a converter that will attempt to turn the JSON structures in our dumps into (lots of) columns in CSV. Some information might be lost in translation, but if you're having issues dealing with JSON, give this tool a go.

## Install

This is distributed as a Python package and can be installed using `pip`.

```
pip install zooniverse-dump
```

## Usage

After installation, you have a single command line script available to you, called `panoptes-expand`. This script will take a path to a Panoptes classifications dump file, and expand the various JSON columns into separate columns. Results are printed (as CSV) on your console, but you can use your terminal's normal redirection with `>` to send results to a new file.

```
panoptes-expand path/to/classifications.csv > expanded-classifications.csv
```

## Development

pip install -r requirements.txt

```python
from panoptes import classifications
pandas_data_frame = classifications.load_csv('path/to/classifications_dump.csv')
pandas_data_frame.to_csv('path/to/exploded_classifications_dump.csv')
```
