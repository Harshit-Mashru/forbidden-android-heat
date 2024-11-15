# forbidden-android-heat
My second CTF Problem for PicoCTF

## Keywords
Web Exploitation
Robots.txt
Python eval
Fuzzing


## Set up steps

1) git clone this repository

2) cd into the repo and run the following command to set-up the docker
```
docker build -t forbidden-android-heat .
```

3) To start the server, run the following command
```
docker run -it forbidden-android-heat
```

4) You should now have access to the server on
```
http://<Docker ip>:4000
```
