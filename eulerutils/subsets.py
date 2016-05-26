import itertools

def is_empty(any_structure):
    if any_structure:
        return False
    else:
        return True
        
        
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))
    

def subsets_of_size(iterable, n):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(n,n+1))
    
    
