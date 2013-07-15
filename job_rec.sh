#!/bin/bash
echo "Going to take twitter Feed of popular tweets"
python twitterstream_rec.py
echo "Tweeter Feed extraction of popular tweets Ended"
echo "Now going to Get text to save it for UI"
python getMovieText_rec.py
echo "Text was wriiten to File"


