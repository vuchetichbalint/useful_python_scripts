#!/bin/bash

SETUP=$1

lvds=LVDS1
vga=VGA2
hdmi=HDMI-1-1

mode="1920x1080_60.00"
modestring="173.00  1920 2048 2248 2576  1080 1083 1088 1120 -hsync +vsync"

mode2="1280x1024_60.00"
modestring2="109.00  1280 1368 1496 1712  1024 1027 1034 1063 -hsync +vsync"

function purge {
    (xrandr --delmode "${vga}" "${mode}" || True) >/dev/null 2>&1
    (xrandr --delmode "${hdmi}" "${mode}" || True) >/dev/null 2>&1
    (xrandr --rmmode "${mode}" || True) >/dev/null 2>&1
}
function vga_init {
    xrandr --newmode "${mode}" ${modestring}
    xrandr --addmode "${vga}" "${mode}"
    xrandr --output "${vga}" --mode "${mode}"
    xrandr --addmode "${hdmi}" "${mode}"
    xrandr --output "${hdmi}" --mode "${mode}"
}
function vga_init2 {
    xrandr --newmode "${mode2}" ${modestring2}
    xrandr --addmode "${vga}" "${mode2}"
    xrandr --output "${vga}" --mode "${mode2}"
    xrandr --addmode "${hdmi}" "${mode2}"
    xrandr --output "${hdmi}" --mode "${mode2}"
}
function vga {
    vga_init
    xrandr --output "${vga}" --mode "${mode}" --primary
    xrandr --output "${lvds}" --off
}
function hdmi {
    vga_init
    xrandr --output "${hdmi}" --mode "${mode}" --primary
    xrandr --output "${lvds}" --off
}
function vga2 {
    vga_init2
    xrandr --output "${vga}" --mode "${mode2}" --primary
    xrandr --output "${lvds}" --off
}
function hdmi2 {
    vga_init2
    xrandr --output "${hdmi}" --mode "${mode2}" --primary
    xrandr --output "${lvds}" --off
}
function lvds {
    xrandr --output "${lvds}" --auto --primary
    xrandr --output "${vga}" --off
    xrandr --output "${lvds}" --auto
    xrandr --output "${vga}" --off
}
function extend {
    vga_init
    xrandr --output "${lvds}" --auto --primary
    xrandr --output "${hdmi}" --auto
    xrandr --output "${hdmi}" --right-of "${lvds}"
}
function extend2 {
    vga_init2
    xrandr --output "${lvds}" --auto --primary
    xrandr --output "${hdmi}" --auto
    xrandr --output "${hdmi}" --right-of "${lvds}"
}
function mirror {
    xrandr --output "${vga}" --off
    xrandr --noprimary
    xrandr --output "${lvds}"
    xrandr --output "${hdmi}" --auto
    xrandr --output "${hdmi}" --same-as "${lvds}"
}

if [ "${SETUP}" == "" ] \
|| [ "${SETUP}" == "vga_init" ] \
|| [ "${SETUP}" == "help" ] \
|| [ "${SETUP}" == "?" ]; then
    echo "1920.sh <mode>"
    echo "   mode:"
    echo "      help or ?: prints this help"
    echo "      vga: VGA only mode with 1920x1080 resolution"
    echo "      vga2: VGA only mode with 1280x1024 resolution"
    echo "      lvds: laptop only mode"
    echo "      extend: laptop and 1920x1080 vga display"
    echo "      extend2: laptop and 1280x1024 vga display"
    echo "      mirror: mirrored laptop to VGA"
    echo "   empty mode defaults to vga_only"
    echo "   bad mode defaults to lvds_only"
else
    purge
    (${SETUP}) || lvds
    purge
    (${SETUP}) || lvds
fi




