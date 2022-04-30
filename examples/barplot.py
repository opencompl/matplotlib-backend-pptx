#!/bin/env python3

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("module://matplotlib_backend_pptx")
plt.plot([1, 2, 3, 4])
plt.ylabel("some numbers")
plt.savefig("barplot.pptx")
