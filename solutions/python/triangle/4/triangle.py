from logging import getLogger
def is_Triangle(sides):
    side_a, side_b, side_c = sides
    return side_a > 0 and side_b > 0 and side_c > 0 and (side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a)
    
def equilateral(sides):
    if not is_Triangle(sides):
        return False
    return len(set(sides)) == 1
    


def isosceles(sides):
    if not is_Triangle(sides):
        return False
    return len(set(sides)) <= 2



def scalene(sides):
    if not is_Triangle(sides):
        return False
    return len(set(sides)) == 3
