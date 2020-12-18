from __future__ import print_function

inp = """2 + 4 * 3
2 * 3 + (4 * 5)
5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"""

inp = """6 * 7 * 8 * 9 * ((8 * 3 * 9) * 7 + 2 + 4 * 8 + 2) + 5
3 * 2 * (5 + (8 + 2 * 2 * 8 + 8) * 8)
5 + 7 * 8 * 2
(8 + 5 * 9 + (8 * 9 + 7 + 8)) * 4 * 3 * (8 * 9) * 3
(7 + 2 + 2 + 5 * 6 * 3) * 8 + 5 * 9
(9 + (2 * 9 + 6 + 5 + 2 + 7) + 4) + 5 + (9 + (7 + 8 * 6 + 3 * 8) * (5 + 3 * 2 * 9) + 7 * (4 * 5 + 6 + 9)) + 9 * 7 * 4
5 * (8 + 2 + 9 * 6)
(4 * 8 + 8 + 5 * (5 * 3 + 7 * 8 + 8 + 2) + 8) * 4 * 2 * 7 + 3 + 8
6 + 9 * (6 + 7 + (3 + 9))
(6 * 7) + 2
9 + (4 * (4 * 2 + 6 + 9) + 2 + 4 * 5 + 9)
2 * (8 + 6 * 2 * 6 + 2 * (6 + 5 + 9 + 6)) * 2 * 6
(5 * 7 * 4) * 3 * (3 * 6)
(2 + 4 + 5 + 2) + 2 * 4 * ((6 + 2 + 3 + 4 + 9 + 8) * 5 + 6) * ((3 + 3 + 5 + 2) * 8 * 5 + 8)
9 + 8 * (9 + 5 * (2 + 4 * 3 * 2 * 9) * 9) * (5 + 2 + 6 + 3 * 4)
(4 * 5 + 4) * 7 * (2 * 5 + 4)
6 + 7 + (2 + (8 + 8) * 6 + 3)
(8 * (9 * 6 + 2 * 2 * 3) * (2 + 2 * 9 * 6) + 9) * 6 + 2
2 + ((2 * 6 + 7) + 3 + 3) * 5 + 9 + 2
5 + 3 + (4 * 3 + 5 * 5 * (8 + 6) * 5) * 9 * 7
6 * 7 + ((2 * 6 + 4 * 2 + 3) + 7 * 5 + 5)
(9 + (2 + 7 + 2 * 2) + 5 * 9 * 6) * ((2 * 6 + 6) * 3 + 5 + (2 * 2)) * 4
6 * ((3 * 4 * 9) * 9 * (4 + 8) + 9 + 3) + (3 * (7 * 9) * 9)
6 * 4 * 4 * (5 * 2 + 4) * 2
4 * 4 * 8 * 3 + 5 * (2 + (9 + 8 * 7 + 6 + 3) * 8 + (6 * 7 * 9) + 9)
7 * ((5 + 2) + 5 * 6 * (4 * 8 * 3 * 9 * 3) * 2 * 6) * ((5 + 7 + 9 * 2 * 4 * 6) + 4 + 3) * (9 + 4 + 7 + 4 * 5 * 9)
4 * 8 * 4 + 6 * (5 * 7) * (6 * 7 * 3 + 2 + (7 + 6 * 4))
(4 + 8 + 4) + 7 * (9 + 8 + 8 * 9)
2 * 7 + 3 * 6 + ((5 + 6 * 9) + (2 + 4 * 6 + 9 * 3 * 9) * 2 + 6 + 2 + 8)
((3 + 4 * 3) + 4 * 9 + 9 * 7) + 7
(4 * 7 + 3 * 9) * 3 + 4 * 6 + (9 + 6 * 9 * (6 + 6 + 5 * 4 * 5) + 2)
2 * (3 + 9 + 9 * 7 * 2) * 2
7 + 4 + ((8 + 2 + 9) + (9 + 4 * 7) + 2 + 8) + 7 * ((8 * 4 + 8 + 6) * (6 * 6 + 3 * 2 * 3 + 8))
4 + ((8 * 6) + 5 + 9 + 9 * 4 * (3 * 9 * 7)) * 6 + 4
8 + 6 + 7 * ((3 * 9 * 2 * 3 + 9 + 7) * (7 * 4 * 8 + 9 * 9))
7 * ((2 + 3 * 7) + (2 + 6 * 9 + 6 + 7 + 4) * 9)
(2 + 8 * 6 * 6) + 5 + 6 + 9 + 2
(5 + (2 + 9 * 7 + 7) + 3 * 2) * 5 + (2 * 7 + 6)
6 * 8 * 4 * 6 + (9 + 8 + 8 * 6 * (8 + 4 * 4 * 3) + 4) * 8
7 + 3 + 4 * (6 * 4) * 6 * 8
2 * 8 + 2 + 6 * (8 + (3 + 8 + 3 + 9 + 6) * 9) + 2
((5 + 2) + 9 * 6 * (2 + 5) + 8 * 2) * 7 + 4 + 9 * 8
(3 + 5 + 2) + 3 + 8 + 6 * 6 * 4
(8 + 9 + 4 + (4 + 5 + 8) + 7 * 6) * 7 * 7 + 3 + 3 * 5
(8 * 6 * 8 + 6 + 6) + ((5 + 8 + 5 + 6) + 8)
3 * ((7 * 7) * 2 + 8 + 8) * (6 + 3 + (4 * 5 * 6 * 6)) * 8
5 + 9 + 3 + 7 + 9 * (5 + 9 * 7 * (9 + 7 * 9 * 7) * 9 * 8)
3 * (2 * 9 + (8 + 6 * 5) + 9)
4 + 5 + 9 * 8 * (7 * (5 * 2) * (3 + 7 * 4 + 6 + 8) + 3)
9 * ((6 * 8 * 3 * 8 * 6) + (3 + 5) + 4)
(3 + (2 * 6 * 7 * 9 * 2 * 9) * (4 * 8 + 4 + 9) + (4 * 4 * 5)) * 9 * ((3 * 3 + 7 + 5) * 7 + 3 * (4 + 7 * 8 + 8)) * 9
((4 * 9 * 6 * 4 * 9 + 6) * 7) + 4
8 * 3 * 7 * ((8 + 3 + 9 * 7 + 3) + 5 * 9)
(8 + 4 + 6 * (7 * 2) + 8 * 7) * 9 * 5
2 * 8 + (8 + (4 * 8 + 6) + 7) * 4
6 * 9 * 6 * 5 + 9 * (3 * 3 * 3 + (7 + 7 + 6 + 2 + 7) * 5)
(3 * 4 * 5 + (9 * 7 * 3 * 2 * 9) * 4) + 6 + (4 + 9 + 2) * 8
9 + 5 * 5 * (9 + 7 * 4 * (9 * 9 + 8)) * 6
8 + ((4 + 5) * 2 + (5 + 5) * 7 + 8 * 5)
(6 + 8) * (2 * (4 + 6 * 4 * 5 * 9)) * 4 + 5 * 4
5 * 4 * (7 + 4 + 9 * (7 * 6 + 2 * 3 + 7 * 7) + (2 * 8 + 7 + 3 * 2) * 8) * 6 * 5
7 * 2 * (9 * 4 * 4) + (5 * 6 * 2 + 6 + 9)
(7 + 2 * 4 * 5 * 4 * 3) + 5 * (3 * 6 * 6 + 8)
5 * (6 * 4) + 6 * 2 * 6 * ((6 * 3) * 3 + (7 * 8 * 5 * 5 * 7) * 7 * 9)
9 * 7 * 9 + 4 * (2 * 3 + 2 + 8 + 2 + (3 + 8 * 9)) * 6
(3 + 8 * 2 * (8 + 9 * 8 + 7) * 9 + 5) + ((5 * 5 * 3) * 9 + 9 * 3 * 6) + 4 + 8 + 2
5 + 8 + 9 * 6
9 * (7 + 5 + 9 * 8 + 5 + 9) + 5 + (3 + 9 * 3 + 6 + 6 + 9) * 8 * 8
8 * (4 + (9 * 6 * 5 + 2 + 3) * (2 + 3 + 4 * 5 * 8) * 3) + 8 + (5 * (8 + 5 * 3 + 4 + 2 + 2) * 6 + 9 * (5 + 3 * 8 + 5) + 9) + 7
3 * 6 + (3 * 2 + 3 * 4) + 3
((5 * 6 + 9 * 6) + 8 * 9 * 8 + 8) + ((3 + 9) * 5 + 6 * 6 + 9) + (9 * 2 + (6 * 9 * 4 * 7 + 9 * 4) + 7 + 2) * 7
((9 + 9 + 9) + 7 + 2) * 8 + 2 * 7 + 4 * 7
3 * 4 + (7 + (7 * 7 * 2 + 2 * 2 + 2)) + 9
(3 + (5 * 2 + 5 * 8) + (5 * 5 + 7) * 6) * 8 * (2 * 7 * 3 + 2 + 9)
4 * (8 + (6 * 9 * 7) + 3 * 8 * 8 * 3) * (6 * 8 * 3) + 9 * 3
6 + 5 + 3 * 3
8 * 4 + (9 + 6 + 9 * (3 * 2 + 8 * 2 + 2) + 7)
2 + 8 * ((4 * 8 * 8 * 4 * 8 * 7) + (3 + 3 + 6 + 2 + 6) * 8 * 9 * 2 * (8 * 3)) + 3 * 9
((7 * 2 + 5 + 6 * 3 * 9) * 4) * 8 * 2 + (5 + (3 * 2 + 8)) * 2
5 + (4 * (4 * 5 + 8 + 7) + 7 + 4) + (6 + 2 + (8 * 7 * 8)) * 4 * 5 * 6
(6 + 4 + (3 * 6 * 9 + 3) * 5 * 2) + (5 * 3 * (9 + 3 * 3) + (5 + 3 + 6) + (2 + 8 + 5) * 2) + 4 * 7
(6 * 2 * 7 * 7 + 4 * 2) + 4 + 2
8 * 3 * 6 + 8 + ((3 + 4) * 3 * 2 * 2 + 8 * (2 * 7 + 2 * 7 + 7 + 6)) * (8 * 8 + 4 * 4 * 3)
(5 + 5 + (9 * 9 * 5) * 4 + 4 + 4) * 7 * 3 * 2
8 + (7 + 3 * 2 * 3) + 8 + 7
3 + 7 * (4 + 5 + 9 + 4) + 5 * (8 + 8 + 5)
((2 + 4 + 2 * 2) * 6 * 2 * 8 * 6 * 9) * 6
2 * (2 * (6 + 8) + 5 * 7 * (4 * 2)) * 9
4 + (4 + 3 * 8) * 3 + (3 * 4 * 3 * (4 * 5 + 7) + 7) * 2
7 * ((7 + 5 + 9 + 9 * 4 + 3) * 9 * 7 + 5 * 8) + 9
(4 + 3 * 6 + 2) * 4 * 4 + ((2 + 4 * 3 * 8 + 6 + 3) + 5 + 5) * 6 * 9
5 * 6
5 + 7 + 7 + ((3 * 3 * 3 * 2 + 3) * 3 + 2 + 4 * 3)
2 * (4 * 4 * 8 * 3 + 2) + 2 * 3 + 2 * ((9 * 7 * 3 * 6 + 7) * 4)
(8 + 9 * 8 * 8 * 7) * 9 + (2 + (9 + 9) * 2 * 9 + 7 * (4 * 9 + 9 + 6 * 8 + 2)) * 9
7 + 3 + 3 * 9 + 8 * (5 + 7 * 3 * (7 + 8 * 3 + 6 + 3) * 2 + 5)
(3 + (6 * 9) * 3) + 2 + 7 + 4
(6 * 8 * 7) * (9 + 4 * 4) * 3 * 2 * ((3 + 3 * 6 + 7 * 6) * (3 + 9 + 5 * 9 * 8) + (7 + 7 * 9 + 2 * 4) + 2 + 4) + 9
6 + (7 * 7 * 5 + 3 + (8 * 7 * 7) * 4) * 4
4 + 7
(7 * (6 * 3 * 5) * 4 * 5 * 7 + 3) + 5 + 6 * 8 * 4 + 5
2 + 2 * 5 + (8 * 7 + 6 + 7 * 4 + 9)
(3 + 6) * (2 * (6 * 8 + 6 * 3) * (3 + 9 * 2) * 3) + 8
(7 * 8 * (5 + 4 + 2 * 8) + 4 * 5) + 5
(2 * 7 * 4 + 6 * (8 * 9 * 2 * 8 + 7) + 5) * (9 * 7 * (4 + 5) * 3 * 2 + 4) * ((6 * 5) + 9 * 4)
(6 + 6 * 9 + 6 * 7) * (5 + 9 * (8 + 7 * 4 + 8 * 4 + 2) + (7 + 2 + 8 * 5)) + 3 + (4 * 8 + (7 + 4)) * (2 * (6 + 2 * 4 * 2) * 5 * 5 + 9 + (6 + 8 * 6 * 4 + 9))
9 + (3 + 8 + (7 + 7 * 3 * 4 * 5))
9 + 9 * (4 + 9 + 9 * 5) * (8 * (4 + 9 + 3 * 3 + 6))
8 * 3 + 7 * (7 * (4 + 5))
2 + (4 + 5 + 2 * 4 * (3 * 6 + 3) * 7)
(5 + (2 * 6 + 9 * 2 + 5) + 8 * 4) + (2 * 5 * 7 + 2 + (5 * 6 * 5 + 4) * 6) * ((4 + 4 + 7 + 9 * 9) * 6 + 6 * 6 * 8 * (7 + 2 * 6)) + 7 * 8
3 * 5 * (7 * 4 + 8 * 4 * 6 * 6)
(2 + 8 + (4 + 8 * 3 + 6) + 5 * 3) + 7 * 6
7 + (9 * (8 * 4 + 2 * 8 + 9 + 4))
(5 * 8 + (8 * 6 + 5 + 6 * 9)) * (5 * (3 * 6 + 5 * 6 + 7 + 8) + 5) + 2 * (6 + 6 * 6) + 5
4 * 6
((6 * 4 * 5 * 4) + (8 * 3 + 2 * 4 * 9 * 5) * 2 + 4 + 4 + 9) + 6 + 6
8 * ((4 * 5) * 6 + 9) + (2 + 2 * 4 + 3) * 3 + 4
2 + 5 * 4 * 6 * (3 * (2 * 9 * 9 + 2 + 2))
(3 * 4 * 3 + 7 * 9) * 3 * (2 + 6 + 6 + 2)
7 + (7 * 5 * 7 * (2 + 9 * 5 * 5 + 3))
5 + 4 * 7 + ((6 + 7 * 9 + 8 + 2) + 5 * 3 * 8)
5 + (2 + (9 * 8 * 6 + 4 + 6) * (4 * 5 * 6 * 4 + 6) * (9 * 9 + 9 + 5) + 3)
((9 + 3 * 7 * 5) * 9 * 4 + 9) * 5
(6 + (6 * 9 * 8 + 4 + 7) * (9 + 2 + 3) + 4 + 6) * 4 + 6 * 5
6 * (2 * 4 + 7 * 3) * (7 + 3 + 7 + 6 * 7 + 2) + 2 + 6 * 3
5 * (6 + 4 * 2 * 6 * (3 * 9 + 2) * 8) * 9 * 8
7 + ((8 + 2 + 2 + 9) * 5) * 2 + 6 + 7 + 4
(5 * 6 + (2 + 4 * 3 * 5) + 3 * (6 + 3 + 2 * 7 * 3 + 7) * 8) + 4 * 9 * 2 + 5 * 2
5 * ((7 * 2 + 2 * 3 + 3) * 7 * 3 + 9 + 9)
3 * 9 * ((7 + 3 * 5 + 9 + 5 * 2) + (3 * 4) * 9 * (7 * 7 + 7)) * 7 + 4
3 * 4 + (8 * 6)
(3 + 4 * 4 * 8 * 6) * (9 + (2 * 8 * 5 * 8 + 7 * 6) + (3 + 6 * 2 + 5) + 2 + 4 * 6) + 5 + (9 + (7 * 4) * 2 * (3 + 9 * 3 * 3 + 6) * 9 + 3)
3 + 8 + 8 * 2 * 5
(7 + 4) + 8 * 5 * 3 * 6 * 4
3 * 3 * 9 + (6 * 7 + 3 + (5 + 7) + 5 + 9) + (9 + (8 + 2 * 9 + 9) * 9 + (5 * 9) + 2)
3 + ((3 + 9 + 8 + 3 * 9) + 3 + (5 + 9 + 3 * 7) * 9) + 8 + 6
9 + 2 + 3 * (8 * 6 * 8 + 9 * (9 + 7 + 2 + 9))
(5 * (9 * 4 + 3 + 8 * 3) + (4 + 5 * 7 + 6 * 9) * 9 * 6) * 7
((6 * 7 * 5 * 2) * 6 + (6 * 9 * 9 + 7 * 3) * (2 * 7) * (8 * 7 + 7 * 8 + 2) + 4) + 5 + ((8 + 5 + 7 * 2 * 2) + 9 + (4 + 5 * 4 * 6 + 4 * 7) * 4 * 5 * 3) * 7 + 9
8 * 2
5 * 2 * (8 * 5) * (6 * 6 * (8 + 6) + 7 + 5)
9 * 9 * (2 + 4 * 6 * 2) + 3 + 7 * ((7 * 5 * 8 * 8 * 4) + 7 * (6 + 9 + 4 + 5) * 3)
4 * 3 * (3 * 4 * 5 * 2) + 3 * (7 + 7 * 4 * 8 + 3 + (3 + 5 + 7 + 5 * 5)) + 5
7 + 8 + 2 + 9 + (2 + 6) * (3 + 2)
3 * (4 + 3) + 6
8 * 4 * (9 + 7 * 2) * 3 + ((5 * 5 * 8 + 5) + 5)
2 * 6 + 5 * 4 + 9 + (8 * (8 + 9 + 9) * 5 * (9 * 8 + 3))
((9 + 9) + 4 + 2 + 9 + 8 * 7) + 4
2 + (8 + (8 + 6) + (2 * 4 + 8 + 7) + 7 * (5 * 5)) + 7 * 3 + (2 + 8)
9 + 6 * 3 + 7 + 4 + 3
6 + 7 * 2
9 * 3 * (2 + 6 * (7 + 3) + (9 + 9 * 2 * 9 * 2 + 3)) + 6
(8 * 8 + (6 + 3 + 4 * 9 + 8 * 4) + 7 * (8 * 2 * 3) * 6) * 5 + 2 * 8
(8 * 4) + 8 + 2
8 + 2 * (8 * 6 * (4 * 6 + 9 * 7 + 8) * 6)
(4 + (5 * 4 + 6 + 7 + 4 * 8) * 9 * 7) * 6 + (3 + 4 * 9 * 3) * 9
8 + 9 * (5 * 2 + 7 + 7 * 2) * 8 + 8
5 + 9 * 2 + 8 + 2 + (6 * 2 * 8 * 5)
4 + 3 + ((9 * 6 * 6 * 5 * 7) + 7 + 4 + 9 + 9) + 2
9 + 3 * 2 + 8 * 6
4 * (3 * 3 + 4)
4 + 4 * ((2 + 2) + 6 + 5)
7 * 2 * 4 * 6 + 9
(9 + 5) * (3 + 5 * 2) * 2 + 7
(6 * 9 + 7 + 2) + 8 * 4 * 4 + (8 * (3 + 8 + 7 + 4 * 5) * (2 * 6) * 6) * 7
3 + ((3 * 6 * 5 * 6 * 4 + 8) * 6 * (2 + 9 + 3) + (4 + 5 * 2 + 9 + 4 + 3) * (4 * 4 + 7 * 3) + 4)
(8 * 4 * 5 * 5) + (5 + 8 * 6) * 7 + 8 + 5
(6 * 7 * 6 + 8 * 9 * 8) * 4 * 8 * 8 * 3
3 * 9 * (6 + 5 + 3 * (4 * 6))
5 * 2 * 4 + (5 + 7 + 8 * 6) + (2 + 3)
((9 * 9 * 4 + 7 * 8 + 7) + 9 + (9 + 3 * 9 + 2)) + 6 * 4 + (2 + 3 + (7 * 3)) + (3 + 6 + 9 + 4) * 2
(3 + 2 * 3 * (5 * 9 + 2 * 7 * 9 * 7) + 7) * 7 + (2 * 8 + 2 * 2) * 3 + 5 * 3
5 * 6 * 6 * (7 * 3 + 7 + 5 * 6 * 6) + (9 * 8 + 3 + 8 + 4 * 5)
(9 + 7 * 8 * 4) * 6
(6 * 5 + 5 * 4) + (4 * 4 * 5 * (7 * 2) * 6 + 8) + 6 * 7
(8 + 7 + 9) * 3 + 2 * 6 * 7
(3 * 6 + 4 + 9 + 5 + 9) + 4 + ((5 + 3) + 6 + 5 * 7 + 6)
5 * 8 * 7 + 8 + ((8 * 9 * 9 * 6 * 2 * 7) + 8 + (2 + 7 * 8 + 6 + 7 * 2) * 8 + (5 + 2)) * 3
((7 + 5 * 4 * 2 * 4 * 7) + 6 + 2 * 8 * 9) * (6 * 3 + 4 + 2 + 3) + 4 + 3 + 4 * 2
9 + 5 * 6 + 8 * 6 * 3
5 * 9 + (9 + (4 + 3 * 4 + 7) + (5 + 6) * 7) * 3 + (5 * 4 * 7)
((5 + 7 * 7 + 2 * 9) * 2 + 8) * (4 * (7 * 5 * 7 + 2 * 8) * (3 * 9 * 9 + 8) * 2 * 9 * 7) * 9
3 * 6 + 7 + 5 + ((7 * 2 + 7) * 9 * 7 * 2) + (3 * 4 + 6)
((9 + 7 * 5 * 7 + 7) * 8 * (6 + 7 + 5 + 9 + 2)) + 9 * (9 + (8 + 4 + 2) + 8 * 7 + 7 * 6) * 7 * 5
(8 + 7 + 6 * (6 * 4 + 2 * 4 * 6 + 6)) * 8 * 5 * (8 + 3)
5 + 2 + 9 + (6 * 7 + 8) * 9 * 7
6 * 3 + 9 * 4 + 3
3 + 8 * 8 + (6 + 8 * 4 * 5 * 6) * 6
7 * (9 * 9 * 5 * 4 * 7 * 9) * 8 * ((4 * 4) * 2 + 7 + 5 * 3 * 8) + 4
5 + (2 * (9 + 4 * 3 + 6 * 4) * 5 + 7 + 2)
9 * (5 * (3 * 3 + 6 + 7) * (2 + 4 + 8) + 8) + 5 * 8
6 * 8 * (8 + 6) * 6 + 8
5 + 6 + 9
(2 * (7 * 9 + 7 + 3 + 9)) * 7 + (5 + 8 * 9 * 7 * (5 + 6)) + 5
(9 + 3 + 4 + 4) + (7 + 5) * 3 + 5 + 4
4 * 7 + 3
4 * 4 + 3 + 6 + 7
3 * 3 + 8 * (2 + 9 * 8 + 9) * 8 * 7
(8 + 5 + 2 + 5 * 3 * 8) + 5
2 * 7 * 4 * (4 + 8 + 5)
(3 + 5 * 4 + 8 * (9 * 8) * 7) + ((9 + 3 * 2) + (3 + 6 * 5 + 8 * 2 + 9) + 6 * 6) + 8 + 5 * 8 + 5
(6 * (5 * 6 * 3 + 8)) + 4 + 4 * 4 + 6 * (6 * 3 + 8 + 4)
3 + 9 * 2 + 8 + (5 * (5 * 2)) * 9
2 * (3 * 2 + (8 * 6 * 3 * 7 * 5 + 6) * 3 * 5)
(8 + 9) * 2 * (3 + 9 * 5 * 9 + 7) * 9
2 * 4 * (9 * 4 + 8 + 7 * 3)
5 * (7 * 2 * 8 * 5 * 4 * 3) * 9
(7 * 4 + 3 + 8) * (6 + 5 + (3 + 2 * 5 * 6) + (8 * 9 * 5 * 6) * 3) * 3
(7 * (2 + 6 * 7)) + 8 * 9 + 5
6 + (2 + 2 * 3 * 6 + 4) + 6 + 6 * (4 * 5 + (8 * 8 * 2 * 6 + 7 + 9) * (5 * 2 * 4 * 7 * 7 + 8) + 9)
(2 + (5 * 8 + 8 + 9) * 3 * 2 + 9 * 8) * 5 * 3
(6 * 2 * (8 * 6 * 4 * 3) + 7 + 7 + 6) * 5 + 6 + 9 + 2
(2 * 8 + (9 * 4 * 5 + 6 * 7 + 8) * 2 + (3 * 7 * 4 + 4 + 9)) + 5 + 3 * 8 * (7 * 2 * (3 * 9)) * 4
8 + (4 + 2 + 9 * 4 * (8 * 8 + 6 + 3 * 6 * 6))
4 + (4 + (5 * 4 * 7) * (4 * 9) + 8 + (3 * 9 * 2 + 7 * 8) * 3) * 8 + (9 + 3) + 6 + (9 * 5 + 5 + 4)
(2 + 6) + 5 * (9 * 5 + 7 + 2 + 7 + 8)
7 + 5 * 3 + 7 + (8 * 5 + (5 * 7 * 4) * 5 * 8 + (6 + 2 + 5)) + 8
5 + ((6 + 7 + 9 * 7 * 8) * (9 * 5 + 4) * 5 * 9 + (4 + 5 * 2 + 4 * 5 * 8))
5 * (9 * 7 + 9) * 7 + 3 + 2
8 * (2 * 5 + (2 * 9 + 8 + 6) + 3) * 4 + 7 + 6
4 + 2 + (4 + 4) * ((2 * 6 * 2 * 2) * 8 * 3 + 9)
((3 + 2 * 5 + 6 * 8) + 3 * 9 + 2 + 5) + 9 + 2 + 4 * (2 * 9 * (9 + 9 * 4 + 7 * 6) + 5 * 8 + (8 * 8 + 5)) + (3 * 3 + 6 + 5 + 4 + 6)
2 * 6 * 4 + (4 * (8 * 3) * 8 + 8 + 8) + 4
4 + (4 * (6 * 8 + 6))
(5 * 8 * (5 + 8 * 7 + 5 * 7) * 5) + (6 + (4 * 7) * 7 * 7)
4 * 5 * 9 + ((3 * 2 * 8 + 8 + 6 + 4) + (4 * 5 * 4)) * 3 * 5
9 * 9 * (7 + 6 * 9) * (9 + (5 * 8 * 5 + 2) + 8 + 4)
((9 * 2 * 7 * 6) + 6 + (5 * 5)) + 8 * 9 * ((5 + 4 + 8) * 5)
7 * 4 * 7 + 9 * ((8 * 7 * 6 * 4 + 3) * 5 + (8 + 9) * 9 + 4 * 8)
9 + 6 * 9 * ((3 + 5 * 9) * 5) * 6
(7 + 5 + 2 + (4 + 5 + 7 * 7 * 4)) * 3 + (2 + 7 * (9 + 9 * 3 + 7 * 2) * 6 * 7 * (3 + 3)) * ((7 + 5) * 4 + 3 * (4 * 6 + 5 * 2 + 8 * 5) + 9 + 8)
6 * 4 * 6 * (8 * 8 * 3 + 3) * 8
(3 + (7 + 2 * 4 + 4 * 8) * (5 + 7 * 3) * 5 * 4 * (2 + 3 * 9)) + 8 + 8
(7 + 5 * (3 + 5 * 5 + 5 * 4)) + 4 + 3
9 + 9 + (9 * 7 + 3) + (7 * 8 * 6 + 5) + 8 * 4
8 * 8 * 6 * 9 + 9 * 4
4 * 3 + (6 * 7 * 7 * 3 * (3 + 6 * 5 * 5 * 6))
2 + 5 + 2 * 4 * (2 + 9)
(6 + 6) * 8 + (9 + 3 + 8 * 4)
(9 + 4 * 3) + 5
7 + 8 * (3 * 6 * 2 + 3 * 9) + 9 * (9 * 3 + 8 * 6 * 5 * 3) * 8
((9 * 8 * 5 + 6 + 2 * 4) + 3 + 5 * 2) + 5 * 4 + 9 * 9 + 7
3 + 6 + 3 + (9 + 7 + 7 * (9 * 2 + 7) * 6 + 2)
(3 * 2 + 9 + 8 * 8) * 4 + 5 + 8 + (3 * 6 + 8 * 3 * (2 * 9)) * 5
8 * ((2 + 9 + 3 + 4 * 7) * (2 + 3 * 9)) * 3
9 * 6 * (3 * 7 * 5) * 5 + 4 * 7
(5 + 8 + 3 + 2 * 9) + 4 * 9 * 6
6 * (7 + 5) * (8 + (6 * 3 + 3)) * 4 * (5 * 2 * 7 + 9 + (2 * 9 + 2 + 6 + 5 * 7))
((7 * 8) + (2 + 6 * 9 + 5 * 4) * (6 + 8 * 9 + 2 + 2) * (3 * 3)) + 3 + (7 + 6 * 4 + 4) * 6 + 4
3 + 9 * (6 * (5 * 5 + 4 + 7 + 7 * 8) + 7 * 3) + 7
5 + (4 + (4 + 4 * 7) + 5) + (7 * 4 * 6) * 8
7 + (4 + 6 + (3 * 2 * 9 + 6 * 5) * 8 * 7 * 5) + 2
5 * ((6 + 6) * 6 + 6 * 3 * 3) + (7 * 2) + (4 + (9 + 9) + (5 + 8 * 6 * 9) + 6) + 7 + 5
(9 * 3 + 7) + 8 * 3 + 2
3 + 9 * (4 + 5 + 4 + 4)
(8 * 5 * 2 + 9 * 4 * (6 + 9 + 3 + 9 * 3 + 5)) + 5 * 3 * 2
4 * (2 * 6 + 9) * 2 * (2 + 6 * (7 + 6 * 9 * 2 * 5) + (3 + 8 * 6)) * 3 * 7
6 + 7
7 + 6 * (2 * 8 + 5 * 3) * (3 * 2 + 2 * 7)
5 + 5 * 5 + 9 * 9 * (2 * 9)
7 * 5 + ((8 * 9 * 3 * 3 + 6) * 5) + 4
6 + (6 + 4 + 3) * 4 + 8 + 8 + 8
(5 * (8 + 2 + 9 * 7 + 6 + 6) + 7 * 4 + (2 * 6 * 3 + 5 * 6) + 7) + (2 * 3 + (5 * 3 * 5 * 5) + 9 * 6 + 7) * 7 + 8
(3 * 3 + 9 + 2 * 5 * 6) + (9 + 3 + 2) * 7 * 6 + 3
(2 + 4 + 8 * 7) + 2 + 5 * 6 * ((4 * 3 * 7 * 5 * 7 * 2) + 4)
9 * (8 + 5)
7 + 6 + (6 * 6 + (7 + 8 * 5) * 9) * 4 + ((3 + 4 + 6 * 7) + 4 + 7 * 3 * 5)
2 * (8 + 7 + 4 + 3 * 8) * 7 + 4 * 5
9 + 9 * (8 + 9 * (7 * 3 * 7) * 3 + 3) + 9
8 + ((4 + 6 * 5 * 6 + 7) + 7 + 7 * 8) * 6
(3 * (9 * 3 * 6 + 5) * 7 * 9 + 9) * 5 * 2
(2 + 4 + 5 * 7 + 6) * (7 + 2 * 6) + 6 * 3 + 3 + 6
(4 + 7 * 2 + 6 + 2) + 3 * 5 * 8 + 7
2 * 7 * 2 + 6
8 + (5 * 9 * (6 * 9 + 4) + 5 + 8) * ((8 * 9 + 4 + 8 + 4) + (6 * 2) + (7 * 9 + 2 * 3 + 4) + 7) + 8 + 8 * (9 + 2 * 5 + 9)
4 * (7 + (9 * 2)) * 9 + 9 + (9 + 3 + 2 + 2 * 8 * 9) + (3 * 4 * (9 * 2 + 5 * 6))
9 * (3 * 8 * 6 * 3 + 7 + 2) + 6 * (5 + 8) * 2 * 3
9 * 2 + 6 * (7 + 3)
4 + (8 * (8 + 2 + 8 * 6 * 9) + 2 + 4 * 2) + 8 * 5 * 4 * 8
4 * 7 + ((7 * 4 + 7 * 9 + 5) + 3 * (6 * 7 * 6 * 4 + 9))
((3 * 4 + 8) + 5 * 7 + 8) + 9 + (9 + 6 + (6 * 5 * 6) * (9 * 3 * 4 * 7 + 7 + 5) + 2 + 4) + 4 * 2 * 3
4 + ((5 * 6 * 5 * 8 + 2) + (6 + 5 * 2 * 2 + 4 * 9) * 8 + (2 * 4 + 5 + 4) + 5)
(2 * 9 + 9 * 2) + 4 * 5
(2 + 9 * 8 + 2 + 6) + 4 + 9
7 + (2 + 2 + 7 * (4 * 8 * 4 + 6 * 9 * 7)) * 3 + 6 * 9
7 * 4 * (9 * 4 + 9) + 4
9 * ((9 * 8 + 8 * 7 * 8) * 9) + ((5 + 4 * 6) + 2 + (3 * 7 * 3 * 7 + 4 * 4))
6 * (9 * 6 * (3 * 3 + 8 * 3 * 6)) * (7 + 3 + 7 * 7 * 9 * (7 * 9)) * (3 + 3 * 5) * 9
3 + (4 + 4 * 9) + 5
((7 + 9 * 6 * 7 + 3 * 5) + 5 + (5 * 9 * 6) + (3 * 4 * 2) + 4) + 6
5 + ((8 + 6 + 9 + 9 + 7) * 7) + 4 * 8 + 3
(9 * 2) + 8 * 6 * 3 * 6
(8 + 7) * 4 * (9 * (4 + 6 * 7 + 4 * 6 + 4)) + 2 * (4 * 3 + 9)
((9 + 6) * 9 + 5 * 2) + 5 * 5 + 6 * 7 * 4
5 * 9 + (5 + 9 * 5 * 7 + (2 * 6 * 4) * 3) * (8 * 4) * 7 * ((9 + 8 * 5 * 5) * 4 + 4 * 6 * (4 + 9 * 2 + 7) + 5)
4 * 8 + 9 * (8 + 6 * (5 + 9 * 3 * 5) * 3)
7 * 6 + ((8 * 3) + (3 * 7 * 7 + 6 * 6) + 8 * 9)
4 + 9 * (6 + 2 + 6 + 5) + 6 + 6
(2 * 8) + 9 * (2 + (5 * 6 * 7 * 8 * 7 + 8) * 4 + (2 * 7 * 3 + 4 + 6) * 7 + 4) * 6 + 2
2 * 5 * 7 + 7 + 3 * ((2 + 4 + 3 + 7 + 3) + (3 + 4 + 6 * 9 * 7 * 8) * 6 + 2 + 2 + 8)
3 + 3 * 5 * ((6 * 8 + 8 * 3) * 6) + (8 + (8 * 9 + 4 * 2 + 5) + 5 * (6 * 4) * 4 + (8 * 4))
2 + (8 * 8 + 4 * (4 + 6 * 2) * 6 * 4) + ((3 + 8) + 8 * 8) * (3 * (7 * 7 + 9 * 7) * 5 + 3 + 5) + (2 + 4 * 4 * (6 + 9) + 8 + 6)
7 * 5 * (5 * 4 * 8 + 3 * 2) + 8 * 5 + 8
7 * 3 + (4 * 8 + 9)
8 + 7 + 5 + 2
((3 * 7 + 3 + 5 * 4 * 2) + 8 * (5 * 9 * 9) * 3 + 5) + (4 * 8 * 9) * 6 * 2 * (6 * (8 + 3 * 4 + 5 * 6 + 3))
7 + (5 + 8 * 4 + 5 + 5 + 3) * 3 + 7
3 * 4 + (8 + 3 * 7 * 3 + (2 + 2 * 9 * 6 * 9)) + 2 * 4 * (6 * 3 * 8 + 6)
(9 * 8 + 2) + 8 * ((6 + 4 + 9) * 7) * 2 + (4 * 5 * 4 + 5)
8 + 3 * 3 * 5 * ((6 * 5 * 7 + 5) + 5 * 2 * 2)
8 + 5 * (5 * 6 * 5 + (8 + 9 + 6 * 3 * 6)) * 3 * 6 * 5
8 + 8 + 6 + ((5 + 9 + 2 * 4 + 4 + 9) + 7) * 2 + (9 * (8 + 5 + 5 * 8) * 5 + 8)
(7 + 5 * 8 * 3 * 8) * 9 + ((8 * 2 * 3 + 9 + 7 * 5) + (6 + 4 * 2 * 4 + 8 + 3) * (3 + 7 * 4 * 9) + 6 + 4) * (3 * 6 * 6 * (2 * 7 + 2) + 2) * 4
(9 * 4 * 8 * 2 + 6 + 4) * (8 * 8) * 4 + 8
4 * 3 * 9 * (6 + 3 + 5 + (6 * 9)) + (2 + 5)
4 * 9 + 6 + (2 + 6 * 6) * (7 + 4 + 4 * 5 * (7 * 6 * 2 * 3 + 9 + 4)) + 9
((8 * 5 + 5) + 2) + 4 * 9
5 + 6 + 6 * 4 * 5 * (9 + (4 + 5 + 9 + 4 * 2) + 4)
2 * 9 * (7 + 2 * 5) + 8 * (2 + 7 * 2)
3 * 3 + 9 * (6 * 3 * (7 + 4 + 3 * 9 * 4) + 4 * 5)
((5 + 5 * 8 + 9 + 9 + 6) + 9 * 8 * 3) + 5 + 7 + (5 + 2 * 8)
2 + (9 * 4) + 6 + 6
(5 + 6 + 9 * 3 * 2) + (8 + 2 + 3 + 5 + (8 + 6 * 2)) + 8 + 3 + 3
(7 + (3 * 6 + 8 * 8 + 8) * (2 * 8) * 6) + (5 + 2 * (5 + 9) + 5 * 6)
(5 + 9 * 9 + 5) * ((5 * 9) * (8 + 3 + 7 * 8 * 7 + 6) + 7 + 4)
4 * (2 * 9) + 9 + 8 * 9 + 2
9 + ((6 + 5 * 9 + 3 + 6) + (6 * 6)) + (2 + 9 + 9) + (3 + 8) + 6
7 + (3 + 2 * 6) * 4 + 9
3 + 7 * 6 + (7 + 6 * 6 * 3 * (3 + 7 + 9 + 8 + 8)) + 7 * (3 * 7 * 9 * 9)
(9 * 5 + 3 * 2 + 2 + 7) * 4 * 5 + 7 * 6 + 6
6 * 6 + 4
6 + 9 + 5 * (2 * 3 * 7 + (7 + 4)) + 9 * 5
6 * 5 + (6 * 4 + (6 * 9 * 9) + 8 * 5 + (8 + 6 + 5 * 2 + 9 * 5))
(5 + (7 * 8 + 8 * 3 * 2 + 6) * 9 * 5) * (4 + (3 * 5 * 5 * 2 * 4) * 6 + 2) * 7
3 * 7 * 8 + 2 + ((4 + 8 + 8 * 4) + 2 * (7 * 5 + 5 * 3 * 3 + 7))
9 + (5 + (5 * 7) + 6 * 6) * 6 + 2 + (7 + 6)
((9 + 7 * 8) + (5 * 4) + (2 + 2 + 6 * 3 + 5) + 3 * (9 + 6) + 2) * 8 * 3 * 9 * (6 + 9) + 8
8 + 2 + 6 * ((9 * 5 + 6 + 2) * 4 * 5 * 9 * 4 + 9) + 5
(5 * 2 * 9 + 8 * 8) * 7 * 8 * 8 + 9 * 9
8 * (2 + (7 + 7)) + 8
(3 + 7) * ((7 + 4) + 5 + 6 * 5 + 9) + 8
3 * 2 * 2 * (3 + (4 + 3 + 2) * (2 * 9) + 3 * 9 * (8 * 3)) * 8
7 + (8 + 4 + (5 + 2 + 3 + 5 * 6) * 2 + 6 + 9) + (6 + 4 * (3 + 2) + 9 * 4)
5 * (5 + 4 * 3 * 7 * 2)
7 + 5 * (3 + 7 + 2 + (8 * 8 + 8) + 8 + 4) + 2
(7 + (9 + 2 * 9 + 2 + 3 * 9) * 6 * 8) + 6 + (3 + 3 * (7 + 6 * 3 * 5 * 6)) + 2
(9 + 6 * 3) + 7 * 6
3 * (9 + 6 + 3 + 5) + 6
3 + 6 * 5 + (6 + (5 * 4) + 7 + 5 * 4 * 4) * 9
(9 * 8 * 3) + ((8 + 2 + 8 + 8 * 8) + (3 + 2 * 7 * 5 + 3) + 5)
2 + (3 + 2) * 5 * 9 * 4
4 + 4 + 3 + 8 * 8 * 4
(5 + 6 * 9) * 9 * 3 + (6 * 9 * 9 + 2 * 9) + 2
7 * (9 + 4 * (8 * 4 * 7 * 8) + (5 * 3) * (8 * 2 + 2 + 8) + 4) + 4 + 7 * (6 * 2 * 9 + 7)
2 + 5 * 6 * (4 + 2 * 8 * 7 * 2)
6 * (4 + (3 * 4 + 5 + 8)) * 6 + 5 * 4 + 3
(9 + 5) * 4 + 2 * (5 * (3 + 2 * 8 + 2) * 3) + 8 * 5
2 * 2 + 7 + 5 + (6 * (7 + 4 * 5) + (8 * 5 * 5 * 2 + 7) + (5 + 2)) * 3
9 + (3 * 9 + 8 * 7 * 8) * (4 * 8 + 7) * (3 * 2) + 7
5 + (5 + (6 * 2) * 8 * 2 + (8 * 6 * 3 + 3 * 9) + (2 * 8 + 2 * 5)) * 4 * 8 * 7
3 * (8 * 9) * (3 * 6 + 4) + 2
7 * (4 * 5 + 5 * 3) + 9 * (9 * 4 + 2 * 4 + 6)
8 + 5 + 7 + 7 * 3 * ((6 * 5 * 4) * 7 * 5 * 3 * 4 * 8)
8 + ((4 + 2 * 4 * 6 * 4) * (3 * 8 * 8 * 4) + 4 + 6 * 6 * 3) * 6 * 8
9 * 9 + (5 + 3 * (8 * 9 + 8 + 3 + 6) * 2 * 2) * 5
8 + 7 + (9 * 3 + 9 * (2 + 4 + 8 + 2) + 4) * 3 + 5 * 5
9 * (3 * 7 * (3 * 6 * 3 * 5) + 5 * 3 + 8) * 7 + 7 * 2
9 + 2 * (7 * (8 * 7 * 4)) + 7 + 4
(2 * 4 * (4 * 9 * 7 * 7 + 3) + 5) * 4 + 8 * 5 + 4 * 5
(7 * 3 + 7 + 7 * 3 + (4 * 4 * 9 + 4 * 7)) * 6 * (4 + 5 * 3) * 4 + 2
8 + (2 + 6 * 9 * (7 * 4 * 9) + (2 * 4 + 3)) + (5 + 9 * 2 * 9 + 7) + 2 * 5
6 + 9 * 6 + 6 + (8 + 7) * 4
8 + 8 * 7 + 6 * 2 + 8
6 * 2 + 8
5 + (7 * 9 + 6) * (8 + (3 + 9 + 8)) + (5 + 4 + 5 + 5 * 5) + (8 * 6)
(9 * 9 * 8 + 7 * 2) + 7
6 + 7 + 8 + (6 * (5 * 8 * 4 + 5 + 7) + 4 + 9 * (3 * 2)) + (7 + 6 + 6)
(5 * 5 * 9 * 6 + (2 + 9 * 5 * 6) + 9) + 7 * 6"""

# inp = "(9 + (2 * 9 + 6 + 5 + 2 + 7) + 4) + 5 + (9 + (7 + 8 * 6 + 3 * 8) * (5 + 3 * 2 * 9) + 7 * (4 * 5 + 6 + 9)) + 9 * 7 * 4"

# inp = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"

def solve_simp(eq):
    # print(eq)
    res = 0
    num = ""
    op = "#"
    for c in eq:
        if c.isnumeric():
            num += c
        else:
            if op == "#":
                res = int(num)
            else:
                if op == "+":
                    res += int(num)
                elif op == "*":
                    res *= int(num)
            op = c
            num = ""
    if op == "#":
        res = int(num)
    else:
        if op == "+":
            res += int(num)
        elif op == "*":
            res *= int(num)
    return res

def solve_adv(eq):
    # print(eq)
    if len(eq) == 0:
        return 1
    i = eq.find("*")
    if i == -1:
        return solve_simp(eq)
    l, r = eq[:i], eq[i + 1:]
    if "*" in l:
        l = solve_adv(l)
    else:
        l = solve_simp(l)
    if "*" in r:
        r = solve_adv(r)
    else:
        r = solve_simp(r)
    return l * r


def brackets(eq):
    #print("brackets ", eq)
    brackets = []
    stack = []
    for i,c in enumerate(eq):
        if c == '(':
            stack.append((i, '('))
        elif c == ')':
            b = stack[-1]
            stack.pop()
            brackets.append((b[0], i))
    return brackets

def solve(eq):
    br = brackets(eq)
    while(len(br) > 0):
        # print("while ", eq)
        ress = []
        for b in br:
            beq = eq[b[0]+1:b[1]]
            # print("beq ", beq)
            if (len(brackets(beq)) > 0):
                ress.append(-1)
                continue
            res = solve_adv(beq)
            ress.append(res)
        offset = 0
        for r,b in zip(ress, br):
            if r == -1:
                continue
            eq = str(r).join([eq[:b[0] - offset], eq[b[1] + 1 - offset:]])
            offset += b[1] - b[0] - len(str(r)) + 1
        br = brackets(eq)
    return solve_adv(eq)

lines = inp.split("\n")
sm = 0
for i, line in enumerate(lines):
    eq = line.replace(" ", "")
    eq = unicode(eq, 'utf-8')
    sol = solve(eq)
    # print(i, sol)
    sm += sol
print(sm)