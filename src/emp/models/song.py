def from_none(x):
    assert x is None
    return x


def from_str(x):
    assert isinstance(x, str)
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def is_type(t, x):
    assert isinstance(x, t)
    return x


def from_int(x):
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f, x):
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Album:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Album(id, name)

    def to_dict(self):
        result = {}
        if self.id is not None:
            result["id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class Song:
    def __init__(self, id, title, name, artist, album, albumartist, disk, track, filename, genre, playlisttrack, time, year, bitrate, rate, mode, mime, url, size, mbid, album_mbid, artist_mbid, albumartist_mbid, art, flag, preciserating, rating, averagerating, playcount, catalog, composer, channels, comment, license, publisher, language, lyrics, replaygain_album_gain, replaygain_album_peak, replaygain_track_gain, replaygain_track_peak, r128_album_gain, r128_track_gain):
        self.id = id
        self.title = title
        self.name = name
        self.artist = artist
        self.album = album
        self.albumartist = albumartist
        self.disk = disk
        self.track = track
        self.filename = filename
        self.genre = genre
        self.playlisttrack = playlisttrack
        self.time = time
        self.year = year
        self.bitrate = bitrate
        self.rate = rate
        self.mode = mode
        self.mime = mime
        self.url = url
        self.size = size
        self.mbid = mbid
        self.album_mbid = album_mbid
        self.artist_mbid = artist_mbid
        self.albumartist_mbid = albumartist_mbid
        self.art = art
        self.flag = flag
        self.preciserating = preciserating
        self.rating = rating
        self.averagerating = averagerating
        self.playcount = playcount
        self.catalog = catalog
        self.composer = composer
        self.channels = channels
        self.comment = comment
        self.license = license
        self.publisher = publisher
        self.language = language
        self.lyrics = lyrics
        self.replaygain_album_gain = replaygain_album_gain
        self.replaygain_album_peak = replaygain_album_peak
        self.replaygain_track_gain = replaygain_track_gain
        self.replaygain_track_peak = replaygain_track_peak
        self.r128_album_gain = r128_album_gain
        self.r128_track_gain = r128_track_gain

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        name = from_union([from_str, from_none], obj.get("name"))
        artist = from_union([Album.from_dict, from_none], obj.get("artist"))
        album = from_union([Album.from_dict, from_none], obj.get("album"))
        albumartist = from_union([Album.from_dict, from_none], obj.get("albumartist"))
        disk = from_union([from_int, from_none], obj.get("disk"))
        track = from_union([from_int, from_none], obj.get("track"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        genre = from_union([lambda x: from_list(Album.from_dict, x), from_none], obj.get("genre"))
        playlisttrack = from_union([from_int, from_none], obj.get("playlisttrack"))
        time = from_union([from_int, from_none], obj.get("time"))
        year = from_union([from_int, from_none], obj.get("year"))
        bitrate = from_union([from_int, from_none], obj.get("bitrate"))
        rate = from_union([from_int, from_none], obj.get("rate"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        mime = from_union([from_str, from_none], obj.get("mime"))
        url = from_union([from_str, from_none], obj.get("url"))
        size = from_union([from_int, from_none], obj.get("size"))
        mbid = from_none(obj.get("mbid"))
        album_mbid = from_none(obj.get("album_mbid"))
        artist_mbid = from_none(obj.get("artist_mbid"))
        albumartist_mbid = from_none(obj.get("albumartist_mbid"))
        art = from_union([from_str, from_none], obj.get("art"))
        flag = from_union([from_int, from_none], obj.get("flag"))
        preciserating = from_none(obj.get("preciserating"))
        rating = from_none(obj.get("rating"))
        averagerating = from_none(obj.get("averagerating"))
        playcount = from_union([from_int, from_none], obj.get("playcount"))
        catalog = from_union([from_int, from_none], obj.get("catalog"))
        composer = from_union([from_str, from_none], obj.get("composer"))
        channels = from_none(obj.get("channels"))
        comment = from_none(obj.get("comment"))
        license = from_none(obj.get("license"))
        publisher = from_none(obj.get("publisher"))
        language = from_none(obj.get("language"))
        lyrics = from_none(obj.get("lyrics"))
        replaygain_album_gain = from_none(obj.get("replaygain_album_gain"))
        replaygain_album_peak = from_none(obj.get("replaygain_album_peak"))
        replaygain_track_gain = from_none(obj.get("replaygain_track_gain"))
        replaygain_track_peak = from_none(obj.get("replaygain_track_peak"))
        r128_album_gain = from_none(obj.get("r128_album_gain"))
        r128_track_gain = from_none(obj.get("r128_track_gain"))
        return Song(id, title, name, artist, album, albumartist, disk, track, filename, genre, playlisttrack, time, year, bitrate, rate, mode, mime, url, size, mbid, album_mbid, artist_mbid, albumartist_mbid, art, flag, preciserating, rating, averagerating, playcount, catalog, composer, channels, comment, license, publisher, language, lyrics, replaygain_album_gain, replaygain_album_peak, replaygain_track_gain, replaygain_track_peak, r128_album_gain, r128_track_gain)

    def to_dict(self):
        result = {}
        if self.id is not None:
            result["id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.artist is not None:
            result["artist"] = from_union([lambda x: to_class(Album, x), from_none], self.artist)
        if self.album is not None:
            result["album"] = from_union([lambda x: to_class(Album, x), from_none], self.album)
        if self.albumartist is not None:
            result["albumartist"] = from_union([lambda x: to_class(Album, x), from_none], self.albumartist)
        if self.disk is not None:
            result["disk"] = from_union([from_int, from_none], self.disk)
        if self.track is not None:
            result["track"] = from_union([from_int, from_none], self.track)
        if self.filename is not None:
            result["filename"] = from_union([from_str, from_none], self.filename)
        if self.genre is not None:
            result["genre"] = from_union([lambda x: from_list(lambda x: to_class(Album, x), x), from_none], self.genre)
        if self.playlisttrack is not None:
            result["playlisttrack"] = from_union([from_int, from_none], self.playlisttrack)
        if self.time is not None:
            result["time"] = from_union([from_int, from_none], self.time)
        if self.year is not None:
            result["year"] = from_union([from_int, from_none], self.year)
        if self.bitrate is not None:
            result["bitrate"] = from_union([from_int, from_none], self.bitrate)
        if self.rate is not None:
            result["rate"] = from_union([from_int, from_none], self.rate)
        if self.mode is not None:
            result["mode"] = from_union([from_str, from_none], self.mode)
        if self.mime is not None:
            result["mime"] = from_union([from_str, from_none], self.mime)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.size is not None:
            result["size"] = from_union([from_int, from_none], self.size)
        if self.mbid is not None:
            result["mbid"] = from_none(self.mbid)
        if self.album_mbid is not None:
            result["album_mbid"] = from_none(self.album_mbid)
        if self.artist_mbid is not None:
            result["artist_mbid"] = from_none(self.artist_mbid)
        if self.albumartist_mbid is not None:
            result["albumartist_mbid"] = from_none(self.albumartist_mbid)
        if self.art is not None:
            result["art"] = from_union([from_str, from_none], self.art)
        if self.flag is not None:
            result["flag"] = from_union([from_int, from_none], self.flag)
        if self.preciserating is not None:
            result["preciserating"] = from_none(self.preciserating)
        if self.rating is not None:
            result["rating"] = from_none(self.rating)
        if self.averagerating is not None:
            result["averagerating"] = from_none(self.averagerating)
        if self.playcount is not None:
            result["playcount"] = from_union([from_int, from_none], self.playcount)
        if self.catalog is not None:
            result["catalog"] = from_union([from_int, from_none], self.catalog)
        if self.composer is not None:
            result["composer"] = from_union([from_str, from_none], self.composer)
        if self.channels is not None:
            result["channels"] = from_none(self.channels)
        if self.comment is not None:
            result["comment"] = from_none(self.comment)
        if self.license is not None:
            result["license"] = from_none(self.license)
        if self.publisher is not None:
            result["publisher"] = from_none(self.publisher)
        if self.language is not None:
            result["language"] = from_none(self.language)
        if self.lyrics is not None:
            result["lyrics"] = from_none(self.lyrics)
        if self.replaygain_album_gain is not None:
            result["replaygain_album_gain"] = from_none(self.replaygain_album_gain)
        if self.replaygain_album_peak is not None:
            result["replaygain_album_peak"] = from_none(self.replaygain_album_peak)
        if self.replaygain_track_gain is not None:
            result["replaygain_track_gain"] = from_none(self.replaygain_track_gain)
        if self.replaygain_track_peak is not None:
            result["replaygain_track_peak"] = from_none(self.replaygain_track_peak)
        if self.r128_album_gain is not None:
            result["r128_album_gain"] = from_none(self.r128_album_gain)
        if self.r128_track_gain is not None:
            result["r128_track_gain"] = from_none(self.r128_track_gain)
        return result


def song_from_dict(s):
    return Song.from_dict(s)


def song_to_dict(x):
    return to_class(Song, x)
