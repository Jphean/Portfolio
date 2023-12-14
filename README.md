## **Project: Survey transformation into a Tableau-compatible format**

### Overview:
This Excel file [Data - Survey Monkey Output] contains data from a questionnaire. And the "Desired Format" sheet contains the desired format.

### File Structure:
The Excel file named [Data - Survey Monkey Output Edited] consists of four sheets:

> Sheet 1 (Raw_Data): Contains the original data.<br>
> Sheet 2 (Question): It's a transformation for the headers.<br>
> Sheet 3 (Edited_Data): It's the original data with the transformed headers.<br>
> Sheet 4 (Desired_Format): Desired format.<br>

The Python file named [Script1-Data_Manipulation] have the transformation process:
  - Data import: Geting the file from a directory with _os_ and _pandas_ libraries.
  - Data cleaning: Dropping columns we don't need.
  - Data transformation: Using _melt_ function we unpivot the dataframe.
  - Data integration: Aggregating columns from the file.
  - Data export: The result is and excel file with the desired format.

### Instructions for Use:
Install pandas and os lybraries before executing the code.
Consider the operating system when you use the file root, for Windows is "\\\\" and for Mac "/".

### Contact Information:
If you hace any sugestion or doubt, please contact me at jhriveros321@gmail.com
