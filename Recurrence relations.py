def recurrence(n):
    if n==0:
        return 1
    return 2*recurrence(n-1)+n
def reccurence_relation(n):
    return f"T(n)=2T(n-1)+n"
n=5
print("Recurrence Relation:", reccurence_relation(n))