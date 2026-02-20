class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s.split()) != len(pattern):
            return False

        words = {}
        patterns = {}
        
        for word, letter in zip(s.split(), pattern): 
            if words.get(letter) is None and patterns.get(word) is None: 
                words[letter] = word
                patterns[word] = letter 
            elif words.get(letter) != word and patterns.get(word) != letter:
                return False

        return True
