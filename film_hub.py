# Importing fresh_tomatoes module to use it's open_movies_page() method.
import fresh_tomatoes

# Importing media module to create multiple instance of it's Movie class.
import media


# Next we create six instances of Movie class,
# giving it the appropriate inputs to store each movie's attributes.

turbo = media.Movie("Turbo",
                    "A snail gets super speed powers and finally lives \
                    it's dream of being a race car.",
                    "https://upload.wikimedia.org/wikipedia\
/en/b/b9/Turbo_%28film%29_poster.jpg",
                    "https://www.youtube.com/watch?v=ADuKkRTiCfI")

spy_kids = media.Movie("Spy Kids",
                       "Kids become spies to \
                       save their kidnapped parent spies.",
                       "https://upload.wikimedia.org/wikipedia\
/en/2/26/Spy_kids.jpg",
                       "https://www.youtube.com/watch?v=GE5aHKJp6HI")

furious7 = media.Movie("Fast & Furious 7",
                       "The crew takes on their previous enemy's brother.",
                       "https://upload.wikimedia.org\
/wikipedia/en/b/b8/Furious_7_poster.jpg",
                       "https://www.youtube.com/watch?v=Skpu5HaVkOc")

the_wolverine = media.Movie("The Wolverine",
                            " A sick guy needs Logan's immortal power and tries\
                            to repay him with mortality.",
                            "https://upload.wikimedia.org/wikipedia\
/en/7/74/The_Wolverine_posterUS.jpg",
                            "https://www.youtube.com/watch?v=Rh1LdTFkm7I")

mi_RogueNation = media.Movie("Mission:Impossible Rogue Nation",
                             "Officially dissolved IMF takes on a \
                             secret society named syndicate.",
                             "https://upload.wikimedia.org/wikipedia\
/en/f/fb/Mission_Impossible_Rogue_Nation_poster.jpg",
                             "https://www.youtube.com/watch?v=gOW_azQbOjw")

iron_man = media.Movie("Iron Man",
                       "Billionare Tony Stark is kidnapped and is forced \
                       to build a devastating weapon in the desert.",
                       "https://upload.wikimedia.org/wikipedia\
/en/7/70/Ironmanposter.JPG",
                       "https://www.youtube.com/watch?v=8hYlB38asDY")


# Storing all the movie instances in an array named 'movies'
movies = [turbo, spy_kids, furious7, the_wolverine, mi_RogueNation, iron_man]


# Finally calling this function with the input of movies array to
# generate an HTML page displaying the movies list with their trailers.

fresh_tomatoes.open_movies_page(movies)
