$packageName = 'timewarp'
$toolsDir = "$(Split-Path -parent $MyInvocation.MyCommand.Definition)"
$installDir = Join-Path $toolsDir 'timewarp'

Install-ChocolateyZipPackage -PackageName $packageName -Url 'URL_TO_YOUR_PACKAGED_BINARY' -UnzipLocation $installDir

