print(sum([(i+j)%3+1+(j-1)*3 for i,j in [[(ord(j)-64)%23 for j in i.split(' ')] for i in open('input.txt').read().strip().split('\n')]]))