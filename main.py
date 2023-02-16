import webbrowser
from tkinter import*
url = ""
# MacOS
chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

window = Tk()
window.title("Web Search")
window.minsize(width = 300,height=300)

sites_label = Label(text="Enter the sites you want to filter for (seperated by commas)")
sites_label.pack()


#webbrowser.get(chrome_path).open(url)
window.mainloop()
