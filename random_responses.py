import random


def random_string():
    random_list = [
        "Tolong coba tuliskan sesuatu yang lebih deskriptif.",
        "Oh! Sepertinya Anda menulis sesuatu yang belum saya pahami",
        "Apakah Anda keberatan mencoba mengulanginya?",
        "Maaf, saya tidak begitu paham.",
        "Saya belum bisa menjawabnya, coba tanyakan hal lain."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
