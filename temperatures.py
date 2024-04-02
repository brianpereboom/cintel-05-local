import pandas as pd
import numpy as np
from datetime import datetime, timedelta

class timeseries:
    def __init__(self, init_value=25, init_size=10, noise_scale=0.1):
        self.noise_scale = noise_scale
        self.temps = np.cumsum(np.random.normal(size=init_size, scale=noise_scale))

    def next(self):
        self.temps = np.append(self.temps, self.temps[-1] + np.random.normal(scale=self.noise_scale))
        return self.temps[-1]
