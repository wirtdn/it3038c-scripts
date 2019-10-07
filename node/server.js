var http = require ("http");
var fs = require("fs");
var os = require("os");
var ip = require("ip");
var cpuCount = require('os').cpus().length;
function uptime(){
    var days1 = (os.uptime/86400);
    var hours1 = ((os.uptime/86400)/3600);
    var minutes1 = (((os.uptime/86400)/3600)/60);
    var seconds1 = ((os.uptime/86400)/3600)/60;
    var days2 =(Number(days1).toFixed(0))
    var hours2 =(Number(hours1).toFixed(0))
    var minutes2 =(Number(minutes1).toFixed(0))
    var seconds2 =(Number(seconds1).toFixed(0))

    return ("Days: " + days2+ ', Hours: ' + hours2+ ", Minutes: " + minutes2 + ", Seconds: " + seconds2)};

var server = http.createServer(function(req, res){
    if (req.url === "/"){
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
        });
    }
    else if (req.url.match("/sysinfo")){
        myHostName=os.hostname();
        myServerUptime = uptime();
        myTotalMemory = os.totalmem();
        myFreeMemory = os.freemem();
        myCPUCount = cpuCount;
        html=`
        <!DOCTYPE HTML>
        <HTML>
            <HEAD>
                <title> NodeJS SysInfo</title>   
            </HEAD> 
            <body>
                <p> Hostname: ${myHostName} </p>
                <p> IP: ${ip.address()}</p>
                <p> Server Uptime: ${myServerUptime}</p>
                <p> Total Memory: ${myTotalMemory} MB</p>
                <p> Free Memory: ${myFreeMemory} MB</p>
                <p> Number of CPUs: ${myCPUCount}</p>
        </HTML>
        `
        res.writeHead(200,{"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("404 file not found");
    }
}).listen(3000);

console.log("Server listening on port 3000");