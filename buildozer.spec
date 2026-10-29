[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.zunn

# (str) Source directory where the application is stored
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusions using pattern matching
source.exclude_patterns = license,images/.*

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate whether you accept the Android SDK License
android.accept_sdk_license = True

# (str) Android API to use
android.api = 33

# (str) Minimum Android API to use
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 28c

# (str) Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (int) Log level (0 = error only, 1 = info, 2 = debug command output)
log_level = 2
