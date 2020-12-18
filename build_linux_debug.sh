#!/bin/bash

# Compile the libbpt first.
cd libs/libbpt

mkdir -p build
mkdir -p build/debug

cd build/debug
conan install -pr="../../conan_profiles/linux_debug.txt" --build missing ../..

cd ../..
cmake -S . -B build/debug -DPYTHON_EXECUTABLE=/usr/bin/python3
cmake --build build/debug

mkdir -p bpt_qgis/libs

cp "build/debug/lib/pylibbpt$(/usr/bin/python3-config --extension-suffix)" \
   ../../bpt_qgis/libs

# Go back to project root.
cd ../..

# Export the plugin into a ZIP file for installation in QGIS.
export_dir=$1
output_zip="$export_dir/bpt_qgis.zip"
zip -r $output_zip bpt_qgis
