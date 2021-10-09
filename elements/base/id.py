import elements.pieces.pawn
import elements.pieces.knight
import elements.pieces.rook
import elements.pieces.bishop
import elements.pieces.king
import elements.pieces.queen

ids = {
    1: "pawn",
    2: "knight",
    3: "rook",
    4: "bishop",
    5: "king",
    6: "queen",

}

starting_positions = {
    1: elements.pieces.pawn.get_starting_position(),
    2: elements.pieces.knight.get_starting_position(),
    3: elements.pieces.rook.get_starting_position(),
    4: elements.pieces.bishop.get_starting_position(),
    5: elements.pieces.king.get_starting_position(),
    6: elements.pieces.queen.get_starting_position(),

}

starting_positions_classes = {
    1: lambda i, j, team: elements.pieces.pawn.Pawn(i, j, team),
    2: lambda i, j, team: elements.pieces.knight.Knight(i, j, team),
    3: lambda i, j, team: elements.pieces.rook.Rook(i, j, team),
    4: lambda i, j, team: elements.pieces.bishop.Bishop(i, j, team),
    5: lambda i, j, team: elements.pieces.king.King(i, j, team),
    6: lambda i, j, team: elements.pieces.queen.Queen(i, j, team),

}
