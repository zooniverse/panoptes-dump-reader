#!/usr/bin/env python
from panoptes import classifications
pandas_data_frame = classifications.load_csv('local/classifications_dump.csv')
pandas_data_frame.to_csv('local/exploded_classifications_dump.csv')
