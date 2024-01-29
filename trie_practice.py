class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        return currentNode

    def insert(self, word):
        currentNode = self.root
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children['*'] = None

    def collectAllWords(self, words, node=None, word=""):
        currentNode = node or self.root
        for key, ChildNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(words, ChildNode, word + key)
        return words

    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords([], currentNode)

    def traverse_and_print(self):
        currentNode = self.root
        for key, ChildNode in currentNode.children.items():
            if key == "*":
                print(key)
            else:
                print(key)
                return self.traverse_and_print(ChildNode)

    def autocorrect(self, word):
        currentNode = self.root
        suggestion = ''
        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
                suggestion += char
            else:
                return suggestion + self.collectAllWords([], currentNode)[0]
        return word
