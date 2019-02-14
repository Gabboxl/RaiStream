def mooseca(argument):
    switcher = {
        1: "January",
        2: "February",
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
        print(str(asd)+") "+switcher.get(asd))
    print(switcher.get(argument, "Selezione non valida"))


#mooseca(13)
mooseca(4)
