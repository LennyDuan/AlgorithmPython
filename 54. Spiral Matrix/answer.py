def spiralOrder(matrix: list(list())) -> list():
    results = list()
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    if len(matrix) == 1:
        results = matrix[0]
        print(results)
        return results
    if len(matrix[0]) == 1:
        for i in matrix:
            results.extend(i)
        print(results)
        return results
    m = len(matrix[0]) - 1
    n = len(matrix) - 1
    m_start = 0
    m_end = m
    n_start = 0
    n_end = n

    while m_start != m_end or n_start != n_end:
        # print('start')
        # print('m_start - m_end: [{}][{}]'.format(m_start, m_end))
        # print('n_start - n_end: [{}][{}]\n'.format(n_start, n_end))

        for m_first in range(m_start, m_end + 1):
            # print('m_first matrix: [{}][{}]'.format(n_start, m_first))
            results.append(matrix[n_start][m_first])
        if n_start != n_end:
            n_start += 1
        # print('m_start - m_end: [{}][{}]'.format(m_start, m_end))
        # print('n_start - n_end: [{}][{}]\n'.format(n_start, n_end))
        if m_start == m_end and n_start == n_end:
            break

        for n_first in range(n_start, n_end + 1):
            # print('n_first matrix: [{}][{}]'.format(n_first, m_end))
            results.append(matrix[n_first][m_end])
        if m_start != m_end:
            m_end -= 1
        # print('m_start - m_end: [{}][{}]'.format(m_start, m_end))
        # print('n_start - n_end: [{}][{}]\n'.format(n_start, n_end))
        if m_start == m_end and n_start == n_end:
            break

        for m_second in range(m_end, m_start - 1, -1):
            # print('m_second matrix: [{}][{}]'.format(n_end, m_second))
            results.append(matrix[n_end][m_second])
        if n_start != n_end:
            n_end -= 1
        # print('m_start - m_end: [{}][{}]'.format(m_start, m_end))
        # print('n_start - n_end: [{}][{}]\n'.format(n_start, n_end))
        if m_start == m_end and n_start == n_end:
            break

        for n_second in range(n_end, n_start - 1, -1):
            # print('matrix: [{}][{}]'.format(n_second, m_start))
            results.append(matrix[n_second][m_start])
        if m_start != m_end:
            m_start += 1
        if m_start == m_end and n_start == n_end:
            break
        # print('m_start - m_end: [{}][{}]'.format(m_start, m_end))
        # print('n_start - n_end: [{}][{}]'.format(n_start, n_end))
        # print(m_start != m_end or n_start != n_end)
        # print('end')

    pop = m - n
    if m == n:
        results.append(matrix[n_start][m_start])
    elif m > n:
        results.pop(-pop)
    elif n > m:
        if n - m == 1:
            results.append(matrix[n_start][m_start])
        else:
            results.pop(pop)
    print(results, m, n)
    return results


test0 = [
    [1, 2],
    [3, 4],
]

test1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

test2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

test3 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]

test4 = [
    [1, 2],
    [3, 4],
    [5, 6],
]

test5 = []
test6 = [[]]

test7 = [[6, 9, 7]]
test8 = [[1], [2], [3]]
test9 = [
    [2, 3, 4],
    [5, 6, 7],
    [8, 9, 10],
    [11, 12, 13],
    [14, 15, 16]]

test10 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
]
# spiralOrder(test0)
# spiralOrder(test1)
# spiralOrder(test2)
# spiralOrder(test3)
# spiralOrder(test4)
# spiralOrder(test5)
# spiralOrder(test6)
# spiralOrder(test7)
# spiralOrder(test8)
# spiralOrder(test9)
spiralOrder(test10)