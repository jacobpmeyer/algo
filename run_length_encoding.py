def runLengthEncoding(string):
  count = 0
  current_char = string[0]
  running_string = ""

  for char in string:
    if char == current_char and count < 9:
      count += 1
    else:
      running_string += str(count) + current_char
      count = 1
      current_char = char

  running_string += str(count) + current_char

  return running_string
