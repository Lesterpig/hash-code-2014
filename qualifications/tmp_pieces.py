def paint_square(image, x, y, s):
    for x in range(x-s, x+s+1):
      for y in range(y-s, y+s+1):
        image[x][y] = True

##################

# Final cleans. Should fix errors in generated procedure.
for r in range(rows):
  for c in range(cols):
    if image[r][c] and not imageref[r][c]: # should not be paint. erase it.
      instructions.append("ERASECELL " + str(r) + " " + str(c))
    if not image[r][c] and imageref[r][c]: # should be paint. paint it.
      instructions.append("PAINTSQ " + str(r) + " " + str(c) + " 0")