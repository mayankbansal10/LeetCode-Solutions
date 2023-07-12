class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            a_dict[sorted_word].append(word)

        return list(a_dict.values())
