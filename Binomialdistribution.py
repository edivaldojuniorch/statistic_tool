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
    def __init__(self, mu=0, sigma=1):
        
        Distribution.__init__(self,mu, sigma)

        pass

    def calculate_mean(self):
        """
        """
        
        pass
    
    def calculate_stdev(self):
        """
        """

        pass

    def replace_stats_with_data(self):
        """
        """
        
        pass

    def plot_bar(self):
        """
        """
        
        pass

    def pdf(self):
        """
        """
        
        pass

    def plot_bar_pdf(self):
        """
        """
        
        pass

