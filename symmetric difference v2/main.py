def sym(set1, set2):
  sym = []
  for i in range(0, len(set1)):
    for j in range(0, len(set2)):
      if set1[i] == set2[j]:
        break
      elif j == len(set2) - 1 and set1[i] != set2[j]:
        sym.append(set1[i])
  for i in range(0, len(set2)):
    for j in range(0, len(set1)):
      if set2[i] == set1[j]:
        break
      elif j == len(set1) - 1 and set2[i] != set1[j]:
        sym.append(set2[i])      
  return sym

set1 = input("Set1: ").split(", ")
set2 = input("Set2: ").split(", ")  
print(sym(set1, set2))       
        
