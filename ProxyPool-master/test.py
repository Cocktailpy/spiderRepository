
import sys
print('打印第 2 到第 5 个元素：', sys.argv[1:5])
print('打印所有参数：', sys.argv[:])
for i in sys.argv:
    print(i)
with open('d','w') as f :
    f.flush()