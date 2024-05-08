# Python

# This will calculate the shapes.
def calculateAreaRectangle(width, length):
    area = width * length
    return area

def main():
    print("This is our shapes program!")
    print(f"The area is {calculateAreaRectangle(10,20)}")

    print(calculateAreaRectangle(20,40))

def calculate_triangle_area(base, height):
    area = (base * height) / 2
    return area

main()