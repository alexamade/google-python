string = 'baby2008.html'
# take the left 4 characters from the .html in the string 
#  
new_string = string[4:8]
# take the left 4 characters from the .html in the string
#  and convert to int
new_string = int(new_string)
# take the left 4 characters from the .html in the string

print (new_string)

list = ['baby2008.html', 'baby2009.html', 'baby2010.html']
# take the left 4 characters from the .html in the string
#  and convert to int
new_list = [int(i[4:8]) for i in list]
# take the left 4 characters from the .html in the string
print (new_list)