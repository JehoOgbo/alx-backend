import { createClient } from "redis";

const client = createClient({
  legacyMode: true
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();
