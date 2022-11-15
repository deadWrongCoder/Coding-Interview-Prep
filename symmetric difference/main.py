def sym_dif(set1, set2):
  intersection = [value for value in set1 if value in set2]
  combined_list = set1 + set2
  sym = [value for value in combined_list if value not in intersection]
  return sym

set1 = input("Set1: ").split(", ")
set2 = input("Set2: ").split(", ")
print(sym_dif(set1, set2))
