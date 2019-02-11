'''
dict = {'A':46, 'B':13}
print(dict.keys())
print(type(dict.keys()))

print(list(dict.keys()))
print(type(list(dict.keys())))
'''


'''
def csv_w_test():
    w_li = [1,2,3,4,5]
    w_li2 = ['a','b','c','d','e']
    with open('csv_w.txt', 'a') as f:
        for item in w_li:
            f.write(str(item))

csv_w_test()
'''

''''''

'''
def partA(l):
    l.sort(key=abs)


def fNdis(v):
    return (v[0] * v[0] + v[1] * v[1])


def partB(l):
    l.sort(key=fNdis)

TT = [[1,4], [1,5], [1,3], [1,2], [1,1]]
partB(TT)
print(TT)
'''
import re
K = 3
leng = '123456789'
print(leng[:4])
print(leng[1:])
#leng = leng + '-'.join(leng)
#print(leng)
a = re.findall('.{%s}'%K,leng)
newlen = '-'.join(a)
print(newlen)

for n in range(3,10):
	print(n)