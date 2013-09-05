# -*- coding: utf-8 -*-

print "你进入的一个黑暗的房间，边上有两扇门。你想进入哪一扇 #1 或者 #2?"

door = raw_input("> ")

if door == "1":
    print "这里有一只正吃着起司蛋糕的大熊。你想干什么？"
    print "1. 拿走蛋糕。"
    print "2. 朝着大熊大吼。"

    bear = raw_input("> ")

    if  bear == "1":
        print "大熊吃了你的脸。干得好！"
    elif bear == "2":
        print "大熊吃了你的胳膊。干得好！"
    else:
        print "好吧 %s 这样做可能确实比较好。熊跑了。" % bear

elif door == "2":
    print "你向着无尽深渊中的克苏鲁的视网膜凝视。"
    print "1. 蓝莓。"
    print "2. 黄色夹克衣夹。"
    print "3. 理解左轮手枪吆喝着的旋律。"

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "你的身体幸存了下来，但是心智混乱了。干得好！"
    else:
        print "疯狂腐化把你的眼睛丢进了垃圾池。干得好！"

else:
    print "你被绊倒了，并且摔在一把刀上死了。干得好！"

