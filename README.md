# geniusthief.py
Python Script meant to scrape lyrics data by artist from Genius using Genius API. Inspired by [this 2019 article](https://medium.com/analytics-vidhya/how-to-scrape-song-lyrics-a-gentle-python-tutorial-5b1d4ab351d2) initally, but made to work with in 2023.

Feel free to collaborate and work on this deeper, as I won't probably continue work on this beyond this point.

Before using make sure to install `requests` and `bs4` with:
```
pip install requests
pip install bs4
```
or 
```
pip3 install requests
pip3 install bs4
```

## Instructions on how to use:

1. Get a Genius API Token [here](https://medium.com/analytics-vidhya/how-to-scrape-song-lyrics-a-gentle-python-tutorial-5b1d4ab351d2).

2. Insert your token in the `TOKEN` variable.

3. IMPORTANT! Make sure that the `div`'s class name in `lyrics_container` variable inside of the `scrape_song_lyrics(url)` function is correct. You can do that by inspecting the element on the page of the artist you need.

4. Insert the artist name in the end of the file. 

5. Create a folder `lyrics` inside of the folder with the script before running it. You can easily do it by running this command in the terminal:
```
mkdir ./lyrics 
```

### That's it! You can use your lyrics text file for your purposes.

Feel free to give any inquiries and contact me @ https://notalim.com/
