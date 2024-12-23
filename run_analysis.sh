#!/bin/bash

# Usage: ./run_analysis.sh input_file output_dir

# Validate arguments
if [[ $# -ne 2 ]]; then
    echo "Usage: $0 <input_file> <output_dir>"
    exit 1
fi

input_file=$1
output_dir=$2

# Check if input file exists
if [[ ! -f $input_file ]]; then
    echo "Error: Input file does not exist."
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p $output_dir

# Run the Python script for analysis
python3 main.py "$input_file" "$output_dir"

# Check if Python script succeeded
if [[ $? -eq 0 ]]; then
    echo "Analysis completed successfully."
    echo "Results saved in $output_dir"
else
    echo "Error: Analysis script failed."
    exit 1
fi
