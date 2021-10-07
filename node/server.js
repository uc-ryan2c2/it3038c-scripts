var fs = require("fs");
var os = require("os");
var http = require("http"); //this is what defines our server
var ip = require('ip');
var uptime = os.uptime()

const { fstat } = require("fs");

//this is to get the server uptime from seconds to minutes, hours, and days.
var ut_sec = os.uptime();
var ut_min = ut_sec/60;
var ut_hour = ut_min/60;
var ut_days = ut_hour/24;
   
ut_sec = Math.floor(ut_sec);
ut_min = Math.floor(ut_min);
ut_hour = Math.floor(ut_hour);
ut_days = Math.floor(ut_days)
  
ut_hour = ut_hour%60;
ut_min = ut_min%60;
ut_sec = ut_sec%60;

//total memory of our system
totalMemory = os.totalmem();
MBmemory = totalMemory / 1000000;

//free memory
free = os.freemem()
MBfree = free / 1000000; 

//this will give up CPU core count
const CPUs = os.cpus().length;

//this builds the web server
var server = http.createServer(function(req, res) {
    if (req.url === "/"){

        res.writeHead(200, {"content-type":"text/html"});
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
            res.writeHead(200, {"content-Type":"text/html"})
            res.end(body);
        });
    }
    //this is the info for the sysinfo page
    else if(req.url.match("/sysinfo")){
        myHostName=os.hostname();
   
        html = `
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Node JS response</title>
                </head>
                    <body>
                    <p>Hostname: ${myHostName} </P>
                    <p>IP: ${ip.address} </P>
                    <p>Server Uptime: Days: ${ut_days}, Hours: ${ut_hour}, Minutes: ${ut_min}, Seconds: ${ut_sec}</P>
                    <p>total Memory: ${MBmemory} MB </P>
                    <p>Free Memory: ${MBfree} MB </P>
                    <p>Number of CPUs: ${CPUs} </P>
                    </body>
            </html>                  
        `
        res.writeHead(200, {"content-type":"text/html"})
        res.end(html)
    }

    else{
        res.writeHead(404, {"Content-Type":"text/html"})
        res.end(`404 file not found at ${req.url}`)
    }

});

server.listen(3000)

console.log("server listening on port 3000");