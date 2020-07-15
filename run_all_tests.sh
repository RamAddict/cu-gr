#!/bin/bash
# The purpose of this script is to run all tests with all executables
# The results are dumped in the same directory as the script
executables=(
	ascendingHP
	ascendingNPins
	ascendingNPinsHP
	descendingHP
	descendingNPins
	descendingNPinsHP
	unordered
)


tests=(
	ispd18_test5_metal5
	ispd18_test8_metal5
	ispd18_test10_metal5
	ispd19_test7_metal5
	ispd19_test8_metal5
	ispd19_test9_metal5
)

LEF_PATH="/data/ICCAD_2019_Contest/"
DEF_PATH="/data/ICCAD_2019_Contest/"


for iccadgr in "${executables[@]}"; do
	echo $iccadgr
	for test in "${tests[@]}"; do
		./csv_executables/$iccadgr -lef ${LEF_PATH}${test}/${test}.input.lef -def ${DEF_PATH}${test}/${test}.input.def -threads 1 -output "${test}.${iccadgr}.guide" > "${test}.${iccadgr}.txt"
	done
done
