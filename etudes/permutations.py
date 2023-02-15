from sys import argv

# compute all permutations of a string in alphabetic order
def permutations(s):
  if len(s) == 0:
    return []
  elif len(s) == 1:
    return [s]
  else:
    head = s[0]
    tail_perms = permutations(s[1:])

    perms = []
    for tail_perm in tail_perms:
      for i in range(len(tail_perm) + 1):
        appendant = tail_perm[:i] + head + tail_perm[i:]
        perms.append(appendant)
    return perms

if __name__ == "__main__":
  s = argv[1] if len(argv) > 1 else "abcd"
  print(permutations(s))
