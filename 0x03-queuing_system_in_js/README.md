# Queuing system in JavaScript

Learn how to implement a simple queuing system

## Tasks to Complete
### Install a redis instance
- Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - [https://redis.io/download](https://redis.io/download)):
  ```
  wget https://download.redis.io/redis-stable.tar.gz
  tar -xvzf redis-stable.tar.gz
  cd redis-stable
  make MALLOC=libc # for linux systems
  # make MALLOC=jemalloc # for Mac OS X systems
  ```

  - Start Redis in the background with `src/redis-server`.
  - Make sure that the server is working with a ping `src/redis-cli` ping.
  - Using the Redis client again, set the value `School` for the key `Holberton`.
  - Kill the server with the process id of the redis-server (hint: use `ps` and `grep`).
- Copy the [dump.rdb](./dump.rdb) from the `redis-stable` directory into the root of this project.
- **Requirements**:
  - Running get `Holberton` in the client, should return `School`.

### Node Redis Client
- Install [node_redis](github.com/redis/node_redis) using yarn or npm.
- Using Babel and ES6, write a script named [0-redis_client.js](./0-redis_client.js). It should connect to the Redis server running on your machine:
  - It should log to the console the message `Redis client connected to the server` when the connection to Redis works correctly.
  - It should log to the console the message `Redis client not connected to the server: ERROR_MESSAGE` when the connection to Redis does not work.
- **Requirements**:
  - To import the library, you need to use the keyword `import`.

### Node Redis client and basic operations
In a file [1-redis_op.js](./1-redis_op.js), copy the code you previously wrote ([0-redis_client.js](./0-redis_client.js)).
- Add two functions:
  - `setNewSchool`:
    - It accepts two arguments `schoolName`, and `value`.
      - It should set in Redis the value for the key `schoolName`.
      - It should display a confirmation message using `redis.print`.
  - `displaySchoolValue`:
    - It accepts one argument `schoolName`.
    - It should log to the console the value for the key passed as argument.
- At the end of the file, call:
  - `displaySchoolValue('Holberton');`.
  - `setNewSchool('HolbertonSanFrancisco', '100');`.
  - `displaySchoolValue('HolbertonSanFrancisco');`.
- **Requirements**:
  - Use callbacks for any of the operation, we will look at async operations later.

### Node Redis client and async operations
In a file [2-redis_op_async.js](./2-redis_op_async.js), copy the code from the previous exercise ([1-redis_op.js](./1-redis_op.js)).
Using `promisify`, modify the function `displaySchoolValue` to use ES6's `async / await`.
Same result as [1-redis_op.js](./1-redis_op.js).

### Node Redis client and advanced operations
In a file named [4-redis_advanced_op.js](./4-redis_advanced_op.js), use the client to store a hash value.
- Create Hash:
  - Using `hset`, let's store the following:
    - The key of the hash should be `HolbertonSchools`.
    - It should have a value for:
      - `Portland=50`.
      - `Seattle=80`.
      - `New York=20`.
      - `Bogota=20`.
      - `Cali=40`.
      - `Paris=2`.
    - Make sure you use `redis.print` for each `hset`. Used an old version redis no longer contains print
- Display Hash:
  - Using `hgetall`, display the object stored in Redis. It should return the following:
    ```
    bob@dylan:~$ yarn dev 4-redis_advanced_op.js

    > queuing_system_in_js@1.0.0 dev /root
    > nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

    [nodemon] 2.0.4
    [nodemon] to restart at any time, enter `rs`
    [nodemon] watching path(s): *.*
    [nodemon] watching extensions: js,mjs,json
    [nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
    Redis client connected to the server
    Reply: 1
    Reply: 1
    Reply: 1
    Reply: 1
    Reply: 1
    Reply: 1
    {
      Portland: '50',
      Seattle: '80',
      'New York': '20',
      Bogota: '20',
      Cali: '40',
      Paris: '2'
    }
    ^C
    bob@dylan:~$
    ```

- **Requirements**:
  - Use callbacks for any of the operation, we will look at async operations later. Use async as it is now the way `node_redis` works

### Node Redis client publisher and subscriber

- In a file named [5-subscriber.js](./5-subsriber.js), create a redis client:
  - On connect, it should log the message `Redis client connected to the server`.
  - On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`.
  - It should subscribe to the channel `holberton school channel`.
  - When it receives message on the channel `holberton school channel`, it should log the message to the console.
  - When the message is `KILL_SERVER`, it should unsubscribe and quit.
- In a file named [5-publisher.js](./5-publisher.js), create a redis client:
  - On connect, it should log the message `Redis client connected to the server`.
  - On error, it should log the message `Redis client not connected to the server: ERROR MESSAGE`.
  - Write a function named `publishMessage`:
    - It will take two arguments: `message` (string) and `time` (integer - in ms).
    - After `time` millisecond:
      - The function should log to the console `About to send MESSAGE`.
      - The function should publish to the channel `holberton school channel`, the message passed in argument after the time passed in arguments.
  - At the end of the file, call:
    ```
    publishMessage("Holberton Student #1 starts course", 100);
    publishMessage("Holberton Student #2 starts course", 200);
    publishMessage("KILL_SERVER", 300);
    publishMessage("Holberton Student #3 starts course", 400);
    ```

- Requirements:
  - You only need one Redis server to execute the program.
  - You will need to have two node processes to run each script at the same time.

- Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call "background workers".

### Create the Job creator
In a file named [6-job_creator.js](./6-job_creator.js):
- Create a queue with `Kue`(Kue is now deprecated so I'll use `Bull`).
- Create an object containing the Job data with the following format:
  ```
  {
    phoneNumber: string,
    message: string,
  }
  ```
- Create a queue named `push_notification_code`, and create a job with the object created before.
- When the job is created without error, log to the console `Notification job created: JOB ID`.
- When the job is completed, log to the console `Notification job completed`.
- When the job is failing, log to the console `Notification job failed`.

Nothing else will happen - to process the job, go to the next task!
If you execute multiple time this file, you will see the `JOB ID` increasing - it means you are storing new jobs to process…
