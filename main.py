import os
import re
import sys
from os import listdir
from os.path import isfile, join
from pathlib import Path


class RetitleEngine(object):

    def run(self, folder, series_title, season_number, quality, regex_filter, episode_number_regex):
        files_to_retitle = [f for f in listdir(folder) if isfile(join(folder, f))]
        for file in files_to_retitle:
            if re.match(regex_filter, file):
                episode_number = re.match(episode_number_regex, file).group(1)
                extension = re.match(r".*\\.(.*)$", file).group(1)
                os.rename(Path(file).absolute(),
                          "{title} - S{season_number}E{episode_number} {quality}.{extension}".format(
                              title=series_title, season_number=season_number, episode_number=episode_number,
                              quality=quality, extension=extension
                          ))


if __name__ == "__main__":
    if len(sys.argv) != 7:
        print("Usage: folder seriesTitle seasonNumber episodeQuality filter episodeNumberRegex")
        sys.exit(1)
    engine = RetitleEngine()
    engine.run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
