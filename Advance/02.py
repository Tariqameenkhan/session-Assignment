# Planetary weight calculator
def planetary_weight():
    planet_gravity = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet_name = input("Enter a planet: ").capitalize()

    if planet_name in planet_gravity:
        planet_weight = round(earth_weight * planet_gravity[planet_name], 2)  
        print(f"The equivalent weight on {planet_name}: {planet_weight}")
    else:
        print("Invalid planet name. Please try again.")
    
planetary_weight()
