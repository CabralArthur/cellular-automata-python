import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros do modelo
grid_size = 50  # Tamanho da grade
tau = 0.3  # Taxa de infecção
gamma = 0.1  # Taxa de recuperação
steps = 100  # Passos da simulação

# Inicialização da grade (0 = S, 1 = I, 2 = R)
grid = np.zeros((grid_size, grid_size), dtype=int)
# Infectar algumas células aleatórias
grid[np.random.randint(0, grid_size, 10), np.random.randint(0, grid_size, 10)] = 1

def update(frame):
    global grid
    new_grid = grid.copy()
    
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:  # Suscetível
                neighbors = [grid[x, y] for x in range(max(0, i-1), min(grid_size, i+2))
                                          for y in range(max(0, j-1), min(grid_size, j+2))
                                          if (x, y) != (i, j)]
                if np.any(np.array(neighbors) == 1) and np.random.rand() < tau:
                    new_grid[i, j] = 1  # Infecta
            elif grid[i, j] == 1:  # Infectado
                if np.random.rand() < gamma:
                    new_grid[i, j] = 2  # Recuperado
    
    grid = new_grid
    mat.set_array(grid)
    return [mat]

# Configuração do plot
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='viridis')
plt.colorbar(mat)

# Configurar limites dos eixos
ax.set_xlim(-0.5, grid_size - 0.5)
ax.set_ylim(-0.5, grid_size - 0.5)

# Criar e exibir a animação
ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, blit=True)
plt.show()
