INPUTSTREAM_PROTOCOLS = {
    'mpd': 'inputstream.adaptive',
    'dash': 'inputstream.adaptive',
    'ism': 'inputstream.adaptive',
    'hls': 'inputstream.adaptive',
    'rtmp': 'inputstream.rtmp'
}

DRM_SCHEMES = {
    'widevine': 'widevine',
    'com.widevine.alpha': 'widevine'
}

WIDEVINE_ARCHS = {
    'x86_64': 'x86_64',
    'AMD64': 'x86_64',
    'x86': 'x86',
    'i386': 'x86',
    'i686': 'x86'
}

WIDEVINE_DOWNLOAD_MAP = {
    'x86_64':
    {
        'Linux': 'Linux_x86_64-gcc3',
        'Windows': 'WINNT_x86-msvc',
        'Darwin': 'Darwin_x86_64-gcc3-u-i386-x86_64'},
    'x86':
    {
        'Linux': 'Linux_x86-gcc3',
        'Windows': 'WINNT_x86-msvc',
        'Darwin': 'Darwin_x86_64-gcc3-u-i386-x86_64'
    }
}

WIDEVINE_CDM_EXTENSIONS = ['.so', '.dll', '.dylib']

WIDEVINE_MINIMUM_KODI_VERSION = '17.4'

WIDEVINE_CDM_SOURCE = 'https://hg.mozilla.org/mozilla-central/raw-file/31465a03c03d1eec31cd4dd5d6b803724dcb29cd/toolkit/content/gmp-sources/widevinecdm.json'

HLS_MINIMUM_IA_VERSION = '2.0.11'
