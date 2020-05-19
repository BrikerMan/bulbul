#!/usr/bin/env bash

echo "Build and Run API documents"

# Copy readme file to docs folder
cp readme.md mkdocs/docs/index.md
cd mkdocs
mkdocs serve
