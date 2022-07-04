def average(array):
    num_plants, heights = int(input()), set(input().split())
    avg = sum(heights) / len(num_plants)

    print(float(avg, 3))
