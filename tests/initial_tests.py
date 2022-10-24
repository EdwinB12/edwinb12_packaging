import mypackage
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("Module Two Test")
    print(mypackage.module2.turn_rand_num_negative())

    print("/n Plotting Test")
    mypackage.mymodule.plot_normal_distribution(size=100)
    plt.show()
