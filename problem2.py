n = int(input())
values = list(map(int, input().split()))
limit = int(input())
low = []
high = []
left = 0
longest = 0
answer_start = 1
for right in range(n):
    # Maintain the smallest value
    while low and values[low[-1]] >= values[right]:
        low.pop()
    low.append(right)
    # Maintain the largest value
    while high and values[high[-1]] <= values[right]:
        high.pop()
    high.append(right)
    # Shrink the window if it is not stable
    while values[high[0]] - values[low[0]] > limit:
        if low[0] == left:
            low.pop(0)
        if high[0] == left:
            high.pop(0)
        left += 1
    size = right - left + 1
    if size > longest:
        longest = size
        answer_start = left + 1
print(longest, answer_start)