# -*- coding: utf-8 -*- 
# 教育机构：马士兵教育
# 讲师： 肖 斌


import subprocess


# 1、简单的写法
# 开启一个子进程执行系统命令，args,encoding,shell三个参数
# runcmd = subprocess.run('dir C:\\scala',encoding= 'utf-8',shell= True)
#
# print(runcmd)

# 2、定义一个函数调用系统的所有命令
def run_cmd(command):
    # 初始化一个子进程执行系统命令
    # subprocess.PIPE 接受子进程的返回信息，一定需要解码，指定编码GBK
    return_cmd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding='GBK', shell=True)

    if return_cmd.returncode == 0:
        print("success:")
        print(return_cmd.stdout)
    else:
        print("命令执行错误:")
        print(return_cmd)


run_cmd('dir D:\\')
run_cmd('ipconfig')
run_cmd('exit 1')
