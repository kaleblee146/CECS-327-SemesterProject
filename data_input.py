import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder

def import_data():
    music_data = (input("Enter the name of the file: [filename.csv] "))
    data = pd.read_csv(music_data)
    return data

def create_scatter():
    pass

def create_bar(data):
    while True:
        column_x = input("Enter column name for x-axis -> ")
        column_y = input("Enter column name for y-axis -> ")

        if column_x not in data.columns or column_y not in data.columns:
            print("Invalid column names. Please try again.")
            continue

        x = encode_or_not(data, column_x)
        y = encode_or_not(data, column_y)
        
        break
        
    fig_1 = int(input("Dimension 1 -> "))
    fig_2 = int(input("Dimension 2 -> "))

    title = input("Please enter a title -> ")
    xlabel = input("Please enter x-label -> ")
    ylabel = input("Please enter y-label -> ")
    xticks = int(input("Enter the amount of xticks -> "))
    ylim = int(input("Enter amount of y-lims - 1 ->"))
    ylim2 = int(input("Enter amount of y-lims - 2 ->"))

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
    plt.show()


def encode(data):
    encoding = input("Enter encoding detail from file: ")
    while encoding:
        if not encoding.isalpha():
            print("Please enter in letters.")
            encoding = input("Enter encoding detail from file: ")
        elif encoding not in data.columns:
            print("Column '{}' not found in the dataset.".format(encoding))
            encoding = input("Enter encoding detail from file: ")
        else:
            encoder = OneHotEncoder()
            encoded_object = encoder.fit_transform(data[[encoding]])
            encoded_objects = pd.DataFrame(encoded_object.toarray(), columns=encoder.get_feature_names_out([encoding]))
            combine_object = pd.concat([data, encoded_objects], axis=1)
            return combine_object
    return None

def encode_or_not(data, column_name):
    if data[column_name].dtype == '':
        encoded_column = encode(data, column_name)
        return encoded_column
    else: 
        return data[column_name]

if __name__ == "__main__":
    data = import_data()
    create_bar(data)
    

    
    



"""
album_peak_position = read_in.groupby('title').agg({'peak_position': ['min', 'max']}).reset_index()

plt.figure(figsize=(10, 6))
plt.scatter(album_peak_position['title'], album_peak_position['peak_position']['min'], color='red', label='Lowest Peak')
plt.scatter(album_peak_position['title'], album_peak_position['peak_position']['max'], color='blue', label='Highest Peak')
plt.title('Taylor Swift Albums: Lowest and Highest Peak Positions on Billboard 200')
plt.xlabel('Album')
plt.ylabel('Peak Position')
plt.xticks(rotation=90)  
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
""" 