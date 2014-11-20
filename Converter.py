def mass(item_1, unit_1, unit_2):
    units={"g":0.001, "kg":1, "lbs":0.45359237 , "oz":0.028349523125, "stone":6.35029318 , "t":1000}
    item_2=item_1*units[unit_1]/units[unit_2]
    return item_2

def pikkused(item_1, unit_1, unit_2):
    units={"m":1, "km":1000, "dm":10, "mm":0.1, "ft":0.3048, "in":0.0254, "mi":1609.344}
    item_2=item_1*units[unit_1]/units[unit_2]
    return item_2

def maht(item_1, unit_1, unit_2):
    units={"l":1, "bu":36.36872 , "cl":0.01, "cc":0.001, "m":1000, "ft":28.316846592 , "in":0.016387064 , "dm":1, "yd":764.554857984 , "oz":0.0295735295625 , "gal":3.785411784, "gil":0.11829411825, "ml":0.001, "pk":8.80976754172 , "pt":0.473176473, "qt":0.946352946}
    item_2=item_1*units[unit_1]/units[unit_2]
    return item_2

operations=["mass", "pikkused", "maht"]
operation = input("Sisestage teisenduse liik")
while operation not in operations:
    operation = input("Sisestage teisenduse liik")

arv1=float(input("Sistage teisendatav arv"))
unit_1=input("sisestage teisendatava arvu ühik")
unit_2=input("sistage ühik, milleks soovite teisendada")
if operation == "mass":
    print(mass(arv1, unit_1, unit_2))
elif operation == "pikkused":
    print(pikkused(arv1, unit_1, unit_2))
elif operation == "maht":
    print(maht(arv1, unit_1, unit_2))
