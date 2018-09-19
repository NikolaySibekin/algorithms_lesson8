# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

import heapq
import collections


class Node(collections.namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):

        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")


class Leaf(collections.namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"


def huffman_encode(s):
    h = []

    for ch, freq in collections.Counter(s).items():
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
        root.walk(code, "")
    return code


s = input('Введите строку: ')
code = huffman_encode(s)
encoded = "".join(code[ch] for ch in s)
print(f'Число символов в строке: {len(code)}')

print('Символ и соответствующий ему код в словаре')
print('*' * 42)

for ch in sorted(code):
    print(f'{ch}: {code[ch]}')

print(f'Закодированная строка: {encoded}')
print(f'Длина закодированной строки: {len(encoded)}')


