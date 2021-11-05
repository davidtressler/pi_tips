# pi_tips
Raspbery Pi Tips and Tricks 





<h1> Terminal Pin Out  </h1> - <b>  </b>
    
    $ pinout 


(On Raspbery Pi Zero - Hold the Pi with the HDMI Top Left) <br>
<img src="https://pimylifeup.com/wp-content/uploads/2019/12/Raspberry-Pi-Pinout-Command.png">
<br>
ref: https://pimylifeup.com/raspberry-pi-pinout/
     


<h1> SCP  </h1> - <b> To Copy File to Pi </b>
    
    scp file1.txt file2.txt pi@192.168.1.xx:folder1/


To Copy All File from a Dir to a Pi
    
    scp -r /Users/name/3 pi@192.168.0.xx:/home/pi/foldername
    
 
<h1> Set the Pi Zero ACT LED trigger to 'off'. </h1>
  
    echo 0 | sudo tee /sys/class/leds/led0/brightness

<h1> Set the Pi Zero ACT LED trigger to 'on'. </h1>
     
     echo 0 | sudo tee /sys/class/leds/led0/brightness
    

 <h1> USEFULL LINKS </h1>

https://www.dataplicity.com/ - Connect to Raspbery Pi terminal in a webbrowser for free 



   

