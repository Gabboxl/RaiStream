import os
import sys


def mooseca():
    stream = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont='
    switcher = {
        1: ["Rai 1", "2606803"],
        2: ["Rai 2", "308718"],
        3: ["Rai 3", "1472284"],
        4: ["Rai 4", "746966"],
        5: ["Rai 5", "395276"],
        6: ["Rai News24", "1"],
        7: ["Rai Sport + HD", "358025"],
        8: ["Rai Sport", "358071"],
        9: ["Rai Movie", "747002"],
        10: ["Rai Premium", "746992"],
        11: ["Rai Yoyo", "746899"],
        12: ["Rai Gulp", "746953"],
        13: ["Rai Storia", "746990"],
        14: ["Rai Scuola", "747011"],
        0: ["Esci"]
    }
    while True:
        try:
            for asd in switcher:
                print(str(asd) + ") " + switcher[asd][0])
            while True:
                try:
                    nums = int(input("Scegli un canale: "))
                    if (nums not in switcher):
                        print("Selezione non valida! Riprova.")
                        continue
                    break
                except ValueError:
                    print("Selezione non valida! Riprova.")
                    continue
            if nums == 0:
                sys.exit(0)
            os.system("ffplay \"" + stream + switcher[nums][1] + "&output=16\"")
        except KeyboardInterrupt:
            sys.exit(0)
            # input("\nWuoi ancora wardare films? ")


mooseca()
