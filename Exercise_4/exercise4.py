"""Devise the necessary code in any language to receive 3 values from prompt. Each value
corresponds to the length of the side of a triangle. Values must be Int. A return in a string should
be made stating what type of triangle will these values form.
Example: 3, 3, 3 -> equilateral triangle."""


def calculate_triangle(triangle):
    if triangle[0] == triangle[1] == triangle[2]:
        return 'Equilateral'
    elif triangle[0] != triangle[1] != triangle[2]:
        return 'Scalene'
    else:
        return 'Isosceles'


def request_input():
    triangle_sides = []
    for i in range(0, 3):
        current_side = ''
        while type(current_side) != int:
            try:
                current_side = int(input("Enter side {} length:".format(str(i+1))))
            except ValueError:
                print("The provided input is not an int! Please enter a valid int")
        triangle_sides.append(current_side)
    return triangle_sides


def main():
    triangle = request_input()
    result = calculate_triangle(triangle)
    print('{} triangle'.format(result))


if __name__== "__main__" :
    main()


