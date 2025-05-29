class VerboseList(list):
    """A list subclass that prints notifications for modifications"""
    
    def append(self, item):
        """Add an item to the end of the list and print a notification"""
        super().append(item)
        print(f"Added [{item}] to the list.")
    
    def extend(self, iterable):
        """Extend the list by appending elements from the iterable and print a notification"""
        initial_length = len(self)
        super().extend(iterable)
        added_count = len(self) - initial_length
        print(f"Extended the list with [{added_count}] items.")
    
    def remove(self, item):
        """Remove first occurrence of item and print a notification"""
        print(f"Removed [{item}] from the list.")
        super().remove(item)
    
    def pop(self, index=-1):
        """Remove and return item at index (default last) and print a notification"""
        item = self[index]  # Get the item before popping
        result = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return result
