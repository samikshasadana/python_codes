'''vowels = "aeiou"

def reverseVowel(string):
    vowels_list = []
    string_list = list(string)

    for index,letter in enumerate(string_list):
        if letter in vowels:
            vowels_list.append(letter)

    reversed_vowels_list = list(reversed(vowels_list))

    new_string_list = list(string_list)
    for index,vowel in enumerate(vowels_list):
        idx_vowel_in_string =  string_list.index(vowel)
        new_string_list[idx_vowel_in_string] = reversed_vowels_list[index]

    print (new_string_list)

reverseVowels("hello ")
'''
l=[]
r=[]
k=[]
s=input()
for i in s:
    if i in 'aeiou':
        l.append(i)
        s=s.replace(i,'@')

#l.reverse()
r=[]
for j in l:
    r.append(j)
print(s,l)
j=len(l)
for i in s:
    if i in '#$@':
       # x=r[j]
        k.append(l[j-1])
        j=j-1
    else:
        k.append(i)
print(''.join(k))
        
