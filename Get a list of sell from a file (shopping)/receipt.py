import csv
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #Create a dictionary to save the information
    dictionary_exported = {}

    with open(filename, "rt") as csv_file_exported:
        
        #Unlock the use of the file in python
        reader = csv.reader(csv_file_exported)
        
        #Jump to the second line (because in the first line have the headers)
        next(reader)
        
        #For every row in the dictionary
        for row_list in reader:
            
            #Which column we use to index
            key = row_list[key_column_index]

            #Unit between the file and the dictionary
            dictionary_exported[key] = row_list

        #Send the dictionary to the global scope
        return dictionary_exported

def main():
    
    # The column headings and indexes.
    ID_OF_PRODUCT = 0
    NAME_OF_PRODUCT = 1
    PRICE_OF_PRODUCT = 2

    QUANTITY_OF_PRODUCTS = 1

    #Read the information of the dictionaries
    try:
        #Data base
        products_dict = read_dict("products.csv", ID_OF_PRODUCT)
        
        #Data base from the user's request of the shopping
        request_of_client_dict = read_dict("request.csv", ID_OF_PRODUCT)
        
        #Default price
        sub_total = 0
        total_quantity = 0

        #Name of the shopping
        print()
        print("Hawk Emporium")
        print()

        for element in products_dict and request_of_client_dict:

            #The column headings and indexes from Data base
            id_data_base =  products_dict[element][ID_OF_PRODUCT]
            name_data_base =  products_dict[element][NAME_OF_PRODUCT]
            price_data_base =  float(products_dict[element][PRICE_OF_PRODUCT])

            #The column headings and indexes from user's request
            id_request_client = request_of_client_dict[element][ID_OF_PRODUCT]
            quantity_of_products_request_client = int(request_of_client_dict[element][QUANTITY_OF_PRODUCTS])
            total_per_product = quantity_of_products_request_client * price_data_base
            
            #Show the list of items
            print(f"{quantity_of_products_request_client} - [{id_data_base}] Item: {name_data_base}: ${price_data_base}  [Total: ${total_per_product:.2f}]")
            
            #Sum the price of the the purchase to the price per product(quantity) in the request
            sub_total = sub_total + total_per_product
            #Sum the items
            total_quantity = total_quantity + quantity_of_products_request_client
        
        #Tax
        sales_tax = sub_total * 0.06
        #Total 
        total = sub_total + sales_tax

        #Show the results
        print()
        print(f"Number of items: {total_quantity}")
        print(f"Subtotal: ${sub_total:.2f}")
        print(f"Sales tax: ${sales_tax:.2f}")
        print(f"Total: ${total:.2f} ")

        print()
        print("Thank you for shopping at the Hawk Emporium.")

        # Use an f-string to print the current
        # day of the week and the current time.
        print(f"{current_date_and_time:%A %I:%M %p}")
    
    #Try to receive the correct files
    except (FileNotFoundError, PermissionError) as file_err:
        print(file_err)
    
    #Try to found each item in the data base
    except KeyError as key_err:
        for element in request_of_client_dict:

            if element in products_dict:
                prod_info_list = products_dict[element]
            else:
                print()
                print(f"Error: Unknown product ID in the request.csv file '{key_err}'")
        


if __name__ == "__main__":
    main()