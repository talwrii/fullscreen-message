#!/usr/bin/env python3
import tkinter as tk
import sys

def show_fullscreen_message(message, bg_color="black", text_color="white", font_size=100):
    """Display a fullscreen message that closes on any key press"""
    
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background=bg_color)
    
    # Close on any key press or Escape
    root.bind('<Key>', lambda e: root.destroy())
    root.bind('<Escape>', lambda e: root.destroy())
    
    # Create label with message
    label = tk.Label(
        root,
        text=message,
        font=('Arial', font_size, 'bold'),
        bg=bg_color,
        fg=text_color
    )
    label.pack(expand=True)
    
    root.mainloop()

def main():
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        message = "PRESS ANY KEY"
    
    show_fullscreen_message(message)
