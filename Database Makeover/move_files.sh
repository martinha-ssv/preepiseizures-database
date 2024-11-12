#!/bin/bash

# Define source and destination directories
SOURCE_DIR="/Volumes/T7 Touch/PreEpiSeizures/Patients_HSM"
DESTINATION_DIR="patient_data"

# Ensure the destination directory exists
mkdir -p "$DESTINATION_DIR"

# Loop over each subdirectory in the source directory
for subdir in "$SOURCE_DIR"/*; do
    if [ -d "$subdir" ]; then  # Check if it's a directory
        # Extract the name of the subdirectory
        subdir_name=$(basename "$subdir")

        # Create a corresponding directory in the destination
        mkdir -p "$DESTINATION_DIR/$subdir_name"

        # Copy only files from the subdirectory to the new location
        find "$subdir" -maxdepth 1 -type f -exec cp {} "$DESTINATION_DIR/$subdir_name" \;
    fi
done

echo "Copy complete."

