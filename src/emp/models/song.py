def from_str(x):
    assert isinstance(x, str)
    return x


def from_none(x):
    assert x is None
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


def to_class(c, x):
    assert isinstance(x, c)
    return x.to_dict()


class Artist:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        return Artist(name)

    def to_dict(self):
        result = {}
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        return result


class Song:
    def __init__(self, id, title, name, artist, url, art):
        self.id = id
        self.title = title
        self.name = name
        self.artist = artist
        self.url = url
        self.art = art

    @staticmethod
    def from_dict(obj):
        assert isinstance(obj, dict)
        id = from_union([from_none, lambda x: int(from_str(x))], obj.get("id"))
        title = from_union([from_str, from_none], obj.get("title"))
        name = from_union([from_str, from_none], obj.get("name"))
        artist = from_union([Artist.from_dict, from_none], obj.get("artist"))
        url = from_union([from_str, from_none], obj.get("url"))
        art = from_union([from_str, from_none], obj.get("art"))
        return Song(id, title, name, artist, url, art)

    def to_dict(self):
        result = {}
        if self.id is not None:
            result["id"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.id)
        if self.title is not None:
            result["title"] = from_union([from_str, from_none], self.title)
        if self.name is not None:
            result["name"] = from_union([from_str, from_none], self.name)
        if self.artist is not None:
            result["artist"] = from_union([lambda x: to_class(Artist, x), from_none], self.artist)
        if self.url is not None:
            result["url"] = from_union([from_str, from_none], self.url)
        if self.art is not None:
            result["art"] = from_union([from_str, from_none], self.art)
        return result


def song_from_dict(s):
    return Song.from_dict(s)


def song_to_dict(x):
    return to_class(Song, x)
