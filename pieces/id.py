import pieces.pawn
import pieces.knight
import pieces.rook
import pieces.bishop
import pieces.king
import pieces.queen

ids = {
    1: "pawn",
    2: "knight",
    3: "rook",
    4: "bishop",
    5: "king",
    6: "queen",

}

starting_positions = {
    1: pieces.pawn.get_starting_position(),
    2: pieces.knight.get_starting_position(),
    3: pieces.rook.get_starting_position(),
    4: pieces.bishop.get_starting_position(),
    5: pieces.king.get_starting_position(),
    6: pieces.queen.get_starting_position(),

}

starting_positions_classes = {
    1: lambda i, j, team: pieces.pawn.Pawn(i, j, team),
    2: lambda i, j, team: pieces.knight.Knight(i, j, team),
    3: lambda i, j, team: pieces.rook.Rook(i, j, team),
    4: lambda i, j, team: pieces.bishop.Bishop(i, j, team),
    5: lambda i, j, team: pieces.king.King(i, j, team),
    6: lambda i, j, team: pieces.queen.Queen(i, j, team),

}
