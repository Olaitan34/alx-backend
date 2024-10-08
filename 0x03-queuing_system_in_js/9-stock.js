import { createClient } from 'redis';
import express from 'express';
import { promisify } from 'util';

//create express server on port 1245
const app = express();

//create redis client
const redisClient = createClient();

redisClient.on('connect', function() {
  console.log('Redis client connected to the server');
});

redisClient.on('error', function (err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

//promisify client.get function
const get = promisify(redisClient.get).bind(redisClient);

const listProducts = [
  { 'itemId': 1, 'itemName': 'Suitcase 250', 'price': 50, 'initialAvailableQuantity': 4},
  { 'itemId': 2, 'itemName': 'Suitcase 450', 'price': 100, 'initialAvailableQuantity': 10},
  { 'itemId': 3, 'itemName': 'Suitcase 650', 'price': 350, 'initialAvailableQuantity': 2},
  { 'itemId': 4, 'itemName': 'Suitcase 1050', 'price': 550, 'initialAvailableQuantity': 5}
];

//retrieve item by id
function getItemById(id) {
  return listProducts.filter((item) => item.itemId === id)[0];
}