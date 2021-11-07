Get-ChildItem -Path (Read-Host -Prompt "Where is this file stored?") ##Change directory to repository where the user requested

$files = Get-ChildItem  ##Gets content from project1.txt and puts it into files variable

$userInput = Read-Host "What are you looking for in this file?"

foreach ($file in $files) {        ##Searches for Cherry, Apple, and Peach in the massive text file, and then outputs which line they are on
    $content = Get-Content $file
    $content.Split("*") | Select-String $userInput | Select-Object Line
}