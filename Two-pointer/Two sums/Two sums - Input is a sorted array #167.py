def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        list = []
        while start <= end: 
            if numbers[start] + numbers[end] ==  target:
                break
            elif numbers[start] + numbers[end] > target:
                end = end - 1 
            elif numbers[start] + numbers[end] < target:
                start = start + 1
        list.append(start+1)
        list.append(end+1)
        return list
