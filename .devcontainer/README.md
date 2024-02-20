# Devcontainer

This project has a devcontainer ready for you to use.
Just use devcontainer CLI or your IDE to launch it.

## Requirements

On your machine, you should have:
- [Docker](https://www.docker.com/) with `docker compose`
- IDE (Visual Studio Code / Visual Studio / ...)
- DPF standalone archive

## Preparation

The container needs a DPF standalone archive.

Download it from the customer portal, pre-release page or any pipeline and put it into `.devcontainer/standalones`.

Copy and rename `compose.override.example/yaml` to `compose.override.yaml`. This will be your local configuration of your current environment.

You can change the arguments to make the configuration change.

## Running the container

*(This procedure has been done with Visual Studio Code.)*
To run the devcontainer, do the following:
- Install [devcontainer extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for VS Code
- If you are using WSL without Docker Desktop:
    - Open settings *(ctrl + ,)*
    - Activate the devcontainer extension option named "Execute in WSL"
- Run the VS Code command `Dev Containers: Reopen in Container` (press F1 and type the preceding command)

This command will start your devcontainer as well as a DPF server in another container. This way you can try remote and in-process connections.

## Adding your own bash commands

You can execute custom shell scripts thanks to hooks created in the mandatory scripts. You can make use of the following scripts (in `.devcontainer/scripts/`):
-  `postcreate.own.sh`: Executed after container creation (after building) as the `vscode` user (has environment set). [runs once]

### Recommended minimal custom postcreate script

We recommend that you use at least this minimal postcreate script (`postcreate.own.sh`):
```bash
git config --global user.name "[FILL_HERE]"
git config --global user.email "[FILL_HERE]"
```

## Using docker compose in the container

Docker compose is launched by default with a specific project name which is the name of the root folder by default.

Environment variable `COMPOSE_PROJECT_NAME` automates `docker compose` talking to the compose project which started your devcontainer.

In case you want to launch another `docker compose` project, specify it with the appropriate flag `-p [PROJECT_NAME]`.

## Switching standalone version used

You can manage multiple standalone versions easily. Just download them and put them all into `.devcontainer/standalones`.

Then use the `DPF_SERVER_VERSION` argument in `compose.override.yaml` file to specify the archive you want (`24.2`, `24.2.pre0`...).

Nothing is made to differenciate between archive origins. But you can use `DPF_SERVER_VERSION` to do so:
- Change the name of the archive as you want (e.g: `dpf_standalone_24.2_from_pipeline.zip`)
- Update `DPF_SERVER_VERSION` accordingly (e.g: `24.2_from_pipeline`)

Everything will be managed for you regarding the version.

**Then rebuild the container.**

In `.devcontainer` folder, you can run:
`docker compose up -d --force-recreate --build dpf_server`
