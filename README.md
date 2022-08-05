# GottaGoFast - PS: The code is not finished yet!!!

Intended to enumerate ports, this script was created aiming to do that with the highest speed possible. Just a lame excuse to practice some scripting skills 'cause nmap can't really be replaced. ¯\_(ツ)_/¯

This is much more for a CTF scenario like rather than a real one. Mainly because, it runs with very high threads, so imagine a ton of connections attempts to a host in a very short time. This might get you block by their firewall or you may crash the application.

**PONDER OVER IT!**

<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/179854800-32a77f78-8aba-48ac-a792-2733a91dba47.gif" />
</p>

The script loops through almost all the 65535, ports that's why I wanted to use ```concurrent.futures``` to speed up the process! The script itself isn't perfect. But, that wasn't the idea. 
 
Be aware that with very high threads you're gonna miss some ports. If you're not like me and gets python better than me, just ```pull``` this repo.

### So called "Proof of Concept"


<h5 align="center">Running with 2000 threads</h5>
<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/183101878-7dfdb847-b38e-44cd-ae11-cacba251252b.gif" />
</p>

<h5 align="center">Running with 1000 threads</h5>
<p align="center">
<img src="https://user-images.githubusercontent.com/78124142/183101866-26826d43-fe74-4eb1-aa1d-5e41d7432531.gif" />
</p>


