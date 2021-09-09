function getIP {
    (Get-NetIPAddress).IPv4address | select-string "192*" 
}
Function getPSV {
    Get-Host | Select-Object version
}
Function Hostname {
    get-content env:computername
}
function getdate {
    Get-Date
}


$DATE = getdate
$HN = Hostname
$PSV = getPSV
$IP = getIP
$USER = $env:USERNAME
$body = "This machine's IP is $IP. The User of this machine is $USER. The hostname is $HN. The powershell version is $PSV.  Todays date is $DATE"


Write-output "($body)" >> C:\it3038c-scripts\powershell\sysInfo.txt         


##Send-MailMessage -To "cboy7315@gmail.com" -from "cboy7315@gmail.com" -Subject "IT3038c Windows sysInfo" -Body $body -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)

