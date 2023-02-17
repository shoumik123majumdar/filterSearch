from tkinter import*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)



filter_list = []
filter_list.append("youtube.com")
filter_list.append("stackoverflow.com")
filter_list.append("reddit.com")

window = Tk()
window.title("Web Search")
window.minsize(width = 300,height=100)


search_label = Label(window,text="Enter your search query")
search_label.pack()
search_entry = Entry(window)
search_entry.pack()



def createSearchQuery(filter,query): return "site:" + filter + " " + query

def search():
    search_string = ""
    for filter in filter_list:
        search_string += createSearchQuery(filter,search_entry.get()) + " OR "
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/")
    box = driver.find_element(By.NAME,"q")
    box.send_keys(search_string)
    box.send_keys(Keys.ENTER)

clickButton = Button(window,text="Click to search",command=search)
clickButton.pack()


window.mainloop()
