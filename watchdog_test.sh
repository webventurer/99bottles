#!/bin/bash

watchmedo shell-command --patterns="*.py" --recursive --command='echo "${watch_src_path}"' .