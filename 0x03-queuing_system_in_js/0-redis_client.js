#!/usr/bin/env node
// when redis connect should log Redis client connected to the server
// when fail should log: Redis client not connected to the server
// : ERROR_MESSAGE
import { createClient } from 'redis';


const client = createClient();


client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.message}`);
});
