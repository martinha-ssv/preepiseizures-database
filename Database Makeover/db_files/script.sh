#!/bin/bash

# Define the source and destination directories
src_dir="patients"
dest_dir="sessions"
template="${dest_dir}/template.json"

# Ensure the template file exists
if [[ ! -f "$template" ]]; then
    echo "Template file not found: $template"
    exit 1
fi

# Loop through all files in the patients directory
for file in "$src_dir"/*.json; do
    # Get the basename of the file
    filename=$(basename "$file")

    # Skip the template file in patients directory
    if [[ "$filename" == "template.json" ]]; then
        continue
    fi

    # Define the destination file path
    dest_file="${dest_dir}/${filename}"

    # Check if the destination file already exists
    if [[ ! -f "$dest_file" ]]; then
        # Copy the template to the new file in sessions directory
        cp "$template" "$dest_file"
        echo "Created $dest_file from template."
    else
        echo "File already exists: $dest_file"
    fi
done

