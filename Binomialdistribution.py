import math
import matplotlib.pyplot as plt
from Generaldistribution import Distribution

class Binomial(Distribution):
    """
    Binomial distribution class for calculating and 
    visualizing a Binomial distribution.

    Attributes:
        mean(float): the mean valur to the distribution
        stdef(float): the standard deviation of the distribution
        datalist(list of floats): a list of floats poins to bre extracted from a data file
        p (float): the probabality of an event occuring
        n (int): number of trials

    """
    def __init__(self, prob=0.5, size=20):
        
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

        pass

    def calculate_mean(self):
        """
        """

        self.mean = self.p * self.n

        return self.mean
    
    def calculate_stdev(self):
        """
        """
        self.stdev = math.sqrt(self.n * self.p * (1-self.p))

        return self.stdev

    def replace_stats_with_data(self):
        """
        """
        self.n = len(self.data)
        self.p = 1.0 * sum (self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n


    def plot_bar(self):
        """
        """

        plt.bar( x = [], height= [(1 -self.p) *self.n, self.p * self.n])
        plt.title('Bar chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        
        pass

    def pdf(self):
        """
        """

        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k )
        
        return a * b

    def plot_bar_pdf(self):
        """
        """
        x = []
        y = []

        for i in range():
            x.append()
            y.append()
        

        # make the plots
        plt.bar(x,y)
        plt.title('Distribution of Outcomes')
        plt.ylabel('Probability')
        plt.xlabel('Outcome')
        
        plt.show()

        return x, y

