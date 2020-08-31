# Function to compute volume of sphere

def volume_of_sphere(radius):
    return 1.33 * 3.14 * radius * radius * radius
    
radius = int(input("Enter radius of sphere : "))
print("Volume of sphere is : {:.2f}".format(volume_of_sphere(radius)))
