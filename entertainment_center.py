import media
import fresh_tomatoes

# create movie objects
memento = media.Movie('Memento',
    'http://ia.media-imdb.com/images/M/MV5BMTc4MjUxNDAwN15BMl5BanBnX' \
    'kFtZTcwMDMwNDg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=0vS0E9bBSL0',
    'A man creates a strange system to help him remember things; so he ' \
    'can hunt for the murderer of his wife without his short-term ' \
    'memory loss being an obstacle.',
    '8.5')

avengers = media.Movie('The Avengers',
    'http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZT'
    'cwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=eOrNdBpGMv8',
    'Earth\'s mightiest heroes must come together and learn to fight as a ' \
    'team if they are to stop the mischievous Loki and his alien army from ' \
    'enslaving humanity.',
    '8.2')

bourne_ultimatum = media.Movie('The Bourne Ultimatum',
    'http://ia.media-imdb.com/images/M/MV5BMTgzNjMwOTM3N15BMl5BanBnXkFt' \
    'ZTcwMzA5MDY0MQ@@._V1_SX214_AL_.jpg',
    'https://www.youtube.com/watch?v=ZT2ZxjUjSo0',
    'Jason Bourne dodges a ruthless CIA official and his agents from a new ' \
    'assassination program while searching for the origins of his life as a ' \
    'trained killer.',
    '8.1')

boyhood = media.Movie('Boyhood',
    'http://ia.media-imdb.com/images/M/MV5BMTYzNDc2MDc0N15BMl5BanBnXkFtZTg' \
    'wOTcwMDQ5MTE@._V1_SY317_CR0,0,214,317_AL_.jpg',
    'https://www.youtube.com/watch?v=Ys-mbHXyWX4',
    'The life of Mason, from early childhood to his arrival at college.',
    '8.1')

fast7 = media.Movie('Furious Seven',
    'http://ia.media-imdb.com/images/M/MV5BMTQxOTA2NDUzOV5BMl5BanBnXkFt' \
    'ZTgwNzY2MTMxMzE@._V1_SX214_AL_.jpg',
    'https://www.youtube.com/watch?v=Skpu5HaVkOc',
    'Deckard Shaw seeks revenge against Dominic Toretto and his family for ' \
    'his comatose brother.',
    '8.0')

frozen = media.Movie('Frozen',
    'http://ia.media-imdb.com/images/M/MV5BMTQ1MjQwMTE5OF5BMl5BanBnXkFtZ' \
    'TgwNjk3MTcyMDE@._V1_SX214_AL_.jpg',
    'https://www.youtube.com/watch?v=TbQm5doF_Uc',
    'When the newly crowned Queen Elsa accidentally uses her power to turn ' \
    'things into ice to curse her home in infinite winter, her sister, Anna,' \
    ' teams up with a mountain man, his playful reindeer, and a snowman to ' \
    'change the weather condition.',
    '7.7')

# store movie objects
movies = [memento, avengers, bourne_ultimatum, boyhood, fast7, frozen]


# generate html file using the movie objects as content
fresh_tomatoes.open_movies_page(movies)
