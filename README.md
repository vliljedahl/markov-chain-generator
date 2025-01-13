# markov-chain-generator
Random text generator utilizing markov chain principle

## Behaviour
The tool takes the entry text file from the `text-file.txt` and processes it.
Text file contents are read into memory and stored into database as 3 word tuples.
Currently the database is in-memory list with tuples of length of three.

## Future improvements
- Dockerize the application
- Create interface using a web framework
    - Django, Flask, etc.
- Utilize a real database
    - MongoDB, redis, etc.
