# Problem 6
# 20/20 points (graded)
#
# In this problem, you will implement a class according to the specifications in the template file usresident.py. The
#  file contains a Person class similar to what you have seen in lecture and a USResident class (a subclass of
# Person). Person is already implemented for you and you will have to implement two methods of USResident.
#
# For example, the following code:
#
# a = USResident('Tim Beaver', 'citizen')
# print(a.getStatus())
# b = USResident('Tim Horton', 'non-resident')
#
# will print out:
#
# citizen
# ## will show that a ValueError was raised at a particular line
#
#
# usresident.py
#
# Paste only your implementation of the USResident class in the box below. Do not leave any debugging print statements.


class USResident(Person):
    """
    A Person who resides in the US.
    """

    def __init__(self, name, status):
        """
        Initializes a Person object. A USResident object inherits
        from Person and has one additional attribute:
        status: a string, one of "citizen", "legal_resident", "illegal_resident"
        Raises a ValueError if status is not one of those 3 strings
        """
        Person.__init__(self, name)
        if status in ("citizen", "legal_resident", "illegal_resident"):
            self.status = status
        else:
            raise ValueError


    def getStatus(self):
        """
        Returns the status
        """
        return self.status