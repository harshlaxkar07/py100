def circle(radius):
    """Calculate the area and circumference of a circle given its radius."""
    pi = 3.14159
    area = pi * (radius ** 2)
    circumference = 2 * pi * radius
    return area, circumference
input_radius = float(input("Enter the radius of the circle: "))
area, circumference = circle(input_radius)  
print(f"The area of the circle is: {area}")
print(f"The circumference of the circle is: {circumference}")