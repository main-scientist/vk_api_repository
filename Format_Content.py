class Format_Content:

    @staticmethod
    def formatting_volgodonsk(string) -> str:
        content = string.split()
        n = len(content)
        for i in range(n):
            if content[i] == 'Подробности:' or content[i] == 'Подробно:':
                string = ' '.join(content[:i])
                break
            if content[i] == 'Реклама.':
                return 'null'
        return string
