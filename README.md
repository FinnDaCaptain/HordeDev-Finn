# Infernal Horde Bot - Finn Edition

## Prerequisites

1. Python
2. pywin32 library
3. GitHub Desktop (optional, for easy updates)

## Installation

### 1. Install Python

If you don't have Python installed:

1. Open Command Prompt
2. Type `python`
3. If Python is not installed, the Microsoft Store will open, allowing you to install it
4. After installation, close command prompt and reopen. Type python --version to ensure it is working

### 2. Install pywin32

After installing Python:

1. Open Command Prompt
2. Run the following command:
   ```
   pip install pywin32
   ```

### 3. Clone the Repository

Option 1: Using GitHub Desktop (Recommended for easy updates)
1. Install [GitHub Desktop](https://desktop.github.com/)
2. Clone this repository using GitHub Desktop

Option 2: Manual Download
1. Download the ZIP file of this repository
2. Extract it to your desired location

## Configuration

1. Navigate to the `enter_horde.lua` file in the bot directory
2. Locate the following line:
   ```lua
   local python_path = "C:your_directory\\diablo_qqt\\scripts\\HordeDev-Finn\\send_key.py"
   ```
3. Update these paths to match the location where you extracted the bot files on your computer

## Usage

1. Start Diablo IV
2. Start the bot outside of the portal
3. Use the in-game menu to configure chests you want to loot at the end.
4. Keep the bot minimized to prevent any press enter issues.

## Staying Updated

If you used GitHub Desktop:
1. Open GitHub Desktop
2. Click on "Fetch origin" to check for updates
3. If updates are available, click "Pull origin" to download them

For manual installations, re-download the ZIP file and extract it, overwriting the old files.

## Troubleshooting

If you encounter any issues:
- Ensure all prerequisites are correctly installed
- Double-check that the file paths in `enter_horde.lua` are correct
- Verify you are in front of the portal when you start the bot
