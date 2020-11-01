"""
Script to compute accuracy between files.
"""

import csv
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file1', type=str,
        help="Output file of translate.py."
    )
    parser.add_argument(
        '--file2', type=str,
        help="Output file of translate.py., synonyms replaced"
    )
    args = vars(parser.parse_args())

    consistent, all_samples = 0, 0

    # Open the prediction files for the regular and synonym replaced test set
    predictions = open(args["file1"], encoding="utf-8")
    predictions_twin = open(args["file2"], encoding="utf-8")

    for line1, line2 in zip(predictions, predictions_twin):
        # Consider two outputs consistent if and only if they are the same
        # and non-empty
        if line1.strip() == line2.strip():
            consistent += 1
        all_samples += 1

    # Report statistics to user
    print("Consistent / All samples", consistent / all_samples)
