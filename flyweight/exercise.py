class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text.split()
        self.formatting = {}

    class Word:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __getitem__(self, item):
        w = self.Word()
        self.formatting[item] = w
        return self.formatting[item]

    def __str__(self):
        result = []
        for i in range(len(self.plain_text)):
            word = self.plain_text[i]
            wf = self.formatting.get(i)
            if wf and wf.capitalize:
                word = word.upper()
            result.append(word)
        return ' '.join(result)


if __name__ == '__main__':
    sentence = Sentence('hello world')
    print(sentence[1])
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"
