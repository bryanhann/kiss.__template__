#!/usr/bin/env python3

from __me__ import ME

def test_ME_my_bucket():
    assert ME.my.bucket_remote.startswith ('s3://')
