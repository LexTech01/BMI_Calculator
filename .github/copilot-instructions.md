# BMI Calculator - AI Coding Instructions

## Project Overview
This is a Python Tkinter GUI application that calculates Body Mass Index (BMI) with visual feedback. The app features interactive sliders, image backgrounds, and a dynamic person visualization that scales with height input.

## Architecture & Key Components

### Main Application (`bmi_calculator.py`)
- **Single-file architecture**: All GUI logic, calculations, and styling in one file
- **Tkinter + PIL/Pillow**: GUI framework with image manipulation capabilities
- **Fixed window size**: 500x600px, non-resizable design with absolute positioning
- **Image dependencies**: All UI elements rely on images in `images/` directory

### Core Functionality Patterns
- **Dual slider system**: Height (0-220cm) and weight (0-200kg) sliders that auto-update entry fields
- **Dynamic person visualization**: `man_standing2.png` resizes based on height slider value
- **BMI calculation**: Uses metric system (height in cm → meters, weight in kg)
- **Health categories**: 4 BMI ranges with specific advice text for each

## Development Conventions

### Image Handling
- All images must be in `images/` directory relative to main script
- Use PIL for resizing: `Image.open().resize((width, height))`
- Convert to PhotoImage for Tkinter: `ImageTk.PhotoImage()`
- Background elements use absolute positioning with `.place(x, y)`

### GUI Layout Strategy
- **Layered approach**: Background images first, then functional elements
- **Color scheme**: `#f0f1f5` (main bg), `#EEBF25` (bottom section), `#0073EE` (button)
- **Fixed positioning**: All elements use `.place()` instead of pack/grid
- **No responsive design**: Hardcoded coordinates for 500x600 window

### Variable Naming & Structure
- Global StringVar objects: `Height`, `Weight` (capitalized)
- Slider variables: `current_value`, `current_value2` (DoubleVar)
- Image variables: `photo`, `photo1`, `photo2` etc. (sequential naming)
- Functions: `BMI()` for calculation, `get_current_value()` pattern for sliders

## Running & Testing

### Dependencies
```bash
pip install pillow  # For PIL/Image support
```

### Execution
```bash
python bmi_calculator.py  # Note: README has typo "bmi_calcultor.py"
```

### Required Assets
- All 6 images in `images/` directory are mandatory for proper execution
- Missing images will cause runtime errors due to absolute file references

## Common Modification Patterns

### Adding new BMI categories
- Extend the if/elif chain in `BMI()` function
- Update `label2.config(text="CATEGORY")` and `label3.config(text="advice")`

### Styling changes
- Colors: Modify hex values in `bg=` and `fg=` parameters
- Fonts: Pattern is `"arial <size> <weight>"` (e.g., `"arial 40 bold"`)
- Positioning: Adjust `.place(x=, y=)` coordinates

### Image updates
- Maintain same dimensions or update resize calls accordingly
- Keep filenames consistent or update all references in code
- Person image scaling logic depends on image aspect ratio

## Integration Points
- **File system**: Direct file path dependencies to `images/` folder
- **PIL/Pillow**: Image processing and Tkinter integration
- **No external APIs**: Fully self-contained application
- **No configuration files**: All settings hardcoded in main script