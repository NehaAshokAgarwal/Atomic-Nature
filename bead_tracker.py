import math
import stdio
import sys
from blob_finder import BlobFinder
from picture import Picture


# Entry point
def main():
    # Accepting pixels, tau, and delta as command line arguments.
    pixels = int(sys.argv[1])
    tau = float(sys.argv[2])
    delta = float(sys.argv[3])
    # Calling the constructor to accept the pic as command line argument.
    pic = Picture(sys.argv[4])
    # Calling the constructor BlobFinder to create a new object called blobfinder for the frame
    # sys.argv[4] (first frame) to find blobs in the picture pic, using a luminance threshold tau.
    blobfinder = BlobFinder(pic, tau)
    # Calling the method getBeads() on the blobfinder object, to get the list of all the blobs
    # with mass greater than or equal to pixels , i.e. list of all beads(prevBeads).
    prevBeads = blobfinder.getBeads(pixels)
    # For each frame starting from sys.argv[5] :
    for i in range(5, len(sys.argv)):
        # Constructing the blobfinder object by calling the constructor BlobFinder to get a list
        # of all the beads (currBeads) in each jpg image.
        blobfinder = BlobFinder(Picture(sys.argv[i]), tau)
        currBeads = blobfinder.getBeads(pixels)
        # For each bead in the list of currBeads[]:
        for currBead in currBeads:
            # initialising the shortest distance between two beads to positive infinity(constant)
            closest_distance = math.inf
            # For each bead in the list of prevBead[]:
            for prevBead in prevBeads:
                # Calling the distanceTo() method to compute the distance between the bead from
                # the prevBead list and the bead from currBead list.
                distance = prevBead.distanceTo(currBead)
                # if the value of distance turn out to be less than infinity and delta,
                # then replacing the  the value of closest_distance from inf to the value of
                # distance.
                if distance < closest_distance and distance <= delta:
                    closest_distance = distance
            # Writing the value of closes_distance as standard output if closes_distance is not
            # equal to the math.inf
            if closest_distance != math.inf:
                stdio.writef('%.4f\n', closest_distance)
        stdio.writeln()
        # set prevBeads to CurrBeads.
        prevBeads = currBeads


if __name__ == '__main__':
    main()
