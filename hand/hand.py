import paramiko
import time

def hand_write(n):
    with paramiko.SSHClient() as ssh:

        #AutoAddPolicyで勝手にhostname & key を登録してもらう
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh接続する
        ssh.connect('10.232.169.107',port=22,username='ubuntu',password='raspberry')
        #shell芸でファイルに値書き込み
        stdin,stdout,stderr=ssh.exec_command("cd /run/shm; echo %s > angles"%(n[0]) )
        stdin,stdout,stderr=ssh.exec_command("cd /run/shm; echo %s > ev_on_off"%(n[1]) )

k=[[ 0 for i in range(2)] for j in range(10)]

k[0]=['0,60,30,-90,8', 0]
k[1]=['45,84,39,-34,0', 0]
k[2]=['45,120,10,-40,30', 0]
k[3]=['45,120,10,-40,30', 1]
k[4]=['45,84,39,-34,0', 1]
k[5]=['-45,84,39,-34,0', 1]
k[6]=['-45,120,10,-40,30', 1]
k[7]=['-45,120,10,-40,30', 0]
k[8]=['-45,84,39,-34,0', 0]
k[9]=['0,60,30,-90,8', 0]

for i in range(10):
    n=k[i]
    #hand_write(n)
    print(n[0])
    print(n[1])
    #time.sleep(5) 
