import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

const channel = 'holberton school channel';

await client.subscribe(channel, async (message) => {
  console.log(message)

  if (message === 'KILL_SERVER') {
    await client.unsubscribe(channel);
    client.quit();
  }
});
