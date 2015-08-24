# Panoptes Dump Reader

## Install

This is distributed as a Python package.

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
