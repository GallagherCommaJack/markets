#!/bin/bash
cp players/dummy.py players/__init__.py players/example.py new_players/
rm -r players
mkdir players
cp new_players/* players/
