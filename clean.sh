#!/bin/bash

echo -e "Removing the following files:\n"
ls | egrep '.gro|.top|.xtc|.tpr|.log|.mdp|.cpt|.edr|.trr|.ndx|.xvg'

rm -f *.gro* *.top* *.xtc* *.tpr* *.log* *.mdp* *.cpt* *.edr* *.trr* *.ndx* *.xvg*
