# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import subprocess

# popen = subprocess.Popen('dir D://',encoding='utf-8',shell=True)
#
# print(popen)
# print(popen.stdout)
# 创建一个子进程执行python命令
popen = subprocess.Popen('python', stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)

# 往python命令中传入三条参数
popen.stdin.write('print("hello")\n'.encode('utf-8'))
popen.stdin.write('import os\n'.encode('utf-8'))
popen.stdin.write('print(os.environ)'.encode('utf-8'))

popen.stdin.close()

# out = popen.stdout.read().decode("GBK")
# popen.stdout.close()
# 第二种输出
out, err = popen.communicate()
print(out.decode('GBK'))


