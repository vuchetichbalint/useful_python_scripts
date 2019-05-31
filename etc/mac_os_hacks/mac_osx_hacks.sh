# disable the applespelling
# source: https://medium.com/@tk512/disabling-applespell-on-os-x-yosemite-7195efa8855a

$ ps auxw|grep Spell
tk 608 0.0 0.0 2623488 7756 ?? S Fri03PM 0:05.42 /System/Library/Services/AppleSpell.service/Contents/MacOS/AppleSpell -psn_0_225335
$ cd /System/Library/Services/
$ sudo kill -9 608 && sudo mv AppleSpell.service AppleSpell.service.disabled


