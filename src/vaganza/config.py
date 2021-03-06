import os
import pwd
import sys
import argparse

import colorama

# ============================================================================================================================ #
# ============================================================================================================================ #
# ============================================================================================================================ #

class Configuration:

    kmer_cache_size = 10000

    class __impl:
        def __init__(self,
                        work_dir,
                        is_album,
                        is_artist,
                        artist_id,
                        set_covers):
            self.work_dir = work_dir
            self.is_album = is_album
            self.is_artist = is_artist
            self.artist_id = artist_id
            self.set_covers = set_covers

    __instance = None

    def __init__(self, **kwargs):
        if Configuration.__instance is None:
            Configuration.__instance = Configuration.__impl(**kwargs)

    def __getattr__(self, attr):
        return getattr(self.__instance, attr)

    def __setattr__(self, attr, value):
        return setattr(self.__instance, attr, value)

# ============================================================================================================================ #
# Configuration
# ============================================================================================================================ #

def init():
    configure(parse_args())

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default = os.path.abspath('/Users/Parsoa/Desktop/tagvaganza'))
    parser.add_argument("--album", action='store_true')
    parser.add_argument("--artist", action='store_true')
    parser.add_argument("--covers", action='store_true')
    parser.add_argument("--artistid")
    args = parser.parse_args()
    #
    return args

def configure(args):
    colorama.init()
    Configuration(
        work_dir = args.path,
        is_album = args.album,
        is_artist = args.artist,
        artist_id = args.artistid,
        set_covers = args.covers
    )