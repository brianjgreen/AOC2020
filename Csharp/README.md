# C#

## .NET 10
Greatly simplified the filesystem structure. Only need *.cs file.
```
dotnet run Day01.cs
```

## Code Formatter
### Install Code Formatting Tool
```
dotnet tool install -g csharpier
```
### Format Code
```
/Users/briangreen/.dotnet/tools/csharpier Csharp/2025/Day01.cs
```

## Archive
### .NET 9 (for reference)
**No longer needed. .NET 10 made this a lot simplier.**

#### Setup filesystem for C# solution and project files.
| Step Description | Command |
| ---------------- | ------- |
| 1. Create a folder for the solution. | ```mkdir <solution_folder_name>``` |
| 2. Change to the folder. | ```cd <solution_folder_name>``` |
| 3. Create a solution file in the folder. | ```dotnet new sln``` |
| 4. Create a folder and project using a template. | ```dotnet new console -o <project_folder_name>``` |
| 5. Add the folder and its project to the solution. | ```dotnet sln add <project_folder_name>``` |
| 6. Repeat steps 4 and 5 to create and add any other projects. | |
| 7. Open the current folder path (.) containing the solution using VS Code. | ```code .``` |

#### Execution Example
```
cd 2015
dotnet run --project Day01
```

#### Add A New Day Example
```
cd 2015
dotnet new console -o Day02
dotnet sln add Day02
```

#### Add a New Year Example
```
mkdir 2015
cd 2015
dotnet new sln
```