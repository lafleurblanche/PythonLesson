import time

start_time = time.perf_counter()

with open('lesson2/num.txt', 'r') as fin:
    content = fin.read()

print(f'ファイル内容:{content}')

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(elapsed_time)
