def union(set1,set2):
    """
    set1 and set2 are collections of objects of the same type.
    
    This function returns one set containing all elements from both input
    sets, but with no duplicates.
    """
    if len(set1)==0:
        return set2
    elif set1[0] in set2:
        return union(set1[1:],set2)
    else:
        return set1[0] + union(set1[1:],set2)