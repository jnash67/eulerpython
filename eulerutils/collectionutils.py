import itertools

# http://stackoverflow.com/questions/464864/python-code-to-pick-out-all-possible-combinations-from-a-list
def all_subsets(ss):
    return itertools.chain(*map(lambda x: itertools.combinations(ss, x), range(0, len(ss) + 1)))


# http://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
def dict_key_with_max_val(d):
    """ a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]


def any_greater_than_n_in_number_list(list, n):
    for i in list:
        if i>n:
            return True
    return False


def do_collections_share_an_item(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False