# C#


| Step Description | Command |
| ---------------- | ------- |
| 1. Create a folder for the solution. | ```mkdir <solution_folder_name>``` |
| 2. Change to the folder. | ```cd <solution_folder_name>``` |
| 3. Create a solution file in the folder. | ```dotnet new sln``` |
| 4. Create a folder and project using a template. | ```dotnet new console -o <project_folder_name>``` |
| 5. Add the folder and its project to the solution. | ```dotnet sln add <project_folder_name>``` |
| 6. Repeat steps 4 and 5 to create and add any other projects. | |
| 7. Open the current folder path (.) containing the solution using VS Code. | ```code .``` |

## Execution Example
```dotnet run --project Day01```

## Add A New Day Example
```
dotnet new console -o Day02
dotnet sln add -o Day02
```
