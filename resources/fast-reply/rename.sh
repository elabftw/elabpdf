#!/bin/bash
i=1
files=$(find . -name '*.png')
for f in $files; do
    mv "$f" "${i}.png"
    let i++
done

