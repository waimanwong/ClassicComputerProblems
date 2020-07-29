from __future__ import annotations

from typing import Protocol, TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar('C', bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, value):
        ...

    def __lt__(self, value):
        ...

    def __gt__(self, value):
        return (not self < value) and self != value
    
    def __le__(self, value):
        return self < value or self == value

    def __ge__(self, value):
        return not self < value

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low = 0
    high = len(sequence) - 1

    while low <= high :
        mid = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    
    return False

if __name__ == "__main__":
    print (linear_contains([1,5, 15, 15, 15, 15, 20], 5))

    print (binary_contains(['a', 'd', 'e', 'f', 'z'], 'f'))
    print (binary_contains(['john', 'mark', 'ronald', 'sarah'], 'sheila'))
