'''
Problem : Given two strings s and t, return true if t is an anagram of s, and false otherwise.
'''
#Approach
'''
1. If length of both strings is not equal return False.
2. Iterate through first string and create hash for each character with its occurance count.
3. Iterate through second string and reduce the occurance count of character if it is present in hash map.
4. Delete the char from hash map if its occurance count become zero.
5. If char not in hash map, return False. Otherwise , return True.  
'''
#Code 
def isAnagram(s, t):
    if len(s)==len(t):
        s_map={}
        for i in s :
            s_map[i]=s_map.get(i,0)+1
        for j in t :
            if j in s_map:
                s_map[j]=s_map.get(j)-1
                if s_map[j]==0 :
                    del s_map[j]
            else :
                return False
        return True
    else :
        return False

s1=input("Enter first String : ")
s2=input("Enter second String : ")
print(isAnagram(s1,s2))