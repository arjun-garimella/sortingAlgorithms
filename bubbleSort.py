import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(seed=42)
SIZE = 10
ordered_data = np.arange(1, SIZE + 1)
messy_data = rng.permutation(ordered_data)
finished_data = []


x_indices = np.arange(SIZE)

fig, ax = plt.subplots(figsize=(10, 5))


ax.set_title("Bubble Sort", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Array Index", fontsize=11, labelpad=8)
ax.set_ylabel("Value", fontsize=11, labelpad=8)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#ax.set_xticks(x_indices)
ax.set_xlim(-0.5, SIZE - 0.5)
ax.set_ylim(0, SIZE + 1)

bars = ax.bar(x_indices, messy_data, color="#33558d", edgecolor="#1d4ed8", width=0.8)

def selection_sort_generator(messy_data):
    swapped = True
    swap_count = 0
    FRAME_SKIP = 50

    while swapped:
        swapped = False
        for data in range(len(messy_data) - 1):
                yield messy_data.copy()
                if messy_data[data] > messy_data[data + 1]:
                    messy_data[data], messy_data[data + 1] = messy_data[data +  1], messy_data[data]
                    swapped = True
                    swap_count += 1

                    if swap_count % FRAME_SKIP == 0:
                        yield messy_data.copy()

    '''
    n = len(messy_data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if messy_data[j] < messy_data[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        messy_data[i], messy_data[min_idx] = messy_data[min_idx], messy_data[i]
        
        # Yield the current array state to the animation frame
        
        '''

    #yield messy_data.copy()

def update(current_state):
    for bar, val in zip(bars, current_state):
        bar.set_height(val)
    return bars

sort_generator = selection_sort_generator(messy_data.copy())

ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=sort_generator, 
    interval=0, 
    repeat=False,
    save_count=len(messy_data),
    cache_frame_data=False
    
)

print(messy_data)

            



plt.show()
