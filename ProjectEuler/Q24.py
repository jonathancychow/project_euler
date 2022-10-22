from itertools import islice, permutations

num_list = list(range(10))
permut = permutations(list(map(str, num_list)))
Ans = (next(islice(permut, 999999, None)))
print(''.join(Ans))
