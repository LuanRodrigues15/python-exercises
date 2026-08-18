student_scores = [180, 124, 199, 100, 50, 30, 173]

maxFor = 0
sumFor = 0
for score in student_scores:
    if (score > maxFor):
        maxFor = score
    
    sumFor+= score
        
print(f"max: {maxFor}")
print(f"sum: {sumFor}")

print("Functions:")
print(max(student_scores))
print(sum(student_scores))