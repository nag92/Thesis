import numpy as np

import MocapAnyalsis
import matplotlib.pyplot as plt


if __name__ == '__main__':

    sub0_dyn_file = "../../data/subject0/Standing_kneebend.csv"
    sub0_static_file = "../../data/subject0/StaticCal.csv"
    sub0 = MocapAnyalsis.MocapAnyalsis(sub0_static_file, sub0_dyn_file)
    sub0_angles = abs(sub0.get_joint_angles()[:, 0])
    sub0_dist_center = sub0.get_distance()
    iptc0 = sub0.iptc
    mank = sub0.mank
    lank = sub0.lank

    fig, ax = plt.subplots(3)
    ax[0].plot(mank.x)
    ax[1].plot(mank.y)
    ax[2].plot(mank.z)
    ax[0].plot(lank.x)
    ax[1].plot(lank.y)
    ax[2].plot(lank.z)


    plt.show()
    sub1_dyn_file = "../../data/subject1/StandingKneeFlex2.csv"
    sub1_static_file = "../../data/subject1/StaticCal.csv"
    sub1 = MocapAnyalsis.MocapAnyalsis(sub1_static_file, sub1_dyn_file)
    iptc1 = sub1.iptc
    sub1_angles = abs(sub1.get_joint_angles()[:, 0])
    sub1_dist_center = sub1.get_distance()
    sub0.play()
    knee0 = sub0.knee
    knee1 = sub1.knee
    start0 = 1760
    end0 = 1890

    start1 = 4100
    end1 = 4216
    #
    start1 = 2763
    end1 = 2848

    fig, ax = plt.subplots(2)
    t0 = np.linspace(0, 1, len(sub0_angles[start0:end0]))
    t1 = np.linspace(0, 1, len(sub0_angles[start1:end1]))
    ax[0].plot(t0, sub0_angles[start0:end0]  )
    ax[0].plot(t1 , sub1_angles[start1:end1])


    z = np.polyfit(np.radians(sub0_angles[start0:end0]), sub0_dist_center[start0:end0], 4 )
    print(z)
    my_poly = np.poly1d(z)
    new_line = my_poly(sub0_angles[start0:end0])
    ax[0].set_title("Angle")
    ax[0].set_xlabel("frames")
    ax[0].set_ylabel("theta")
    ax[0].legend(["subject0", "subject1"])
    ax[1].set_title("dist vs angle")
    ax[1].plot(sub0_angles[start0:end0], sub0_dist_center[start0:end0])
    ax[1].plot(sub1_angles[start1:end1], sub1_dist_center[start1:end1])
    #ax[1].plot(sub0_angles[start0:end0], new_line)

    # ax[2].set_title("IPTC")
    # ax[2].plot(iptc0.x )
    # ax[2].plot(iptc0.y )
    # ax[2].plot(iptc0.z )
    #
    # ax[2].legend(["sub0_x","sub0_y","sub0_z"])
    #
    # ax[3].plot(iptc1.x)
    # ax[3].plot(iptc1.y)
    # ax[3].plot(iptc1.z)
    # ax[3].legend(["sub1_x", "sub1_y", "sub1_z"])
    #
    #
    # # ax[3].plot(knee0.x)
    # # ax[3].plot(sub0_angles)
    # #
    # # ax[3].plot(knee1.x)
    # # ax[3].plot(sub1_angles)
    # #
    # # ax[3].legend(["sub0_kne_x", "sub0_knee_angle","sub1_kne_x", "sub1_knee_angle"])
    #
    # ax[1].set_title("angle vs distance")
    # ax[1].set_xlabel("angle")
    # ax[1].set_ylabel("dist (mm)")

    plt.show()
