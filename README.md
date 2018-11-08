# Watchout-Companion
Automatically creates buttons on your Stream Deck for every timeline in your WO project file.

Run the script from the command line with the Production Machine's IP address as an argument. Restart companion and your buttons will populate. This uses TCP/IP to fetch the timelines so ensure that network communication is enabled in your project.

The script currently overwrites the original db file Companion uses to save buttons. If my script corrupts that data somehow, just delete it. Companion will generate a new one.  You could also just backup the file.

C:\Users\Username\AppData\Roaming\Companion\DB

There aren't many comments in the code yet and there are some extra files in there. I'll clean this up soon. Just run main.py.

Python 3.5+ because it uses pathlib. This could be changed if needed.

If you need to add more buttons afterwards, you can just start from page 99.
