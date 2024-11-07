# cptext
A useful tool for extracting text from a selection of a screenshot to the clipboard.

## Installation (fedora):
`sudo dnf install cairo cairo-devel`

`sudo dnf install gobject-introspection gobject-introspection-devel`

`sudo dnf install cairo-gobject cairo-gobject-devel`

`sudo dnf install gi`

`sudo dnf install tesseract`

`pip install evdev pyscreenshot pytesseract pyperclip`
`pip install PyGObject`

`python3 -c "import gi; print(gi.__version__)"`

## Running:
`python cptext.py`
