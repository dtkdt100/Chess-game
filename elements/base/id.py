import elements.pieces.pawn
import elements.pieces.knight
import elements.pieces.rook
import elements.pieces.bishop
import elements.pieces.king
import elements.pieces.queen

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
    1 or 11: lambda i, j, team: elements.pieces.pawn.Pawn(i, j, team),
    2 or 12: lambda i, j, team: elements.pieces.knight.Knight(i, j, team),
    3 or 13: lambda i, j, team: elements.pieces.rook.Rook(i, j, team),
    4 or 14: lambda i, j, team: elements.pieces.bishop.Bishop(i, j, team),
    5 or 15: lambda i, j, team: elements.pieces.king.King(i, j, team),
    6 or 16: lambda i, j, team: elements.pieces.queen.Queen(i, j, team),

}
