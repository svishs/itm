import sys
# пример использования скрипта: ls -l | python stdin_sample.py
if __name__ == '__main__':
    for line in sys.stdin:
        print(line.rstrip())
    print('завершение')