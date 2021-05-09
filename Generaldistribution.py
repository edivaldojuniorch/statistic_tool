class Distribution:
    def __init__(self, mu=0, sigma=1):
        """
        
        """
        self.mean = mu
        self.stdev = sigma
        self.data = []
    
    def read_data_file(self, file_name):
        """

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