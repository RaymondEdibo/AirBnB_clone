#!/usr/bin/python3
"""
    model init module.
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
