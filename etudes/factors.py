# compute all factors of a number
def factors(n):
  def factors(n):
    k = 1
    while k**2 < n:
      if n % k == 0:
        yield k
        yield n // k
      k += 1
    if k**2 == n:
      yield k
  return list(set(factors(n)))

if __name__ == '__main__':
  print(factors(20))
