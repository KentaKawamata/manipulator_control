import numpy as np

def inverse(x, y, z, thx, thy, thz, l1, l2, l3, l4, l5):

    th1 = thx
    print(th1)

    p = np.array([[x],[y],[z]])
    a = np.array([[np.sin(th1)*np.sin(thy)],
                  [-np.cos(th1)*np.sin(thy)],
                  [np.cos(thy)]])
    
    #a = np.array([[np.sin(thx)], [np.cos(thx)], [np.sin(thy)]])
    print(a)

    p45 = l4*a
	
    p3 = p - p45
    print("p3 = " + str(p3) )

    p3x = p3[0]**2
    p3y = p3[1]**2
    p3z = (p3[2]-l1)**2

    c3 = (p3x + p3y + p3z - l2**2 - l3**2)/(2*l2*l3)
    print("c3 = " + str(c3) )    
    th3 = np.arctan2(np.sqrt(1-c3**2), c3)

    A = np.sqrt(p3x + p3y)
    B = p3[2] - l1
    M = c3*l3+l2
    N = np.sin(th3)*l3
    th2 = np.arctan2(M*A-N*B, N*A + M*B)

    th4 = thy - th3 - th2
    th5 = thz

    print("P = " + str(p))
    print("theta1 = " + str(np.degrees(th1)) )
    print("theta2 = " + str(np.degrees(th2)) )
    print("theta3 = " + str(np.degrees(th3)) )
    print("theta4 = " + str(np.degrees(th4)) )
    print("theta5 = " + str(np.degrees(th5)) )

    #th1, th2, th3 ,th4, th5 = np.degrees(th1), np.degrees(th2), np.degrees(th3), np.degrees(th4), np.degrees(th5)

    #with open('angle.txt', 'a')as f:
    #    f.write('0,{0},{1},{2},0'.format(int(th2),int(th3),int(th4))+'\n')
    
if __name__ =='__main__':

    pr = np.array([[310],[310],[80]])
    th = ([[np.radians(45)], [np.radians(90)], [np.radians(0)]])	
    inverse(pr[0], pr[1], pr[2], th[0], th[1], th[2], 300, 200, 160, 72, 0)
