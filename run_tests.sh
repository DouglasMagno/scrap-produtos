#!/usr/bin/env bash
PREFIX="\e[1m[BUILDING]\e[0m"
echo -e "${PREFIX}" &&
docker build -t scrap-product-test ./ &&
echo -e "${PREFIX} DONE" || echo -e "${PREFIX} FAILED"

PREFIX="\e[1m[TEST]\e[0m"
echo -e "${PREFIX}" &&
docker run --rm --net=host -it scrap-product-test python -m unittest discover -s ./tests -p '*_test.py' &&
echo -e "${PREFIX} DONE" || echo -e "${PREFIX} FAILED"
