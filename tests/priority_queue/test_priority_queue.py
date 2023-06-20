from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    # Test enqueue priority
    queue = PriorityQueue()
    queue.enqueue({
        "qtd_linhas": 9,
        "nome_arquivo": "arquivo1.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 7,
        "nome_arquivo": "arquivo2.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 2,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    })

    assert len(queue.high_priority) == 1
    assert len(queue.regular_priority) == 2

    # Test dequeue
    queue = PriorityQueue()
    queue.enqueue({
        "qtd_linhas": 5,
        "nome_arquivo": "arquivo1.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 6,
        "nome_arquivo": "arquivo2.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 3,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    })

    assert queue.dequeue() == {
        "qtd_linhas": 3,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    }

    # Test search
    queue = PriorityQueue()
    queue.enqueue({
        "qtd_linhas": 3,
        "nome_arquivo": "arquivo1.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 7,
        "nome_arquivo": "arquivo2.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 2,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    })

    assert queue.search(0) == {
        "qtd_linhas": 3,
        "nome_arquivo": "arquivo1.txt",
        "linhas_do_arquivo": "linha 1"
    }
    assert queue.search(1) == {
        "qtd_linhas": 2,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    }
    assert queue.search(2) == {
        "qtd_linhas": 7,
        "nome_arquivo": "arquivo2.txt",
        "linhas_do_arquivo": "linha 1"
    }

    # Test raises IndexError
    queue = PriorityQueue()
    queue.enqueue({
        "qtd_linhas": 8,
        "nome_arquivo": "arquivo1.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 4,
        "nome_arquivo": "arquivo2.txt",
        "linhas_do_arquivo": "linha 1"
    })
    queue.enqueue({
        "qtd_linhas": 1,
        "nome_arquivo": "arquivo3.txt",
        "linhas_do_arquivo": "linha 1"
    })

    with pytest.raises(IndexError):
        queue.search(3) == {
            "qtd_linhas": 9,
            "nome_arquivo": "arquivo4.txt",
            "linhas_do_arquivo": "linha 1"
        }
