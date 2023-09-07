"""Chess_piece = {}
max_length = 2
while len(Chess_piece) < max_length:
    piecename = input("Enter Piece name: ")
    if piecename not in Chess_piece and Chess_piece[piecename] == ['Rook', 'Queen', 'Bishop', 'Knight']:
        position = input("Enter Position: ")
        Chess_piece[piecename] = position
    else:
        print("Already exist please enter valid name:")
        pass


print(Chess_piece)"""
"""

Chess_piece = {}
Chess_piece['Rook'] = input("Enter position")
Chess_piece['Queen'] = input("Enter position")
Chess_piece['Bishop'] = input("Enter position")
Chess_piece['Knight'] = input("Enter position")

"""

Chess_piece = {}
max_length = 4
while len(Chess_piece) < max_length:
    name = input("Enter Piece name (Rook, Queen, Bishop, or Knight): ")
    if name not in Chess_piece and name in ['Rook', 'Queen', 'Bishop', 'Knight']:
        position = input("Enter Position in Alphanumeric eg( A4,H6): ")
       # print(Chess_piece.get(position))
       # if position not in Chess_piece or Chess_piece.get(position) is None:
        Chess_piece[name] = position
        #else:
         #   print("Two pieces cannot be in the same position")
          #  pass
    else:
        print("Invalid piece name. Please enter one of Rook, Queen, Bishop, or Knight")
        pass

print(Chess_piece)


