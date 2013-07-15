#!/bin/bash
echo "Going to get all the Recent tweets and Select 15 text out of them"
#./job_rec.sh

echo "Going to get all the popular tweets and get all of them"
#./job.pop.sh

cd logs
for file in *.txt
do
	echo $file
done
