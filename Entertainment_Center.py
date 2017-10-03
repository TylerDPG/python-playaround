import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life.", "http://cdn.collider.com/wp-content/uploads/toy-story-poster1.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)
#toy_story.show_trailer()

avatar = media.Movie("Avatar", "A Marine on an alien planet", "http://cafmp.com/wp-content/uploads/2012/11/avatar.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")
#print (avatar.storyline)
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "Take notes.", "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
#print (school_of_rock.storyline)
#school_of_rock.show_trailer()

movies = [toy_story, avatar, school_of_rock]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__module__)
