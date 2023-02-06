class Sentence:
    def __init__(self, plain_text):
        self.plain_text = plain_text.split()

    def __getitem__(self, item):
        return self.plain_text[item]

    def capitalize(self): return None



if __name__ == '__main__':
    sentence = Sentence('hello world')
    print(sentence[1])
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"
