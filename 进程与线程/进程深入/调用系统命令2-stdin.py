# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌

import subprocess

f = open(r"in.txt",'r')

# return_cmd = subprocess.run('python',stdin=subprocess.PIPE,stdout=subprocess.PIPE,shell= True)
# 通过文件句本的方式传参给系统命令，PIPE是不能传参给系统命令。subprocess有接口Popen可以传参给系统命令
return_cmd = subprocess.run('python', stdin=f, stdout=subprocess.PIPE, shell=True,encoding='UTF-8')

print(return_cmd)
print(return_cmd.stdout)
