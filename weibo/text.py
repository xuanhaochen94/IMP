import sys

def read(edges):
    sys.stdin = open("rel_users.sql")
    for i in range(23):
        input()

    while True:
        str = input()
        if str[:11] == "INSERT INTO":
            line = "[" + input()[30:-1] + "]"
            edges += eval(line)
        else:
            break

def get_fans(edges, fans):
    def add_edge(u, v):
        if u not in fans:
            fans[u] = []
        fans[u].append(v)

    for edge in edges:
        if edge[3] == 0:
            add_edge(edge[2], edge[1])
        else:
            add_edge(edge[1], edge[2])


def max_fans(fans, l, r):
    fans = fans.items()
    fans = sorted(fans, key=lambda x:len(x[1]))
    fans.reverse()
    return fans[l:r]

def get_str(fans):
    left = {}
    for i in range(len(fans)):
        left[fans[i][0]] = len(left)+1

    edges = []
    right = {}
    for i in range(len(fans)):
        for j in fans[i][1]:
            if j not in left:
                if j not in right:
                    right[j] = len(right) + 1 + len(left)
                edges.append("%d %d\n"%(left[fans[i][0]], right[j]))
    fout = open("graph.txt", "w")
    fout.write("%d %d\n"%(len(left)+len(right), len(edges)))
    print("written first line")
    str = "".join(edges)
    print("get str")
    fout.write(str)
    print("written str")
    print(len(left), len(right))
    fout.close()
