#!/usr/bin/env python
import os
import sys
import socket

httpStatusMessages = {
    200: 'OK',
    403: 'Forbidden',
    404: 'Not Found',
    405: 'Method Not Allowed',
}

def respond_error(connection, statuscode):
    """Short-handle for responding with a generic error message."""
    respond(connection, statuscode, "text/plain", httpStatusMessages[statuscode])

def runServer(port):
    """Set up and run the server."""
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("localhost", port))
    s.listen(1)
    while True: # infinite loop
        print 'Awaiting client connection...\n'
        
        conn, addr = s.accept()
        print 'Client connected : ', addr
        
        ##### read the request
        keepReading = True
        data = ""
        while keepReading:
            data += conn.recv(256) #256, abitrary buffer size
            if (not data) or (data.find("\r\n\r\n") != -1):
                keepReading = False
        
        # extract the first line
        firstLine = data[:data.find("\r\n")]
        
        # extract the method and path
        firstSpace = firstLine.find(' ')
        lastSpace = firstLine.rfind(' ')
        method = firstLine[:firstSpace]
        path = firstLine[firstSpace+1:lastSpace]
        
        ##### respond
        
        #TODO: respond with a minimal HTML or TEXT page
        #      with a counter of how many times the page
        #      has been served. You may customize the
        #      reply given the path and method extracted
        #      from the request.
        
        conn.close()

if __name__ == '__main__':
    runServer(8080)