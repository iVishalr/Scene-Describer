const express = require("express");
const bodyParser = require("body-parser");
const ejs = require("ejs");
const upload = require("express-fileupload");
const { spawn, fork, spawnSync } = require("child_process");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(__dirname + "/public"));
app.use(upload());
app.set("view engine", "ejs");

app.get("/", function (req, res) {
  fs.readdir("./video", function (err, files) {
    if (err) {
      console.log(err);
    }
    for (const file of files) {
      fs.unlinkSync(path.join("./video", file), function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
  fs.readdir("../data", function (err, files) {
    if (err) {
      console.log(err);
    }
    for (const file of files) {
      fs.unlinkSync(path.join("../data", file), function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
  fs.readdir("./public/video", function (err, files) {
    if (err) {
      console.log(err);
    }
    for (const file of files) {
      fs.unlinkSync(path.join("./public/video", file), function (err) {
        if (err) {
          console.log(err);
        }
      });
    }
  });
  res.render("home");
});
app.post("/dashboard", function (req, res) {
  res.render("dashboard");
});
app.post("/dashboard/u", function (req, res) {
  if (req.files) {
    let file = req.files.filename;
    let filename = file.name;
    let flag = false;
    file.mv("./video/" + filename, function (err) {
      if (err) {
        console.log(err);
        res.send("There was an error!");
      } else {
      }
    });
    file.mv("./public/video/" + filename, function (err) {
      if (err) {
        console.log(err);
      }
    });
    setTimeout(() => {
      res.render("predict", { filename: filename });
    }, 1000);
  }
});
app.post("/dashboard/process", function (req, res) {
  res.render("processing1", {
    filename: req.body.video,
    content: req.body.content,
  });
});

app.post("/dashboard/timestamp", function (req, res) {
  const childProcess = fork("./index.js");
  console.log(req.body);
  childProcess.send({
    pathToVideo: "./video/" + req.body.filename,
    content: req.body.content,
  });
  childProcess.on("message", (message) => {
    console.log(message);
  });
  childProcess.on("exit", (code) => {
    let data = JSON.parse(fs.readFileSync("../timestamp.json"));
    data.Time_Stamps.sort();
    res.render("timestamp", { filename: req.body.filename, data: data });
  });
});

app.post("/dashboard/repredict", function (req, res) {
  res.render("predict1", { filename: req.body.video });
});
app.post("/dashboard/r/timestamp", function (req, res) {
  const child = spawnSync("python3", ["./predict.py", `${req.body.content}`]);
  let data = JSON.parse(fs.readFileSync("../timestamp.json"));
  data.Time_Stamps.sort();
  res.render("timestamp", { filename: req.body.video, data: data });
});
app.listen(process.env.PORT || 5000, function () {
  console.log("Server Running on Port 5000");
});
