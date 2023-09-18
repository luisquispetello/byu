from math import pi
from datetime import datetime

PI = pi
date = datetime.now()

width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = PI * (width**2) * ratio * (width * ratio + 2540 * diameter) / 10**10

print(f'The approximate volume is {volume:.2f} liters')

with open('volumes.txt', 'at') as tires_file:
    print('')
    print(f'{date:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume:.2f}', file=tires_file)