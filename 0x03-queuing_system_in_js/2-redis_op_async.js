import { createClient } from "redis";

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

await client.connect();

async function setNewSchool(schoolName, value) {
  await client.set(schoolName, value);
}

async function displaySchoolValue(schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', 100)
displaySchoolValue('HolbertonSanFrancisco')

