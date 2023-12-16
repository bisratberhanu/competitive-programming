class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_info={}
        for cpdomain in cpdomains:
            splitted= cpdomain.split(' ')
            ndomains= int(splitted[0])
            main_domain= splitted[1]
            subdomains= main_domain.split('.')
            for i in range(len(subdomains)):
                domain= '.'.join(subdomains[i:])
                if domain not in domain_info:
                    domain_info[domain]=0
                domain_info[domain]+= ndomains
        ans=[]
        for val in domain_info:
            ans.append(str(domain_info[val])+' '+val)
        return ans 