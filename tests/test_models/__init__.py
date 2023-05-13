#!/usr/bin/python3
"""
Initialize the file storage system for the models directory.
"""
from models.engine.file_storage import FileStorage

# Create a FileStorage object
file_storage = FileStorage()

# Reload the stored data from the JSON file into the object
file_storage.reload()
