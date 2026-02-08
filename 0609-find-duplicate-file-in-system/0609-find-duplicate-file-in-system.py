class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:


        content_map = {}

        for p in paths:
            parts = p.split()
            directory = parts[0]

            for file_info in parts[1:]:
                name, rest = file_info.split("(")
                content = rest[:-1]
                full_path = directory + "/" + name

                if content not in content_map:
                    content_map[content] = []
                content_map[content].append(full_path)

        res = []
        for v in content_map.values():
            if len(v) > 1:
                res.append(v)

        return res
