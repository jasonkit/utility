break_timer.py
===============

Simple timer utility for Mac OS 10.8+ (with notification center)
Depends on terminal-notifier (http://rubygems.org/gems/terminal-notifier)

Usage
-----
break_timer INTERVAL|stop [MESSAGE]
INTERVAL: [0-9]+[s|m|h]

Example
-------
./break_timer 1h

This will setup a timer and prompt you every hour with default message "Time to have a break"

./break_timer 30m "Stand up and move!"

This will setup a timer and prompt you every 30 minutes with message "Stand up and move!"
