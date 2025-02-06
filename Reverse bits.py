def reverse_bits(n):
    num_bits=n.bit_length()

    reversed_n=0
    for i in range(num_bits):
        reversed_n|=((n>>i)&1)<<(num_bits-1-i)
    return reversed_n
num=int(input("Enter a number: "))
reversed_num=reverse_bits(num)
print(f"Number with reversed bits:{reversed_num}")