import torch
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder

class PredictData:
    def __init__(self):
        self.data = None
        self.w = torch.tensor(2.0, requires_grad=True)
        self.b = torch.tensor(90.0, requires_grad=True)

    def import_data(self):
        name_of_file = input("Enter the name of the file: -> ")
        format_of_file = input("Enter the format of the file: -> ")
        file_data = (name_of_file + '.' + format_of_file)
        self.data = pd.read_csv(file_data)

    def encode(self, column_name):
        label_encoder = LabelEncoder()
        self.data[column_name] = label_encoder.fit_transform(self.data[column_name])

    def encode_or_not(self, column_name):
        if self.data[column_name].dtype == 'object':
            self.encode(column_name)
        return pd.to_numeric(self.data[column_name], errors='coerce').fillna(0)

    def forward(self, x):
        return self.w * x + self.b
    
    def criteron(self, y_pred, y):
        return torch.mean((y_pred - y) ** 2)
    
    def create_plot(self):
        while True:
            column_x = input("Enter column x: -> ")
            column_y = input("Enter column y: -> ")

            if column_x not in self.data.columns or column_y not in self.data.columns:
                print("Invalid column names. Please try again.")
                continue
            encode_x = self.encode_or_not(column_x)
            encode_y = self.encode_or_not(column_y)
        
            X = torch.tensor(encode_x.values, dtype=torch.float32).view(-1, 1)
            Y = torch.tensor(encode_y.values, dtype=torch.float32).view(-1, 1)
        
            step_size = float(input("Enter step size: -> "))
            loss_list = []
            iterations = int(input("Enter # of iterations: -> "))

            for i in range(iterations):
                Y_pred = self.forward(X)
                loss = self.criteron(Y_pred, Y)
                loss_list.append(loss.item())

                loss.backward()

                with torch.no_grad():
                    self.w -= step_size * self.w.grad
                    self.b -= step_size * self.b.grad

                    self.w.grad.zero_()
                    self.b.grad.zero_()

                if (i + 1) % 100 == 0:
                    print(f"Iteration {i + 1}: Loss = {loss.item()}, Slope = {self.w.item()}, Intercept = {self.b.item()}")
            
            rows = int(input("Enter rows: -> "))
            cols = int(input("Enter cols: -> "))
            fig_1 = int(input("Dimension 1: -> "))
            fig_2 = int(input("Dimension 2: -> "))

            loss_title = input("Enter Loss Title: -> ")
            loss_xlabel = input("Enter Loss X-Label: -> ")
            loss_ylabel = input("Enter Loss Y-Label: -> ")

            scatter_color = input("Enter Scatter Color: -> ")
            scatter_label = input("Enter Scatter Label: -> ")

            plot_color = input("Enter Plot Color: -> ")
            plot_label = input("Enter Plot Label: -> ")

            data_title = input("Enter Data Title: -> ")
            data_xlabel = input("Enter Data X-Label: -> ")
            data_ylabel = input("Enter Data Y-Label: -> ")
            


            fig, (ax1, ax2) = plt.subplots(rows, cols, figsize=(fig_1, fig_2))
            ax1.plot(loss_list, 'b')
            ax1.set_title(loss_title)
            ax1.set_xlabel(loss_xlabel)
            ax1.set_ylabel(loss_ylabel)
            ax1.grid(True)

            # Plotting the original data and the predicted line
            ax2.scatter(X.numpy(), Y.numpy(), color = scatter_color, label = scatter_label)
            ax2.plot(X.numpy(), self.forward(X).detach().numpy(), color= plot_color, label = plot_label)
            ax2.set_title(data_title)
            ax2.set_xlabel(data_xlabel)
            ax2.set_ylabel(data_ylabel)
            ax2.legend()
            ax2.grid(True)
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
            break
        
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