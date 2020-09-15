def plotter2(plt, fig, ax, title, color, xv, yv):
    #fig, ax = plt.subplots(1, figsize=(8, 8))
    fig.suptitle(title)
    if (color == 'blue'):
        ax.plot(xv, yv, color='blue',linewidth=6)
    else:
        ax.plot(xv, yv, color='red',linewidth=6)

    plt.axhline(y=0, color="black", linestyle="-")
    plt.axvline(x=0, color="black", linestyle="-")
    plt.ylabel('y=f(x)')
    plt.xlabel('x')
    plt.grid(b=True, which='major', color='#eeeeee', linestyle='-')
    plt.xlim(-5, 5)
    plt.ylim(-10, 10)
    plt.yticks(range(-10,10,2))
    plt.title('function f(x)')
    return plt.figure()
