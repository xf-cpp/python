import math

def calculate_area_of_circle(r):
    return math.pi * (r ** 2)

if __name__ == '__main__':
    print( f"the area is {calculate_area_of_circle(int(input('please inpur r:'))) :.2f}")
