import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = ''' 
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Tivoli Cinema - Best movies trailer</title>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css"
      integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
      crossorigin="anonymous"
    />
    <style type="text/css">
      body {
        background-color: #000000;
      }
      #trailer .modal-dialog {
        margin-top: 200px;
        width: 640px;
        height: 480px;
      }
      .hanging-close {
        position: absolute;
        top: -12px;
        right: -12px;
        z-index: 9001;
      }
      #trailer-video {
        width: 100%;
        height: 100%;
      }
      .movie {
        background-color: #171717;
        cursor: pointer;
        width: 16rem;
      }
      .movie:hover {
        margin-top: 0.5rem;
      }
      .scale-media {
        padding-bottom: 56.25%;
        position: relative;
      }
      .scale-media iframe {
        border: none;
        height: 100%;
        position: absolute;
        width: 100%;
        left: 0;
        top: 0;
        background-color: white;
      }
    </style>
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js"
      integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js"
      integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k"
      crossorigin="anonymous"
    ></script>
    <script type="text/javascript" charset="utf-8">
      // Pause the video when the modal is closed
      $(document).on(
        "click",
        ".hanging-close, .modal-backdrop, .modal",
        function(event) {
          // Remove the src so the player itself gets removed, as this is the only
          // reliable way to ensure the video stops playing in IE
          $("#trailer-video-container").empty();
        }
      );
      // Start playing the video whenever the trailer modal is opened
      $(document).on("click", ".card", function(event) {
        var trailerYouTubeId = $(this).attr("data-trailer-youtube-id");
        var sourceUrl =
          "http://www.youtube.com/embed/" +
          trailerYouTubeId +
          "?autoplay=1&html5=1";
        $("#trailer-video-container")
          .empty()
          .append(
            $("<iframe></iframe>", {
              id: "trailer-video",
              type: "text-html",
              src: sourceUrl,
              frameborder: 0
            })
          );
      });

    </script>
  </head>


'''

# The main page layout and title bar
main_page_content = ''' 
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a
            href="#"
            class="hanging-close"
            data-dismiss="modal"
            aria-hidden="true"
          >
            <img
              src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"
            />
          </a>
          <div class="scale-media" id="trailer-video-container"></div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container">
      <div class="row mt-4">
        <div class="col-12 col-lg-2 p-0 m-0">
          <div
            id="logo"
            class="d-flex justify-content-center justify-content-lg-end"
          >
            <img src="logov2.svg" alt="tivoli" height="123" width="123" />
          </div>
        </div>
        <div class="col-12 col-lg-10">
          <div class="d-flex flex-wrap justify-content-center justify-content-lg-start">
            {movie_tiles}
            
            
          </div>
        </div>
      </div>
    </div>
    
  </body>
</html>

'''

# A single movie entry html template
movie_tile_content = '''
<div class="card text-white mr-2 mb-2 movie" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img width="200" height="322" src="{poster_image_url}" class="card-img" alt="movie" />
    <div class="card-body">
        <h5 class="card-title">{movie_title}</h5>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('tivoli_cinema.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
