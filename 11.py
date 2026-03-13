def maxArea(height):
    maxVol = 0
    left, right = 0, len(height)-1
    while left < right:
        width = right - left
        length = min(height[left], height[right])
        vol = width * length
        maxVol = max(maxVol, vol)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
            
    return maxVol