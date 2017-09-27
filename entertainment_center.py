# Coded by Oto Tabares
# Movie description credit: IMDB

import fresh_tomatoes
import media

tron_legacy = media.Movie(
    "Tron: Legacy",
    "The son of a virtual world designer goes looking for his father and ends up inside the digital world that his father designed. He meets his father's corrupted creation and a unique ally who was born inside the digital world.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/c/c2/Tron_Legacy_poster.jpg",
    "https://www.youtube.com/watch?v=L9szn1QQfas",
    "PG", "2h 5min", "2010")

guardians = media.Movie(
    "Guardians of the Galaxy",
    "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
    "https://www.youtube.com/watch?v=d96cjJhvlMA",
    "PG-13", "2h 1min", "2014")

inception = media.Movie(
    "Inception",
    "A thief, who steals corporate secrets through use of dream-sharing technology, is given the inverse task of planting an idea into the mind of a CEO.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=YoHD9XEInc0",
    "PG-13", "2h 28min", "2010")

a_beautiful_mind = media.Movie(
    "A Beautiful Mind",
    "After John Nash, a brilliant but asocial mathematician accepts secret work in cryptography, his life takes a turn for the nightmarish.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/b/b8/A_Beautiful_Mind_Poster.jpg",  # noqa
    "https://www.youtube.com/watch?v=YWwAOutgWBQ",
    "PG-13", "2h 15min", "2001")

x_men = media.Movie(
    "X-Men: First Class",
    "In 1962, the United States government enlists the help of Mutants with superhuman abilities to stop a malicious dictator who is determined to start World War III.",  # noqa
    "https://upload.wikimedia.org/wikipedia/en/5/55/X-MenFirstClassMoviePoster.jpg",  # noqa
    "https://www.youtube.com/watch?v=UrbHykKUfTM",
    "PG-13", "2h 12min", "2011")

movies = [tron_legacy, guardians, inception, a_beautiful_mind, x_men]
fresh_tomatoes.open_movies_page(movies)
