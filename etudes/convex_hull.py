from matplotlib import pyplot as plt
from collections import namedtuple
from random import randint as rand

Point = namedtuple('Point', 'x y')

def convex_hull(points):
  def orientation(origin, p1, p2):
    dx = lambda p: p.x - origin.x
    dy = lambda p: p.y - origin.y
    return dx(p2) * dy(p1) - dx(p1) * dy(p2)

  point = start = min(points, key=lambda p: p.x)
  hull = [start]
  far_point = None

  while far_point is not start:
    far_point = p1 = next(filter(lambda p: p is not point, points), None)

    candidates = (p for p in points if p is not point and p is not p1)
    candidates = filter(lambda p: orientation(point, far_point, p) > 0, points)

    for p in candidates:
      far_point = p
    hull.append(point := far_point)

  return hull

def plot(points, hull):
  x = [p.x for p in points]
  y = [p.y for p in points]
  plt.plot(x, y, marker='D', linestyle='None')

  x = [p.x for p in hull]
  y = [p.y for p in hull]
  plt.plot(x, y)

  plt.title('Convex Hull')
  plt.show()

def main():
  points = [Point(rand(-100, 100), rand(-100, 100)) for _ in range(50)]
  hull = convex_hull(points)
  plot(points, hull)

main()
