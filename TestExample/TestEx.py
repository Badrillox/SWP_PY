def median(dataset):
    n = len(dataset)
    sort(dataset)
    if n % 2 == 0:
        median1 = dataset[n // 2]
        median2 = dataset[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = dataset[n // 2]
    return median


def avg(dataset):
    sumd = sum(dataset)
    count = len(dataset)
    return sumd / count


def sort(dataset):
    n = len(dataset)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if dataset[j] > dataset[j + 1]:
                dataset[j], dataset[j + 1] = dataset[j + 1], dataset[j]


if __name__ == '__main__':
    list = [1, 2, 3, 6, 8, 9, 10]
    print("Average: ", avg(list))
    print("Median: ", median(list))
