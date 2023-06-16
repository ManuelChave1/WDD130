
# def main():
#     start_miles = float(input("Enter the first odometer reading (miles): "))
#     end_miles = float(input("Enter the second odometer reading (miles): "))
#     amount_gallons = float(input("Enter the amount of fuel used (gallons): "))
#     mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)
#     lp100k = lp100k_from_mpg(mpg)
#     print(f"{mpg:.1f} miles per gallon")
#     print(f"{lp100k:.2f} liters per 100 kilometers")


# def miles_per_gallon(start_miles, end_miles, amount_gallons):
#     mpg = abs(end_miles - start_miles) / amount_gallons
#     return mpg

# def lp100k_from_mpg(mpg):
  
#     lp100k = 235.215 / mpg
#     return lp100k

# main()

# def kilometers_from_miles(miles):
#     """Convert a value in miles to kilometers
#     and return the kilometers value.
#     """
#     miles = float(input("Please enter a distance in miles: "))
#     km = miles * 1.60934
#     return km
# kilometers_from_miles()
import math
def torus_volume(inner, outer):
    """Compute and return the volume of a torus."""
    vol = 2 * (math.pi * inner) ** 2 * outer