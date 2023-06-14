import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    if any(file['nome_do_arquivo'] == path_file for file in instance.queue):
        return

    lines = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines,
    }

    instance.enqueue(data)

    print(data)


def remove(instance):
    try:
        file_name = instance.dequeue()['nome_do_arquivo']
        print(f'Arquivo {file_name} removido com sucesso')
    except IndexError:
        print('Não há elementos')


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print('Posição inválida', file=sys.stderr)
