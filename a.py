from classes import *


a = Movie("A",[1,2,3,5,7])
b = Movie("B",[1,2,3,6,8])
c = Movie("C",[1,3,5,6,9])
d = Movie("D",[1,5,8,10,12])
e = Movie("E",[2,5,10,11,15])
f = Movie("F",[4,5,8,12,15])
g = Movie("G",[1,4,5,8,12])
h = Movie("H",[1,4,6,8,15])
i = Movie("I",[3,5,7,9,10])
j = Movie("J",[3,6,8,9,15])

movie_list = [a,b,c,d,e,f,g,h,i,j]
gr_list = []
for m in movie_list:
    print(m.name)
    print(m.keyword)
    gr_list.append(Group(m))
T = 60
while(True):
    H = makeH(gr_list)
    i,j = findmax(H)
    if(H[i,j] >= T):
        mix_group(gr_list[i], gr_list[j])
        gr_list.pop(j)
    else:
        break

for gr in gr_list:
    for m in gr.member:
        print(m.name)
    print("-----")