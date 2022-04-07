# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
    # def __repr__(self):
    #     return "[{}]".format(", ".join(map(str, self)))

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

def link2list(link):
    new_list = []
    i = 1
    while link is not None:
        new_list.append(link.val)
        link = link.next
    new_list.reverse()
    return new_list

def list2link(list):
    current_link = ListNode(list[0])
    for i in range(len(list)):
        current_link.val = list[i]
        current_link.next = current_link

    return current_link

print(list2link([1, 2, 3, 4, 5]).next.next.next.val)

# list1 = link2list(l1)
# list2 = link2list(l2)

# len_l1 = len(list1)
# len_l2 = len(list2)
# if len_l1 > len_l2:
#     list_len = len_l1 + 1
#     greater_list = list1
#     lesser_list = list2
# if len_l2 >= len_l1:
#     list_len = len_l2 + 1
#     greater_list = list2
#     lesser_list = list1

# next_sum = 0
# ans_list = [0] * list_len

# for i in range(len(greater_list)):
#     if (i + 1) > len(lesser_list):
#         val = 0
#     else:
#         val = lesser_list[i]
#     num = greater_list[i] + val + next_sum
#     next_sum = 0
#     if num >= 10:
#         num = num - 10
#         next_sum = 1
#     ans_list[list_len - i - 1] = num

# ans_list[0] = next_sum

# if ans_list[0] == 0:
#     ans_list.pop(0)

# print(ans_list)
    
            
             


