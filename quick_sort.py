import random


def quick_sort(lst: list):
    if len(lst) < 2:
        return lst
    elif len(lst) == 2:
        return lst if lst[0] <= lst[-1] else lst[::-1]
    else:
        pivot_idx = random.randint(0, len(lst) - 1)
        pivot_value = lst[pivot_idx]
        less, greater = [], []
        for item_idx, item in enumerate(lst):
            if item_idx != pivot_idx:
                if item <= pivot_value:
                    less.append(item)
                else:
                    greater.append(item)
        return quick_sort(less) + [pivot_value] + quick_sort(greater)


if __name__ == '__main__':
    print(random_sample := random.sample(range(0, 100), 10))
    print(quick_sort(random_sample))
