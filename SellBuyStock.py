def calculateProfits(arr, arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i - 1]:
            profit += arr[i] - arr[i - 1]
    return profit

prices = [615, 648, 742, 235, 572, 547, 245]
profit = calculateProfits(prices, len(prices))
print("Max profit:", profit)