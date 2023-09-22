from math import pi


def main():

    with open('can_info.txt') as can_info:
        next(can_info)

        best_store = None
        best_cost = None
        max_store_eff = -1
        max_cost_eff = -1

        for data in can_info:
            row = data.split('	')
            name = row[0]
            radius = float(row[1])
            height = float(row[2])
            cost = float(row[3].lstrip('$'))

            volume = calculate_volume(radius, height)
            surface_area = calculate_surface_area(radius, height)
            storage_efficiency = compute_storage_efficiency(volume, surface_area)
            cost_efficiency = compute_cost_efficiency(volume, cost)

            print(f'{name} {storage_efficiency:.2f} {cost_efficiency:.2f} ')

            if storage_efficiency > max_store_eff:
                best_store = name
                max_store_eff = storage_efficiency

            if cost_efficiency > max_cost_eff:
                best_cost = name
                max_cost_eff = cost_efficiency

        print()
        print("Best can size in storage efficiency:", best_store)
        print("Best can size in cost efficiency:", best_cost)


def calculate_volume(radius, height):
    volume = pi * radius**2 * height
    return volume


def calculate_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area


def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency


def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency


main()
