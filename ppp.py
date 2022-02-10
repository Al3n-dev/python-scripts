import random
random.seed()
line=" "
for i in range(0,300): 
	r=random.randrange(5)
	if r==0 and line[-1]!="x": line=line+"x"
	elif r==1 and line[-1]!="!": line=line+"!"
	elif r==2 and line[-1]!="-": line=line+"+"
	elif r==3 and line[-1]!="+": line=line+"-"
print(line)