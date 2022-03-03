N, M, L = [int(x) for x in input().split(' ')]

folds = [int(x) for x in input().split(' ')]
cuts = [int(x) for x in input().split(' ')]


intervals = [[0, L]]

def make_fold(f, left=True):
    top_fold = intervals[-1]
    B = top_fold[0]
    E = top_fold[1]

    k = E-f if left else B+f

    sp, ep = None, None
    if left == True:
        #sp = E - ((E-k)*2)
        sp = E - f*2
        ep = k
        top_fold[1] = ep
    else:
        sp = k
        #ep = B + ((k-B)*2)
        ep = B + f*2
        top_fold[0] = sp
    
    new_interval = [sp, ep]
    intervals.append(new_interval)

left = True
for fold in folds:
    make_fold(fold, left)
    left = not left

intervals.sort(key = lambda x: x[0])

sum_per_cut = [0]
prefix_sum = [0]

def make_cut(cut):
    global intervals
    total_length = 0
    for interval in intervals:
        lb, rb = interval
        if lb >= cut: break
        rb = min(rb, cut)
        total_length += abs(rb - lb)
    real_dist = total_length-prefix_sum[-1]
    sum_per_cut.append(real_dist)
    prefix_sum.append(prefix_sum[-1] + real_dist)

for cut in cuts:
    make_cut(cut)

missing = L - sum(sum_per_cut)
[print(x) for x in sum_per_cut[1:]]
print(missing)
        