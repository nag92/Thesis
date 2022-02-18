def solve_riccati(expSigma, dt=0.01, reg =1e-8):
    ric = {}
    size = expSigma[0].shape[0]
    Ad = np.kron([[0, 1],[0, 0]], np.eye(size))*dt + np.eye(2*size)
    Q = np.zeros((size*2, size*2))
    Bd = np.kron([[0],[1]], np.eye(size))*dt
    R = np.eye(size)*reg
    P = [np.zeros((size*2, size*2))] * len(expSigma)
    P[-1][:size, :size] = np.linalg.pinv(expSigma[-1])

    for ii in range(len(expSigma)-2, -1, -1):
        Q[:size, :size] = np.linalg.pinv(expSigma[ii])
        B = P[ii + 1]*Bd
        C = np.linalg.pinv(np.dot(Bd.T * P[ii + 1] , Bd) + R)
        D = Bd.T*P[ii + 1]
        F = np.dot(np.dot(Ad.T, B*C*D - P[ii + 1]), Ad)
        P[ii] = Q - F

    ric["Ad"] = Ad
    ric["Bd"] = Bd
    ric["R"] = R
    ric["P"] = P
    return ric


