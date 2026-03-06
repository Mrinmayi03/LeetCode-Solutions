def topK(nums, k):
    map = {}
    for num in nums:
        if num in map:
            map[num] += 1
        else:
            map[num] = 1
    
    # Creating a bucket for bucket sort:
    bucket = [[] for num in nums]
    for key, freq in map.items():
        bucket[freq - 1].append(key)
    
    # Traversing the bucket to get the resultant array:
    result = []
    for i in range(len(nums)-1, -1, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
