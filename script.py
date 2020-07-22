import os
f = open("stats.txt", "r")
content = int(f.read())
streamnumber = content + 1
f.close()
print(streamnumber)
update = str(streamnumber)
wittemplate = "🔴 [LIVE] 🔴\n🔴 720p/60fps Stream 🔴\n\n\n🔥 Some [gameName] Action 🔥\n🔥 Livestream:#" + f"{update} 🔥\n🔥 Thanks you for watching 🔥"
f = open('template.txt',"w+", encoding="utf8")
f.write(wittemplate)
f.close()
f = open('stats.txt',"w+", encoding="utf8")
f.write(update)
f.close()






#gameName = input('What game are you playing?\n')
