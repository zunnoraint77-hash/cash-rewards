[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.zunn

# (list) Source files to include (let it include py, png, kv, etc.)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusions using pattern matching
source.exclude_patterns = license,images/*.jpg

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Yahan apne app ki dependencies dein (jaise python3, kivy, requests, etc.)
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# --- ANDROID SPECIFIC CONFIGURATIONS ---

# (int) Target Android API, should be as high as possible. (API 34 stable hai)
android.api = 34

# (int) Minimum API your APK will support
android.min_api = 21

# (int) Android SDK version to use
android.sdk = 34

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (string) Presets
android.presplash_color = #FFFFFF

# (bool) Automatically accept Android SDK license agreements (Yeh error se bachata hai)
android.accept_sdk_license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
