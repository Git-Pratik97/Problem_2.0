n = int(input())
ar = list(map(int, input().rstrip().split()))

my_dict = {i:ar.count(i) for i in ar}
print(my_dict)
count = 0
for key, value in my_dict.items():
    count += value//2
print(count)