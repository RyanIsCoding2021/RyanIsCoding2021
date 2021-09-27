from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('capital_data.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            country, city = line.split('/')
            the_world[country] = city
            
def write_to_file(country_name, city_name):
    with open('capital_data.txt', 'a') as file:
        file.write('\n' + country_name + '/' + city_name)

print ('Ask the expert - capital cities of the world')
root = Tk()
root.withdraw()
the_world = {}
read_from_file()



while True:
    query_coutry = simpledialog.askstring('Country', 'Type the name of a country:')
    
    if query_coutry in the_world:
        result = the_world[query_coutry]
        messagebox.showinfo('Answer',
                            'the capital city of' + query_coutry + '!')
    else:
        new_city = simpledialog.askstring('Teach me',
                                          'I don\'t know!' +
                                          'what is the capital city of ' + query_coutry + '?')
        the_world[query_coutry] = new_city
        write_to_file(query_coutry, new_city)