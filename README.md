External-Sort
=============

About the code : This folder has 2 files --
		 1. lfile.py - to generate a text file with random numbers
		 2. problem3.py - Python file to have implementation of external sort


How to run the code. 
1. From the linux terminal go to the directory where code is present

2. Create a "largefile.txt" using the lfile.py module by typing 

	python lfile.py

3. If one wishes to sort multiple files then run the above command multiple times
   by changing the output file name in lfile.py. It will create multiple files with 
   random numbers in it. You can also vary the file sizes by changing the number of 
   iteration in the for loop. Copy all the files to a input directory (say Input). 

4. Type "python" (without quotes)

5. Suppose the input directory name in "Input" and you want to produce a sorted file by
   name "output.txt"

6. Type the following lines in the terminal

	import problem3 as pr

	ob = pr.sort('Input','out.txt')
	
	ob.external_sort()

7. Process 6. will take some time to sort the files in the given input directory.
8. To rotate a sorted list type
	
	ob.rotate()
   
   Follow the steps asked by the function. The output response will be in a text file
   "rotate.txt" in the same folder where the problem3.py is present
9. To get the minimum element in the sorted rotated file type the command

	ob.find_min()

Sample Run

anurag@Anurag:~/Desktop/Problem2$ python

	>>> import problem3 as pr
	>>> ob = pr.sort('Input','out.txt')
	>>> ob.external_sort()
	Creating Chunk: 0
	Creating Chunk: 1
	Creating Chunk: 2
	Creating Chunk: 3
	Creating Chunk: 4
	Creating Chunk: 5
	Creating Chunk: 6
	Creating Chunk: 7
	Creating Chunk: 8
	Creating Chunk: 9
	Creating Chunk: 10
	Creating Chunk: 11
	Creating Chunk: 12
	Creating Chunk: 13
	Creating Chunk: 14
	Creating Chunk: 15
	Creating Chunk: 16
	Creating Chunk: 17
	Creating Chunk: 18
	Creating Chunk: 19
	Creating Chunk: 20
	Creating Chunk: 21
	Creating Chunk: 22
	Creating Chunk: 23
	Merging chunks, Please wait till the processing ends!!!
	Performing Essential cleanups !!!
	>>> ob.rotate()
	Enter the value of N
	20000
	Enter the number of times you want to perform rotation
	Hit enter if you want perform random number of rotations
	
	>>> ob.find_min()
	Minimum number in rotated list is: 10

