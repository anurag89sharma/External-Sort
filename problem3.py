import sys
import os
import random
from tempfile import gettempdir
from itertools import islice, cycle, imap
import heapq


# class to perform External Sorting
class sort(object):
	
    # Constructor for the class, initializes various variables
    def __init__(self,indir,outfile):
	# Variable to store Input director path
	self.input = indir
	# variable to store output-file name
	self.outfile = outfile
	# File to store rotation of the sorted List
	self.rotatefile = "rotate.txt"
	# Temp file to do intermediate processing
	self.tmpfile = "tmp.txt"
	# Buffer size 
	self.buffer_size = 1280000
	# Chunk size for temporary files
	self.chunk_size = 1024 * 1024
	self.tempdir = '/tmp'

	# Perform Necessary cleanup
	if os.path.exists(self.rotatefile):
	    os.remove(self.rotatefile)
	if os.path.exists(self.tmpfile):
	    os.remove(self.tmpfile)

    # Function to perform merging of small chunks formed
    # by slicing of the larger files. This function requires 
    # that the immediate chunk files are already in sorted order. 
    # It then performs sorted merging of these chunks using merge 
    # function of python library "heapq" 
    def merge(self, *flist):
	print "Merging chunks, Please wait till the processing ends!!!"
        out = heapq.merge(*[imap(int, f) for f in flist])
        with open(self.outfile,'w+b', self.chunk_size) as output_file:
    	    for element in out:
	        output_file.writelines(str(element) + '\n')
    
    # Function which reads the input directory and break files present 
    # in the directory into smaller chunks of size "64 * 1024". Use the 
    # inbuilt sort to sort them and store them in "/tmp" directory. After
    # merging these chunks gets deleted from "/tmp" folder 
    def external_sort(self):
        chunks = []
        try:
	    # For each file in input directory
	    for item in os.listdir(self.input):
	        fpath = self.input + '/' + item
		# load a portion (buffer upto "chunk_size" in memory) of file 
                with open(fpath,'rb',self.chunk_size) as fin:
                    input_iter = iter(fin)
		    for item in input_iter:
		        # slice the loaded content into 1280000 ("buffer_size") elements
			chunk = list(islice(input_iter,self.buffer_size))
		        # sort those buffers
		        chunk.sort(key = lambda x : int(x))
		        # write the above sorted buffers on the disk in "/tmp" directory
                        out_chunk = open(os.path.join(self.tempdir,'%06i'%len(chunks)),'w+b')
			print "Creating Chunk: " + str(len(chunks))
                        chunks.append(out_chunk)
                        out_chunk.writelines(chunk)
                        out_chunk.flush()
		        # Place the file pointer to the beginning of the chunk
                        out_chunk.seek(0)
	    # call merge to combine the chunks into a single large file
	    self.merge(*chunks)    
	# Finally perform cleanup task, remove the chunks form the "/tmp" directory 
        finally:
	    print "Performing Essential cleanups !!!"
	    for chunk in chunks:
               try:
                    chunk.close()
                    os.remove(chunk.name)
               except Exception, e:
                    print "Error " + e


    # Function to perform retation of the sorted file. It ask a user for "N", the number
    # of elements and "r" the number of times rotation has to be performed. The idea is to 
    # read first "N" lines from the sorted output file and first r lines are stroed in a temp
    # file and next "N-r" lines are stored in the "rotate.txt". After that append the "r" lines
    # from temp file to "rotate.txt"
    def rotate(self):
	print "Enter the value of N"
	N = raw_input()
	N = int(N)
	print "Enter the number of times you want to perform rotation"
	print "Hit enter if you want perform random number of rotations"
	r = raw_input()
	# If r is not entered then take some random integer between 1 and "N"
	if r == '':
	    r = int(random.randrange(1,N))
	else:
	    r = int(r)

	tf = open(self.tmpfile,'a')
	rf = open(self.rotatefile,'a')
	# read the first "N" lines of sorted file produced by calling "external_sort()" function
	# store "r" lines in a temp file and "N-r" in "rotate.txt". After that append the temp file
	# into "rotate.txt" 
	with open(self.outfile, 'r') as ofile:
	    i = 0
	    for line in islice(ofile, N):
		if i < r:		
		    tf.write(line)
		else : 
		    rf.write(line)
		i += 1
	tf.close()
	with open(self.tmpfile, 'r') as tmpfile:
	    for i in xrange(r):
	        line = tmpfile.readline()
	        rf.write(line)

	rf.close()
	os.remove(self.tmpfile)

    # Function to find minimum number in the sorted rotated text file"rotate.txt"
    # Given an O(n) solution here, due to the condition that the file can contain 
    # duplicate entries. Can prapose an O(lg(n)) solution, binary search on a 
    # sorted rotated array if the array contains unique elements. 
    def find_min(self):
	min_ = sys.maxint
	with open(self.rotatefile) as infile:
            for line in infile:
		a = int(line.strip())
	    	if a < min_:
		    min_ = a
	print "Minimum number in rotated list is: " + str(min_)

