from sys import argv
l=map(int,argv[1:])
print(sum(l))
print(sum([int(x) for x in argv[1:]]))


def tr(x):
    l = []
    if int(x)<2:
        l.append(x)
    return l
print(list(filter(tr,argv[1:])))


