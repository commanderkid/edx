ESTIMATED TIME TO COMPLETE: 10 minutes

Consider the following code from the last lecture video:



class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        new_mass = []
        if (self.vals==[]) or (other.vals==[]):
            return "{}"
        else:
            for i in range(len(self.vals)):
                for j in range(len(other.vals)):
                    if self.vals[i] == other.vals[j]:
                        new_mass.append(other.vals[j])
            return "{" + ','.join([str(i) for i in new_mass]) + "}"

    def __len__(self):
        return(len(self.vals))

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
