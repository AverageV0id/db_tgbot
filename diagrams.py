from matplotlib import pyplot as plt


def save_bar(names: list[str], values: list[int], path: str):
    plt.bar(names, values)
    plt.savefig(path)


def save_graph(begin: int, end: int, step: int, func: str, path: str):
    x_value = [x for x in range(begin, end, step)]
    y_value = [eval(func) for x in x_value]



    plt.figure(figsize=(8, 6))
    plt.plot(x_value, y_value, label=func)

    plt.title(func)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.legend()
    plt.savefig(path)


def save_graphs(begin1: int, end1: int, step1: int, func1: str,
               begin2: int, end2: int, step2: int, func2: str, path: str):
    x1_value = [x for x in range(begin1, end1, step1)]
    y1_value = [eval(func1) for x in x1_value]

    x2_value = [x for x in range(begin2, end2, step2)]
    y2_value = [eval(func2) for x in x2_value]

    plt.figure(figsize=(8, 6))
    plt.plot(x1_value, y1_value, label=func1)
    plt.plot(x2_value, y2_value, label=func2)
    plt.title(func1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid()
    plt.legend()
    plt.savefig(path)


