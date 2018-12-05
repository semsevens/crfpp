
echo "install-local start"
INSTALL_PATH=$HOME/local/CRF++
echo $INSTALL_PATH
./configure --prefix=$INSTALL_PATH &&
make &&
make install
echo "install-local done"
