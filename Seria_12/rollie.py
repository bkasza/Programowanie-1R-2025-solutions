#przykład np rolla
import numpy as np
import matplotlib.pyplot as plt

a = np.diag(np.linspace(0.1, 1, 10))

a[0, 0] = 2.0 


roll_down  = np.roll(a, shift=1, axis=0)
roll_up    = np.roll(a, shift=-1, axis=0)
roll_right = np.roll(a, shift=1, axis=1)
roll_left  = np.roll(a, shift=-1, axis=1)
roll_diag  = np.roll(a, shift=(1, 1), axis=(0, 1))

# Wyrysowanie
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

axes[0, 1].set_title('Oryginał')
axes[0, 1].imshow(a, cmap='viridis')

axes[0, 0].set_title('Lewo (shift=-1, axis=1)')
axes[0, 0].imshow(roll_left, cmap='viridis')

axes[0, 2].set_title('Prawo (shift=1, axis=1)')
axes[0, 2].imshow(roll_right, cmap='viridis')

axes[1, 1].set_title('Dół (shift=1, axis=0)')
axes[1, 1].imshow(roll_down, cmap='viridis')

axes[1, 0].set_title('Góra (shift=-1, axis=0)')
axes[1, 0].imshow(roll_up, cmap='viridis')

axes[1, 2].set_title('Na ukos (Dół-Prawo)\nshift=(1, 1), axis=(0, 1)')
axes[1, 2].imshow(roll_diag, cmap='viridis')

plt.tight_layout()
plt.show()

