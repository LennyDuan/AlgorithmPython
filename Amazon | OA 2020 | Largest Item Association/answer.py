from collections import defaultdict, deque


#
# def largest_item_association(items_list):
#     res = list()
#     item_dict = defaultdict(list)
#     for items in items_list:
#         item_dict[items[0]].append(items[1])
#         item_dict[items[1]].append(items[0])
#     print(item_dict)
#
#     def dfs(visited, key, c_list):
#         associateds_items = item_dict.get(key)
#
#         for need_to_check_item in associateds_items:
#             if need_to_check_item in visited:
#                 res.append(c_list)
#                 continue
#             else:
#                 visited.append(need_to_check_item)
#                 c_list.append(need_to_check_item)
#                 dfs(visited, need_to_check_item, c_list)
#
#     for start_item in list(item_dict.keys()):
#         visited = list([start_item])
#         dfs(visited, start_item, [start_item])
#     return sorted(max(res))


def largest_item_association(item_association):
    item_map = defaultdict(set)

    for item_pair in item_association:
        item_map[item_pair[0]].add(item_pair[1])
        item_map[item_pair[1]].add(item_pair[0])
    print(item_map)
    largest_group = []
    visited = set()

    for key, val in item_map.items():
        if key not in visited:
            curr_group = []
            q = deque()
            q.append(key)
            while q:
                curr = q.popleft()
                visited.add(curr)
                curr_group.append(curr)
                for neighbor in item_map[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
            print(curr_group)
            if len(curr_group) > len(largest_group):
                largest_group = curr_group.copy()

    largest_group.sort()
    return largest_group


print(largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
# print(largest_item_association([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1", "item4"]]))
