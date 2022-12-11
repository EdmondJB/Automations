import tkinter as tk
from pytube import YouTube

# Create the GUI window
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create a label and an entry field to enter the URL of the YouTube video
url_label = tk.Label(root, text="Enter the URL of the YouTube video:")
url_label.pack()
url_entry = tk.Entry(root)
url_entry.pack()

# Create a function to download the video
def download_video():
    # Get the URL from the entry field
    url = url_entry.get()
    
    # Use pytube to download the video
    yt = YouTube(url)
    
    # Get the selected resolution
    resolution = resolution_var.get()
    
    # Download the video in the selected resolution
    video = yt.streams('mp4', resolution)
    video.download('download_path')

# Create a variable to store the selected resolution
resolution_var = tk.StringVar()
resolution_var.set("4K")

# Create a dropdown menu to select the resolution
resolution_menu = tk.OptionMenu(root, resolution_var, "4K", "1080p", "720p", "480p", "360p")
resolution_menu.pack()

# Create a button to trigger the download
download_button = tk.Button(root, text="Download Video", command=download_video)
download_button.pack()

# Run the GUI
root.mainloop()
