#huffman encoding using greedy stategy
import heapq

def huffman_encoding(characters, frequencies):

    heap = []
    count = 0

    for char, freq in zip(characters, frequencies):
        heapq.heappush(heap, (freq, count, char))
        count += 1

    while len(heap) > 1:

        f1, _, left = heapq.heappop(heap)
        f2, _, right = heapq.heappop(heap)

        new_node = (left, right)

        heapq.heappush(heap, (f1 + f2, count, new_node))
        count += 1

    codes = {}

    def generate_codes(node, code=""):

        if isinstance(node, str):
            codes[node] = code
            return

        generate_codes(node[0], code + "0")
        generate_codes(node[1], code + "1")

    generate_codes(heap[0][2])

    return codes




characters = ['a', 'b', 'c', 'd', 'e', 'f']
frequencies = [5, 9, 12, 13, 16, 45]

codes = huffman_encoding(characters, frequencies)

print("Huffman Codes:")

for char, code in codes.items():
    print(char, ":", code)