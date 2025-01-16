import time

# getting info from user
print("Witaj! Podaj swoje dane poniżej.")  # Powitanie użytkownika

# ask for the user's name
imie = input("Jak masz na imię? ")  

# ask for the user's age
wiek = int(input("Ile masz lat? "))  

# ask for the user's height (because yes)
wzrost = int(input("Jaki masz wzrost (w cm)? "))  

# aks for the user's home city
miejsce_zamieszkania = input("Gdzie mieszkasz? ")  

# generating the like answer or sum
print("\nPrzetwarzanie danych...\n")  # information about the progress
time.sleep(1)  # optional delay

# creating message
if wiek < 18:
    pozostalo_do_18 = 18 - wiek
    print(f"Hej {imie}, masz {wiek} lat, mieszkasz w {miejsce_zamieszkania}, a Twój wzrost to {wzrost} cm.")
    print(f"Zostało Ci {pozostalo_do_18} lat, aby osiągnąć pełnoletność.")
elif wiek >= 18 and wiek < 100:
    pozostalo_do_100 = 100 - wiek
    print(f"Hej {imie}, masz {wiek} lat, mieszkasz w {miejsce_zamieszkania}, a Twój wzrost to {wzrost} cm.")
    print(f"Zostało Ci {pozostalo_do_100} lat, aby mieć 100 lat.")
else:
    print(f"Hej {imie}, masz {wiek} lat, mieszkasz w {miejsce_zamieszkania}, a Twój wzrost to {wzrost} cm.")
    print("Już przekroczyłeś/aś 100 lat!")

# goodbye
print("\nDziękujemy za podanie swoich danych! Miłego dnia!")  
