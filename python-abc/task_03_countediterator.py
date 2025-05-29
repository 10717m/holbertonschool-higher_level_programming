class CountedIterator:
    """An iterator that keeps track of how many items have been fetched"""
    
    def __init__(self, iterable):
        """Initialize with an iterable and set counter to 0"""
        self.iterator = iter(iterable)
        self.counter = 0
    
    def __next__(self):
        """Fetch the next item and increment the counter"""
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise
    
    def get_count(self):
        """Return the number of items fetched so far"""
        return self.counter
    
    def __iter__(self):
        """Return self to allow the iterator to be used in for loops"""
        return self
