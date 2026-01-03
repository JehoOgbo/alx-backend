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


