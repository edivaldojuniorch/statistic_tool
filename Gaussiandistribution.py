import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Guassian(Distribution):
    """
    Gaussian distribution class for calculating and 
    visualizing as Guassian distribution.
    """

    def __init__(self, mu, sigma):

        Distribution.__init__(self, mu, sigma)

    def calculate_mean(self):

        return

    def calculate_stdev(self, sample=True):

        return
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
        """


    
    def pdf(self, x):
        """
        """

        return
    
    def plot_histogram_pdf(self, n_spaces=50):

        """
        """

        return

