import matplotlib.pyplot as plt

fig, ax = plt.subplots()

ax.set_title("Right Ear")
ax.set_ylabel("db HL")
ax.set_xlabel("Frequency")
ax.set_xlim(100,9000)
ax.set_ylim(130,-10)
ax.set_facecolor("#ffd2d2")

x = [125,250,500,1000,2000,4000,8000]
ticks = [125,250,500,"1K","2K","4K","8K"]
xm = [750,1500,3000,6000]

ax.set_xscale('log', basex=2)
ax.set_xticks(x)
ax.set_xticks(xm, minor=True)
ax.set_xticklabels(ticks)
ax.set_xticklabels([""]*len(xm), minor=True)


ax.yaxis.set_ticks([120,110,100,90,80,70,60,50,40,30,20,10,0,-10])

ax.plot()
ax.grid(color="grey")
ax.grid(axis="x", which='minor',color="grey", linestyle="--")
plt.show()