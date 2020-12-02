# docker_flask
A simple flask app (and API) in docker.  
The folder structure supports scaling, and there is a segregation of init and app. 

Many possibilities

![](https://github.com/ayushsubedi/docker_flask/blob/master/feature.PNG?raw=true)

### Change

```
if __name__ == '__main__':
    application.run(host= '0.0.0.0', debug=True)
```

### Build
```docker build -f Dockerfile -t docker_flask .```

### Run
```docker run -p 5000:5000 -ti docker_flask /bin/bash -c "cd /src && source activate ml && python run.py"```
