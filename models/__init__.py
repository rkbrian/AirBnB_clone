#!/usr/bin/python3
"""Module creates unique instance of ``FileStorage`` for the console."""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
