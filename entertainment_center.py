import media
import fresh_tomatoes
# initialize Toy Story
toy_story = media.Movie("Toy Story",
                        "A story of a boy an his toys tha come to life",
                        "https://upload.wikimedia.org/wikipedia/pt/d/dc/Movie_poster_toy_story.jpg", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# initialize Avatar
avatar = media.Movie("Avatar", "A marine on a alien planet",
                        "https://upload.wikimedia.org/wikipedia/pt/b/b0/Avatar-Teaser-Poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# initialize Elite Squad
elite_squad = media.Movie("Elite Squad",
                            "Captain Roberto Nascimento (Wagner Moura) \
                            narrates the film, briefly explaining how the \
                            police and the drug lords of Rio de Janeiro \
                            cooperate with each other (policemen collect \
                            periodic bribes and drug lords are left free to\
                             operate) in the 90's.",
                            "https://upload.wikimedia.org/wikipedia/en/2/2a/TropaDeElitePoster.jpg", # noqa
                            "https://www.youtube.com/watch?v=ELlkWtNWyKY")

# initialize The Shawshank Redemption
the_shawshank_redemption = media.Movie("The Shawshank Redemption", "In 1947 \
                        Portland, Maine, banker Andy Dufresne is convicted of\
                         murdering his wife and her lover, and is sentenced \
                         to two consecutive life sentences at the Shawshank\
                          State Penitentiary.",
                            "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg", # noqa
                            "https://www.youtube.com/watch?v=6hB3S9bIaco")

# initialize The Perks Of Being a WallFlower
the_perks_of_being_a_wallflower = media.Movie("The Perks of Being a Wallflower",
                            "The film is set against the background of a young\
                             student, Charlie, who has been suffering from\
                          clinical depression from childhood setbacks and\
                           has recently been discharged from a mental\
                            health care institution to begin his adaptation\
                             to a normal lifestyle as a young high\
                              school student. ",
                            "https://upload.wikimedia.org/wikipedia/en/0/0b/The_Perks_of_Being_a_Wallflower_Poster.jpg", # noqa
                            "https://www.youtube.com/watch?v=n5rh7O4IDc0")

# Put all toguether in a array
movies = [toy_story, elite_squad, the_shawshank_redemption,
                        the_perks_of_being_a_wallflower, ]
# Open the site page
fresh_tomatoes.open_movies_page(movies)
# jus for loggin
print(media.Movie.__module__)
