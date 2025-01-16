def sprawdz_liczbe():
    try:
        liczba = float(input("Podaj liczbę: ")) # ask for the number
        if liczba >= 1:
            print("Liczba jest dodatnia.") # if number is 1 or more its positive
        elif liczba <= -1:
            print("Liczba jest ujemna.") # if number is -1 or less its negative
        else:
            print("Liczba nie jest ani dodatnia, ani ujemna.") # if the user types 0 its not positive or negative
    except ValueError:
        print("Proszę podać poprawną liczbę.") # output this if its not a number or its wrongly typed

sprawdz_liczbe()
