import stdio


# A data type to represent a blob.
class Blob:
    # Constructs an empty blob.
    def __init__(self):
        # composing the constructor to define and initialise the instance variable for the
        # particle blob.
        self._x = 0.0  # x-coordinate of center of mass
        self._y = 0.0  # y-coordinate of center of mass
        self._pixels = 0  # number of pixels

    # Adds pixel (x, y) to this blob.
    def add(self, x, y):
        # Centre of mass is calculate as follows (the equation os applied to each axis):
        # (sum of the (total no of pixel * x coordinate of centre of mass)) divided by the total no
        # of pixels. (physics formula to calculate the centre of mass)
        # To update the centre of mass, we add x( x coordinate of the pixel) in the numerator and
        # 1 in the denominator respectively.
        self._x = (self._pixels * self._x + x) / (self._pixels + 1)
        # Similar to x axis.
        self._y = (self._pixels * self._y + y) / (self._pixels + 1)
        # update the number of pixel by 1
        self._pixels += 1

    # Returns the mass of this blob, ie, the number of pixels in it.
    def mass(self):
        return self._pixels

    # Returns the Euclidean distance between the center of mass of this blob and the center of
    # mass of the other blob.
    def distanceTo(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5

    # Returns a string representation of this blob.
    def __str__(self):
        return '%d (%.4f, %.4f)' % (self._pixels, self._x, self._y)


# Unit tests the data type (DO NOT EDIT).
def _main():
    a = Blob()
    a.add(0, 0)
    b = Blob()
    while not stdio.isEmpty():
        x = stdio.readFloat()
        y = stdio.readFloat()
        b.add(x, y)
    stdio.writeln('a          = ' + str(a))
    stdio.writeln('b          = ' + str(b))
    stdio.writeln('dist(a, b) = ' + str(a.distanceTo(b)))


if __name__ == '__main__':
    _main()
