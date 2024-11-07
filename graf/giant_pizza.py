import sys
sys.setrecursionlimit(500000)

def tarjan_scc(n, adj):
    index = [None] * n
    lowlink = [None] * n
    on_stack = [False] * n
    stack = []
    sccs = []
    idx = [0]

    def strongconnect(v):
        index[v] = lowlink[v] = idx[0]
        idx[0] += 1
        stack.append(v)
        on_stack[v] = True

        for w in adj[v]:
            if index[w] is None:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif on_stack[w]:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            scc = []
            while True:
                w = stack.pop()
                on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            sccs.append(scc)

    for v in range(n):
        if index[v] is None:
            strongconnect(v)

    return sccs

def solve_2sat(n, clauses):
    adj = [[] for _ in range(2 * n)]

    def add_implication(u, v):
        adj[u].append(v)

    for x, y in clauses:
        x_var = abs(x) - 1
        y_var = abs(y) - 1
        x_is_true = x > 0
        y_is_true = y > 0

        add_implication(x_var * 2 + (not x_is_true), y_var * 2 + y_is_true)
        add_implication(y_var * 2 + (not y_is_true), x_var * 2 + x_is_true)

    sccs = tarjan_scc(2 * n, adj)
    component = [-1] * (2 * n)
    for i, scc in enumerate(sccs):
        for node in scc:
            component[node] = i

    assignment = [False] * n
    for i in range(n):
        if component[2 * i] == component[2 * i + 1]:
            return None
        assignment[i] = component[2 * i] > component[2 * i + 1]

    return assignment

def main():
    input = sys.stdin.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    clauses = []
    index = 2
    for _ in range(m):
        t1 = data[index]
        x1 = int(data[index + 1])
        t2 = data[index + 2]
        x2 = int(data[index + 3])
        index += 4
        x1 = x1 if t1 == '+' else -x1
        x2 = x2 if t2 == '+' else -x2
        clauses.append((x1, x2))

    result = solve_2sat(n, clauses)
    if result is None:
        print("IMPOSSIBLE")
    else:
        print(''.join('+' if x else '-' for x in result))

if __name__ == "__main__":
    main()
