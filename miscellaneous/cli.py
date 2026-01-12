""" 
CLI in Python

Creating a simple CLI
Running a simple server on port 8000 using the command.
    python -m http.server 8000
    This command runs a simple HTTP server that serves files from the current directory on port 8000. 
    To access the server, open a web browser and navigate to XXXXXXXXXXXXXXXXXXXXX.
    Replace XXXXXXXXXXXXXXXXXXXXX with the IP address of the machine running the server and the port number (8000 in this case).
    For example, if the server is running on the machine with IP 192.168.1.100, you would navigate to http://192.168.1.100:8000 in your web browser.
    This will display the files in the current directory on the server.
    You can also access individual files by navigating to XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX, where filename.html is the name of the file you want to view.
    For example, to view the file named index.html, you would navigate to http://192.168.1.100:8000/index.html in your web browser.
    This will display the contents of the index.html file on the server.
    You can modify the files on the server by editing them directly in your text editor or IDE.
    When you make changes to the files, you can refresh the web page in your browser to see the updated content.
    To stop the server, you can press Ctrl+C in the terminal window where the server is running.
    This will stop the server and allow you to access the files on the server again.
    If you want to run the server in the background, you can use the nohup command, which runs the server in the background and allows you to disconnect from the terminal session.
    For example, you can run the server using the following command:
    nohup python -m http.server 8000 &
    This will start the server and continue running even if you disconnect from the terminal session.
    To stop the server, you can use the kill command, which sends a SIGTERM signal to the server process, which will cause it to shut down gracefully.
    For example, you can stop the server using the following command:
    kill $(pgrep -f "python -m http.server 8000")
    This will send a SIGTERM signal to the server process identified by the pgrep command, which will cause the server to shut down gracefully.
    If you want to run the server in the background and stop it later, you can use the following command:
    python -m http.server 8000 &
    This will start the server in the background and continue running even if you disconnect from the terminal session.
    To stop the server, you can use the following command:
    fg

These files can be accessed from any other devices using the ip like this
    if your ip is 192.168.1.5:~ python -m http.server 8000 -b 192.168.1.5 ---> The prerequisite is that the ip should exist and the -b is bind to this ip and send an request to the server.
                              You can also access your server from any other devices using the ip like this
 """
