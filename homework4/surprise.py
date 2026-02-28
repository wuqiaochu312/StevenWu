# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_stars_names(targets):
    for stars in targets:
        print(stars)

print_stars_names(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_stars_names_spectral_type(targets):
    for stars in targets:
        print(stars, targets[stars]["Spectral Type"])

print_stars_names_spectral_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_greater_than_point1(targets):
    for stars in targets:
        if targets[stars]["Magnitude"] > 0.1:
            print(stars)

find_greater_than_point1(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Procyon"] = {
    "RA": "07h 39m 18.1s",
    "Dec": "+05° 13′ 30″",
    "Magnitude": 0.34,
    "Spectral Type": "F5IV-V"
}

# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def brightest_closest_to_20(targets):
    closest_degree = 360
    brightest_star = ""

    for stars in targets:
        dec_string = targets[stars]["Dec"]
        get_degree = dec_string.split("°")[0]
        get_degree = get_degree.replace("+", "")
        get_degree = get_degree.replace("−", "-")
        get_degree = float(get_degree)

        if get_degree < 20 and 20 - get_degree < closest_degree:
            closest_degree = 20 - get_degree
            brightest_star = stars

        if get_degree >= 20 and get_degree - 20 < closest_degree:
            closest_degree = get_degree - 20
            brightest_star = stars
        
    print(brightest_star)

brightest_closest_to_20(targets)

# 6) What is your favorite constellation?
# My favorite constellation is Pisces.