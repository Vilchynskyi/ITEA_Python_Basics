# function that calculates the arithmetic average
if __name__ == '__main__':
    q = [56, 3, 90, 573]
    w = int(q[0])
    e = int(q[1])
    r = int(q[2])
    t = int(q[3])
    def sum(w, e, r, t):
        return (w + e + r + t) / 4
    print(sum(w, e, r, t))
