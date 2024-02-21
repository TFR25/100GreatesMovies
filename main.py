import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Define the target URL
url = "https://www.empireonline.com/movies/features/best-movies-2/"

# Get the current date and time in a formatted string
date = datetime.now().strftime("%b.%d,%Y %H:%M:%S")

# Try connecting to the website and handle potential exceptions
try:
    # Fetch the webpage content using requests
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception if request failed

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all movie titles within h3 elements
    movies = soup.find_all("h3")

    # Extract movie names and reverse the order (optional)
    movie_names = [movie.text.strip() for movie in reversed(movies)]

    # Create the output file and include the date and time it was created
    with open("100_Greatest_Movies.txt", "a", encoding="utf-8") as file:
        file.write("=" * len(f"\n100 Greatest Movies Of All Time as of {date}\n"))  # Add the underline
        file.write(f"\n100 Greatest Movies Of All Time as of {date}\n")
        file.write("=" * len(f"100 Greatest Movies Of All Time as of {date}\n"))
        file.write("\n")

        # Write each movie name to the file
        for movie_name in movie_names:
            file.write(f"{movie_name}\n")

    # Print a confirmation message (optional)
    print("Movie list saved to 100_Greatest_Movies.txt!")

except requests.exceptions.RequestException as e:
    print(f"Error connecting to the website: {e}")

except FileNotFoundError as e:
    print(f"Error creating or writing to the file: {e}")



