#!/bin/bash
IFS_TMP=$IFS
IFS=$'\n'

if [ "${#}" -eq "2" ]; then
	video_ext=$1
	sub_ext=$2
else
	video_ext=mkv
	sub_ext=ass
fi

i=-1
for video in `ls | grep $video_ext`
do
	((i++))
	v[$i]=${video%.*}
done

index=-1
for subtitle in `ls | grep $sub_ext`
do
	((index++))
	mv $subtitle ${v[$index]}.$sub_ext
done 

IFS=$IFS_TMP
