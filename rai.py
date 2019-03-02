import os
import sys


def mooseca():
    stream = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont='
    switcher = {
        1: ["Rai 1", "2606803"],
        2: ["Rai 2", "180116"],
        3: ["Rai 3", "180117"],
        4: ["Rai 4", "746966"],
        5: ["Rai 5", "72382"],
        6: ["Rai News24", "1"],
        7: ["Rai Sport + HD", "4145"],
        8: ["Rai Sport", "179975"],
        9: ["Rai Movie", "72381"],
        10: ["Rai Premium", "72383"],
        11: ["Rai Yoyo", "72384"],
        12: ["Rai Gulp", "4119"],
        13: ["Rai Storia", "24269"],
        14: ["Rai Scuola", "24268"],
        15: ["Rai Play Sport", "9681540"],
        16: ["Rai Play Sport 1", "9681597"],
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
            os.system("ffplay " + stream + switcher[nums][1])
        except KeyboardInterrupt:
            sys.exit(0)
            # input("\nWuoi ancora wardare films? ")


mooseca()
