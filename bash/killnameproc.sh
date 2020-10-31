#!/bin/bash
# 该脚本用于kill某种固定名字的进程
# 如当想要杀死名字时manage名字的进程时使用如下命令
# ./killnameproc manage
# 注意不要杀死不必要进程

res="ps aux"
for i in "$*"; do
    echo $i
    res="${res}"" | grep "$i" "
    # echo ${res} 
done
res="${res}| grep -v grep|awk '{print \$2}'|xargs kill"
echo ${res}
eval $res
