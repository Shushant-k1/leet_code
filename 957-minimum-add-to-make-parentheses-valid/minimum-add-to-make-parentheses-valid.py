class Solution:
    def minAddToMakeValid(self, pars: str) -> int:
        
        st = []
        d = { '}' : "{" , ")" :"(" ,"]" : "["}
        res = 0
        for par in pars :
            if par not in d :
                st.append(par)
            
            else :
                if len(st) == 0 :
                    res += 1
                elif d[par] != st[-1] :
                    res += 1
                    st.pop()
                else :
                    st.pop()
                
        
        return res + len(st)