# -*- coding: utf-8 -*-
"""EES: Too much yelling..

---
layout:     post
error_code: SCH
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10 12:31:19
categories: writing
---

Too much yelling.

"""
from proselint.tools import blacklist

err = "MAU103"
msg = u"Too much yelling."

check = blacklist(["[A-Z]+ [A-Z]+ [A-Z]+"], err, msg, ignore_case=False)
