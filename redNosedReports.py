def numSafeReports(data):
    safeCount = 0
    for line in data.splitlines():
        readings = list(map(int, line.split()))
        if isSafe(readings): safeCount += 1
    return safeCount

def isSafe(readings):
    increasing = None
    for i in range(0, len(readings) - 1):
        diff = readings[i+1] - readings[i]
        if diff == 0 or abs(diff) > 3: return False
        if increasing is None: increasing = diff > 0
        if increasing and diff < 0: return False
        if not increasing and diff > 0: return False
    return True

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = file.read()
    print(numSafeReports(data))
