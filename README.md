# GottaGoFast
# PS: The code is not finished yet!!!

Intended to enumerate ports, this script was created aiming to do that with the highest speed possible. Just a lame excuse to practice some scripting skills 'cause nmap can't really be replaced. ¯\_(ツ)_/¯

<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/179854800-32a77f78-8aba-48ac-a792-2733a91dba47.gif" />
</p>

The script loops through almost all the 65535 ports that's why I wanted to use ```concurrent.futures``` to speed up the process. But I'm unable to predict them, maybe you can help!   

### So called "Proof of Concept"

<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/180364199-ce24c503-70fe-48cd-9884-1a68e64f6f56.gif" />
</p>



By default ```threads``` are set to 1000. If you go higher than that you're gonna miss some ports and gonna need this as well:

  <strong>ctypes_</strong> library  
  <strong>libgcc_s = ctypes.CDLL('libgcc_s.so.1')</strong>
