set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pip install -e .

pip install -e /dpf_standalone/.

cat <<'EOF' >> $HOME/.bashrc
    alias dpf-ip="docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' dpf-server"
    alias dpf-info="docker exec dpf-server cat /ansys_inc/.env"
    alias dc="docker compose -f $REPO_ROOT/.devcontainer/compose.yaml"
    alias dpf-recreate="dc up -d --force-recreate --build dpf-server"
EOF

if [ -f "$SCRIPT_DIR/postcreate.own.sh" ]; then
    . "$SCRIPT_DIR/postcreate.own.sh"
fi
