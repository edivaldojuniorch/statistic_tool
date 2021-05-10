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
        Calculate the mean from p and n

        Args:
            none

        Returns:
            mean(float): mean of the data set
        """

        self.mean = self.p * self.n

        return self.mean
    
    def calculate_stdev(self):
        """
        Calculate the standard deviation from p and n

        Args:
            none
        Returns:
            stdev(float): standard deviation from the data set
        """

        self.stdev = math.sqrt(self.n * self.p * (1-self.p))

        return self.stdev

    def replace_stats_with_data(self):
        """
        To calculate the p and n from the data set 

        Args:
            none

        Returns:
            none

        """
        self.n = len(self.data)
        self.p = 1.0 * sum (self.data) / len(self.data)
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p, self.n


    def plot_bar(self):
        """
        Output a histogram of the instance variable data using matplolib pyplot 
        library.

        Args:
            none

        Returns:
            none

        """

        plt.bar( x = [], height= [(1 -self.p) *self.n, self.p * self.n])
        plt.title('Bar chart of Data')
        plt.xlabel('outcome')
        plt.ylabel('count')
        
        pass

    def pdf(self):
        """
        Probability density function calculator for the binomila distribution. 

        Args:
            none

        Returns:
            y (float): y values to the pdf plot
            x (float): x values to the pdf plot
        """

        a = math.factorial(self.n) / (math.factorial(k) * (math.factorial(self.n - k)))
        b = (self.p ** k )
        
        return a * b

    def plot_bar_pdf(self):
        """

        Args:

        Returns:
        
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

    def __add__(self, other):
        """
        """

        result = Guassian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt(math.pow(self.stdev,2) + math.pow(other.stdev,2))
    
        return result

    def __repr__(self):
        """
        """

        return "mean {}, standard deviation {}".format(self.mean, self.stdev)

