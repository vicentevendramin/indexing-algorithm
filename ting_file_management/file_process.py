from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    file = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": (file),
    }

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    if not instance or instance.__len__() == 0:
        return sys.stdout.write("Não há elementos\n")

    file_to_delete = instance.dequeue()
    file_path = file_to_delete["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {file_path} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        data_info = instance.search(position)
        sys.stdout.write(str(data_info))
    except IndexError:
        sys.stderr.write("Posição inválida")
