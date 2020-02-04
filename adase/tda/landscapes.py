import numpy as np

def landscapes(diagram, nb_landscapes=5, num_points=50):
    ldc = np.zeros((nb_landscapes, num_points))

    if len(diagram) == 0:
        return np.array([[0]])

    if np.max(diagram) == np.float64('inf'):
        diagram = diagram[:-1]

    stp = np.linspace(np.min(diagram), np.max(diagram), num=num_points)
    for idx, ele in enumerate(stp):
        val = []
        for pair in diagram:
            b, d = pair[0], pair[1]
            if (d + b) / 2.0 <= ele <= d:
                val.append(d - ele)
            elif b <= ele <= (d + b) / 2.0:
                val.append(ele - b)
        val.sort(reverse=True)
        val = np.asarray(val)
        for j in range(nb_landscapes):
            if (j < len(val)): ldc[j, idx] = val[j]
        del val
    del stp

    return ldc