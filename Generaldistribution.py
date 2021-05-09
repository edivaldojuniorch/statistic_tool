class Distribution:
    def __init__(self, mu=0, sigma=1):
        """
        Generic distribution class for initialize and read data set 
        to be analysed.

        Attributes:
            mean (float) represente the mean value of the distribution
            stdev (float) represents the standard deviaion of the distribution
            data_list (lis of floats) a list of floats extrected from the data file

        """
        self.mean = mu
        self.stdev = sigma
        self.data = []

    
    def read_data_file(self, file_name):
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

        line = file.append()