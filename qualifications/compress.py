import pprint,math
# A more clever approach of the problem
def computeScore(r, c, s, rows, cols):
  score = 0
  for x in range(r-s, r+s+1):
      for y in range(c-s, c+s+1):
        if x < rows and x >= 0 and y < cols and y >= 0:
          if not image[x][y]:
            score+=1
  return score

def paint_square(image, x, y, s, rows, cols):
  for x in range(x-s, x+s+1):
    for y in range(y-s, y+s+1):
      if x < rows and x >= 0 and y < cols and y >= 0:
        #print(str(x)+" "+str(y))
        image[x][y] = True

# Reading dimensions

dimensions = input().split(" ");
rows       = int(dimensions[0]);
cols       = int(dimensions[1]);

# Reading image description

image = []
imageref = []
instructions = []

for r in range(rows):
  
  lol = input()
  row = list(lol)
  row2 = list(lol)
  
  for c in range(cols):
    if row[c] == ".":
      row[c] = False
      row2[c] = False
    else:
      row[c] = True
      row2[c] = True

  image.append(row)
  imageref.append(row2)

# Compute cell score = number of false cells inside a 3*3 square around this cell

scores = [] # !! (rows-2) * (cols-2)
s = 1

for r in range(1, rows-1):

  current_row = []

  for c in range(1, cols-1):
    current_row.append(computeScore(r,c,s,rows,cols))

  scores.append(current_row)


# Display matrix
for x in range (1, rows-2):
  for y in range (1, cols-2):
    if scores[x-1][y-1] < math.ceil(0.5*9):
      # Write Instruction
      instructions.append("PAINTSQ "+str(x)+" "+str(y)+" 1")
      # Remove # on image
      paint_square(image,x,y,1,rows,cols)
      # Recompute score
      for r in range (max(1,x-s-1), min(rows-1,x+s+2)):
        c1 = max(1 , y - s - 1)
        c2 = min(cols-2 ,y + s + 1)
        scores[r-1][c1-1] = computeScore(r,c1,s,rows,cols)
        scores[r-1][c2-1] = computeScore(r,c2,s,rows,cols)

      for c in range (max(1,y-s-1), min(cols-1,y+s+2)):
        r1 = max(1,x - s)
        r2 = min(rows-2, x + s)
        scores[r1-1][c-1] = computeScore(r1,c,s,rows,cols)
        scores[r2-1][c-1] = computeScore(r2,c,s,rows,cols)


# Final cleans. Should fix errors in generated procedure.
for r in range(rows):
  for c in range(cols):
    if image[r][c] and not imageref[r][c]: # should not be paint. erase it.
      instructions.append("ERASECELL " + str(r) + " " + str(c))
    if not image[r][c] and imageref[r][c]: # should be paint. paint it.
      instructions.append("PAINTSQ " + str(r) + " " + str(c) + " 0")

print(len(instructions))

for i in range(len(instructions)):
  print(instructions[i])

print("")
