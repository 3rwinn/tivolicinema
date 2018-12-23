# Tivoli Cinema
A web page powered by python that showcase the best movies trailer

# Installation
To install the program please run the following instructions in your terminal:
```
git clone https://github.com/3rwinn/tivolicinema
```
# Usage
### Display the list of movies in a web page:
In your terminal run: `python entertainment_center.py`
### Add a movie to the list
In the _entertain_center.py_ file create a new variable which will contain all the information about the movie you want to add:
```
new_movie = media.Movie("Title", "Storyline", "Poster Image URL", "Trailer Youtube URL")

```
_NB: you can use a variable name of your choice (new_movie is just an example)_

After created the variable for your movie, you need to add it to the *movies* list:
```
movies = [transformers, avengers, now_you_see_me, bird_box, mowgli, casa_de_papel, creed_2, new_movie]
```

# License
This project is licensed under the MIT License
