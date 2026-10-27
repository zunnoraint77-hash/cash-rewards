[app]

# (str) Title of your application
title = My Cash Rewards App

# (str) Package name
package.name = cashrewards

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (str) Version of your application
version = 0.1

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,kivymd,requests

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
#services = 

#
# Android specific
#

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
#android.permissions = INTERNET

# (list) target API version for the application
android.target_api = 33

# (list) Kotlin version
#android.kotlin_version = 1.6.10

# (str) Android min API version
android.min_api = 21

# (str) Android SDK version
android.android_sdk_version = 33

# (str) Android NDK version
#android.android_ndk_version = 23b

# (str) Android aab (true) or apk (false) (format)
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = int, 1 = false)
level = 2
warn_on_root = 1
