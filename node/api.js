//Creates a webservedr with data from a json file

var http = require("http");
var data = require("./widgets.json")

function listblue(res){
    var colorBlue = data.filter(function(item){
        return item.color === "blue"
    });
    res.writeHead(200, {"Content-Type": "text/json"});
    res.end(JSON.stringify(colorBlue))
}

var server = http.createServer(function(req, res){
    if (req.url === "/"){
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));
    }
    else if (req.url ==="/blue"){
        listblue(res)
    }
    else {
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end("404 data not found")
    }
});

server.listen(3000);
console.log('server is listening on port 3000');


