def hist_maker(students_results):
    import math
    students_results.sort()
    elements_num = len(students_results)
    min_num = min(students_results)
    max_num = max(students_results)
    gap = max_num - min_num
    intervals_num = math.ceil(1 + 3.322 * math.log10(elements_num))
    amplitude = math.ceil(gap / intervals_num)
    interval_bounds = [min_num + num * amplitude for num in range(intervals_num)]

    lower_ = interval_bounds[:-1]

    upper_ = interval_bounds[1:]
    upper_ = [min(hi - 1, 100) for hi in upper_]

    if upper_[-1] < 100:
        lower_.append(upper_[-1] + 1)
        upper_.append(100)
    interval_values = [[] for _ in range(len(lower_))]
    for num in students_results:
        for i, (lo, hi) in enumerate(zip(lower_, upper_)):
            if lo <= num <= hi:
                interval_values[i].append(num)
                break
    F = [len(interval_list) for interval_list in interval_values]
    Fa = [sum(F[:x]) for x in range(1, len(F) + 1)]
    # Num_of_class = [num for num in range(1, intervals_num + 1)]
    result = [
        [i + 1, [lower_[i], upper_[i]], F[i], Fa[i]]
        for i in range(len(lower_))
    ]

    return result
