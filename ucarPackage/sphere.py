#This is the sample sphere class that creates a sphere object and the volume function to return its volume.
#this makes it very easy to add mroe functionalities to this.
class sphere:

    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return ((4/3) * (22/7) * (self.radius ** 3))

