class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        s=list(ransomNote)
        t=list(magazine)
        for i in range (len(s)):
            found = False
            for j in range (len(t)):
                if s[i] == t[j]:
                    found=True
                    t.pop(j)
                    break
            if found==False:
                    return False    
        
        return True            
        