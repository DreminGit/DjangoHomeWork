#!/usr/bin/env python
"""Программа конмандной строки (Джанго)"""
import os
import sys


def main():
    """Запуск административных задач"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Не удалось импортировать Django. Вы уверены, что он установлен и "
            " доступен в вашей переменной среды PYTHONPATH? Вы "
            " забыли активировать виртуальную среду?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()