#Adott egy lista, mely október havi napi középhőmérséklet értékeket tartalmazza.
# homerseklet= [0,12,13,9,2,7].
#Az első érték október 1.
# A program írja ki, melyik napon csökkent az előző naphoz képest  a hőmérséklet több, mint 3 fokot?

homerseklet= [0,12,13,9,2,7]
i = 0
nap = 1
while i < len(homerseklet) -1:
    if (homerseklet[i] - homerseklet[i+1] > 3):
        print(f"A hőmérséklet az alábbi napokon csökkent több mint 3 fokot az elöző napokhoz képest: Október {i+2}")
    i += 1

