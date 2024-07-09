def max_score(points,k):
    n=len(points)
    total_sum=sum(points)
    window_sum=sum(points[:n-k])
    max_score=total_sum-window_sum
    for i in range(n-k,n):
        window_sum+=points[i]-points[i-(n-k)]
        max_score = max(max_score,total_sum-window_sum)
    return max_score

# Example Test cases
print(max_score([1,2,3,4,5,6,1], 3))
print(max_score([2,2,2], 2))
print(max_score([9,7,7,9,7,7,9], 7))
# Custom Test cases
print(max_score([1,2,6,3,1],3))