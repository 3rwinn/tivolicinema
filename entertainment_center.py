import tivoli
import media

transformers = media.Movie("Transformers: The Last Knight",
                           "Autobots and Decepticons are at war, with humans on the sidelines. Optimus Prime is gone. The key to saving our future lies buried in the secrets of the past, in the hidden history of Transformers on Earth.",
                           "https://m.media-amazon.com/images/M/MV5BMTk3OTI3MDk4N15BMl5BanBnXkFtZTgwNDg2ODIyMjI@._V1_UY268_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=AntcyqJ6brc")

avengers = media.Movie("Avengers: Infinity war",
                       "The Avengers and their allies must be willing to sacrifice all in an attempt to defeat the powerful Thanos before his blitz of devastation and ruin puts an end to the universe. ",
                       "http://fr.web.img5.acsta.net/r_1920_1080/pictures/18/03/16/14/42/0611719.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")

now_you_see_me = media.Movie("Now you see me 2",
                             "The Four Horsemen resurface, and are forcibly recruited by a tech genius to pull off their most impossible heist yet.",
                             "https://m.media-amazon.com/images/M/MV5BNzQ0NDgwODQ3NV5BMl5BanBnXkFtZTgwOTYxNjc2ODE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                             "https://www.youtube.com/watch?v=VMYqjAfFiMU")

bird_box = media.Movie("Bird Box", "Five years after an ominous unseen presence drives most of society to suicide, a mother and her two children make a desperate bid to reach safety.",
                       "https://m.media-amazon.com/images/M/MV5BMjAzMTI1MjMyN15BMl5BanBnXkFtZTgwNzU5MTE2NjM@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/o2AsIXSh2xo")

mowgli = media.Movie("Mowgli", "A human child raised by wolves must face off against a menacing tiger named Shere Khan, as well as his own origins.",
"https://m.media-amazon.com/images/M/MV5BMjMzODc2NzU5MV5BMl5BanBnXkFtZTgwNTMwMTE3NjM@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/OVBjPpUlQrE")

casa_de_papel = media.Movie("La casa de Papel", "A group of very peculiar robbers assault the Factory of Moneda and Timbre to carry out the most perfect robbery in the history of Spain and take home 2.4 billion euros. ", "https://m.media-amazon.com/images/M/MV5BMzBlY2QzNzYtMWU1NS00NjFkLWJiMzItYmM3YTc4MDFjNDQwXkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg", "https://youtu.be/V-ETJ9YpyEI")

creed_2 = media.Movie("Creed II", "Under the tutelage of Rocky Balboa, heavyweight contender Adonis Creed faces off against Viktor Drago, son of Ivan Drago. ", "https://m.media-amazon.com/images/M/MV5BMTcxMjUwNjQ5N15BMl5BanBnXkFtZTgwNjk4MzI4NjM@._V1_UX182_CR0,0,182,268_AL_.jpg",
"https://youtu.be/AdS5ux3G-Gc")

movies = [transformers, avengers, now_you_see_me, bird_box, mowgli, casa_de_papel, creed_2]

tivoli.open_movies_page(movies)
