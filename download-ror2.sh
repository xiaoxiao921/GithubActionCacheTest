#!/bin/sh
wget https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz
tar -xvzf steamcmd_linux.tar.gz
rm -rfv steamcmd_linux.tar.gz
./steamcmd.sh +login anonymous +force_install_dir ror2 +@sSteamCmdForcePlatformType windows +app_update "1180760" +quit
