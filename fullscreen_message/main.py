#!/usr/bin/env python3
"""Display fullscreen messages that close on keypress."""

import tkinter as tk
import tkinter.font as tkfont
import sys


def find_optimal_font_size(text, screen_width, screen_height, font_family='Arial'):
    "Find the largest font size that fits the text on screen"
    # Target: fill 80% of screen width and 60% of height
    target_width = screen_width * 0.8
    target_height = screen_height * 0.6
    
    # Binary search for optimal font size
    min_size = 10
    max_size = 1000
    optimal_size = min_size
    
    # Create a temporary root for font measurements
    temp_root = tk.Tk()
    temp_root.withdraw()
    
    while min_size <= max_size:
        mid_size = (min_size + max_size) // 2
        
        # Create font and measure text
        font = tkfont.Font(family=font_family, size=mid_size, weight='bold')
        text_width = font.measure(text)
        text_height = font.metrics('linespace')
        
        # Check if it fits
        if text_width <= target_width and text_height <= target_height:
            optimal_size = mid_size
            min_size = mid_size + 1
        else:
            max_size = mid_size - 1
    
    temp_root.destroy()
    
    return optimal_size


def show_fullscreen_message(message, bg_color="black", text_color="white"):
    "Display a fullscreen message that closes on any key press."
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background=bg_color)
    
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    font_size = find_optimal_font_size(message, screen_width, screen_height)
    
    # Close on any key press or Escape
    root.bind('<Key>', lambda e: root.destroy())
    root.bind('<Escape>', lambda e: root.destroy())
    
    label = tk.Label(root,
        text=message,
        font=('Arial', font_size, 'bold'),
        bg=bg_color,
        fg=text_color
    )
    label.pack(expand=True)
    
    root.mainloop()


def main():
    """Main entry point for the CLI."""
    if len(sys.argv) > 1:
        message = ' '.join(sys.argv[1:])
    else:
        message = "PRESS ANY KEY"
    
    show_fullscreen_message(message)


if __name__ == "__main__":
    main()
