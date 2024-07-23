#!/usr/bin/env python3
from typing import Dict, Any, Optional
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """
    Child class of BseCaching, also stores data in dictionary
    """
    def __init__(self):
        super().__init__()
    def put(self, key: Any, item: Any) -> None:
        """
        put method for adding data to a cache
        """
        self.cache_data[key] = item
    def get(self, key: Any) -> Optional[Any]:
        """
        Get method for retrieving the cache
        """
        return self.cache_data.get(key)
if __name__ == "__main__":
    my_cache = BasicCache()
    my_cache.print_cache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.print_cache()
    print(my_cache.get("A"))
    print(my_cache.get("B"))
    print(my_cache.get("C"))
    print(my_cache.get("D"))
    my_cache.print_cache()
    my_cache.put("D", "School")
    my_cache.put("E", "Battery")
    my_cache.put("A", "Street")
    my_cache.print_cache()
    print(my_cache.get("A"))
