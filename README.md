## Fusion 360: Batch Export Components as STEP Files

This script provides an automated solution for Fusion 360 users who need to export multiple sub-components as separate STEP files.

# Description

The provided Python script automates the process of exporting all sub-components in a Fusion 360 design as individual STEP files. When you run the script, it prompts the user to select a directory. Each sub-component is then saved as a .step file in the chosen directory, using the name of the component as the filename.

# Prerequisites

Autodesk Fusion 360 installed on your machine.

# How to Use

Open Fusion 360.
Navigate to Tools > Add-Ins > Scripts and Add-ins.
In the opened dialog box, go to the My Scripts tab.
Click the + (Add) button and choose New Script.
Select Python as the language and provide a name for the script.
Paste the provided script into the editor and save.
Run the script by selecting it and clicking the Run button.
You'll be prompted to select a folder. Choose your desired directory.
The script will then export each sub-component to the specified folder with its name.
Notes

Ensure your design is saved before running the script.
Always back up your work before using any scripts to prevent potential loss.
This script assumes a single top-level component with multiple sub-components. Adjustments might be necessary based on your specific design structure or requirements.
License

This project is licensed under the MIT License. (You can choose any other if you want).