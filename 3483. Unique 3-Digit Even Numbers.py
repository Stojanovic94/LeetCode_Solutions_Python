class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        from collections import defaultdict

        freq = defaultdict(int)
       
        uniq_even = set()
        count = 0
        for d in digits:
            if d%2 == 0:
                uniq_even.add(d)
            freq[d]+=1

        for e in uniq_even:
            freq[e]-=1

            keys = [k for k in freq if freq[k]>0]
            for i in range(len(keys)):
                for j in range(i+1,len(keys)):
                    a,b = keys[i], keys[j]
                    ## a,b,e 
                    if a!=0:
                        count+=1
                    if b!=0:
                        count+=1
                    
            for num in keys:
                if freq[num] >=2 and num!=0 :
                    ## num num e
                    count+=1
            freq[e]+=1
        
        return count