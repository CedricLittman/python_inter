# A simple Python script to calculate the area of a rectangle

def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Input from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate and display the area
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
