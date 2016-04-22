import time
today = time.strftime("%Y-%m-%d")
print "The date is: " + today
category = input("Enter 1 for President's update: ")
if category == 1:
    print "Category is: President's Update"
    posttitle = "Presidents-Update"
else:
    print "Category is: General post"

title = today + "-" + posttitle + ".md"
print "Title is: " + title
