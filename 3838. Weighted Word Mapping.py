class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha="abcdefghijklmnopqrstuvwxyz"
        dict_={}
        j=0
        for i in alpha:
            dict_[i]=weights[j]
            j+=1
        add=0
        ans=[]
        for i in words:
            add=0
            for j in i:
                add=add+dict_[j]
            result=add%26
            ans.append(result)
        answer=""
        for i in ans:
            answer=answer+chr(96+26-i)
        return answer
        