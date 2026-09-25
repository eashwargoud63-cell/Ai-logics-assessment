total = int(input())
ranges = []
for _ in range(total):
    left, right = map(int, input().split())
    ranges.append([left, right])
ranges.sort()
merged = []
for left, right in ranges:
    if merged and left <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], right)
    else:
        merged.append([left, right])
for left, right in merged:
    print(left, right)