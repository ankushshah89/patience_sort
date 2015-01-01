"""
author: ankush.shah.nitk@gmail.com
date: 1st Jan 2015
desc: This is an implementation of sorting an array using Patience Sort. 
(https://en.wikipedia.org/wiki/Patience_sorting)

The top cards are maintained as an ordered list. This is used to 
find the position of the pile where the next number should be placed. 

Piles are maintained as a list of list. The original array is iterated 
and each element is placed on the correct pile. 

Once the piles are created, the top number of each pile is inserted 
into a heap. Iteratively, the minimum element from the heap is removed and 
a new element from the corresponding pile is inserted into the heap.

The time complexity is O(n \log n) and the space complexity is O(n).
"""

import bisect
import heapq

def find_pile(top_cards, n):
    """
    return the pile_id on which the 
    number 'n' should be placed
    If no such pile exist return -1
    
    It also updates the list of top cards
    """
    pos = bisect.bisect_right(top_cards, n)
    if pos == len(top_cards):
        top_cards.append(n)
        return -1
    else:
        top_cards[pos] = n
        return pos

def patience_sort(a):
    top_cards = [] #maintain the list of top cards of each pile
    piles = [] #each pile will be a python list. 
    
    for i in a:
        pile_id = find_pile(top_cards, i)
        if pile_id == -1:
            pile = [i] #create a new pile
            piles.append(pile)
        else:
            piles[pile_id].append(i)
    
    #piles are created now. 
    #put the top cards of every pile in a heap
    heap = [(pile.pop(),pile_id) for pile_id,pile in enumerate(piles)] 
    sorted_a = []
    while heap:
       i,pile_id  = heapq.heappop(heap)
       sorted_a.append(i)
        
       #get the next top_card from that pile:
       pile = piles[pile_id]
       if len(pile) > 0:
           i = pile.pop()
           heapq.heappush(heap, (i,pile_id))
       
        
    return sorted_a
    
def run():
    a = [2,6,3,1,5,9,2]
    sorted_a = patience_sort(a)
    print sorted_a
    
def test(n=10000):
    import random
    a = random.sample(xrange(1000000), n)
    sorted_a = patience_sort(a)
    sorted_by_python = sorted(a)
    n = len(a)
    assert n == len(sorted_a)
    for i in range(n):
        assert sorted_a[i] == sorted_by_python[i]

if __name__ == "__main__":
    test()
    run()