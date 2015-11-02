#!/usr/bin/python
import pkgutil
import inspect
import importlib
import xmatch
from xmatch.catalog import ArchesXmatchCatalog


def get_loaders():
    """
    Creates list of available catalogs by scanning all .py files.
    """
    catalogs = {}
    for catalog_module in pkgutil.walk_packages(xmatch.__path__, 'xmatch.'):
        modul = importlib.import_module(catalog_module[1])
        for _, obj in inspect.getmembers(modul):
            if inspect.isclass(obj) and \
               issubclass(obj, ArchesXmatchCatalog) and \
               not obj == ArchesXmatchCatalog:
                catalogs[obj.__module__.split('.')[1]] = obj
    return catalogs
