patience_sort
=============

This is an implementation of sorting an array using Patience Sort. 
(https://en.wikipedia.org/wiki/Patience_sorting)

The top cards are maintained as an ordered list. This is used to 
find the position of the pile where the next number should be placed. 

Piles are maintained as a list of list. The original array is iterated 
and each element is placed on the correct pile. 

Once the piles are created, the top number of each pile is inserted 
into a heap. Iteratively, the minimum element from the heap is removed and 
a new element from the corresponding pile is inserted into the heap.

The time complexity is O(n \log n) and the space complexity is O(n).
