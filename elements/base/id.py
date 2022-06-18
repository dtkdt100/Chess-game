from elements.pieces.pawn import Pawn
from elements.pieces.knight import Knight
from elements.pieces.rook import Rook
from elements.pieces.bishop import Bishop
from elements.pieces.king import King
from elements.pieces.queen import Queen

import elements

ids = {
    1 or 11: "pawn",
    2 or 12: "knight",
    3 or 13: "rook",
    4 or 14: "bishop",
    5 or 15: "king",
    6 or 16: "queen",

}

starting_positions = {
    1 or 11: elements.pieces.pawn.get_starting_position(),
    2 or 12: elements.pieces.knight.get_starting_position(),
    3 or 13: elements.pieces.rook.get_starting_position(),
    4 or 14: elements.pieces.bishop.get_starting_position(),
    5 or 15: elements.pieces.king.get_starting_position(),
    6 or 16: elements.pieces.queen.get_starting_position(),

}

starting_positions_classes = {
    1: lambda i, j: Pawn(i, j, 0),
    2: lambda i, j: Knight(i, j, 0),
    3: lambda i, j: Rook(i, j, 0),
    4: lambda i, j: Bishop(i, j, 0),
    5: lambda i, j: King(i, j, 0),
    6: lambda i, j: Queen(i, j, 0),

    11: lambda i, j: Pawn(i, j, 1),
    12: lambda i, j: Knight(i, j, 1),
    13: lambda i, j: Rook(i, j, 1),
    14: lambda i, j: Bishop(i, j, 1),
    15: lambda i, j: King(i, j, 1),
    16: lambda i, j: Queen(i, j, 1),


}
