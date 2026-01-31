PI = 3.141592653589793

def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):

    if not isinstance(radiusOfCircle1, int) or not isinstance(radiusOfCircle2, int):
        return "Both radii must be integers."

    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Both radii must be positive."

    theAreaofCircle1 = PI * (radiusOfCircle1 ** 2)
    theAreaofCircle2 = PI * (radiusOfCircle2 ** 2)

    if theAreaofCircle1 > theAreaofCircle2:
        bigger_circle = theAreaofCircle1
        smaller_circle = theAreaofCircle2
    else:
        bigger_circle = theAreaofCircle2
        smaller_circle = theAreaofCircle1

    percent_of_coverage = (smaller_circle / bigger_circle) * 100
    return percent_of_coverage

print(circleAreaCoverage(4, 5))
print(circleAreaCoverage(7, 3))