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
