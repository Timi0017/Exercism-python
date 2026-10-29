def isTriangle(sides):
    a, b, c = sides
    return a > 0 and b > 0 and c > 0 and (a + b >= c and a + c >= b and b + c >= a)
    
def equilateral(sides):
    if not isTriangle(sides):
        return False
    return len(set(sides)) == 1
    


def isosceles(sides):
    if not isTriangle(sides):
        return False
    return len(set(sides)) <= 2



def scalene(sides):
    if not isTriangle(sides):
        return False
    return len(set(sides)) == 3
