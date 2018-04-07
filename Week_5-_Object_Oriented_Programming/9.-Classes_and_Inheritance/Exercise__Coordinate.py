# Exercise: coordinate
# 5/5 points (graded)
# ESTIMATED TIME TO COMPLETE: 7 minutes

# Consider the following code from the last lecture video:

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, obj):
        if self.x == obj.x and self.y == obj.y:
            return True
        return False

    def __repr__(self):
        return "Coordinate(" + str(self.x) + "," + str(self.y) + ")"

