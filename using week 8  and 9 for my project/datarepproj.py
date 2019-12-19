import datarepdb
#import pmongo
## this contains the main menu choices
def main():
	display_menu()
	while True:
		choice =input("Enter Choice: ") ##user is asked to select from the menu
		
		## when user selects 1 the first 15 cities in the city table are displayed
		if(choice=="1"):
			## call to "first_15_cities" 15 function 
			menu = datarepdb.menutitle()
			print(menu)
			## formatted output of query
			##print ("|",'{:>5}'.format("CITY"),"|", '{:>15}'.format("NAME"),"|",'{:>5}'.format("CODE"),"|", '{:>15}'.format("DISTRICT"),"|", '{:>10}'.format("POPULATION"),"|",)
			#print ("|",'{:>5}'.format("*****"),"|", '{:>15}'.format("***************"),"|",'{:>5}'.format("*****"),"|", '{:>15}'.format("***************"),"|", '{:>10}'.format("**********"),"|",)
			##for menu in menu:
				#print(menu)
			
			## the menu is displayed once query complete			
			display_menu()	
		
			
## the main menu display
def display_menu():
	print("")
	print("Menu")
	print("======")
	print(" 1 - menu titles")
	print(" 2 - View Cities by Population")
	print(" 3 - Add New City")
	print(" 4 - Find Car by Engine Size")
	print(" 5 - Add New Car")
	print(" 6 - View Countries by Name")
	print(" 7 - View Countries by Population")
	print(" x - Exit Application")  
	print()

if __name__=="__main__":
	main()