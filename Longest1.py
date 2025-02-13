def longest_consecutive_ones(n):
    binary_representation=bin(n)[2:]
    consecutive_ones=binary_representation.split("0")
    max_ones=max(len(seq)for seq in consecutive_ones)
    return max_ones
num=int(input("Enter a number:"))
print("Longest consecutive 1s is:", longest_consecutive_ones(num))