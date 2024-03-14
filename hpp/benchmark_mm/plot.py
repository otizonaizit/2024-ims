import matplotlib.pyplot as plt
import pandas as pd

data = []
for i in range(1, 4):
    with open(f"hpp/benchmark_mm/results_{i}", "r") as f:
        # each row is: processes, threads, size, time
        data.extend([f"{i}_{line}".split("_") for line in f.readlines()])

df = pd.DataFrame(data, columns=["processes", "threads", "size", "time"])

fig, ax = plt.subplots(3, 1)
fig.set_figheight(10)
fig.set_figwidth(6)

for i, s in enumerate(df["size"].unique()):
    for p in df["processes"].unique():
        xi = list(df.loc[(df["processes"] == p) & (df["size"] == s), "threads"].astype(float))
        yi = list(df.loc[(df["processes"] == p) & (df["size"] == s), "time"].astype(float))
        ax[i].plot(xi, yi, label=p)
    ax[i].set_title(f"size={s}")
    
handles, labels = ax[i].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', title="processes")

fig.text(0.5, 0.04, 'n_threads', ha='center')
fig.text(0.0, 0.5, 'time', va='center', rotation='vertical')
plt.savefig("hpp/benchmark_mm/results.png", dpi=300)


