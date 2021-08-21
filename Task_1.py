import hashlib


def substring_count(string):
    # в сумму не включаем пустую строку
    if len(string) == 0:
        return len(string)

    hash_set = set()
    for i in range(len(string) + 1):
        for j in range(i + 1, len(string) + 1):
            hash_set.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())

    # в сумму не включаем строку целиком
    hash_set.remove(hashlib.sha1(string[0:len(hash_set) + 1].encode('utf-8')).hexdigest())
    return len(hash_set)


if __name__ == '__main__':
    data_string = 'cat'
    print(f'Количество различных подстрок в строке "{data_string}": {substring_count(data_string)}')
