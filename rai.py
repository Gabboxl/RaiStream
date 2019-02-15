def mooseca(argument):
    stream = 'https://mediapolis.rai.it/relinker/relinkerServlet.htm?cont='
    switcher = {
        1: ["Rai 1", "2606803"],
        2: ["Rai 2", "test2"],
        3: ["Rai 3", "test2"],
        4: ["Rai 4", "test2"],
        5: ["Rai 5", "test2"],
        6: ["Rai News24", "test2"],
        7: ["Rai Sport + HD", "test2"],
        8: ["Rai Sport", "test2"],
        9: ["Rai Movie", "test2"],
        10: ["Rai Premium", "test2"],
        11: ["Rai Yoyo", "test2"],
        12: ["Rai Gulp", "test2"],
        13: ["Rai Storia", "test2"],
        14: ["Rai Scuola", "test2"],
        15: ["Rai Play Sport", "test2"],
        16: ["Rai Play Sport 1", "test2"],
    }
    for asd in switcher:
        print(str(asd)+") "+switcher[asd][0])
    print(switcher.get(argument, "Selezione non valida"))


#mooseca(13)
mooseca(4)
