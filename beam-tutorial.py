from __future__ import absolute_import

import argparse
import logging
import re

from past.builtins import unicode

import apache_beam as beam
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

def run(argv=None, save_main_session=True):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        dest='input',
        default='gs://dataflow-samples/shakespeare/kinglear.txt',
        help='Input file to process.')
    parser.add_argument(
        '--output',
        dest='output',
        default='default_output.txt',
        help='Output file to write the results to.')
    known_args, pipeline_args = parser.parse_known_args(argv)
    pipeline_args.extend([
        '--runner=DirectRunner',
        '--project=SET_YOUR_PROJECT_ID_HERE',
        '--staging_location=gs://YOUR_BUCKET_NAME/AND_STAGING_DIRECTORY',
        '--temp_location=gs://YOUR_BUCKET_NAME/AND_TEMP_DIRECTORY',
        '--job_name=your-wordcount-job',
    ])

    pipeline_options = PipelineOptions(pipeline_args)
    pipeline_options.view_as(SetupOptions).save_main_session = save_main_session
    with beam.Pipeline(options=pipeline_options) as p:
        