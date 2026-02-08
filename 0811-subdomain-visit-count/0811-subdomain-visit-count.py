class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        cp_count = {}
        for domain in cpdomains:

            rep, d= domain.split()
            cp_pair = d.split('.')
            d_name = cp_pair[-1]

            if d_name not in cp_count:
                cp_count[d_name] = 0
            cp_count[d_name] = cp_count.get(d_name,0) + int(rep)

            for i in range(1,len(cp_pair)-1):
                comb = cp_pair[i] +'.'+d_name
                if comb not in cp_count:
                    cp_count[comb] = 0
                cp_count[comb] = cp_count.get(comb,0) + int(rep)

            if d not in cp_count:
                cp_count[d] = 0
            cp_count[d] = cp_count.get(d,0) + int(rep)

        ans = []
        for key,value in cp_count.items():
            ans.append(f"{value} {key}")

        return ans
        