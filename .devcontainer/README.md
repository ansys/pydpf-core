# Devcontainer

This project has a devcontainer ready for you to use.

Everything was tested based on Visual Studio Code. Feel free to test with other tools but expect failures if you do so.

## Requirements

On your machine, you should have:
- [Docker](https://www.docker.com/) with `docker compose`
- IDE (Visual Studio Code or other) supporting DevContainer or have DevContainer CLI
- DPF standalone archive(s)

## Prerequisites

### Standalone archives

In `.devcontainer/standalones/`, put at least one DPF standalone archive (from customer portal, pre-release page or pipeline).

### Compose file

Copy and rename `compose.example.yaml` to `compose.yaml`. This will be your local configuration of your current environment.

You can change the arguments to make the configuration change.

### Environment file

Copy and rename `dpf.example.env` to `dpf.env`, then fill it. These are environment variables needed by dpf-server to start and work properly.

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

We recommend that you use at least this minimal postcreate script (`.devcontainer/scripts/postcreate.own.sh`):
```bash
git config --global user.name "[FILL_HERE]"
git config --global user.email "[FILL_HERE]"
```

## Switching standalone version used

You can manage multiple standalone versions easily. Just download them and put them all into `.devcontainer/standalones/`.

Then use the `DPF_SERVER_VERSION` argument in `compose.yaml` file to specify the archive you want (`24.2`, `24.2.pre0`...).

Nothing is made to differenciate between archive origins. But you can use `DPF_SERVER_VERSION` to do so:
- Change the name of the archive as you want (e.g: `dpf_standalone_v24.2_from_pipeline.zip`) but you need to keep `dpf` then `v[VERSION]` and `.zip` extension.
- Update `DPF_SERVER_VERSION` accordingly (e.g: `24.2_from_pipeline`)

Everything will be managed for you regarding the version (you will find `ansys_inc/.env` in `dpf-server` with all deduced variables).

**Then rebuild the container.**

You can run: `docker compose -f $REPO_ROOT/.devcontainer/compose.yaml up -d --force-recreate --build dpf-server`

## Using docker compose in the container

Docker compose is launched by default with the root folder's name (folder containing `.devcontainer/` folder) as project name, which is the prefix you see before the container's name.

Environment variable `COMPOSE_PROJECT_NAME`, which is set for you, automates `docker compose` talking to the compose project which started your devcontainer.

In case you want to launch another `docker compose` project, specify it with the appropriate flag `-p [PROJECT_NAME]`.