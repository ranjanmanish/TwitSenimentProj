#!/bin/bash
echo "Going to take twitter Feed of popular tweets"
python twitterstream_pop.py
echo "Tweeter Feed extraction of popular tweets Ended"
echo "Now going to Get text to save it for UI"
python getMovieText_pop.py
echo "Text was wriiten to File"

