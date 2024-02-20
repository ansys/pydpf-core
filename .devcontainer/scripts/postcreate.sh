set -e

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

pip install -e .

pip install -e /dpf_standalone/.

cat <<'EOF' >> $HOME/.bashrc
    alias dpf-ip="docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' dpf-server"
EOF

if [ -f "$SCRIPT_DIR/postcreate.own.sh" ]; then
    . "$SCRIPT_DIR/postcreate.own.sh"
fi
