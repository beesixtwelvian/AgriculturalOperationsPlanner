# Krigeage = interpolation = méthode d'estimation linéaire garantissant le minimum de variance

import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel as C

# Générer des données d'exemple
np.random.seed(42)
X = np.sort(5 * np.random.rand(20, 1), axis=0)
y = np.sin(X).ravel()

# Définir le modèle de krigeage avec un noyau RBF (Radial Basis Function)
kernel = C(1.0, (1e-3, 1e3)) * RBF(1.0, (1e-2, 1e2))
gp = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

# Entraîner le modèle
gp.fit(X, y)

# Prédiction pour de nouveaux points
X_new = np.linspace(0, 5, 1000)[:, np.newaxis]
y_pred, sigma = gp.predict(X_new, return_std=True)

# Visualisation des résultats
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 4))
plt.scatter(X, y, c='r', s=50, zorder=10, edgecolors=(0, 0, 0))
plt.plot(X_new, y_pred, 'k', label='Prédiction')
plt.fill_between(X_new.ravel(), y_pred - sigma, y_pred + sigma, alpha=0.2, color='k')
plt.title('Krigeage avec noyau RBF')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()