class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap ={}

        for i in strs:
            sorted_word = ''.join(sorted(i))

            if sorted_word in hashmap:

                hashmap[sorted_word].append(i)


            else:

                hashmap[sorted_word] = [i]

        return list(hashmap.values())

         