from typing import List

def list_avg(sequence: List) -> float:
    return sum(sequence)/len(sequence)

print(list_avg([123,34,4,4,43]))
