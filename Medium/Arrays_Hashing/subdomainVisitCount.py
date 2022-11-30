class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}
        
        for domain in cpdomains:
            arr = domain.split()
            visited = int(arr[0])
            ind = 0
            dom = arr[1]
            while ind + 1 < len(dom) and dom.find('.', ind) != -1:
                ind = dom.find('.', ind + 1)
                count[dom[ind + 1:]] = count.get(dom[ind + 1:], 0) + visited
        res = []
        for key, value in count.items():
            curr = f'{value} {key}'
            res.append(curr)
        return res
            
