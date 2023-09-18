from math import pi

def main():
    return compute_storage_efficiency()

def compute_volume(radius, height):
    volume = pi * radius**2 * height
    return volume

def compute_surface_area(radius, height):
    area = 2 * pi * radius * (radius + height)
    return area

def compute_storage_efficiency():
    volume = compute_volume()
    area = compute_surface_area()
    storage_efficiency = volume / area
    return storage_efficiency

def compute_cost_efficiency():
    return 0

main()