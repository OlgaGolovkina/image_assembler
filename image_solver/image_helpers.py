import numpy as np
from .piece import Piece


def flatten_image(image, piece_size, indexed=False):
    """Converts image into list of square pieces.

    Input image is divided into square pieces of specified size and than flattened into list. Each
    list element is PIECE_SIZE x PIECE_SIZE x 3

    :params image:      Input image
    :params piece_size: Size of single square piece. Each piece is PIECE_SIZE x PIECE_SIZE
    :params indexed:    If True list of Pieces with IDs will be returned, otherwise just plain list
                        of ndarray pieces
    """
    offset = int(piece_size / 2)
    rows, columns = (int((image.shape[0] - offset) // piece_size // 1.5),
                     int((image.shape[1] - offset) // piece_size // 1.5))
    pieces = []

    # Crop pieces from original image
    for y in range(rows):
        for x in range(columns):
            left, top = offset + x * (piece_size + offset), offset + y * (piece_size + offset)
            right, bottom = left + piece_size, top + piece_size
            piece = np.empty((piece_size, piece_size, image.shape[2]))
            piece[:piece_size, :piece_size, :] = image[top:bottom, left:right, :]
            pieces.append(piece)

    if indexed:
        pieces = [Piece(value, index) for index, value in enumerate(pieces)]

    return pieces, rows, columns


def assemble_image(pieces, rows, columns):
    """Assembles image from pieces.

    Given an array of pieces and desired image dimensions, func assembles image by stacking pieces.

    :params pieces:  Image pieces as an array.
    :params rows:    Number of rows in resulting image.
    :params columns: Number of columns in resulting image.
    """
    vertical_stack = []
    for i in range(rows):
        horizontal_stack = []
        for j in range(columns):
            horizontal_stack.append(pieces[i * columns + j])
        vertical_stack.append(np.hstack(horizontal_stack))
    return np.vstack(vertical_stack).astype(np.uint8)
