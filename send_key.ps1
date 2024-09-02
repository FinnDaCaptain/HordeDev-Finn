Invoke-Expression @'
$wshell = New-Object -ComObject wscript.shell

# Attempt to activate the English title
$activated = $wshell.AppActivate('Diablo IV')

# If the English title was not found, attempt to activate the Chinese title
if (-not $activated) {
    $activated = $wshell.AppActivate('暗黑破坏神IV')
}

# Sleep for a short duration to ensure the window is activated
Start-Sleep -Seconds 1

# Check if the window was successfully activated
if ($activated) {
    Write-Output "Window activated"
    $wshell.SendKeys('{ENTER}')
    Write-Output "Enter key sent"
} else {
    Write-Output "Failed to activate window"
}
'@
