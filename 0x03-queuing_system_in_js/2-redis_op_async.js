#!/usr/bin/env node
// when redis connect should log Redis client connected to the server
// when fail should log: Redis client not connected to the server
// : ERROR_MESSAGE
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});

const setAsync = promisify(client.set).bind(client);
const getAsync = promisify(client.get).bind(client);

// it should set in Redis the value for the key schoolName
// it should display a confirmation message using redis.print
const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
}

// it should log to the console the value for the key passed as argument
const displaySchoolValue = async (schoolName) => {
  const result = await getAsync(schoolName);
  console.log(result)
}
// call displaySchoolValue with the Holberton key
displaySchoolValue('Holberton');
// add a new key-value pair using setNewSchool with HolbertonSanFrancisco
// as the key and 100 as the value
setNewSchool('HolbertonSanFrancisco', '100');
// call displaySchoolValue again with the new key.
displaySchoolValue('HolbertonSanFrancisco');
