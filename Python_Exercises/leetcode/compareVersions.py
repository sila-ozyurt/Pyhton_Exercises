class Solution(object):

    def compareVersion(self,version1:str, version2:str)->int:
        try:
                
            #we will compare versions by splitting them 
            v1=[int(i) for i in version1.split(".")]
            v2=[int(i) for i in version2.split(".")]

            #take length of them to compare one by one
            len1=len(v1)
            len2=len(v2)            


            #control constraint 2
            if not (1<=len1,len2<=500):
                raise ValueError("invalid length for version number")


            #control constraint 2
            if not(version1.replace('.','').isdigit() and version2.replace('.','').isdigit()):
                raise ValueError("version number has invalid character")

            #extend the shorter version with 0's
            if len1>len2:
                v2.extend([0]*(len1-len2))
            elif len2>len1:
                v1.extend([0]*(len2-len1))
            
            #compare versions one by one
            for i,j in zip(v1,v2):
                if i>j:
                    return 1
                elif j>i:
                    return -1
            return 0
            
        except Exception as e:
            print("error: ",e)
            return 111