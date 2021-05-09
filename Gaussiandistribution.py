import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Guassian(Distribution):
    """
    Gaussian distribution class for calculating and 
    visualizing as Guassian distribution.

    Attributes:
        mean(float): the mean valur to the distribution
        stdef(float): the standard deviation of the distribution
        datalist(list of floats): a list of floats poins to bre extracted from a data file

    """

    def __init__(self, mu, sigma):

        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):
        """
        """

        avg = 1.0 * sum(self.data) / len(self.data)

        self.name = avg

        return avg

    def calculate_stdev(self, sample=True):
        """
        Calculate the standard deviatino of the data set.

        Args:
            sample (bool): wheter the data represents a sample or population

        Returns:
            sigma (float): standard deviation of the data set

        """
        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.calculate_mean()

        sigma = sum([math.pow(d - mean, 2) for d in self.data])

        sigma = math.sqrt(sigma/n)
        
        self.stdev = sigma 

        return sigma



    def read_data_file(self, file_name, sample=True):
        """
        function to read in the txt file. The txt file have to have 
        one number (float) per line. The exctracted numbers are 
        stored in the data attribute.

        Asgs:
            file_name(string): name of the a file to read from.
        
        Returns:
            none

        """
        # open document file
        with open(file_name) as file:

            # initialise lists
            data_list = []
            line = file.readline()

            # get line by line data:
            while line:
                data_list.append(int(line))
                line = file.readline()
            
        file.close()

        self.data = data_list
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev(sample)
    

    def plot_histogram(self):
        
        """
        To output a histogram of the instance variable data using matplotlib
        pyplot library.

        Args:
            None

        Returns:
            None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('data')
        plt.ylabel('count')

    
    def pdf(self, x):
        """
        Probability density function calculator for gaussian distribution.

        Args:
            x (float): point for calculating the probability density function

        Returns:
            pdf_out (float):probality density function

        """

        return (1.0 / self.stdev * math.sqrt(2*math.pi)) * math.exp(-0.5*((x-self.mean)/self.stdev)**2)
    
    def plot_histogram_pdf(self, n_spaces=50):

        """
        Plot the normalized histogram of the data and a plot of the probability
        density function along the same range.

        Args:
            n_spaces (int): number of data points

        Returns:
            x (list) values for the pdf plot
            y (list) values for the pdf plot
        
        """
        mu = self.mean
        sigma = self.stdev 

        min_range = min()
        max_range = max()

        # calculates the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        x = []
        y = []

        for i in range(n_spaces):
            tmp = min_range + interval * i
            x.append(tmp)
            y.append(self.pdf(tmp))


        fig, axes = plt.subplot(2, sharex=True)
        fig.subplots_adjust(hspace = .5)
        # histogram plot
        axes[0].his(self.data, density=True)
        axes[0].set_title('Normed Hitogram of Data')
        axes[0].set_ylabel()

        # scatter plot
        axes[1].plot(x, y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')

        plt.show()

        return x, y

    
    
