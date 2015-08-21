# Panoptes Dump Reader

## Install

pip install -r requirements.txt

## Usage

```python
from panoptes import classifications
pandas_data_frame = classifications.load_csv('path/to/classifications_dump.csv')
pandas_data_frame.to_csv('path/to/exploded_classifications_dump.csv')
```
