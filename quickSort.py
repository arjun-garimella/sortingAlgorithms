import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

rng = np.random.default_rng(seed=42)
SIZE = 100
ordered_data = np.arange(1, SIZE + 1)
messy_data = rng.permutation(ordered_data)
finished_data = []
history = []

#graph setup
x_indices = np.arange(SIZE)

fig, ax = plt.subplots(figsize=(10, 5))


ax.set_title("Quick Sort", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Array Index", fontsize=11, labelpad=8)
ax.set_ylabel("Value", fontsize=11, labelpad=8)

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.set_xlim(-0.5, SIZE - 0.5)
ax.set_ylim(0, SIZE + 1)

bars = ax.bar(x_indices, messy_data, color="#33558d", edgecolor="#1d4ed8", width=0.8)

def update(current_state):
    # Check if the generator is sending a green sweep tuple command
    if isinstance(current_state, tuple) and current_state[0] == "success":
        green_up_to_idx = current_state[1]
        for idx, bar in enumerate(bars):
            if idx <= green_up_to_idx:
                bar.set_color("#22c55e")  # Smooth vibrant green
        return bars

    # Standard frame behavior: update bar heights and keep them blue
    for bar, val in zip(bars, current_state):
        bar.set_height(val)
        bar.set_color("#33558d")  # Blue color while sorting
    return bars


print(ordered_data)
print(messy_data)

#quick sort algorithm
def quick_sort(arr):
            if len(arr) == 0 or len(arr) == 1:
                yield arr
                return
                
            
            pivot = arr[-1]
            left = [x for x in arr if x < pivot]
            right = [x for x in arr if x > pivot]
            #return quick_sort(left) + [pivot] + quick_sort(right)

            for sorted_left in quick_sort(left):
                  yield sorted_left + [pivot] + right

            for sorted_right in quick_sort(right):
                  yield left + [pivot] + sorted_right

            left_gen = quick_sort(left)
            right_gen = quick_sort(right)

            final_left = list(left_gen)[-1] if left else []
            final_right = list(right_gen)[-1] if right else []

            yield final_left + [pivot] + final_right

            
def full_animation_wrapper(arr):
    final_sorted_state = []
    
    # 1. Yield all moving array states during the sorting loops
    for state in quick_sort(arr):
        final_sorted_state = state
        yield state
        
    # 2. Yield one final state frame to ensure it locks in place perfectly
    yield final_sorted_state

    # 3. Append the green sweep commands to turn bars green one at a time
    for i in range(SIZE):
        yield ("success", i)

#animation
sort_generator = full_animation_wrapper(messy_data.tolist())

ax.set_title("Quick Sort", fontsize=14, fontweight="bold", pad=15)

ani = animation.FuncAnimation(
    fig, 
    update, 
    frames=sort_generator, 
    interval=0, 
    repeat=False,
    save_count=len(messy_data),
    cache_frame_data=False
    
)

sorted_data = quick_sort(messy_data.tolist())
            
print(sorted_data)

        
plt.show()
    