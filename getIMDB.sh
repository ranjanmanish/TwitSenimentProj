#!/bin/bash

if [ -e 'abc' ];
then
	rm -f 'abc'
	rm -fr 'result'
fi
python getIMDB.py >> abc

if [ -e 'abc' ];
then
	while read line
	do
		echo "IMDB Detail for Movie" \""$line"\" >> 'result'
		./imdb2.py \'$line\' >> result
		#sleep 10
	done < 'abc'
fi

