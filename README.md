# Kedro Iris API

This is an enhanced implementation of the Kedro Iris Starter project, running as a Flask API on Docker.

## Run Locally

Clone the project,

```
git clone https://github.com/MinuraPunchihewa/kedro-iris-flask-docker.git
```

Go to the project directory,

```
cd kedro-iris-flask-docker
```

Build the Docker image,

```
docker build -t <image-name> .
```

Run the Docker image,

```
docker run -p 5000:5000 <image-name>
```

Run the default pipeline by submitting a call to the `/run` endpoint along with train-test split ratio,
```
localhost:5000/run/<train-test-split>
```

## Testing

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
kedro test
```

## Related Projects

- [Kedro Iris Starter](https://github.com/quantumblacklabs/kedro-starter-pandas-iris.git): The original Kedro Iris Starter Project.
- [Kedro Iris Enhancements](https://github.com/MinuraPunchihewa/kedro-iris.git): An enhanced implementation of the Kedro Iris Starter project.
