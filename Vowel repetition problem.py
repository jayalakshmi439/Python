def most_frequent_vowel(s):
    vowels = 'aeiouAEIOU'
    frequency = {}
    for char in s:
        if char in vowels:
            frequency[char] = frequency.get(char,0) + 1
            
    if not frequency:
        return "No vowels found"
    
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent
s = input()
print(most_frequent_vowel(s))
