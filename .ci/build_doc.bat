set SPHINX_APIDOC_OPTIONS=inherited-members
call sphinx-apidoc -o ../docs/source/api ../ansys -f --implicit-namespaces --separate  --no-headings
pushd .
cd ../docs/
call make clean
call make html

copy /y build\html\_images\graphviz* source\examples\06-distributed-post\images
copy /y source\examples\06-distributed-post\images build\html\_images\graphviz*
popd
