    def train(self, save=True):
        """
        train a model to reproduction
        """
        sIn = []
        alpha = 1.0
        sIn.append(1.0)  # Initialization of decay term

        nb_dim = len(self._demo[0])
        self.gmm = TPGMM.TPGMM(nb_states=self._n_rfs, nb_dim=nb_dim, reg=self.reg)
        taus = []
        goals = []
        relocated_tau = []
        for i in range(len(self._demo)):
            tau, motion, goal = self.gen_path(self._demo[i])
            taus.append(tau)
            goals.append(goal)

        # make the decay term
        for t in range(1, self.nbData):
            sIn.append(sIn[t - 1] - alpha * sIn[t - 1] * self._dt)  # Update of decay term (ds/dt=-alpha s) )

        # stack the decay term and all the demos
        t = sIn * self.samples
        tau = np.vstack((t, taus[0]))

        for tau_ in taus[1:]:
            tau = np.vstack((tau, tau_))

        # Make all the transformations
        for i in range(len(goals[0])):
            b = [0.0]
            for j in range(len(goals)):
                b.append(goals[j][i].tolist()[0])
            b = np.asarray(b).reshape((-1, 1))
            self.b.append(b)
            self.A.append(np.eye(len(goals)+1))

        # Do all the transformations
        gammam, BIC = self.gmm.train(tau) # get the goodness of fit
        self.gmm.relocateGaussian(self.A, self.b) # more the gaussian based on the frame transformations
        sigma, mu, priors = self.gmm.get_model() # get all the model parameters
        gmr = GMR.GMR(mu=mu, sigma=sigma, priors=priors) # set up the GMR trainers
        expData, expSigma, H = gmr.train(sIn, [0], range(1, 1+len(self._demo)), self.reg) # train the model
        #ric1 = solve_riccati(expSigma)
        ric2 = solve_riccati_mat(expSigma, 0.01, self.reg) # get the gains for the system
