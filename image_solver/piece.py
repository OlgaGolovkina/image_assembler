class Piece:
    """Represents single image piece.

    Each piece has identifier so it can be tracked across different individuals.

    :param image: ndarray representing piece's RGB values
    :param index: Unique id withing piece's parent image
    """
    def __init__(self, image, index):
        self.image = image[:]
        self.id = index

    def __getitem__(self, index):
        return self.image.__getitem__(index)

    def size(self):
        """Returns piece size"""
        return self.image.shape[0]

    def shape(self):
        """Returns shape of piece's image"""
        return self.image.shape
