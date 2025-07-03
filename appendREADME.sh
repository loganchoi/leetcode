#!/bin/bash

# Usage: ./append_leetcode_entry.sh 637 "Average of Levels in Binary Tree" "https://leetcode.com/problems/average-of-levels-in-binary-tree/" BFS AverageLevelsBinaryTree Easy




NUM="$1"
TITLE="$2"
URL="$3"
TOPIC="$4"
FOLDER="$5"
DIFFICULTY="$6"

mkdir $FOLDER
mv $FOLDER code 
touch code/$FOLDER/"$FOLDER.py"


LINE=$'\n'"|$NUM|[$TITLE]($URL)|$TOPIC|[Python](./code/$FOLDER/$FOLDER.py)|$DIFFICULTY|"

echo "$LINE" >> README.md
echo "Appended to README.md:"
echo "$LINE"
