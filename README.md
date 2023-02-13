# TouchDisabler

Automatically enable or disable the touchscreen on windows 10/11 devices by checking the stylus Bluetooth device status.

I have an ASUS ROG Flow X16. It has a touchscreen and it is compatible with Surface Pen which is supported by mpp 2.0.

I often use them to draw something. However, when I do this, the touch input and stylus input will work simultaneously, and that causes my hands will easily accidentally tap something wrong. Even if I enabled "disable touch when using pen" settings, the previous problem still exists.

So I have to disable the touchscreen by Windows Device Manager manually when I want use stylus, and enable it again when I want use touchscreen then... Well, I don't want to do this over and over again. So I made this script.

It works by checking the Bluetooth connection status of the stylus, so your stylus needs to support Bluetooth. 

The script may need some changes to work properly on your device. It requires administrator privileges to run, use it at own your risk.
