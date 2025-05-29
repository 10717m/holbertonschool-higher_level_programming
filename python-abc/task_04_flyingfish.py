class Fish:
    """Base class representing a fish"""
    
    def swim(self):
        """Print basic swimming message"""
        print("The fish is swimming")
    
    def habitat(self):
        """Print fish habitat"""
        print("The fish lives in water")


class Bird:
    """Base class representing a bird"""
    
    def fly(self):
        """Print basic flying message"""
        print("The bird is flying")
    
    def habitat(self):
        """Print bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Class representing a flying fish that inherits from both Fish and Bird"""
    
    def fly(self):
        """Override fly method for flying fish"""
        print("The flying fish is soaring!")
    
    def swim(self):
        """Override swim method for flying fish"""
        print("The flying fish is swimming!")
    
    def habitat(self):
        """Override habitat method for flying fish"""
        print("The flying fish lives both in water and the sky!")
