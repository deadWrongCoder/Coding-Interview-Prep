string = "asdddsssa"
substrings = []

def max_length():
  max = 0
  for i in range(0, len(substrings)):
    if len(substrings[i]) > max:
      max = len(substrings[i])
  return max    


def generate_substring(start):
  repeated_letters = []
  for i in range(start, len(string)):
    if i == start:
      new_substring = ""
      new_substring += string[i]
      repeated_letters.append(string[i])
    else:
      if string[i] in repeated_letters:
        break
      else:
        new_substring += string[i]
        repeated_letters.append(string[i]) 
  substrings.append(new_substring)
    

for i in range(0, len(string)):
  generate_substring(i)
print(max_length())
  
