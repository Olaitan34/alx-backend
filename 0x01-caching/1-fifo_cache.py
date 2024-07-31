#!/usr/bin/env python3
from typing import Any, Dict, Optional
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """
    Child class of BseCaching, also stores data in dictionary
    """
    def __init__(self):
    """
    instantiation of the class
    """
        super().__init__()

