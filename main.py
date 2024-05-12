from DataVisualizer import DataVisualizer
from PredictData import PredictData
import time 
running = True




if __name__ == "__main__":
    while running:
        print("Welcome to Data Analysis Tool 1.0...\n")
        time.sleep(3)
        print("What would you like to do today?\n")
        print("1 -> Analyze Current Data\n")
        print("2 -> Predict Data\n")
        print("3 -> Quit\n")
        choice = int(input("Enter choice: -> \n"))
        if choice == 1:
            print("Starting up the DataVisualizer tool..")
            time.sleep(3)
            visualizer = DataVisualizer()
            visualizer.import_data()
            visualizer_options = input("Would you like a bar, scatter or plot?: -> ")
            if visualizer_options.lower() == "scatter":
                visualizer.create_scatter()
            elif visualizer_options.lower() == "bar":
                visualizer.create_bar()
            elif visualizer_options.lower() == "plot":
                visualizer.create_plot()
            else:
                print("Invalid Option. Please try again.\n")
        elif choice == 2:
            print("Starting up Predicting Data tool..")
            time.sleep(3)
            DataPredict = PredictData()
            DataPredict.import_data()
            DataPredict.create_plot()
            
        elif choice == 3:
            running = False
        else:
            print("Invalid Option.\n")