import { client } from "./client.js";

async function redisString(){
    await client.set("user:1", "deepak")
    const result = await client.get("user:1")
    console.log("result", result);
}

export default redisString