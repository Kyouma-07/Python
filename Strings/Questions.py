#Ques1:  Partial Reverse:
s1 = "abcdefgh"
#rev only "cdef"
print(s1[:2] + s1[2:6][::-1]  +s1[6:])

#Ques2: Reverse words ( No splits allowed)
s2 = "hello world python"
print(s2[::-1])  #rev the entire string

#Ques3: Alternate Characters Reverse
#Take every 2nd character and reverse that result.
s3= "abcdefghij"
print(s3[::2][::-1])

#Ques4: Middle Extraction + Reverse
#Extract "structure" and reverse it.
s4 = "datastrtucture"
print(s4[4:][::-1])

#Ques5: Problem 5 — Step Trap (Prediction)
s = "0123456789"
print(s[8:2:-2])
#"864"

#Ques6: Right Rotation:
s6 = "python"
k = 2
print(s6[-k:] + s6[:-k])


#Ques7: Left Rotation:
s7 = "python"
k = 2
print(s7[k:] + s7[:k])


#Ques8: CHUNKING:
s8 = "abcdefghij"
k3 = 3
#make in chunks of 3
chunks = []
for i in range(0, len(s8),k3):
    chunks.append(s8[i:i+3])
print(chunks)

#Ques9: Palindrome CHECK (using slicing)
s9 = "racecar"
mid = len(s9)//2
print(s9 == s9[::-1])





