import numpy as np
import math as mat
import time

def inverse(x, y, z, pos, l1, l2, l3, l4, l5):

    th1 = np.arctan2(y,x)
    print(pos)
    print(th1)


	#先端座標
    p = np.array([[x],[y],[z]])

	#L4, L5の姿勢
    A = np.array([[np.sin(th1)*np.sin(pos[0]+pos[1]+pos[2])],
                  [-np.cos(th1)*np.sin(pos[0]+pos[1]+pos[2])],
                  [np.cos(pos[0]+pos[1]+pos[2])]])
    print(A)

    p3 = p - l4*A
    print(p3)

    p3x = p3[0]**2
    p3y = p3[1]**2
    p3z = (p3[2]-l1)**2
    c3 = (p3x + p3y + p3z - l2**2 - l3**2)/(2*l2*l3)
    print(c3)
    th3 = np.arctan2(np.sqrt(1-c3**2), c3)

    r = np.sqrt(p3x + p3y)
    h = p3[2] - l1
    M = c3*l3+l2
    N = np.sin(th3)*l3
    th2 = np.arctan2( M*r-N*h, N*r+M*h )

    th4 = pos[1] - th3 - th2
    th1 = pos[0]
    th5 = pos[2]

    print("P = " + str(p))
    print("theta1 = " + str(mat.degrees(th1)) )
    print("theta2 = " + str(mat.degrees(th2)) )
    print("theta3 = " + str(mat.degrees(th3)) )
    print("theta4 = " + str(mat.degrees(th4)) )
    print("theta5 = " + str(mat.degrees(th5)) )

    th1, th2, th3 ,th4, th5 = mat.degrees(th1), mat.degrees(th2), mat.degrees(th3), mat.degrees(th4), mat.degrees(th5)

    with open('angle.txt', 'a')as f:
        f.write('{0},{1},{2},{3},{4}'.format(int(th1), int(th2), int(th3), int(th4), int(th5)) + '\n')
    
if __name__ =='__main__':

    #初期位置
    #pr = np.array([[0],[300],[300]])

    #各リンクとハンドの長さ
    L1 = 300
    L2 = 200
    L3 = 160
    L4 = 72
    L5 = 180

    #初期位置
    th1 = 0	
    th2 = 60	
    th3 = 30
    th4 = -90
    th5 = 8

    #欲しい位置
    Pr = [ 0 for i in range(10)]
    Pr[0] = np.array([[285],[285],[300]])
    Pr[1] = np.array([[285],[285],[80]])
    Pr[2] = np.array([[298],[298],[80]])
    Pr[3] = np.array([[285],[285],[80]])
    Pr[4] = np.array([[285],[285],[300]])

    Pr[5] = np.array([[-285],[285],[300]])
    Pr[6] = np.array([[-285],[285],[80]])
    Pr[7] = np.array([[-298],[298],[80]])
    Pr[8] = np.array([[-285],[285],[80]])
    Pr[9] = np.array([[-285],[285],[300]])


    #欲しい姿勢
    pos = np.array([[0], [0], [0]])

    with open('angle.txt', 'a')as f:
        f.write('{0},{1},{2},{3},{4}'.format(int(th1), int(th2), int(th3), int(th4), int(th5)) + '\n')

    #inverse(Pr[0], Pr[1], Pr[2], pos,  L1, L2, L3, L4, L5)

    for i in range(10):
        
        inverse(Pr[i][0], Pr[i][1], Pr[i][2], pos, L1, L2, L3, L4, L5)
        time.sleep(5)

    with open('angle.txt', 'a')as f:
        f.write('{0},{1},{2},{3},{4}'.format(int(th1), int(th2), int(th3), int(th4), int(th5)) + '\n')
