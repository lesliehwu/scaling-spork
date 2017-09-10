def draw_stars(star_list):
    for estrella in star_list:
        if isinstance(estrella,int):
            print "*" * estrella
        else:
            print estrella[0].lower() * len(estrella)

star_boy = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

draw_stars(star_boy)
