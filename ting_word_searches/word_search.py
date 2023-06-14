def exists_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)

        if any(
            word.lower() in line.lower()
            for line in file['linhas_do_arquivo']
        ):
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': [
                    {'linha': index + 1}
                    for index, line in enumerate(file['linhas_do_arquivo'])
                    if word.lower() in line.lower()
                ]
            })

    return result


def search_by_word(word, instance):
    result = []

    for i in range(len(instance)):
        file = instance.search(i)

        occurences = [
            {
                'linha': index + 1,
                'conteudo': line.strip()
            }
            for index, line in enumerate(file['linhas_do_arquivo'])
            if word.lower() in line.lower()
        ]

        if occurences:
            result.append({
                'palavra': word,
                'arquivo': file['nome_do_arquivo'],
                'ocorrencias': occurences
            })

    return result
