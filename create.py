import time
today = time.strftime("%Y-%m-%d")
print "The date is: " + today

custom_date = raw_input('Would you prefer a custom date (y/n)? ')
if custom_date == 'n':
    print('Today\'s date chosen')
    today_month = time.strftime(" %b ")
    today_day = time.strftime("%d")
elif custom_date == 'y':
    today = raw_input('Enter custom date e.g. 2016-12-02: ')
else:
    print('That is not a valid answer!')

category = input("Enter 1 for President's update: ")
if category == 1:
    print "Category is: President's Update"
    filename_main = "Presidents-Update"
    category = "president-update"
    author = "Gabriel Lessard"
    image = "/images/truss.png"
else:
    print "Category is: General post"

filename = today + "-" + filename_main + ".md"
print "File name is: " + filename

yaml_layout = "layout: post"
yaml_title = "title: " + raw_input('Enter title here with no special chars: ') + today_month + today_day
yaml_categories = "categories: " + category
yaml_author = "author: " + author
yaml_image = "image: " + image
