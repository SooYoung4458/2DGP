; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{F8BD492F-4B28-4689-898C-BD548E67FD39}
AppName=MarioRun
AppVersion=1.5
;AppVerName=MarioRun 1.5
AppPublisher=My Company, Inc.
AppPublisherURL=http://www.example.com/
AppSupportURL=http://www.example.com/
AppUpdatesURL=http://www.example.com/
DefaultDirName={pf}\MarioRun
DefaultGroupName=MarioRun
OutputDir=C:\Users\������\Desktop
OutputBaseFilename=MarioRun
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\2DGP\MarioRun\dist\MarioRun.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\2DGP\MarioRun\dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{group}\MarioRun"; Filename: "{app}\MarioRun.exe"
Name: "{commondesktop}\MarioRun"; Filename: "{app}\MarioRun.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\MarioRun.exe"; Description: "{cm:LaunchProgram,MarioRun}"; Flags: nowait postinstall skipifsilent
