#!/bin/sh
echo "Checking screen orientation ..."
mkdir /boot_tmp
mount /dev/mmcblk0p1 /boot_tmp
sed -i "s/lcd_rotate=2/#display_rotate=0/g" /boot_tmp/config.txt
umount /boot_tmp
rm -rf /boot_tmp
echo "Starting app ..."
python /app/rest_api.py