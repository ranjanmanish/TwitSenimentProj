from __future__ import print_function
import sys
import os
import json
from DBConnect import *
# =============================
# Do not modify above this line
# Do not modify below this line
# =============================
if __name__ == '__main__':
	counter=len(List)
	i = 0
        while ( counter > 0 ):
		name = List[i][0]
		releaseYear = List[i][7]
		if ( name is not None and releaseYear is not None ):
			namereleaseYear = List[i][0]+" ("+List[i][7]+")"
			print (namereleaseYear)
		i = i + 1
                counter = counter - 1
