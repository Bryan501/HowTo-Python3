while ($true) {
    [System.Reflection.Assembly]::LoadWithPartialName("System.Windows.Forms")
    [System.Windows.Forms.MessageBox]::Show("Blue Screen of Death!")
    Start-Sleep -Seconds 10
}
