# zip in action

# list_a = [1, 2, 3]
# list_b = [4, 5, 6]

# zipped = zip(list_a, list_b) # Output: Zip Object. <zip at 0x4c10a30>

# print(list(zipped)) 
# print(list(zipped))  # zip follows lazy evaluation, so it gets exhausted after first call


# HackerRank Problem Starts Here....

N, X = map(int, input().split())
# print("Students = ", N)
# print("Subjects = ", X)

scores = []

for _ in range(X):
    score = map(float, input().split())
    scores.append(score)

# print(scores)

for s in zip(*scores):
    print( sum(s)/len(s) ) 

