
from pyrplidar import PyRPLidar
import time


def simplescan():
    cet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    first = 1
    firsta = 2
    lidar_ha = []
    lidar_hb = []
    lidar_hd = []
    com = True
    low = 1
    lidar = PyRPLidar()
    lidar.connect()
    lidar.set_motor_pwr(500)
    time.sleep(2)
    scan_generator = lidar.force_scan()
    try:
        for scan in scan_generator:
            if not com:
                break
            if first == 1:
                # the first scan will be for the first spin to find the
                first += 1
                firsta = scan.angle
                lidar_ha.append(scan.angle)
                lidar_hb.append(scan.distance)
            elif first <= 20:
                first += 1
                lidar_ha.append(scan.angle)
                lidar_hb.append(scan.distance)
            elif first >= 20:
                if firsta - 2 < scan.angle < firsta + 2:
                    for i in range(len(lidar_hb)):
                        if not com:
                            print(low)
                            break
                        if 904 > lidar_hb[i] > 924:
                            low = lidar_hb[i]
                            com = False
                            lidar_hd.append(lidar_hb[i])
                            for c in range(len(cet)):
                                lidar_hd.append(lidar_hb[i+c])
                            for n in range(len(lidar_hd)-1):
                                if lidar_hd[n] > lidar_hd[n+1]:
                                    low = lidar_hd[n+1]

    finally:
        lidar.stop()
        lidar.set_motor_pwr(0)
        lidar.disconnect()



if __name__ == '__main__':
    simplescan()
