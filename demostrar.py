import numpy as np

econ1 = 1
gamma = 20
pho=140
econ2=econ1 * np.exp(pho * 1j)
econ3=econ1*np.exp(gamma*1j)
econ4=econ1*np.exp((gamma*pho)*1j)