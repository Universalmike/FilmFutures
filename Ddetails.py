def movie_details(part):
    if part == 1:
        return "A Nonsense Christmas with Sabrina Carpenter"
    elif part == 2:
        return "Mufasa: The Lion King"
    elif part == 3:
        return "Nofseratu"
    elif part == 4:
        return "The Lord of the Rings: The War of the Rohirrim"
    elif part == 5:
        return "Seven Doors"
    else:
        return "This is everything"

def movie_info(parts):
    if parts == 1:
        return (
            "Stars: Sabrina Carpenter \n\n"
            "Released Date: December 6th \n\n"
            "MOVIE \n\n"
            "RATED: PG \n\n"
            "RUNTIME: 2h18m \n\n"
            "Genre: Music, Holiday \n\n"
            "It’s a nonsense holiday and we’re so here for it. In this special with musical guests, pop icon Sabrina Carpenter will perform songs from her holiday EP fruitcake and other iconic chart-topping holiday covers. This special will also feature show-stopping music performances, comedic guests, unexpected duets, plus many more surprises and fun cameos. \n\n"
            "(credit: Movie Insider)"
        )
    elif parts == 2:
        return (
            "Stars: Seth Rogen, Thandiwe Newton, Mads Mikkelsen\n\n"
            "Released Date: December 20th \n\n"
            "MOVIE \n\n"
            "RATED: PG \n\n"
            "RUNTIME: 1h39m \n\n"
            "Genres: Animation, Adventure \n\n"
            "Told in flashbacks—Rafiki, Timon and Pumbaa tell the story of Mufasa to a young lion cub— Mufasa reveals the rise of one of the greatest kings of the Pride Lands. \n\n"
            "(credit: MovieInsider)"
        )
    elif parts == 3:
        return (
            "Stars: Emma Corrin, Aaron Taylor-Johnson, Bill Skarsgård \n\n"
            "Release Date: December 25th"
            "MOVIE \n\n"
            "RATED: R. \n\n"
            "RUNTIME: 2h13m \n\n"
            "Genres: Horror, Mystery \n\n"
            "A gothic tale of obsession between a haunted young woman and the terrifying vampire infatuated with her, causing untold horror in its wake. \n\n"
            "(credit: IMDB)"
        )
    elif parts == 4:
        return (
            "Stars: Brian Cox, Christopher Lee, Miranda Otto\n\n"
            "RELEASE DATE: December  13"
            "MOVIE \n\n"
            "RATED: PG-13 \n\n"
            "RUNTIME: 2h14m \n\n"
            "Genres: Dark Fantasy, Animation \n\n"
            "A sudden attack by Wulf, a clever and ruthless Dunlending lord seeking vengeance for the death of his father, forces Helm Hammerhand, the King of Rohan, and his people to make a daring last stand in the ancient stronghold of the Hornburg. \n\n"
            "(credit: IMDB)"
        )
    elif parts == 5:
        return (
            "Stars: Femi Adebayo, Chioma Chukwuka Akpotha\n\n"
            "RELEASE DATE: December 13th"
            "MOVIE \n\n"
            "RATED: PG"
            "GENRES: Drama, Hisatory"
            "Seven Doors is set in two eras, the 18th century and the 19th century, it is about a Yoruba king mar­ried to an Igbo woman, with a Hausa man coming to invest in their kingdom. \n\n"
            "(credit: IMDB)"
        )
    else:
        return "This is everything"

def blog_title(blog):
    if blog == 1:
        return "The Impact of Movies on Society"
    elif blog == 2:
        return "The Mirage Heist – Releasing September 29th"
    elif blog == 3:
        return "The Astral Crusade – Releasing September 15th"
    else:
        return "This is everything"

def blog_details(blogs):
    if blogs == 1:
        return "Movies have a profound impact on society, shaping cultural norms, influencing public opinion, and reflecting social issues.\n They serve as a powerful medium for storytelling, bringing diverse perspectives and fostering empathy.\nThrough their portrayal of characters, conflicts, and resolutions, films can inspire change, challenge stereotypes, and raise awareness about critical topics.\nAdditionally, movies offer a shared experience that unites audiences, sparking conversations and collective emotions.\nIn essence, cinema not only entertains but also educates and motivates, leaving a lasting imprint on societal values and individual lives."
    elif blogs == 2:
        return (
            "If you’re in the mood for a pulse-pounding thriller, look no further than The Mirage Heist. Directed by Guy Ritchie, this stylish film brings together a team of world-class thieves in a daring mission to steal a priceless artifact hidden within an impenetrable desert fortress."
            "Leading the team is Eva Rook, an enigmatic mastermind played by Ana de Armas, who brings her A-game in this role filled with cunning, charisma, and unexpected depth. The crew must navigate a maze of shifting sand dunes, deceptive mirages, and ruthless mercenaries guarding the treasure. As they delve deeper into the fortress, deadly traps and unforeseen betrayals challenge their resolve, pushing each member to confront their own personal demons."
            "With Henry Cavill, Rami Malek, and Lupita Nyong’o adding their talents to the cast, The Mirage Heist offers a blend of intricate heist elements and heart-stopping action sequences set against the exotic backdrop of the desert. Guy Ritchie’s signature style of fast-paced storytelling and sharp dialogue ensures this film will be a rollercoaster ride from start to finish."
            "Why You Should Watch:\n\n"
            "- A thrilling plot with complex characters and high stakes. \n\n"
            "- Exhilarating action scenes set in stunning desert landscapes. \n\n"
            "- An exceptional cast delivering top-notch performances."
        )
    elif blogs == 3:
        return (
            "Prepare for a cosmic journey like no other! The Astral Crusade is an epic space adventure that brings together an all-star cast in a battle for humanity's survival against a mysterious alien force. The story centers on Captain Lena Corvus, portrayed by Zoë Kravitz, a seasoned astronaut with a tumultuous past who is tasked with leading a diverse crew on a mission beyond the known universe."
            "With groundbreaking technology at their disposal, they must navigate treacherous galaxies, uncover hidden worlds, and unravel ancient secrets to prevent an interstellar catastrophe. But with tensions running high and trust becoming a rare commodity among the crew, Captain Corvus faces the ultimate test of leadership and courage."
            "Directed by Denis Villeneuve, known for his visually spectacular films and gripping storytelling, The Astral Crusade promises an unforgettable cinematic experience, combining breathtaking visual effects with a compelling narrative of survival and discovery. The movie also features Michael B. Jordan, Idris Elba, and Oscar Isaac, making it one of the most anticipated releases of the year."
            "Why You Should Watch:\n\n" 
            "- Stunning visual effects and state-of-the-art CGI. \n\n"
            "- A suspenseful storyline filled with unexpected twists. \n\n"
            "- A powerhouse cast that delivers intense and memorable performances."
        )


def movie_cover(parted):
    # Replace with actual URLs for movie covers
    cover_urls = {
        1: "FilmFutures/christmas.jpg",
        2: "FilmFutures/mufasa.jpg",
        3: "FilmFutures/nosferatu.jpg",
        4: "FilmFutures/LOTR2.jpg",
        5: "FilmFutures/sevendoors.jpg",
    }
    return cover_urls.get(parted, "C:/Users/BABA/DEFAUL.png")
