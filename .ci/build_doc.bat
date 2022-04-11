set SPHINX_APIDOC_OPTIONS=inherited-members
call sphinx-apidoc -o ../docs/source/api ../ansys -f --implicit-namespaces --separate  --no-headings
pushd .
cd ../docs/
call make clean
call make html
popd
