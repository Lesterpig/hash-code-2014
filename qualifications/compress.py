# A more clever approach of the problem

# Reading dimensions

dimensions = input().split(" ");
rows       = int(dimensions[0]);
cols       = int(dimensions[1]);

# Reading image description

image = []
instructions = []

for r in range(rows):
  
  row = list(input())
  
  for c in range(cols):
    if row[c] == ".":
      row[c] = False
    else:
      row[c] = True

  image.append(row)

# Compute cell score = number of false cells inside a 3*3 square around this cell

scores = [] # !! (rows-2) * (cols-2)
s = 1

for r in range(1, rows-1):

  current_row = []

  for c in range(1, cols-1):

    score = 0

    for x in range(r-s, r+s+1):
      for y in range(c-s, c+s+1):
        if not image[x][y]:
          score+=1

    current_row.append(score)

  row.append(current_row)