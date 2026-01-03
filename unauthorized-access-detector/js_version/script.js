const http =require("http");
const fs = require("fs");

const createFile = funtion("new_file.txt",)

const server = http.createServer(function (req, res) {
    console.log(req.url, req.method);
    res.end()
});

const PORT = 3000;
server.listen(PORT, function () {
    console.log(`Server started on https://localhost:${PORT}`)
    console.log(`Listening on port ${PORT}`);
});