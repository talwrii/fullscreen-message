#!/usr/bin/env python3
"""Display fullscreen messages that close on keypress."""
import tkinter as tk
import sys


def calculate_font_size(text, screen_width, screen_height):
    """Calculate appropriate font size based on text length and screen size."""
    # Base calculation: smaller font for longer text
    text_length = len(text)
    
    # Use the smaller dimension as reference
    base_size = min(screen_width, screen_height)
    
    # Scale inversely with text length, with some padding
    if text_length < 10:
        font_size = int(base_size / 5)
    elif text_length < 20:
        font_size = int(base_size / 7)
    elif text_length < 40:
        font_size = int(base_size / 10)
    else:
        font_size = int(base_size / 15)
    
    # Ensure reasonable bounds
    font_size = max(40, min(font_size, 500))
    
    return font_size


def show_fullscreen_message(message, bg_color="black", text_color="white"):
    """Display a fullscreen message that closes on any key press.
    
    Args:
        message: Text to display
        bg_color: Background color (default: black)
        text_color: Text color (default: white)
    """
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background=bg_color)
    
    # Get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate font size based on screen and text
    font_size = calculate_font_size(message, screen_width, screen_height)
    
    # Close on any key press or Escape
    root.bind('<Key>', lambda e: root.destroy())
    root.bind('<Escape>', lambda e: root.destroy())
    
    # Create label with message
    label = tk.Label(
        root,
        text=message,
        font=('Arial', font_size, 'bold'),
        bg=bg_color,
        fg=text_color,
        wraplength=int(screen_width * 0.9)  # Wrap text at 90% screen width
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