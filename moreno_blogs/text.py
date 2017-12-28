import sys
def read(fans):
    sys.stdin = open("out.moreno_blogs_blogs")
    input()
    input()
    while True:
        try:
            line = input().split(' ')
        except:
            break
        u = int(line[0])
        v = int(line[1])
        if v not in fans:
            fans[v] = []
        fans[v].append(u)

def max_fans(fans, l, r):
    fans = fans.items()
    fans = sorted(fans, key=lambda x:len(x[1]))
    fans.reverse()
    return fans[l:r]

def get_str(fans):
    left = {}
    for i in range(len(fans)):
        left[fans[i][0]] = []

    edges = []
    right = set()
    for i in range(len(fans)):
        for j in fans[i][1]:
            if j not in left:
                right.add(j)
                edges.append("%d %d\n"%(fans[i][0], j))
    fout = open("graph.txt", "w")
    fout.write("%d %d\n"%(len(left)+len(right), len(edges)))
    print("written first line")
    str = "".join(edges)
    print("get str")
    fout.write(str)
    print("written str")
    print(len(left), len(right))
    fout.close()


def get_graph(fans):
    max_fan = 0
    cnt = [0 for i in range(3000)]
    for u in fans:
        max_fan = max(max_fan, len(fans[u]))
        cnt[len(fans[u])] += 1

    s = 0
    for i in range(0, 3000):
        s += cnt[i]
        cnt[i] = s

    for i in range(0, 3000):
        if cnt[i] != cnt[i-1]:
            print(i, cnt[i], sep="\t")

fans = {}
read(fans)
fanlist = max_fans(fans, 0, 100)
get_str(fanlist)
