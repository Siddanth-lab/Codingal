class StringReverser:
    def reverse_words(self, s: str) -> str:
        
        words = s.split()
        reversed_words = words[::-1]
       
        return ' '.join(reversed_words)

reverser = StringReverser()
result = reverser.reverse_words("Hello Codingal")
print(result)