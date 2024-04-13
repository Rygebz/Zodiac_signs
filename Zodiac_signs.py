def get_zodiac_sign(month, day):
    zodiac_signs = [
        (1, 20, "Aquarius"),
        (2, 19, "Pisces"),
        (3, 21, "Aries"),
        (4, 20, "Taurus"),
        (5, 21, "Gemini"),
        (6, 21, "Cancer"),
        (7, 23, "Leo"),
        (8, 23, "Virgo"),
        (9, 23, "Libra"),
        (10, 23, "Scorpio"),
        (11, 22, "Sagittarius"),
        (12, 22, "Capricorn")
    ]

    for sign_month, sign_day, sign_name in zodiac_signs:
        if (month == sign_month and day >= sign_day) or (month == sign_month + 1 and day < sign_day):
            return sign_name

print("Signs of the zodiac\n")
month = int(input("Month: "))
day = int(input("Day: "))
print("Zodiac sign:", get_zodiac_sign(month, day))
