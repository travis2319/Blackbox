// server.js

const http = require("http");
const socketIo = require("socket.io");

const server = http.createServer();
const io = socketIo(server);

io.on("connection", (socket) => {
  console.log("Client connected");

  socket.on("message", (data) => {
    console.log("Received from client:", data);
    if (data === "logout") {
      socket.disconnect();
    } else {
      socket.emit("message", "Hello from Node.js server");
    }
  });

  socket.on("disconnect", () => {
    console.log("Client disconnected");
  });
});

server.listen(12345, () => {
  console.log("Server listening on port 12345");
});
