def mooseca(argument):
    switcher = {
        1: ["Rai 1", "test"],
        2: ["Rai 2", "test2"],
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    for asd in switcher:
        print(str(asd)+") "+switcher[asd][0])
    print(switcher.get(argument, "Selezione non valida"))


#mooseca(13)
mooseca(4)
