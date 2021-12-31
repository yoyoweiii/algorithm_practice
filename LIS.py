import bisect
nums = [1,3,5,4,7,10,8,2,8]

if not nums: print(0)
    
decks, ends_decks, paths = [], [], []
for num in nums:
    deck_idx = bisect.bisect_left(ends_decks, num)
    n_paths = 1
    if deck_idx > 0:
        l = bisect.bisect(decks[deck_idx-1], -num)
        n_paths = paths[deck_idx-1][-1] - paths[deck_idx-1][l]
                
    if deck_idx == len(decks):
        decks.append([-num])
        ends_decks.append(num)
        paths.append([0,n_paths])
    else:
        decks[deck_idx].append(-num)
        ends_decks[deck_idx] = num
        paths[deck_idx].append(n_paths + paths[deck_idx][-1])
              
print(paths[-1][-1])
