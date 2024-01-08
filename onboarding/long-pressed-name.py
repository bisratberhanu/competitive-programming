class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        nameptr=0
        typedctr=0
        #if len(name)> len(typed):
            #return False
        n=len(name)
        for typedptr in range(len(typed)):
            
            if name[nameptr]!=typed[typedptr]:
                temp= name[nameptr]
                namectr=0
                while nameptr<n and temp==name[nameptr]: 
                    nameptr+=1
                    namectr+=1
                
                if nameptr==n or name[nameptr]!=typed[typedptr] or namectr>typedctr:
                    return False
                typedctr=0
            typedctr+=1
        nameptr+=1
        namectr=0
        while  nameptr<n:
            if name[nameptr]!=typed[typedptr] or namectr>typedctr:
                
                return False
            nameptr+=1  
        return True