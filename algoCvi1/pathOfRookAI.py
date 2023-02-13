# Read the input and create the chessboard
chessboard = []
for i in range(8):
  line = input()
  chessboard.append(line)

# Find the starting and ending positions
start_row = -1
start_col = -1
end_row = -1
end_col = -1
for i in range(8):
  for j in range(8):
    if chessboard[i][j] == 'v':
      start_row = i
      start_col = j
    if chessboard[i][j] == 'c':
      end_row = i
      end_col = j

# Calculate the minimum number of moves
if start_row == -1 or end_row == -1:
  # One or both of the positions were not found
  print(-1)
else:
  num_moves = 0
  if start_row != end_row:
    # Check for occupied squares in the path
    for i in range(min(start_row, end_row)+1, max(start_row, end_row)):
      if chessboard[i][start_col] == 'x':
        # Cannot move to destination
        print(-1)
        break
    else:
      num_moves += 1
  if start_col != end_col:
    # Check for occupied squares in the path
    for i in range(min(start_col, end_col)+1, max(start_col, end_col)):
      if chessboard[start_row][i] == 'x':
        # Cannot move to destination
        print(-1)
        break
    else:
      num_moves += 1
  print(num_moves)