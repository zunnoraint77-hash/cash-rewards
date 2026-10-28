[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android packaging)
package.domain = org.zunn

# (str) Source directory where the application lives
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusions using pattern matching
source.exclude_patterns = license,images/.*/*.jpg

# (str) Application versioning
version = 0.1

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

#
# Android specific
#

# (bool) Indicate whether you accept the Android SDK terms of use.
# Needed for packages that require explicit agreement.
android.accept_sdk_license = True

# (str) Android API to use
android.api = 33

# (str) Minimum Android API to use
android.min_api = 21

# (str) Android SDK version to use
android.sdk = 33
