string="hello world Hello WOrld java Python"
data=string.lower().split()
word_counts ={}
for word in data:
    if word in word_counts:
        word_counts[word] += 1  # Increment count if word exists
    else:
        word_counts[word] = 1   # Add word to dict with count 1 if new
    
print(word_counts)