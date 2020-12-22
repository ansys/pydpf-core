### DPF Docker Image

Run DPF within a container on any OS using `docker`.

---

There are several situations in which it is advantageous to run DPF
in a containerized environment (e.g. Docker or singularity):

- Run in a consistent environment regardless of the host OS.
- Portability and ease of install.
- Large scale cluster deployment using Kubernetes
- Genuine application isolation through containerization.

### Usage

This repository hosts several docker images which you can use to start
working with DPF immediately.  Assuming you have docker installed,
you can get started by authorizing docker to access this repository
using a personal access token.  Create a GH personal access token with
`packages read` permissions according to
[Creating a personal access token](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)

Save that token to a file with:
```
echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX > GH_TOKEN.txt
```

This lets you send the token to docker without leaving the token value
in your history.  Next, authorize docker to access this repository
with:

```
GH_USERNAME=myusername
cat GH_TOKEN.txt | docker login docker.pkg.github.com -u $GH_USERNAME --password-stdin
```

You can now launch DPF directly from docker with a short script or
directly from the command line.

```bash
docker run -it --rm -v `pwd`:/dpf -p 50054:50054 docker.pkg.github.com/pyansys/dpf-core/dpf:v2021.1
```

Note that this command shares the current directory to the `/dpf`
directory contained within the image.  This is necessary as the DPF
binary within the image needs to access the files within the image
itself.

Additionally, to avoid having to run `connect_to_server` at the start of every script, you can tell `ansys.dpf.core` to always attempt to connect to DPF running within the docker image by setting the following environment variables:

```
export DPF_START_SERVER=False
export DPF_PORT=50054
```

``DPF_PORT`` is the port exposed from the DPF container and should match
the first value within the `-p 50054:50054` pair.

``DPF_START_SERVER`` tells `ansys.dpf.core` not to start an instance and
rather look for the service running at DPF_IP and DPF_PORT.  If
those environment variables are undefined, they default to 127.0.0.1
and 50054 for DPF_IP and DPF_PORT respectively.
