import { Redis } from "ioredis";
const client = new Redis({
  host: "redis", // Docker service name
  port: 6379,
});

export { client };
