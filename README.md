# Requirements
[docker](https://www.docker.com/get-docker)
[pip](https://pip.pypa.io/en/stable/installing/)

# Getting started
To create the database for the application, run the following commands:
```
python
>>> from app import init_db
>>> init_db()
```

You should see a confirmation message printed to the terminal: `users table created for BST maxSum Database`

Now, you can run docker

```
docker-compose up --build
```

Visit [http://localhost:5000/](http://localhost:5000/) in your browser to get started

# Binary Search Tree
To create a binary search tree, pass a list of comma separated integers. Non-number characters will not be added to the tree and ignored. Each node will be added in order. 

The max sum will be calculated and displayed in the UI once submitted for creation and analysis


## Future Optimizations
This is a basic web application with a basic `SQLite` instance. To improve scalability, I would do the following:
- Remove `debug=True` from app configuration
- Deploy multiple instances of the application with one `ngnix` web server, cache, and load balancer in front to handle simultaneous connections
- Employ multi-tenancy for the database as well as allow users to save, retrieve, modify, and delete binary search trees
- Use `celery` for long running tasks, such as the max sum calculation and provide async responses to the front-end upon completion
