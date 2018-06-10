[https://developer.android.com/training/basics/firstapp/creating-project]  
When I connected the power cable to one of the USB ports, screen was blinking and the power was going on and off.  
Thought it was some connection issue, but changing the port fixed this.

[https://codelabs.developers.google.com/codelabs/androidthings-classifier/index.html?index=..%2F..%2Fio2018#1]  
adb devices -> lists the devices  
Downloaded androidthings-imageclassifier-master.zip    
Chose open existing project, gradle build is happening.  
It says Gradle - Downloading some files.  
I ran a project before but its not the correct one, Gradle download happened for that too.  
This time it started at 8.03, lets see how much time it takes.
It took 2 mins.   
Build Tools missing, it is installing now - 26.0.2. Took less than 2 mins.   
gradle sync started - 3mins  
Idexing happening now - took 1min  
After this, run button is enabled/visible..  

Got the below error when i ran the app, because an app with same package already exists since I installed it before.  

```
Installation failed with message Failed to finalize session : INSTALL_FAILED_UPDATE_INCOMPATIBLE: Package com.example.androidthings.imageclassifier signatures do not match the previously installed version; ignoring!.
It is possible that this issue is resolved by uninstalling an existing version of the apk if it is present, and then re-installing.  
```

Logcat tab in Android Studio shows the logs.  

Trying another tutorial now  
[https://developer.android.com/things/training/first-device/create-studio-project]    

conda create -n py36 python=3.6
activate py36

google-oauthlib-tool --client-secrets client.json --credentials shared/src/main/res/raw/credentials.json --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save

When building the google assistant project, it again downloaded  build tools, this time a newer version.  
gradle sync happening again  
gradle build running  

Nothing worked today!!  
Will continue tomorrow  

Trying with my old pico now  
[https://gist.github.com/davidnunez/1404789] -> this has commands for listing packages  
https://developer.android.com/things/hardware/imx7d -> link for flashing Android Things  
Currnet verison on old Pico is 0.6.1 devpreview  
Once the default image is downloaded, it gets flashed into PicoPro board and it restarts.  
There is blank screen after reboot, but the instructions say it takes upto 3mins, so im waiting  
The setup utility shows the logs of what's happening.  

Now that you’re set up, try sample projects in Android Studio or in the sample repository here: [https://developer.android.com/things/sdk/samples.html]  

Took a couple of mins and the device is loading now!!


488 W AlarmManager: Unrecognized alarm listener com.android.server.wifi.scanner.WificondScannerImpl$3@967ef76 -> getting this error when connecting to wifi through shell.  
I connected to wifi using the launcher and it worked.  
Now the version is 1.0.1 and I can access camera directly from launcher and also check rainbow hat. It blinks colors.  

[https://github.com/androidthings/sample-tensorflow-imageclassifier/archive/master.zip]  
**If you have tried the previous sample, remember to uninstall it before continuing, so that one does not interfere with the other:**  
I should keep track of what apps im installing on AT. so that i can use adb uninstall package to uninstall it before installing another.   
FInally, some project that worked. It is an image classifier, it doesn't do well on all classes of objects, but yea its working atleast!!

Now flashing the new pico, its current version is 0.8.1 devpreview  
Its a 330mb file - the default image. Since we already downloaded it, it is directly flashing the new pico using the same image.
After the new image got flashed and device turned on, it showed me get started screen and I tried clicking on continue but it was not working.  
It was working in other pico but not this.  
Maybe something wrong with device? Or maybe the screen or its touch.  
Maybe i should flash once again?  
Well the reason was I missed one connection!!  

If you have a Rainbow HAT, press the "A" button. -> didnt read this and thought rainbow hat buttons are not working with this project.  

If the RGB LED strip on the Rainbow HAT doesn’t turn on, make sure the Rainbow HAT is seated correctly. It needs to be pushed down such that the pins from the i.MX7D are fully inserted into the connector while making sure the Rainbow HAT board is not in contact with the i.MX7D board  
So basically everything I struggled with and took time to get done, had answers..all I had to do was read these.  


[https://androidthings.withgoogle.com/#!/kits/starter-kit]  

Will try Google Assistant project now.  
```adb uninstall com.example.androidthings.imageclassifier // removing existing project```  

[https://androidthings.withgoogle.com/#!/samples/sample-googleassistant]

[https://stackoverflow.com/questions/18930050/adb-connection-over-tcp-not-working-now] -> fix for adb connect not working  
Connect phone with usb cable to PC.  
Issue command: adb usb  
Issue command: adb tcpip 5555  
Issue command: adb connect xxx.xxx.xxx.xxx  

Imported googleassistant -> got compile time error, tried few things. Finally realized it is because the credentials.json is missing  

File - Settings - Build - Instant Run - Turn off  

Stuck at this error for GA project - android.os.ServiceSpecificException: Unknown I/O name BCM16 (code 19)  




