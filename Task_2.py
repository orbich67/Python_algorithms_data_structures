import heapq
from collections import Counter
from collections import namedtuple


# класс для хранения информации о структуре дерева
class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


# класс для листьев дерева
class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


# функция кодирования символов в коды Хаффмана
def huffman_encode(s):
    h = []
    for ch, freq in Counter(s).items():
        h.append((freq, len(h), Leaf(ch)))
    heapq.heapify(h)
    count = len(h)
    while len(h) > 1:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, '')
    return code


def huffman_decode(encoded, code):
    sx = []
    enc_ch = ''
    for ch in encoded:
        enc_ch += ch
        for dec_ch in code:
            if code.get(dec_ch) == enc_ch:
                sx.append(dec_ch)
                enc_ch = ''
                break
    return ''.join(sx)


if __name__ == '__main__':
    data_str = 'beep boop beer!'
    data_code = huffman_encode(data_str)
    data_encoded = ''.join(data_code[ch] for ch in data_str)
    print(f'Строка: {data_str}\nКоды символов: {data_code} \nЗакодированная строка: {data_encoded}')
    print(f'Раскодированная строка: {huffman_decode(data_encoded, data_code)}')
