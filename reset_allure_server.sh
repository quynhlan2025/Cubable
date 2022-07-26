#!/bin/bash

lsof -ti tcp:3000 | xargs kill
sleep 3

