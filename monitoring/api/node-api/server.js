import express from "express";
import { doHeavyTask } from "./util.js";
const app = express();

const PORT = process.env.PORT || 8080;

app.get("/", (req, res) => {
  res.json({ message: "Welcome to Nodejs Server" });
});

app.get("/heavy", (req, res) => {
  let total = 0;
  for (let i = 0; i < 1e5; i++) {
    total += i;
  }
  res.json({ total });
});

app.get("/heavy-task", async (req, res) => {
  try {
    const timeTaken = await doHeavyTask();
    return res.json({
        status: "Success",
        message: `Task completed in ${timeTaken} ms`
    })
  } catch (err) {
    return res.status(500).json({
      status: "Error",
      error: err.message,
    });
  }
});

app.listen(PORT, () => {
  console.log("Server is running port", PORT);
});
