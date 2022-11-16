class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
  
        for pos, speed in pair:
            time = (math.ceil(target - pos) / speed)
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        return len(stack)