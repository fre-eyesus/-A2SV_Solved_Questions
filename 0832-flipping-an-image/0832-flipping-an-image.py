class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)

        for i in range(n):
            image[i].reverse()
            
        for k in range(n):
            for l in range(n):
                if image[k][l] == 0:
                    image[k][l] = 1
                else:
                    image[k][l] = 0
        return image
