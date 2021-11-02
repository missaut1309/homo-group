import numpy as np
import random

from classes import *
a = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
movie_list = []
gr_list = []
i = 0
T = 45
while(i < 20):
    kw_list = random.sample(a,7)
    movie_list.append(Movie("Phim %d"%(i), kw_list))
    gr_list.append(Group(movie_list[i]))
    i += 1

for m in movie_list:
    print(m.name)
    print(m.keyword)

while(True):
    H = makeH(gr_list)
    i,j = findmax(H)
    if(H[i,j] > T):
        mix_group(gr_list[i], gr_list[j])
        gr_list.pop(j)
    else:
        break

for gr in gr_list:
    for m in gr.member:
        print(m.name)
    print("-----")



