# Lyrics-Scraper
Just a simple web scraper utilizing the Genius API to extract lyrics from the web. I use this in my various other fun side projects involving music!

# How to Use:

1. First, you must obtain an API token from [Genius](https://docs.genius.com/), directions on how to do so are clearly labeled on their website.
2. Next, prepare your Python environment! You will need to pip install these modules:
  - `requests`
  - `bs4 from BeautifulSoup`
  - `os`
  - `re` 
3. Create a `secrets.py` file (which should be placed in your .gitignore) and store your Genius API token as follows:
`GENIUS_API_TOKEN = '<your API token>'`
4. Simply fill in your artist and number of songs to scraped for lyrics, for example:
```
if __name__ == '__main__':
    write_lyrics_to_file('My Chemical Romance', 100)
```
5. Enjoy your lyrics! They will be printed to a txt file with the artist name as it's title.

