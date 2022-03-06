# 2079. Watering Plants
# https://leetcode.com/problems/watering-plants/submissions/

def wateringPlants(self, plants: List[int], capacity: int) -> int:
    steps = 0
    currCap = capacity
    for i in range(len(plants)):
        if currCap < plants[i]:
            steps += 2 * i + 1
            currCap = capacity - plants[i]
        else:
            steps += 1
            currCap -= plants[i]
    return steps