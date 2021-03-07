const { spawnSync, fork } = require("child_process");
process.on("message", async (message) => {
  await extarctImages(message.pathToVideo, message.content);
  process.send("done");
  process.exit();
});
async function extarctImages(pathToVideo, content) {
  try {
    const child1 = spawnSync("sh", ["./scripts.sh", pathToVideo, `${content}`]);
    console.log(child1.status);
  } catch (error) {
    console.log(error);
  }
}
