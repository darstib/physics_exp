import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


# Convert degrees and minutes to radians
def deg_min_to_rad(deg_min):
    deg, min_str = deg_min.split("°")
    min_val = float(min_str.strip("'"))
    return np.radians(float(deg) + min_val / 60)


# Given data
deltas = ["57°39'", "56°22'", "53°57'", "53°33'"]
A = np.radians(60)  # Convert A to radians
lambdas = np.array([404.7, 435.8, 546.0, 577.1])  # nm

# Calculate refractive indices
n_values = []
for delta in deltas:
    delta_rad = deg_min_to_rad(delta)
    n = np.sin((delta_rad + A) / 2) / np.sin(A / 2)
    n_values.append(round(n, 3))

print("Refractive indices:", n_values)


# Define Cauchy dispersion formula
def cauchy(x, a, b, c):
    return a + b / (x**2) + c / (x**4)


# Fit the data
popt, _ = curve_fit(cauchy, lambdas, n_values)
a, b, c = popt
print(f"n = {a:.3f} + {b:.3f}/λ² + {c:.3f}/λ⁴")
# Generate points for smooth curve
lambda_fit = np.linspace(380, 600, 1000)
n_fit = cauchy(lambda_fit, *popt)

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(lambda_fit, n_fit, "r-", label="Cauchy fit")
plt.plot(lambdas, n_values, "bo", label="Measured data")

plt.xlabel("Wavelength λ (nm)")
plt.ylabel("index of refractive n")
plt.title("Cauchy dispersion curve of glass material")
plt.grid(True)
plt.legend()

# Format axes
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter("%.3f"))
plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter("%.0f"))

# Save plot
plt.savefig("cauchyDispersionCurveOfGlassMaterial.png", dpi=300, bbox_inches="tight")
