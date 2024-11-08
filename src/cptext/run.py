import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import pyscreenshot as ImageGrab
import pyperclip
import pytesseract

# List to store clicked points (top-left and bottom-right)
click = []

# Function to capture the selected area when two points are clicked
def getorigin(widget, event):
    global click
    # Get the x and y coordinates of the mouse click
    x = int(event.x_root)
    y = int(event.y_root)
    print(f"Click registered at {(x, y)}")
    click.append((x, y))
    # For some reason getorigin gets called twice on each click
    if len(click) == 4:
        select_area_and_capture(click[0], click[2])

# Function to take screenshot of selected area
def select_area_and_capture(c1, c2):
    dummy = None
    on_destroy(dummy)
    try:
        # This uses pyscreenshot to capture the selected area
        box = (c1[0], c1[1], c2[0], c2[1])
        im = ImageGrab.grab(bbox=box)  # None allows for free selection

        print("Area selected, capturing screenshot...")

        # Extract the text from the screenshot
        text = pytesseract.image_to_string(im)

        # Copy the text to clipboard
        pyperclip.copy(text)
        print("Text extracted and copied to clipboard.")
    except ValueError as e:
        print(f"Error: {e}. Please make sure the top-left corner is selected before the bottom-right corner.")
        return

# Main GTK setup
def on_destroy(window):
    print("Closing window...")
    Gtk.main_quit()

def main():
    global click

    # Create a new GTK window
    window = Gtk.Window(title="Select area for screenshot")
    window.set_decorated(False)
    # Set the window size to cover the entire screen area
    screen = Gdk.Screen.get_default()
    monitor = screen.get_monitor_geometry(0)  # Use the first monitor (adjust if necessary)
    window.set_default_size(monitor.width, monitor.height)

    # Create an overlay to add the red border
    overlay = Gtk.Overlay()
    window.add(overlay)

    # Set a transparent background widget as the main area
    main_area = Gtk.DrawingArea()
    overlay.add(main_area)

    # Add the red border frame as an overlay
    border_frame = Gtk.Frame()
    border_frame.set_shadow_type(Gtk.ShadowType.NONE)  # Remove default shadow
    border_frame.set_name("border-frame")  # Set name for CSS styling
    overlay.add_overlay(border_frame)

    # Set CSS styling for the red border
    css_provider = Gtk.CssProvider()
    css_provider.load_from_data(b"""
        #border-frame {
            border-width: 4px;
            border-color: red;
            border-style: solid;
        }
    """)
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(
        Gdk.Screen.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

    # Make the window transparent and set opacity
    window.set_app_paintable(True)
    window.set_opacity(0.64)  # Adjust opacity as desired
    window.connect("destroy", on_destroy)

    # Connect the mouse click event
    window.connect("button-press-event", getorigin)

    # Display the window
    window.show_all()
    print("Select the top-left corner and then the bottom-right corner.")

    # Start the GTK main loop
    Gtk.main()

if __name__ == "__main__":
    main()
