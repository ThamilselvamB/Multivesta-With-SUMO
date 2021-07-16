import random
#input file
fin = open("data/cross1.sumocfg", "rt")
#output file to write the result to
fout = open("data/cross.sumocfg", "wt")
randomNum = random.randint(1,20)
#for each line in the input file
for line in fin:
	#read replace the string and write to output file
	
	replaceValue = "cross.rou.xml"
	replaceToValue = "routes/cross_"+str(randomNum) +".rou.xml"
	fout.write(line.replace(replaceValue,replaceToValue ))
#close input and output files
fin.close()
fout.close()
