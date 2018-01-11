# It's the main program to create the web page
# Run "python entertainment_center.py" to create the HTML web page
# Created by Gerald Ding (horzon16@gmail.com)

# import the relative programs
import media
import fresh_tomatoes

# call the function Movie in media class

# The Martian -- information
the_martian = media.Movie("The Martian",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # noqa
                        "https://youtu.be/ej3ioOneTy8")

# Sully -- information
sully = media.Movie("Sully",
                    "https://upload.wikimedia.org/wikipedia/en/8/82/Sully_xxlg.jpeg",  # noqa
                    "https://youtu.be/9uhuyyY5WuU")

# Your Name -- information
your_name = media.Movie("Your Name",
                        "https://upload.wikimedia.org/wikipedia/en/0/0b/Your_Name_poster.png",  # noqa
                        "https://youtu.be/s0wTdCQoc2k")

# Catogory of the movies
movies = [the_martian, sully, your_name]
# using fresh_tomatoes to create the web page
fresh_tomatoes.open_movies_page(movies)

