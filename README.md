# Raspberry Pi Stranger Things Wall

Web-enabled Stranger Things inspired ouija wall using WS2811 programmable LEDs and Raspberry Pi

This is setup to get around university wifi restrictions by hosting the server separately

If you want to run everything on the Pi, see this [repo][1] 

This GIT repo contains: 

* A flask server to recieve and hold messages (/server)
* A simple HTML page with a form to send messages to the server (/website)
* A raspberry pi client to periodically poll for messages and display them on your wall (/client)

[1]:https://github.com/CalebKussmaul/Stranger-Things-Integrated