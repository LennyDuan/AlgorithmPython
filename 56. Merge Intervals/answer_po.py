## Possible but too much if else

def merge(self, intervals):
    res = [intervals[0]]
    for interval in intervals[1:]:
        c_start, c_end = interval[0], interval[1]
        for merged in res:
            print('current: {}'.format(interval))
            print('merged: {}'.format(merged))
            m_start, m_end = merged[0], merged[1]
            if m_start < c_start < m_end < c_end:
                merged[1] = c_end
            elif c_start < m_start < c_end < m_end:
                merged[0] = c_start
            elif c_start < m_start < c_end < m_end:
                merged[0] = c_start
            elif c_start < m_start < m_end < c_end:
                merged[0], merged[1] = interval[0], interval[1]
            elif c_start == m_start:
                merged[1] = max(m_end, c_end)
            elif c_start == m_end:
                merged[1] = c_end
            elif c_end == m_start:
                merged[0] = c_start
            elif c_end == m_end:
                merged[0] = min(m_start, c_start)
            elif m_start < c_start < c_end < m_end:
                break
            else:
                res.append(interval)
                break

    return res


intervals = [[1, 4], [0, 5]]
# [[1,4],[0,2]]
# [[1,4],[0,1]]
# [[1,4],[4,5]]
# [[1,4],[1,5]]
# [[1, 3], [2, 6], [8, 10], [15, 18]]
# intervals = [[2, 6], [1, 3], [8, 10], [15, 18]]

# [[1,6],[8,10],[15,18]]
print(merge(None, intervals))
