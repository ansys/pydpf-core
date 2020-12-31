.. _docker:

************************
Using DPF Through Docker
************************

You can run DPF within a container on any OS using `docker`.



There are several situations in which it is advantageous to run DPF
in a containerized environment (e.g. Docker or singularity):

- Run in a consistent environment regardless of the host OS.
- Portability and ease of install.
- Large scale cluster deployment using Kubernetes
- Genuine application isolation through containerization.

Installing the DPF Image
------------------------
There is a docker image hosted on the `DPF-Core GitHub
<https://https://github.com/pyansys/DPF-Core>`_ repository that you
can download using your GitHub credentials.

Assuming you have docker installed, you can get started by
authorizing docker to access this repository using a personal access
token.  Create a GH personal access token with ``packages read`` permissions
according to `Creating a personal access token <https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token>`_

Save that token to a file with:

.. code::

   echo XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX > GH_TOKEN.txt


This lets you send the token to docker without leaving the token value
in your history.  Next, authorize docker to access this repository
with:

.. code::

    GH_USERNAME=<my-github-username>
    cat GH_TOKEN.txt | docker login docker.pkg.github.com -u $GH_USERNAME --password-stdin


You can now launch DPF directly from docker with a short script or
directly from the command line.

.. code::

   docker run -it --rm -v `pwd`:/dpf -p 50054:50054 docker.pkg.github.com/pyansys/dpf-core/dpf:v2021.1


Note that this command shares the current directory to the ``/dpf``
directory contained within the image.  This is necessary as the DPF
binary within the image needs to access the files within the image
itself.  Any files you wish to have DPF read will have to be placed in
the ``pwd``.  You can map other directories as needed, but these
directories must be mapped to the ``/dpf`` directory for the server to
see the files you wish it to read.


Using the DPF Container from Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Normally ``ansys.dpf.core`` attempts to start the DPF server at the first usage of a DPF class.  If you do not have ANSYS installed and simply wish to use the docker image, you can override this behavior by connecting to the DPF server on the port you mapped with:

.. code:: python

   from ansys.dpf import core as dpf_core

   # uses 127.0.0.1 and port 50054 by default
   dpf_core.connect_to_server()
   

If you wish to avoid having to run ``connect_to_server`` at the start of
every script, you can tell ``ansys.dpf.core`` to always attempt to
connect to DPF running within the docker image by setting the
following environment variables:

.. code::

   export DPF_START_SERVER=False
   export DPF_PORT=50054

Or on windows:

.. code::

   set DPF_START_SERVER=False
   set DPF_PORT 50054


Where ``DPF_PORT`` environment variable is the port exposed from the
DPF container and should match the first value within the ``-p 50054:50054`` pair.

And ``DPF_START_SERVER`` tells ``ansys.dpf.core`` not to start an
instance and rather look for the service running at ``DPF_IP`` and
``DPF_PORT``.  If those environment variables are undefined, they
default to 127.0.0.1 and 50054 for ``DPF_IP`` and ``DPF_PORT``
respectively.

