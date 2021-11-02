import numpy as np
class Movie:
    def __init__(self, name, keyword):
        self.name = name
        self.keyword = keyword

class Group:
    def __init__(self, member: Movie):
        self.member = []
        self.member.append(member)
        self.keyword = member.keyword
    
    def update_keyword(self, keyword):
        temp = []
        for key in self.keyword:
            same = False
            for k in keyword:
                if(key == k):
                    same = True
                    break
            if(same == False):
                temp.append(key)
        for k in temp:
            self.keyword.remove(k)

    def add_member(self, member: Movie):
        self.member.append(member)
        self.update_keyword(member.keyword)

def mix_group(group1: Group, group2: Group):
    for mem in group2.member:
        group1.member.append(mem)
    group1.update_keyword(group2.keyword)

def similarity(group1: Group, group2: Group):
    n = max(len(group1.keyword),len(group2.keyword))
    common = 0
    for a in group1.keyword:
        for b in group2.keyword:
            if(a == b):
                common += 1
    return int(common/n * 100)

def findmax(H):
    i_max = 0
    j_max = 0
    for i in range(len(H)):
        for j in range(len(H)):
            if(H[i][j] >= H[i_max][j_max]):
                i_max = i
                j_max = j
    return i_max, j_max

def makeH(gr_list):
    H = np.zeros((len(gr_list), len(gr_list)), dtype= int)
    for i in range(len(gr_list)):
        for j in range(len(gr_list)):
            if(i < j):
                H[i,j] = similarity(gr_list[i], gr_list[j])
            
    return H