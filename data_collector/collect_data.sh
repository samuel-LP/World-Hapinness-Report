#!/bin/bash

mkdir "data"

curl https://raw.githubusercontent.com/MainakRepositor/Datasets/master/World%20Happiness%20Data/2020.csv -o ./data/WorldHapiness.csv
curl https://raw.githubusercontent.com/lukes/ISO-3166-Countries-with-Regional-Codes/master/all/all.csv -o ./data/Mapping.csv
