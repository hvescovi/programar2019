var express = require("express");

var app = express();
var server = require("http").Server(app);
var path = require("path");
var THREE = require("three");

app.get("/", function (req, res) { 
    res.sendFile(__dirname + "/public/index.html");
});

app.use(express.static(path.join(__dirname, "public")));

server.listen(3000);
console.log("Server initialized!");

var socket_list = {};

var io = require("socket.io")(server, {pingInterval: 5000});
io.sockets.on("connection", function(socket){
	console.log("Socket ID: " + socket.id);

	socket_list[socket.id] = socket;
	socket.on('disconnect', function(){
		delete socket_list[socket.id];
	});
	
	socket.on('ping_back', function(data){
		//console.log(socket.id+": "+data.ping);
	});
	
});