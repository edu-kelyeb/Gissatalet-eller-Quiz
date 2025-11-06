# del 1 - Hälsning

namn=input("vad heter du")
print(f"hej {namn}välkommen till spelet!")
      
# del 2 - slumpa ett tal

import random
hemligt_tal= random.randint(1,10)

while true:
    gissning=int(input("Gissa talet"))
    antal_gissning += 1

    if gissning < hemligt_tal:
        print("För lågt! försök igen.")
    elif gissning > hemligt_tal:
        print("för stor! försök igen.")
    else:
        print(f"rätt gissat! Talet är {hemligt_tal}.")
    break

