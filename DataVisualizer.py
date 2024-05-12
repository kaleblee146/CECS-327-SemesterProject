import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder

class DataVisualizer:
    def __init__(self):
        self.data = None

    def import_data(self):
        name_of_file = input("Enter the name of the file: -> ")
        format_of_file = input("Enter the format of the file: -> ")
        file_data = (name_of_file + '.' + format_of_file)
        self.data = pd.read_csv(file_data)

    def create_scatter(self):
        while True:
            column_x = input("Enter column name for x-axis -> ")
            column_y = input("Enter column name for y-axis -> ")

            if column_x not in self.data.columns or column_y not in self.data.columns:
                print("Invalid column names. Please try again.")
                continue
            else:
                break
                
        data_input = self.data.groupby(column_x).agg({column_y: ['min', 'max']}).reset_index()
        fig_1 = int(input("Dimension 1: -> "))
        fig_2 = int(input("Dimension 2: -> "))
        title = input("Title: -> ")
        xlabel = input("X-Label: -> ")
        ylabel = input("Y-Label: -> ")
        xticks = int(input("X-Ticks: -> "))
        ylim1 = int(input("Y-Lim1: -> "))
        ylim2 = int(input("Y-Lim2: -> "))

        color_1 = input("Color 1: -> ")
        marker_1 = input("Marker 1: -> ")
        linestyle_1 = input("Linestyle 1: -> ")
        label_1 = input("Label 1: ->")

        
        plt.figure(figsize = (fig_1, fig_2))
        plt.scatter(data_input[column_x], data_input[column_y]['min'], color = color_1, marker = marker_1, linestyle = linestyle_1, label = label_1)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation = xticks)
        plt.ylim(ylim1, ylim2)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        save_option = input("Would you like to save this plot? ->")
        if save_option in ["Yes", "yes", "No", "no"]:
            if save_option == "Yes":
                self.saveFile()
            elif save_option == "yes":
                self.saveFile()
            else:
                print("Plot not saved.")
        else:
            print("Invalid input. Please enter (Yes/No).")
        plt.show()

    def create_bar(self):
        while True:
            column_x = input("Enter column name for x-axis -> ")
            column_y = input("Enter column name for y-axis -> ")

            if column_x not in self.data.columns or column_y not in self.data.columns:
                print("Invalid column names. Please try again.")
                continue

            x = self.encode_or_not(column_x)
            y = self.encode_or_not(column_y)
            
            break
            
        fig_1 = int(input("Dimension 1 -> "))
        fig_2 = int(input("Dimension 2 -> "))

        title = input("Please enter a title -> ")
        xlabel = input("Please enter x-label -> ")
        ylabel = input("Please enter y-label -> ")
        xticks = int(input("Enter the amount of xticks -> "))
        ylim = int(input("Enter amount of y-lims - (1) -> "))
        ylim2 = int(input("Enter amount of y-lims - (2) -> "))

        alignment = input("Enter the aligment: [center], [edge] -> ")
        alphaNum = float(input("Enter the alpha: -> "))
        label_name = input("Please enter the label name: -> ")
        
        plt.figure(figsize=(fig_1, fig_2))
        plt.bar(x, y - ylim, bottom = ylim, align = alignment, alpha=alphaNum, label=label_name)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation = xticks)
        plt.ylim(ylim, ylim2)
        plt.legend()
        plt.tight_layout()
        
        save_option = input("Would you like to save this plot? ->")
        if save_option in ["Yes", "yes", "No", "no"]:
            if save_option == "Yes":
                self.saveFile()
            elif save_option == "yes":
                self.saveFile()
            else:
                print("Plot not saved.")
        else:
            print("Invalid input. Please enter (Yes/No).")
        
        plt.show()
    
    def create_plot(self):
        while True:
            column_x = input("Enter column name for x-axis -> ")
            column_y = input("Enter column name for y-axis -> ")

            if column_x not in self.data.columns or column_y not in self.data.columns:
                print("Invalid column names. Please try again.")
                continue

            x = self.encode_or_not(column_x)
            y = self.encode_or_not(column_y)
            
            break
            
        fig_1 = int(input("Dimension 1 -> "))
        fig_2 = int(input("Dimension 2 -> "))

        title = input("Please enter a title -> ")
        xlabel = input("Please enter x-label -> ")
        ylabel = input("Please enter y-label -> ")
        xticks = int(input("Enter the amount of xticks -> "))
        ylim = int(input("Enter amount of y-lims - (1) -> "))
        ylim2 = int(input("Enter amount of y-lims - (2) -> "))

        alignment = input("Enter the aligment: [center], [edge] -> ")
        alphaNum = float(input("Enter the alpha: -> "))
        label_name = input("Please enter the label name: -> ")
        
        plt.figure(figsize=(fig_1, fig_2))
        plt.bar(x, y - ylim, bottom = ylim, align = alignment, alpha=alphaNum, label=label_name)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation = xticks)
        plt.ylim(ylim, ylim2)
        plt.legend()
        plt.tight_layout()
        
        save_option = input("Would you like to save this plot? ->")
        if save_option in ["Yes", "yes", "No", "no"]:
            if save_option == "Yes":
                self.saveFile()
            elif save_option == "yes":
                self.saveFile()
            else:
                print("Plot not saved.")
        else:
            print("Invalid input. Please enter (Yes/No).")
        
        plt.show()


    def encode(self, column_name):
        encoder = OneHotEncoder()
        encoded_object = encoder.fit_transform(self.data[[column_name]])
        encoded_objects = pd.DataFrame(encoded_object.toarray(), columns=encoder.get_feature_names_out([column_name]))
        self.data = pd.concat([self.data, encoded_objects], axis=1)
        

    def encode_or_not(self, column_name):
        if self.data[column_name].dtype == '':
            self.encode(column_name)
            return self.data[column_name]
        else: 
            return self.data[column_name]
        
    def saveFile(self):
        while True:
            try:
                name = input("Enter name you want to save the file as: -> ")
                format = input("Enter desired format output: -> ")
                if format not in ["SVG", "svg", "JPG", "jpg", "PNG", "png"]:
                    raise ValueError("Invalid File format. Please try again.")
                else:
                    plt.savefig(f"{name}.{format}")
                    print("Plot saved successfully.")
                    break
            except ValueError as e:
                print(e)