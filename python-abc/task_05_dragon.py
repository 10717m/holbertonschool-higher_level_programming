class SwimMixin:
    """Mixin class that provides swimming capability"""
    
    def swim(self):
        """Print swimming message"""
        print("The creature swims!")


class FlyMixin:
    """Mixin class that provides flying capability"""
    
    def fly(self):
        """Print flying message"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that inherits swimming and flying capabilities"""
    
    def roar(self):
        """Print dragon's roar"""
        print("The dragon roars!")
