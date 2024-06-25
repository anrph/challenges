# Challenge #5

# AREA OF A POLYGON
# Create a single function (it must be only one) that calculates and returns the area of ​​a polygon.
# - The function will receive only ONE polygon per parameter at a time.
# - The supported polygons will be Triangle, Square, and Rectangle.
# - Prints the calculation of the area of ​​a polygon of each type.

def get_area(polygon_type, *dimensions):
    # Check if the polygon is a square
    if polygon_type == "square":
        # Check if there are the required dimensions
        if len(dimensions) != 1:
            raise ValueError("A square requires exactly 1 dimension: side lenght.")
        # Extract the dimensions
        side = dimensions[0]
        # Calculate the area of the square
        area = side ** 2
    
    # Check if the polygon is a rectangle
    elif polygon_type == "rectangle":
        # Check if there are the required dimensions
        if len(dimensions) != 2:
            raise ValueError("A rectangle requires exactly 2 dimensions: lenght and width.")
        # Extract the dimensions
        lenght, width = dimensions
        # Calculate the area of the rectangle
        area = lenght * width
    
    # Check if the polygon is a triangle
    elif polygon_type == "triangle":
        # Check if there are the required dimensions
        if len(dimensions) != 2:
            raise ValueError("A triangle requires exactly 2 dimensions: base and height.")
        # Extract the dimensions
        base, height = dimensions
        # Calculate the area of the triangle
        area = 0.5 * base * height

    # Raise an error if the polygon is not supported
    else:
        raise ValueError("Unsupported polygon type. Supported types are: Triangle, Square, Rectangle.")

    # Return the calculated area
    return area


print("Area of Square: ", get_area("square", 5))
print("Area of Rectangle: ", get_area("rectangle", 12, 7))
print("Area of Triangle: ", get_area("triangle", 10, 15))