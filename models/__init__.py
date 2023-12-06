#!/usr/bin/python3
"""Defines the __init__ module for the pythone package"""


from models.engine.file_storage import FileStorage
"""Defines the imported modules"""


storage = FileStorage()
storage.reload()
